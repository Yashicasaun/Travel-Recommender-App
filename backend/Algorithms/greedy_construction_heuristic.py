### Using a Greedy Construction Heuristic to create an initial solution
import copy
import random

from backend.Algorithms.CostFunction import cost_function

import pandas as pd
import numpy as np

from backend.data.distance_matrix import get_distance,get_distance_from_hotel

"""
Pseudocode for a Greedy Construction Heuristic
Basic Idea - Take the best cost from each location added to path
(this might not be the best path overall.)
"""

def calculate_ratio(distance_matrix, profit_matrix):  # calculate cost
    ratio_matrix = pd.DataFrame(np.zeros(distance_matrix.shape),
                                columns=distance_matrix.index,
                                index=distance_matrix.index)
    try:
        for i in ratio_matrix.index:
            for j in ratio_matrix.index:
                distance = distance_matrix[i][j]
                profit = profit_matrix.loc[j]['rating']
                if i != j:
                    ratio_matrix.loc[i][j] = cost_function(distance, profit)
    except KeyError as e:
        print(e)

    return ratio_matrix


def get_top_locations(num_days, candidate_list, start, profit_matrix, data, city):
    # get top locations to be visited from the start point
    scores = []
    for poi in candidate_list:
        distance = get_distance_from_hotel(start, poi, data, city)
        profit = profit_matrix.loc[poi]["rating"]
        score = cost_function(distance, profit)
        scores.append(score)

    top_locations = list(np.argpartition(-np.array(scores), num_days * 5)[:num_days * 5])
    #top_locations = random.sample(top_locations, num_days)  # escape local optima

    return list(top_locations)


def construct_initial_solution(num_days, distance_matrix, profit_matrix, compulsory_pois, hotel, data, city, max_distance, max_locations):
    # constructing solution in a greedy way
    # taking the best cost at each step
    cities = list(distance_matrix.keys())
    ratio_matrix = calculate_ratio(distance_matrix, profit_matrix)
    final = []
    solution =[]

    # give a headstart to nearby locations
    top_locations = get_top_locations(num_days, cities, hotel, profit_matrix, data, city)
    top_locations = random.sample(top_locations, num_days)
    for idx in top_locations:
        solution.append([cities[idx]])
        ratio_matrix[cities[idx]] = 0.0
        if cities[idx] in compulsory_pois:
            compulsory_pois.remove(cities[idx])

    """initial_pois = random.sample(compulsory_pois, num_days)   #TOD0 Hotel
    solution = [[initial_pois[i]] for i in range(num_days)]
    for poi in initial_pois:
        compulsory_pois.remove(poi)
        ratio_matrix[poi] = 0.0"""

    while compulsory_pois:
        for day_solution in solution:
            scores = []
            last_visited = day_solution[-1]
            for poi in compulsory_pois:
                distance = distance_matrix[last_visited][poi]
                profit = profit_matrix.loc[poi]["rating"]
                score = cost_function(distance, profit)
                scores.append(score)

            if scores:
                idx_max = scores.index(max(scores))
                day_solution.append(compulsory_pois[idx_max])
                ratio_matrix[compulsory_pois[idx_max]] = 0.0
                compulsory_pois.remove(compulsory_pois[idx_max])

    for day_solution in solution:
        distance = get_distance(day_solution, distance_matrix) + get_distance_from_hotel(hotel, day_solution[0], data, city)
        day_sol = copy.deepcopy(day_solution)

        best_cost_idx = ratio_matrix.loc[day_sol[-1]].idxmax()
        while distance + distance_matrix[day_sol[-1]][best_cost_idx] + get_distance_from_hotel(hotel, best_cost_idx, data, city) <= max_distance and len(day_sol) < max_locations:
            distance += distance_matrix[day_sol[-1]][best_cost_idx]
            day_sol.append(best_cost_idx)
            ratio_matrix[best_cost_idx] = 0.0
            best_cost_idx = ratio_matrix.loc[day_sol[-1]].idxmax()

        final.append(day_sol)

    print("solution = ", final)

    #print(solution)
    return final
