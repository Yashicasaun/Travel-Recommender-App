"""from flask import Blueprint, jsonify, request

from backend.fetchers.fetch_cities import fetch_cities
from backend.fetchers.fetch_hotels import fetch_hotels
from backend.fetchers.fetch_pois import fetch_pois"""
#from backend.fetchers.fetch_routes import create_routes

"""from urllib.parse import parse_qs

bp = Blueprint('app', __name__)


@bp.route('/')
def run_app():
    print("test")

@bp.route('/api/cities', methods=['GET'])
def get_locations():
    # Retrieve the list of available locations from your data source
    cities = fetch_cities()
    print("here")

    # Return the locations as a response
    return jsonify(cities)

@bp.route('/api/hotels', methods=['GET'])
def get_hotels():

    city = request.args.get('city')
    if city:
        hotels = fetch_hotels(city)
    else:
        hotels = []

    # Return the locations as a response
    return jsonify(hotels)

@bp.route('/api/pois', methods=['GET'])
def get_pois():

    categories = request.args.get('categories')
    categories = categories.split(",")
    city = request.args.get('city')
    print(city, categories)
    pois = fetch_pois(city, categories)

    # Return the locations as a response
    return jsonify(pois)

@bp.route('/api/routes', methods=['GET'])
def create_route():

    params = parse_qs(request.args.get('params'))
    city = params.get('city')[0]
    hotel = params.get('hotel')[0]
    categories = params.get('categories')[0].split(",")
    compulsory_pois = params.get('compulsory_pois')[0].split(",")
    num_days = int(params.get('days')[0])

    #routes = create_routes(city, hotel, categories, compulsory_pois, num_days)
    routes = {'Iterated Location Search':
                    {'Day 0': 
                        {'Nymphenburg Palace (Schloss Nymphenburg)': [48.158311, 11.503469], 
                        'Maximiliansanlagen': [48.136305, 11.59672], 
                        'Wiener Platz': [48.133893, 11.593795], 
                        'Museum Fünf Kontinente': [48.137536, 11.585622], 
                        'GOP Varieté-Theater München': [48.138031, 11.5879], 
                        'Maxmonument': [48.137572, 11.588032], 
                        'Maximiliansbrücke': [48.137046, 11.591765], 
                        'Praterstrand': [48.135755, 11.590237], 
                        'Ampere': [48.132974, 11.589474], 
                        'Isartor': [48.135113, 11.581875], 
                        'Marienplatz': [48.137262, 11.575096], 
                        'Nationaltheater': [48.139566, 11.579386], 
                        'Bayerische Staatsoper': [48.139615, 11.579334], 
                        'Max-Joseph-Platz': [48.139852, 11.578247], 
                        'Antiquarium': [48.140547, 11.578958], 
                        'Bayerische Staatskanzlei': [48.142277, 11.58272], 
                        'Eisbach Wave (Eisbachwelle)': [48.143474, 11.587886]},
                    'Day 1': 
                        {'Monopteros': [48.149863, 11.590922], 
                        'Englischer Garten': [48.151673, 11.592511]}, 
                    'Day 2': 
                        {'Alte Pinakothek': [48.148327, 11.569776], 
                        'Architekturmuseum der TU München': [48.14702, 11.572219], 
                        'Hofgarten': [48.142925, 11.580047], 
                        'Karlsplatz': [48.139069, 11.565978], 
                        'Rindermarkt': [48.13617, 11.574083], 
                        'Kath. Kirchenstiftung St. Peter in Altstadt (St. Peter)': [48.13633, 11.575472], 
                        'Gärtnerplatz': [48.131688, 11.576187], 
                        'Drehleier': [48.126088, 11.598523], 
                        'KnödelAlm': [48.12523, 11.604747]}}, 
                'SAILS': 
                    {'Day 0': 
                        {'Alte Pinakothek': [48.148327, 11.569776], 
                        'Englischer Garten': [48.151673, 11.592511], 
                        'Maximiliansanlagen': [48.136305, 11.59672], 
                        'Maximilianeum': [48.136355, 11.594586], 
                        'Wiener Platz': [48.133893, 11.593795], 
                        'Praterstrand': [48.135755, 11.590237], 
                        'Ampere': [48.132974, 11.589474], 
                        'Nymphenburg Palace (Schloss Nymphenburg)': [48.158311, 11.503469]}, 
                    'Day 1': 
                        {'Dianatempel': [48.142975, 11.579994], 
                        'Hofgarten': [48.142925, 11.580047], 
                        'Herkulessaal': [48.141779, 11.579716], 
                        'Nationaltheater': [48.139566, 11.579386], 
                        'Bayerische Staatsoper': [48.139615, 11.579334], 
                        'Max-Joseph-Platz': [48.139852, 11.578247], 
                        'Antiquarium': [48.140547, 11.578958], 
                        'P1': [48.144384, 11.585141], 
                        'House of Art (Haus der Kunst)': [48.144068, 11.585896], 
                        'Wasserfall im Englischen Garten': [48.14514, 11.587347], 
                        'Bayerisches Nationalmuseum': [48.143066, 11.590925], 
                        'Bayerische Staatskanzlei': [48.142277, 11.58272], 
                        'Karlsplatz': [48.139069, 11.565978], 
                        'GOP Varieté-Theater München': [48.138031, 11.5879], 
                        'Isartor': [48.135113, 11.581875], 
                        'Kath. Kirchenstiftung St. Peter in Altstadt (St. Peter)': [48.13633, 11.575472], 
                        'Rindermarkt': [48.13617, 11.574083], 
                        'Cathedral of Our Dear Lady (Dom zu Unserer Lieben Frau (Frauenkirche))': [48.138857, 11.574321], 
                        'Kunsthalle München': [48.140042, 11.575858]}, 
                    'Day 2': 
                        {'M.C. Mueller': [48.131163, 11.571444], 
                        'Sub': [48.132549, 11.573495], 
                        'Asamkirche (Asamkirche (St. Johann Nepomuk))': [48.135137, 11.569677], 
                        'Kronepark': [48.121466, 11.580702], 
                        'Mariahilfplatz': [48.125617, 11.583323], 
                        'Corneliusbrücke': [48.128364, 11.580169], 
                        'Deutsches Museum': [48.129902, 11.583512], 
                        'Gärtnerplatz': [48.131688, 11.576187], 
                        'Staatstheater am Gärtnerplatz': [48.131284, 11.575788], 
                        'Reichenbachbrücke': [48.127371, 11.576969], 
                        'Isarufer an der Reichenbachbrücke': [48.126804, 11.576537], 
                        'CinemaxX München': [48.13433, 11.582091], 
                        'Marienplatz': [48.137262, 11.575096], 
                        'Architekturmuseum der TU München': [48.14702, 11.572219]}}}

    print("routes", routes)

    return routes
"""


