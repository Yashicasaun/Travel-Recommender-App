from flask import Blueprint, jsonify, request, Flask
from flask_cors import CORS

from backend.fetchers.fetch_categories import fetch_categories, fetch_subcategories
from backend.fetchers.fetch_cities import fetch_cities
from backend.fetchers.fetch_hotels import fetch_hotels
from backend.fetchers.fetch_pois import fetch_pois
from backend.fetchers.fetch_routes import fetch_routes

from urllib.parse import parse_qs

app = Flask(__name__)
CORS(app)


@app.route('/api/cities', methods=['GET'])
def get_locations():
    # Retrieve the list of available locations from your data source
    cities = fetch_cities()
    print("here")

    # Return the locations as a response
    return jsonify(cities)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    city = request.args.get('city')
    if city:
        hotels = fetch_hotels(city)
    else:
        hotels = []

    # Return the locations as a response
    return jsonify(hotels)


@app.route('/api/pois', methods=['GET'])
def get_pois():
    categories = request.args.get('categories')
    categories = categories.split(",")
    city = request.args.get('city')
    pois = fetch_pois(city, categories)

    return jsonify(pois)


@app.route('/api/categories', methods=['GET'])
def get_categories():
    city = request.args.get('city')
    categories = fetch_categories(city)

    return jsonify(categories)


@app.route('/api/subcategories', methods=['GET'])
def get_subcategories():
    city = request.args.get('city')
    subcategories = fetch_subcategories(city)

    return jsonify(subcategories)


@app.route('/api/routes', methods=['GET'])
def get_routes():
    params = parse_qs(request.args.get('params'))
    city = params.get('city')[0]
    hotel = params.get('hotel')[0]
    categories = params.get('categories')[0].split(",")
    compulsory_pois = params.get('compulsory_pois', [])
    if compulsory_pois:
        compulsory_pois = compulsory_pois[0].split(",")
    num_days = int(params.get('days')[0])
    max_distance = int(params.get('max_distance')[0])
    max_locations = int(params.get('max_locations')[0])

    routes, distance = fetch_routes(city, hotel, categories, compulsory_pois, num_days, max_distance, max_locations)
    result = {
        'routes': routes,
        'distance': distance
    }

    return result

#app.run(debug=True)