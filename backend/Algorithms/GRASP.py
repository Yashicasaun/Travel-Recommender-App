import random
import copy
import numpy as np
import time
from Algorithms.CostFunction import cost_function, cost_function_local_search
from data.distance_matrix import get_distance, attach_long_lat, get_distance_from_hotel
from data.distance_matrix import get_distance_matrix, process_data
from data.profit_mat import get_profit_table

"""
ILS vs GRASP
In ILS, we start with an initial solution and keep improving it. 
However, in GRASP, we have multiple initial solutions and improve multiple initial solutions.
Pseudo Code of GRASP:
Construction Phase - 
1. create a new solution for each iteration
2. store the best cost and solution
Local Search - 
1. perform two opt swap
"""

max_iterations = 10
local_search_iterations = 10

class GRASP(object):

    def __init__(self, distance_matrix, profit_matrix, num_days, compulsory_pois, hotel, data, city, max_distance, max_locations):
        self.pois = list(distance_matrix.keys())
        self.num_days = num_days
        self.distance_matrix = distance_matrix
        self.profit_matrix = profit_matrix
        self.compulsory_pois = compulsory_pois
        self.hotel = hotel
        self.data = data
        self.city = city
        self.top_start_points = self.top_locations_from_hotel()
        self.max_distance = max_distance
        self.max_locations = max_locations


    def generate_multi_day_tours(self):
        best_tour = None  # maintain this value across iterations
        best_cost = 0

        for i in range(max_iterations):
            # new solution each time - multi-start algorithm
            print("iteration ", i)
            tour = self.grasp()
            current_cost, _, best_distances  = self.tour_cost(tour)

            distance_flag = True
            for dist in best_distances:
                if dist > self.max_distance:
                    distance_flag = False

            if (best_tour is None or (current_cost > best_cost)) and distance_flag:
                best_tour = copy.deepcopy(tour)
                best_cost = current_cost
                print("improved", best_distances)

        best_tour = attach_long_lat(best_tour, self.data, self.hotel, self.city)

        return best_tour


    def grasp(self):
        best_tour = self.construct_tour()
        best_cost, day_costs, _ = self.tour_cost(best_tour)

        for i in range(local_search_iterations):
            tour = copy.deepcopy(best_tour)
            local_search_tour = self.local_search(tour)
            local_search_cost, _, best_distances = self.tour_cost(local_search_tour)

            distance_flag = True
            for dist in best_distances:
                if dist > self.max_distance:
                    distance_flag = False

            if local_search_cost > best_cost and distance_flag:
                best_tour = copy.deepcopy(local_search_tour)
                best_cost = local_search_cost

        return best_tour

    def top_locations_from_hotel(self):
        # get top locations to be visited from the start point
        scores = []
        for poi in self.pois:
            distance = get_distance_from_hotel(self.hotel, poi, self.data, self.city)
            profit = self.profit_matrix.loc[poi]["rating"]
            score = cost_function(distance, profit)
            scores.append(score)

        top_locations = list(np.argpartition(-np.array(scores), self.num_days * 5)[:self.num_days*5])
        top_locations = [self.pois[idx] for idx in top_locations]
        # top_locations = random.sample(top_locations, num_days)  # escape local optima

        return list(top_locations)

    def construct_tour(self):
        final = []
        candidate_list = copy.deepcopy(self.pois)
        start_points = copy.deepcopy(self.top_start_points)
        compulsory_pois = copy.deepcopy(self.compulsory_pois)
        tour = []
        #add pois near hotel
        for _ in range(self.num_days):
            selected_start = random.choice(start_points)
            tour.append([selected_start])
            start_points.remove(selected_start)
            candidate_list.remove(selected_start)
            if selected_start in compulsory_pois:
                compulsory_pois.remove(selected_start)

        #add compulsory pois
        while compulsory_pois:
            for day_solution in tour:
                scores = []
                for poi in compulsory_pois:
                    distance = self.distance_matrix[day_solution[-1]][poi]
                    profit = self.profit_matrix.loc[poi]["rating"]
                    score = cost_function(distance, profit)
                    scores.append(score)
                if scores:
                    idx_max = scores.index(max(scores))
                    day_solution.append(compulsory_pois[idx_max])
                    candidate_list.remove(compulsory_pois[idx_max])
                    compulsory_pois.remove(compulsory_pois[idx_max])


        for day_solution in tour:
            distance = get_distance(day_solution, self.distance_matrix) + \
                        get_distance_from_hotel(self.hotel, day_solution[0], self.data, self.city)
            day_sol = copy.deepcopy(day_solution)

            # selects one randomly from top 5
            selected_poi = self.select_poi(candidate_list, day_sol[-1])

            while (distance + self.distance_matrix[day_sol[-1]][selected_poi] + get_distance_from_hotel(self.hotel, selected_poi, self.data, self.city ))<= self.max_distance and len(day_sol) < self.max_locations:
                distance += self.distance_matrix[day_sol[-1]][selected_poi]
                day_sol.append(selected_poi)
                candidate_list.remove(selected_poi)
                selected_poi = self.select_poi(candidate_list, day_sol[-1])

            final.append(day_sol)

        return final


    def select_poi(self, candidate_list, last_visited):
        # Calculate the weighted score for each POI and select the one with the highest score
        scores = []
        for poi in candidate_list:
            distance = self.distance_matrix[last_visited][poi]
            profit = self.profit_matrix.loc[poi]['rating']
            score = cost_function(distance, profit)
            scores.append(score)

        #select one in top 5; introduce randomness
        selected_poi = candidate_list[random.choice(np.argpartition(-np.array(scores), 5)[:5])]

        return selected_poi

    def tour_cost(self, tour):
        #only minimizing distance when a set of poi have been chosen
        cost = []
        distances = []
        for day_solution in tour:
            distance = get_distance_from_hotel(self.hotel, day_solution[0], self.data, self.city) + \
                get_distance_from_hotel(self.hotel, day_solution[-1], self.data, self.city)
            day_cost = cost_function_local_search(get_distance_from_hotel(self.hotel, day_solution[0], self.data, self.city), 0) + \
                       cost_function_local_search(get_distance_from_hotel(self.hotel, day_solution[-1], self.data, self.city), 0)
            total_distance = distance
            for i in range(len(day_solution) - 1):
                distance = self.distance_matrix[day_solution[i]][day_solution[i + 1]]
                profit = self.profit_matrix.loc[day_solution[i+1]]['rating']
                total_distance += distance
                day_cost += cost_function_local_search(distance, profit)

            distances.append(total_distance)
            cost.append(day_cost)

        return sum(cost), cost, distances

    def local_search(self, tour):
        """
        Performs local search on each day of the solution by swapping pairs of destinations to improve the cost.
        """
        # two opt swap
        tour = self.two_opt_swap(tour)
        tour = self.multi_day_cross_exchange(tour)

        return tour

    def two_opt_swap(self, tour):
        # Two-Opt Swap heuristic
        improved = False
        best_tour = copy.deepcopy(tour)
        _, best_costs, _ = self.tour_cost(tour)

        for day_idx, day in enumerate(tour):
            for i in range(len(day) - 1):
                for j in range(i + 1, len(day)):
                    new_tour = copy.deepcopy(tour)
                    new_tour[day_idx] = day[:i] + list(reversed(day[i:j + 1])) + day[j + 1:]
                    _, new_costs, _ = self.tour_cost(new_tour)

                    if new_costs[day_idx] > best_costs[day_idx]:
                        best_tour = copy.deepcopy(new_tour)
                        best_costs = new_costs
                        improved = True
                        #print("local search improved")

        if improved:
            return best_tour
        else:
            return tour

    def multi_day_cross_exchange(self, tour):
        """
        Perturbs the solution by randomly swapping two destinations on different days.
        """
        current_cost, _, _ = self.tour_cost(tour)  # Assuming tour_cost is a separate function

        if len(tour) > 1:
            day1_idx, day2_idx = random.sample(range(len(tour)), 2)
            day1 = tour[day1_idx]
            day2 = tour[day2_idx]

            if len(day1) > 0 and len(day2) > 0:
                for i in range(len(day1)):
                    for j in range(len(day2)):
                        dest1_idx = i
                        dest2_idx = j

                        dest1 = day1[dest1_idx]
                        dest2 = day2[dest2_idx]

                        day1[dest1_idx] = dest2
                        day2[dest2_idx] = dest1

                        new_cost, _, new_distance = self.tour_cost(tour)

                        if new_cost < current_cost:
                            # Revert the swap
                            day1[dest1_idx] = dest1
                            day2[dest2_idx] = dest2

        return tour


"""max_distance = 30
max_locations = 6
city = "Bangalore"
hotel = "Holiday Inn Express and Suites"
categories = ['16000', '12000', '10000']
days = 1
comp_pois  =  ["Tippu's Summer Palace", "Bangalore Palace"]"""
#hotel = "Holiday Inn München - Zentrum"
"""city = "Munich"
hotel = "Louis Hotel"
categories = ['10000','16000']
days = 3
comp_pois = ["Olympic Park (Olympiapark)", "Englischer Garten", "Marienplatz", "Nymphenburg Palace (Schloss Nymphenburg)"]"""
"""data = process_data(city, categories)
profit_matrix = get_profit_table(data)
distance_matrix = get_distance_matrix(data)
start_time = time.time()
grasp = GRASP(distance_matrix, profit_matrix, days, comp_pois, \
                 hotel, data, city, max_distance, max_locations)

results = grasp.generate_multi_day_tours()
end_time = time.time()
execution_time = end_time - start_time
print("execution time is", execution_time)
print("process further here")"""
