import pandas as pd
import requests

# Define the API endpoint and parameters
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params = {
    "location": "48.1351,11.5820",  # latitude and longitude of Munich, Germany
    "radius": 10000,  # radius of the search area, in meters
    "type": ["point_of_interests"],
    #"types": ["museum","zoo","art_gallery","amusement_park","point_of_interests",
    #"church","night_club"], # type of place you want to search for
    "key": "",  # your Google Places API key
    # "fields": ["current_opening_hours","secondary_opening_hours","opening_hours/periods"]
}

# Send a GET request to the API endpoint with the specified parameters
response = requests.get(url, params=params)
i = 5
final_df = pd.DataFrame()
# Check the status code of the response to make sure the request was successful
while i:
    if response.status_code == 200:
        # Extract the list of places from the JSON response
        results = response.json()["results"]
        df = pd.DataFrame(results)
        final_df = pd.concat([final_df, df]).reset_index(drop=True)
        if response.json().get("next_page_token"):
            params["pagetoken"] = response.json()["next_page_token"]
        else:
            break
        response = requests.get(url, params=params)
        i -= 1
    else:
        # Handle any errors that occurred during the request
        print(f"Error {response.status_code}: {response.text}")
final_df.to_clipboard()
