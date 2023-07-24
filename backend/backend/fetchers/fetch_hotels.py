import os.path

import pandas as pd

from backend.fetchers.fetch_fsq_data import fetch_hotels_from_fsq


def fetch_hotels(city):
    fetch_hotels_from_fsq(city)
    path = os.path.join("data", "Hotels_" + city + ".csv")
    data = pd.read_csv(path, encoding= 'unicode_escape')
    names = data["name"].drop_duplicates()

    return list(names)