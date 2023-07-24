import os

from backend.data.foursquare import get_data

def fetch_data_from_fsq(categories, city):
    path = os.path.join("data", city + ".csv")
    print(path)
    if not os.path.exists(path):
        df = get_data(categories, city)
        df.to_csv(path)
    else:
        print("ignoring, file already present!")

def fetch_hotels_from_fsq(city):
    path = os.path.join("data", "Hotels_" + city + ".csv")
    if not os.path.exists(path):
        df = get_data(["19014"], city)    # hotel category
        df.to_csv(path)
    else:
        print("ignoring, file already present!")

