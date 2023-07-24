cities = list(distance_matrix.index)
ratings = {}
for key,value in routes.items():
    r = 0
    for dic in value:
        name = dic['name']
        if name in cities:
            r += profit_matrix.loc[name]['rating']
    ratings[key] = r



