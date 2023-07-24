import pandas as pd
import requests

def get_data(categories, city):
    categories = ",".join(cat for cat in categories)
    params = {
        "sort": "rating",
        "categories": categories,
        "fields": "name,geocodes,categories,link,rating,popularity",
        "limit": "10",
        "near": city
    }

    url = "https://api.foursquare.com/v3/places/search"

    headers = {
        "Accept": "application/json",
        "Authorization": ""
    }

    response = requests.request("GET", url, params=params, headers=headers)
    results = response.json()["results"]
    df = pd.DataFrame(results)

    while (response.links):
        url = response.links["next"]["url"]
        response = requests.request("GET", url, headers=headers)
        new_df = pd.DataFrame(response.json()["results"])
        df = pd.concat([df, new_df]).reset_index(drop=True)

    return df

