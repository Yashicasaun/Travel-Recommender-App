import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
import os
from haversine import haversine

from backend.data.hotels_func import get_hotel_longlat


def get_distance(path, distance_matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += distance_matrix[path[i]][path[i + 1]]

    return distance


def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def get_data(city):
    path = os.path.join("data", city + ".csv")
    df = pd.read_csv(path)
    df = df.groupby("name").apply(lambda x: x.loc[x.popularity.idxmax()]).reset_index(drop=True)
    new_df = pd.DataFrame(columns=["name", "latitude", "longitude", "category", "rating"])
    new_df["name"] = df["name"]
    new_df["latitude"] = df["geocodes"].apply(lambda x: eval(x)["main"]["latitude"])
    new_df["longitude"] = df["geocodes"].apply(lambda x: eval(x)["main"]["longitude"])
    new_df["category"] = df["categories"].apply(lambda x: int(str(eval(x)[0]["id"])[:2] + '000'))
    new_df["subcategory"] = df["categories"].apply(lambda x: eval(x)[0]["name"])
    new_df["rating"] = df["rating"]

    return new_df


def get_distance_matrix(df):
    dist_matrix = pd.DataFrame(np.zeros((len(df), len(df))), columns=df['name'], index=df['name'])

    # calculate the distance between each pair of cities using the Haversine formula
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            #dist = haversine_distance(df['longitude'][i], df['latitude'][i], df['longitude'][j], df['latitude'][j])
            dist = haversine((df['latitude'][i], df['longitude'][i]), (df['latitude'][j], df['longitude'][j]))
            dist_matrix.iloc[i, j] = dist
            dist_matrix.iloc[j, i] = dist

    return dist_matrix  # distances in kilometers as the radius in km


def get_longlat(name, data):
    # data = process_data()
    latitude = data[data["name"] == name]["latitude"]
    longitude = data[data["name"] == name]["longitude"]

    return latitude, longitude


def filter_categories(categories, data):
    categories = [cat[:2] for cat in categories]
    data = data[data["category"].apply(lambda x: str(x)[:2] in categories)]
    data.reset_index(drop=True, inplace=True)
    data.drop("category", axis=1, inplace=True)

    return data


def process_data(city, categories):
    """
    :param city:
    :param categories:
    :return: dataset containing selected city and categories
    """
    data = get_data(city)
    data = filter_categories(categories, data)

    return data


def attach_long_lat(solution, df, hotel, city):
    # attach the longitudes, latitudes associated with pois
    # for Google map integration

    lat, long = get_hotel_longlat(hotel, city)
    distance = {}
    distance_matrix = get_distance_matrix(df)
    data = df.set_index('name')
    routes = {}
    for idx, day in enumerate(solution):
        day_result = [{'name' :  hotel, 'value' : [lat, long], 'subcategory': 'Start Point'}]
        distance_from_hotel_start = get_distance_from_hotel(hotel, day[0], df, city)
        distance_from_hotel_end = get_distance_from_hotel(hotel, day[-1], df, city)
        for poi in day:
            key = {}
            key['name'] = poi
            key['value'] = [data.loc[poi]['latitude'], data.loc[poi]['longitude']]
            key['subcategory'] = data.loc[poi]['subcategory']
            day_result.append(key)

        day_result.append({'name': hotel, 'value': [lat, long], 'subcategory': 'End Point'})

        distance['Day ' + str(idx + 1)] = get_distance(day, distance_matrix) + distance_from_hotel_start + distance_from_hotel_end

        routes['Day ' + str(idx + 1)] = day_result

    result = {
        'routes' :  routes,
        'distance' : distance
    }

    return result

def get_distance_from_hotel(location1, location2, data, city):
    lat_start, long_start = get_hotel_longlat(location1, city)
    lat_poi, long_poi = data[data["name"] == location2]["latitude"].values[0], \
                        data[data["name"] == location2]["longitude"].values[0]

    distance = haversine((lat_start, long_start), (lat_poi, long_poi))
    #distance = haversine_distance(long_start, lat_start, long_poi, lat_poi)

    return distance
