import copy
import random

from Algorithms.CostFunction import cost_function_local_search
from data.distance_matrix import get_distance_from_hotel


def calculate_solution_cost(solution, distance_matrix, profit_matrix, hotel, data, city):
    """
    Calculates the total cost of a solution, where cost is the sum of distances between adjacent destinations
    for each day, and returns a list of day costs.
    """
    day_costs = []
    distances = []
    for day in solution:
        distance = get_distance_from_hotel(hotel, day[0], data, city) + get_distance_from_hotel(
            hotel, day[-1], data, city)
        total_distance = distance
        day_cost = cost_function_local_search(distance, 0)
        for i in range(len(day) - 1):
            distance = distance_matrix[day[i]][day[i + 1]]
            profit = profit_matrix.loc[day[i + 1]]["rating"]
            total_distance += distance
            day_cost += cost_function_local_search(distance, profit)

        day_costs.append(day_cost)
        distances.append(total_distance)
    return sum(day_costs), day_costs, distances

def local_search(solution):
    """
    local search : performing 2-opt and multi-day heurisitics
    """
    # two opt swap
    solution = two_opt_swap(solution)
    solution = multi_day_cross_exchange(solution)

    return solution


def two_opt_swap(solution):
    current_cost, day_costs, _ = calculate_solution_cost(solution)
    new_solution = copy.deepcopy(solution)
    for day_idx, day in enumerate(new_solution):
        day_cost = day_costs[day_idx]
        for i in range(len(day) - 1):
            for j in range(i + 1, len(day)):
                new_solution[day_idx][i], new_solution[day_idx][j] = new_solution[day_idx][j], \
                                                                     new_solution[day_idx][i]
                _, new_day_costs, _ = calculate_solution_cost(new_solution)
                new_day_cost = new_day_costs[day_idx]
                if new_day_cost > day_cost:
                    solution = copy.deepcopy(new_solution)
                    day_costs = copy.deepcopy(new_day_costs)
                    day_cost = copy.deepcopy(day_costs[day_idx])
                else:
                    new_solution = copy.deepcopy(solution)

    return solution


def multi_day_cross_exchange(solution):
    """
    Perturbs the solution by randomly swapping two destinations on different days.
    """
    current_cost, _, _ = calculate_solution_cost(solution)

    if len(solution) > 1:
        day1_idx, day2_idx = random.sample(range(len(solution)), 2)
        day1 = solution[day1_idx]
        day2 = solution[day2_idx]

        if len(day1) > 0 and len(day2) > 0:
            for i in range(len(day1)):
                for j in range(len(day2)):
                    dest1_idx = i
                    dest2_idx = j

                    dest1 = day1[dest1_idx]
                    dest2 = day2[dest2_idx]

                    day1[dest1_idx] = dest2
                    day2[dest2_idx] = dest1

                    new_cost, _, _ = calculate_solution_cost(solution)

                    if new_cost < current_cost:
                        # Revert the swap
                        day1[dest1_idx] = dest1
                        day2[dest2_idx] = dest2

    return solution