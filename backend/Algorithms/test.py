routes = results['routes']
distances = results['distance']

tour = []
for key,value in routes.items():
    x = []
    for dic in value:
        x.append(dic['name'])
    tour.append(x)

num_locations = []
for t in tour:
    num_locations.append(len(t)-2)

def tour_cost(tour):
    # only minimizing distance when a set of poi have been chosen
    cost = []
    distances = []
    ratings = []
    for day_solution in tour:
        distance = get_distance_from_hotel(day_solution[0], day_solution[1], data, city) + \
                   get_distance_from_hotel(day_solution[-1], day_solution[-2], data, city)
        day_cost = cost_function(get_distance_from_hotel(day_solution[0], day_solution[1], data, city), 0) + \
                   cost_function(get_distance_from_hotel(day_solution[-1], day_solution[-2], data, city), 0)
        total_distance = distance
        total_profit = profit_matrix.loc[day_solution[1]]['rating']
        for i in range(1, len(day_solution) - 2):
            distance = distance_matrix[day_solution[i]][day_solution[i + 1]]
            profit = profit_matrix.loc[day_solution[i+1]]['rating']
            total_distance += distance
            total_profit += profit
            day_cost += cost_function(distance, profit)
        distances.append(total_distance)
        ratings.append(total_profit)
        cost.append(day_cost)
    return sum(cost), cost, distances, ratings


tour_cost(tour)

import matplotlib.pyplot as plt
# Extract x and y values from the data
x = [point[0] for point in convergence]
y = [point[1] for point in convergence]
# Plot the line graph
plt.plot(x, y, marker='o')
# Set the labels for x and y axes
plt.xlabel('Iteration')
plt.ylabel('Best cost')
# Set the title of the plot
plt.title('Convergence of Iterated Local Search')
# Display the plot
plt.show()
