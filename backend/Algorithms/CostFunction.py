alpha = 0.7
beta = 1

def cost_function(distance, profit):
    cost = alpha * profit + \
           (1 - alpha) * 1 / (distance + 0.00001)
    return cost

def cost_function_local_search(distance, profit):
    cost = (1-beta) * profit + \
           beta * 1 / (distance + 0.00001)

    return cost