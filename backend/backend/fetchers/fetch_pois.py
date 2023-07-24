from backend.fetchers.fetch_fsq_data import fetch_data_from_fsq
from data.distance_matrix import process_data



def fetch_pois(city, categories):
    fetch_data_from_fsq(categories, city)
    data = process_data(city, categories)
    names = data["name"]
    return list(names)