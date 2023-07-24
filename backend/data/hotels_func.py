import pandas as pd
import os


def get_hotel_longlat(name, city):
    #path = os.path.join("../data", "Hotels_" + city + ".csv")
    path = os.path.join("data", "Hotels_" + city + ".csv")
    hotels_data =  pd.read_csv(path,encoding= 'unicode_escape')
    data = hotels_data[hotels_data["name"]==name]
    data = eval(data["geocodes"].values[0])["main"]
    latitude  = data["latitude"]
    longitude = data["longitude"]

    return latitude, longitude




#print(get_hotel_longlat("Holiday Inn München - Zentrum"))