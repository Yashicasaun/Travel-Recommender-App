import requests
import json
from geopy.geocoders import Nominatim

bbox = "51.2868,-0.5104,51.6919,0.334" # example bounding box for London
poi_types = ["tourism", "natural", "historic"] # list of POI types

def get_name(lat, lon):
    # create Nominatim geocoder object
    geolocator = Nominatim(user_agent="my_app")

    # reverse geocode to get location information
    location = geolocator.reverse(f"{lat}, {lon}")

    # get location name from location.raw dictionary
    place_name = location.raw['display_name']

    print(place_name)

def get_bbox(name):
    address = name
    url = f'https://nominatim.openstreetmap.org/search?q={address}&format=jsonv2'
    response = requests.get(url).json()

    bbox = response[0]['boundingbox']
    print(bbox)

# construct Overpass API query string
query = f"""
[out:json];
(
"""
for poi_type in poi_types:
    query += "node['" + poi_type + "'](" + bbox + ");"
query += """
);
out center;
"""

# send request to Overpass API
url = "https://overpass-api.de/api/interpreter"
params = {"data": query}
response = requests.get(url, params=params)

# parse response data
data = json.loads(response.content)

# extract relevant information from response
for element in data["elements"]:
    poi_type = list(element["tags"].keys())[0]
    if element["tags"].get("rating"):
        poi_name = element["tags"].get("name")
    else:
        continue
    poi_lat = element["lat"]
    poi_lon = element["lon"]
    print(f"{poi_name} ({poi_type}): ({poi_lat}, {poi_lon})")
