"""
-----------------------------------------------------
Simulated Annealing Iterated Local Search
-----------------------------------------------------
"""
import copy
import time

import numpy as np

from backend.Algorithms.CostFunction import cost_function_local_search
from backend.Algorithms.greedy_construction_heuristic import construct_initial_solution
from backend.data.distance_matrix import attach_long_lat, get_distance_from_hotel
from backend.data.distance_matrix import process_data, get_distance_matrix
from backend.data.profit_mat import get_profit_table

"""
Pseudocode:

1. Create an Initial Solution and assign it as the best solution and cost
    Also, assign it as the current solution
2. Perturb the solution with local search heuristics.
3. Calculate Delta Cost -> new cost - best cost
4. If delta cost > 0 (new cost < best cost) or np.exp(-delta/ temp) > random number:
    i) Accept the new solution as  the best solution, current solution and cost
    exponential probability - np.exp(-delta/temp)
5. Cool the temperature -> temp = temp * cooling_factor. 
   (As temperature reduces, exponential probability becomes small, making more 
   difficult to accept worse solutions)
6. Continue until max iterations
"""

import random

max_iterations = 30
cooling_factor = 0.99
global temperature
temperature = 200


class SAILS(object):

    def __init__(self, distance_matrix, profit_matrix, num_days, compulsory_pois, hotel, data, city, max_distance, max_locations):

        self.cities = list(distance_matrix.keys())
        self.num_days = num_days
        self.distance_matrix = distance_matrix
        self.profit_matrix = profit_matrix
        self.compulsory_pois = compulsory_pois
        self.hotel = hotel
        self.data = data
        self.city = city
        self.max_distance = max_distance
        self.max_locations = max_locations

    def create_initial_solution(self):
        """
        Creates an initial solution using a greedy construction heursitic.
        """
        solution = construct_initial_solution(self.num_days, self.distance_matrix, self.profit_matrix, \
                                              self.compulsory_pois, self.hotel, self.data, self.city, self.max_distance, self.max_locations)

        return solution

    def calculate_solution_cost(self, solution):
        """
        Calculates the total cost of a solution, where cost is the sum of distances between adjacent destinations
        for each day, and returns a list of day costs.
        """
        day_costs = []
        distances = []
        for day in solution:
            distance = get_distance_from_hotel(self.hotel, day[0], self.data, self.city) + get_distance_from_hotel(self.hotel, day[-1], self.data, self.city)
            total_distance = distance
            day_cost = cost_function_local_search(distance, 0)
            for i in range(len(day) - 1):
                distance = self.distance_matrix[day[i]][day[i + 1]]
                profit = self.profit_matrix.loc[day[i + 1]]["rating"]
                total_distance += distance
                day_cost += cost_function_local_search(distance, profit)

            day_costs.append(day_cost)
            distances.append(total_distance)
        return sum(day_costs), day_costs, distances

    def iterated_local_search(self):
        """
        Searches for the optimal solution using ILS.
        """
        local_search_solution = self.create_initial_solution()
        best_solution = copy.deepcopy(local_search_solution)
        distance_flag = True
        no_impr = 0
        threshold = 10
        global temperature
        local_search_cost, _, _ = self.calculate_solution_cost(best_solution)
        best_cost = local_search_cost
        convergence = [[0, best_cost]]
        for i in range(max_iterations):
            print("iteration ", i)
            local_search_solution = self.local_search(local_search_solution)
            local_search_cost, _, local_search_distances = self.calculate_solution_cost(local_search_solution)

            for dist in local_search_distances:
                if dist > self.max_distance:
                    distance_flag = False

            delta_cost = local_search_cost - best_cost
            exp_cost = np.exp(delta_cost / temperature)

            if local_search_cost > best_cost and distance_flag:
                best_solution = copy.deepcopy(local_search_solution)
                best_cost = local_search_cost
                best_day_distances = copy.deepcopy(local_search_distances)
                # best_day_costs = local_search_day_costs
                print("improved", best_day_distances)
                no_impr = 0
            elif (delta_cost > 0 or exp_cost > random.random()) and distance_flag:
                best_solution = copy.deepcopy(local_search_solution)
                best_cost = local_search_cost
                best_day_distances = copy.deepcopy(local_search_distances)
                # best_day_costs = local_search_day_costs
                print("not improved but accepted", best_day_distances)
                no_impr += 1
            else:
                no_impr += 1

            convergence.append([i + 1, best_cost])

            if (no_impr + 1) % threshold == 0:
                local_search_solution = copy.deepcopy(best_solution)
                print("reset")

            temperature = temperature * cooling_factor

        best_solution = attach_long_lat(best_solution, self.data, self.hotel, self.city)

        return best_solution

    def local_search(self, solution):
        """
        local search : performing swap1 and swap2 heurisitics
        """
        solution = self.swap1(solution)
        solution = self.swap2(solution)

        return solution

    def swap1(self, solution):
        current_cost, day_costs,_ = self.calculate_solution_cost(solution)
        new_solution = copy.deepcopy(solution)
        for day_idx, day in enumerate(new_solution):
            day_cost = day_costs[day_idx]
            for i in range(len(day) - 1):
                for j in range(i + 1, len(day)):
                    new_solution[day_idx][i], new_solution[day_idx][j] = new_solution[day_idx][j], \
                                                                         new_solution[day_idx][i]
                    _, new_day_costs,_ = self.calculate_solution_cost(new_solution)
                    new_day_cost = new_day_costs[day_idx]
                    if new_day_cost > day_cost:
                        solution = copy.deepcopy(new_solution)
                        day_costs = copy.deepcopy(new_day_costs)
                        day_cost = copy.deepcopy(day_costs[day_idx])
                    else:
                        new_solution = copy.deepcopy(solution)

        return solution

    def swap2(self, solution):
        """
        Perturbs the solution by randomly swapping two destinations on different days.
        """
        current_cost, _,_ = self.calculate_solution_cost(solution)

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

                        new_cost, _, _ = self.calculate_solution_cost(solution)

                        if new_cost < current_cost:
                            # Revert the swap
                            day1[dest1_idx] = dest1
                            day2[dest2_idx] = dest2

        return solution

"""city = "Munich"
#hotel = "Holiday Inn München - Zentrum"
hotel = "Louis Hotel"
categories = ['10000','16000']
days = 3
compulsory_pois = ["Olympic Park (Olympiapark)", "Englischer Garten", "Marienplatz", "Nymphenburg Palace (Schloss Nymphenburg)"]"""

"""city = "Bangalore"
hotel = "Holiday Inn Express and Suites"
categories = ['16000', '12000', '10000']
days = 1
compulsory_pois  = ["Tippu's Summer Palace", "Bangalore Palace"]"""

"""data = process_data(city, categories)
profit_matrix = get_profit_table(data)
distance_matrix = get_distance_matrix(data)
max_distance = 15
max_locations = 15
start_time = time.time()
sails = SAILS(distance_matrix, profit_matrix, days, compulsory_pois, \
                 hotel, data, city, max_distance, max_locations)

results = sails.iterated_local_search()
end_time = time.time()
execution_time = end_time - start_time
print("execution time is", execution_time)
print("process further here")"""