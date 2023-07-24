"""
-----------------------------------------------------
Ant Colony Optimization
-----------------------------------------------------
"""
import copy
#import time

from backend.Algorithms.CostFunction import cost_function, cost_function_local_search
from backend.data.distance_matrix import get_distance, attach_long_lat, get_distance_from_hotel
#from data.distance_matrix import get_distance_matrix, process_data
#from data.profit_mat import get_profit_table
import numpy as np
import pandas as pd
import random

"""
Pseudocode
Initialize parameters: 
number of ants  n_ants,
pheromone evaporation rate  pho,
alpha, beta for calculating transition probabilities
stopping criteria   max_iterations 

1. Initialize pheromone matrix
2. Loop through n_ants and randomly select a starting node
3. Loop through n_days until all nodes have been visited. Do the following -
    - Calculate transition probability for each unvisited node based on pheromones, profit, distance
    - Select the next node based on this probability
    - Update the pheromone matrix based on the selected path
4. Update the best tour if new tour better than earlier
5. Update the pheromone matrix based on new best tour(increase them?)
6. evaporate pheromone to encourage exploration
        
"""


class AntColonyOptimization:
    def __init__(self, distance_matrix, profit_matrix, num_days, compulsory_pois, hotel, data, city, max_distance,
                 max_location):
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
        self.max_locations = max_location

    def initialize_tau(self):
        index_names = ["pois", "pois", "days"]
        multi_index = pd.MultiIndex.from_product([self.pois, self.pois, range(self.num_days)], names=index_names)
        n_dim = len(self.pois)
        tau = pd.DataFrame(np.ones((n_dim, n_dim, self.num_days)).ravel() * 0.1, index=multi_index)

        return tau

    def top_locations_from_hotel(self):
        # get top locations to be visited from the start point
        scores = []
        for poi in self.pois:
            distance = get_distance_from_hotel(self.hotel, poi, self.data, self.city)
            profit = self.profit_matrix.loc[poi]["rating"]
            score = cost_function(distance, profit)
            scores.append(score)

        top_locations = list(np.argpartition(-np.array(scores), self.num_days * 3)[:self.num_days * 3])
        top_locations = [self.pois[idx] for idx in top_locations]
        # top_locations = random.sample(top_locations, num_days)  # escape local optima

        return list(top_locations)

    def create_initial_path(self):
        # create an initial path which includes nearby popular places to hotel
        # and compulsory pois
        solution = []
        compulsory_pois = copy.deepcopy(self.compulsory_pois)
        start_points = copy.deepcopy(self.top_start_points)
        for _ in range(self.num_days):
            location = random.choice(start_points)
            solution.append([location])
            start_points.remove(location)
            if location in compulsory_pois:
                compulsory_pois.remove(location)

        while compulsory_pois:
            for day_solution in solution:
                scores = []
                last_visited = day_solution[-1]
                for poi in compulsory_pois:
                    distance = self.distance_matrix[last_visited][poi]
                    profit = self.profit_matrix.loc[poi]["rating"]
                    score = cost_function(distance, profit)
                    scores.append(score)

                if scores:
                    idx_max = scores.index(max(scores))
                    day_solution.append(compulsory_pois[idx_max])
                    compulsory_pois.remove(compulsory_pois[idx_max])

        return solution

    def optimize(self):

        tau = self.initialize_tau()

        # Initialize the best path and profit
        best_paths = None
        best_profit = 0

        convergence = [[0, best_profit]]
        for i in range(max_iterations):

            print("iteration ", i)
            ant_paths = [[] for _ in range(num_ants)]
            ant_costs = np.zeros((num_ants, self.num_days))

            for ant in range(num_ants):

                # Initialize ant paths and ant profit
                initial_paths = self.create_initial_path()
                initial_cost, day_costs, day_distances = self.calculate_cost(initial_paths)
                ant_paths[ant].extend(initial_paths)
                ant_costs[ant] = day_costs

                visited = []
                for day in range(self.num_days):
                    visited.extend(initial_paths[day])
                unvisited_pois = list(set(self.pois) - set(visited))

                for day in range(self.num_days):
                    ant_path = ant_paths[ant][day]
                    ant_cost = day_costs[day]
                    distance = get_distance(ant_path, self.distance_matrix) + \
                               get_distance_from_hotel(self.hotel, ant_path[0], self.data, self.city)

                    current_city = ant_path[-1]
                    choice_probs, cost = self._calculate_choice_probs(day, current_city, unvisited_pois, tau)
                    next_city = np.random.choice(list(unvisited_pois), p=choice_probs)
                    while distance + self.distance_matrix[current_city][next_city] + get_distance_from_hotel(self.hotel, next_city, self.data, self.city)<= self.max_distance \
                            and len(ant_path) < self.max_locations:
                        ant_path.append(next_city)
                        ant_cost += self._calculate_eta(current_city, next_city)
                        distance += self.distance_matrix[current_city][next_city]
                        unvisited_pois = list(set(unvisited_pois) - set(ant_path))

                        current_city = ant_path[-1]
                        # Calculate choice probability for each unvisited city
                        choice_probs, cost = self._calculate_choice_probs(day, current_city, unvisited_pois, tau)
                        # Choose the next city to visit based on the choice probabilities
                        next_city = np.random.choice(list(unvisited_pois), p=choice_probs)

                    # Update ant path and profit
                    ant_paths[ant][day] = ant_path
                    ant_costs[ant][day] = ant_cost


                    # Update pheromone trail matrix every day a pth has been chosen
                    delta_tau = self._calculate_delta_tau(day, ant, ant_paths, ant_costs)
                    tau += delta_tau

                distance_flag = True
                for dist in day_distances:
                    if dist > self.max_distance:
                        distance_flag = False

                """local_search_solution = copy.deepcopy(ant_paths[ant])

                                local_search_solution = self.local_search(local_search_solution)
                                total_cost, local_search_cost, day_distances = self.calculate_cost(local_search_solution)
                """
                """if total_cost > best_profit and distance_flag:
                    best_paths = copy.deepcopy(local_search_solution)
                    best_profit = total_cost
                    print("improved", best_paths)"""

                if np.sum(ant_costs[ant]) > best_profit and distance_flag:
                    best_paths = copy.deepcopy(ant_paths[ant])
                    best_profit = np.sum(ant_costs[ant])
                    print("improved", day_distances)

            # evaporate pheromones after each iteration
            tau *= (1 - rho)  # pheromone evaporation
            convergence.append([i+1, best_profit])

        best_paths = self.sort_by_distance(best_paths)
        best_paths = attach_long_lat(best_paths, self.data, self.hotel, self.city)
        return best_paths

    def sort_by_distance(self, tour):
        def tour_cost(solution):
            # cost is distance based
            cost = []
            for day_solution in solution:
                day_cost = 0
                for idx in range(len(day_solution) - 1):
                    distance = self.distance_matrix[day_solution[idx]][day_solution[idx + 1]]
                    profit = self.profit_matrix.loc[day_solution[idx + 1]]['rating']
                    day_cost += cost_function_local_search(distance, profit)
                cost.append(day_cost)
            return cost

        best_tour = copy.deepcopy(tour)
        best_costs = tour_cost(tour)

        improved = False

        for day_idx, day in enumerate(tour):
            for i in range(len(day) - 1):
                for j in range(i + 1, len(day)):
                    new_tour = copy.deepcopy(tour)
                    new_tour[day_idx] = day[:i] + list(reversed(day[i:j + 1])) + day[j + 1:]
                    new_costs = tour_cost(new_tour)

                    if new_costs[day_idx] > best_costs[day_idx]:
                        best_tour = copy.deepcopy(new_tour)
                        best_costs = new_costs
                        improved = True

        if improved:
            return best_tour
        else:
            return tour

    def _calculate_choice_probs(self, day, current_city, unvisited_pois, tau):
        choice_probs = copy.deepcopy(unvisited_pois)
        cost = 0
        for next_city in unvisited_pois:
            tau_ij = tau.loc[current_city].loc[next_city].loc[day].values[0]  # amount of pheromone between i and j
            eta_ij = self._calculate_eta(current_city, next_city)
            choice_probs[choice_probs.index(next_city)] = (tau_ij ** alpha) * (eta_ij ** beta)
            cost += eta_ij

        choice_probs /= sum(choice_probs)
        return choice_probs, cost

    def _calculate_eta(self, current_city, next_city):
        # calculate the cost
        # minimizing distance and maximising profit
        distance = self.distance_matrix[current_city][next_city]
        profit = self.profit_matrix.loc[next_city]['rating']
        eta_ij = cost_function(distance, profit)
        return eta_ij

    def calculate_cost(self, tour):
        # calculate cost of a tour
        cost = []
        distances = []
        for day_solution in tour:
            distance_from_hotel = get_distance_from_hotel(self.hotel, day_solution[0], self.data, self.city)
            distance_to_hotel = get_distance_from_hotel(self.hotel, day_solution[-1], self.data, self.city)
            profit = self.profit_matrix.loc[day_solution[0]]['rating']
            day_cost = cost_function(distance_from_hotel, profit)
            total_distance = distance_from_hotel + distance_to_hotel
            for i in range(len(day_solution) - 1):
                distance = self.distance_matrix[day_solution[i]][day_solution[i + 1]]
                profit = self.profit_matrix.loc[day_solution[i + 1]]['rating']
                day_cost += cost_function(distance, profit)
                total_distance += distance

            distances.append(total_distance)
            cost.append(day_cost)

        return sum(cost), cost, distances


    def _calculate_delta_tau(self, day, ant, ant_paths, ant_profits):
        # n = ant_paths.shape[1]
        delta_tau = self.initialize_tau() * 0.0
        path_length = len(ant_paths[ant][day])
        for i in range(path_length - 1):
            # Get the pois visited by the ant in this iteration
            city_i = ant_paths[ant][day][i]
            city_j = ant_paths[ant][day][i + 1]
            if city_i != city_j:
                # Update the pheromone trail value for this edge
                delta_tau.loc[city_i].loc[city_j].loc[day] += q * ant_profits[ant][day]
                # since we are maximizing profit

        return delta_tau

    def local_search(self, tour):
        """
        Performs local search on each day of the solution by swapping pairs of destinations to improve the cost.
        """
        tour = self.swap1(tour)
        tour = self.swap2(tour)

        return tour

    def swap2(self, tour):
        # Swap two locations heuristic
        improved = False
        best_tour = copy.deepcopy(tour)
        _, best_costs, _ = self.calculate_cost(tour)

        for day_idx, day in enumerate(tour):
            for i in range(len(day) - 1):
                for j in range(i + 1, len(day)):
                    new_tour = copy.deepcopy(tour)
                    new_tour[day_idx] = day[:i] + list(reversed(day[i:j + 1])) + day[j + 1:]
                    _, new_costs, _ = self.calculate_cost(new_tour)

                    if new_costs[day_idx] > best_costs[day_idx]:
                        best_tour = copy.deepcopy(new_tour)
                        best_costs = new_costs
                        improved = True
                        #print("local search improved")

        if improved:
            return best_tour
        else:
            return tour

    def swap2(self, tour):
        """
        Perturbs the solution by randomly swapping two destinations on different days.
        """
        current_cost, _, _ = self.calculate_cost(tour)  # Assuming tour_cost is a separate function

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

                        new_cost, _, new_distance = self.calculate_cost(tour)

                        if new_cost < current_cost:
                            # Revert the swap
                            day1[dest1_idx] = dest1
                            day2[dest2_idx] = dest2

        return tour




# max_locations = 10
max_iterations = 6
num_ants = 5
alpha = 1
beta = 3
rho = 0.3
q = 1

"""city = "Munich"
hotel = "Holiday Inn München - Zentrum"
categories = ['10000','16000']
days = 3
comp_pois = ["Olympic Park (Olympiapark)", "Englischer Garten", "Marienplatz", "Nymphenburg Palace (Schloss Nymphenburg)"]"""
"""city = "Bangalore"
hotel = "Holiday Inn Express and Suites"

categories = ['16000', '12000', '10000']
days = 1
comp_pois  = ["Tippu's Summer Palace", "Bangalore Palace"]
max_locations = 6
max_distance = 30
data = process_data(city, categories)
distance_matrix = get_distance_matrix(data)
profit_matrix = get_profit_table(data)
start_time = time.time()
aco = AntColonyOptimization(distance_matrix, profit_matrix, days, comp_pois, \
                            hotel, data, city, max_distance, max_locations)
results = aco.optimize()
end_time = time.time()
execution_time = end_time - start_time
print("execution time is", execution_time)
print("process further here")"""