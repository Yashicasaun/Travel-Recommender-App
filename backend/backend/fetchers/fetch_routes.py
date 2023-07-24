from Algorithms.ILS import ILS
from Algorithms.SAILS import SAILS
from Algorithms.ACO import AntColonyOptimization
from Algorithms.GRASP import GRASP

from data.distance_matrix import get_distance_matrix, process_data
from data.profit_mat import get_profit_table

routes_Munich = {
    "Iterated Local Search": {
        'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Rindermarkt', 'value': [48.13617, 11.574083], 'subcategory': 'Plaza'},
                  {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'},
                  {'name': 'Marstallmuseum', 'value': [48.15608, 11.50566], 'subcategory': 'History Museum'},
                  {'name': 'Ehrenhof', 'value': [48.158272, 11.504344], 'subcategory': 'Garden'},
                  {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469],
                   'subcategory': 'Museum'},
                  {'name': 'Amalienburg', 'value': [48.155996, 11.500441], 'subcategory': 'Monument'},
                  {'name': 'Botanischer Garten München-Nymphenburg (Botanischer Garten)',
                   'value': [48.162651, 11.500261], 'subcategory': 'Garden'},
                  {'name': 'Gewächshäuser', 'value': [48.163716, 11.501614], 'subcategory': 'Garden'},
                  {'name': 'Nymphenburger Kanal', 'value': [48.158724, 11.51708], 'subcategory': 'Canal'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'New Town Hall (Neues Rathaus)', 'value': [48.137582, 11.575793], 'subcategory': 'Monument'},
                  {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'},
                  {'name': 'Monopteros', 'value': [48.149863, 11.590922], 'subcategory': 'Monument'},
                  {'name': 'Eisbach Wave (Eisbachwelle)', 'value': [48.143474, 11.587886], 'subcategory': 'Surf Spot'},
                  {'name': 'House of Art (Haus der Kunst)', 'value': [48.144068, 11.585896], 'subcategory': 'Museum'},
                  {'name': 'Bayerische Staatskanzlei', 'value': [48.142277, 11.58272], 'subcategory': 'Monument'},
                  {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'},
                  {'name': 'Dianatempel', 'value': [48.142975, 11.579994], 'subcategory': 'Monument'},
                  {'name': 'Feldherrnhalle', 'value': [48.141743, 11.577155], 'subcategory': 'Monument'},
                  {'name': 'Antiquarium', 'value': [48.140547, 11.578958],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Max-Joseph-Platz', 'value': [48.139852, 11.578247], 'subcategory': 'Theater'},
                  {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'},
                  {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'},
                  {'name': 'Kunsthalle München', 'value': [48.140042, 11.575858], 'subcategory': 'Art Museum'},
                  {'name': 'Denkmal-fuer-Michael-Jackson', 'value': [48.140281, 11.573416], 'subcategory': 'Monument'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Jüdisches Museum München', 'value': [48.134375, 11.572263],
                   'subcategory': 'History Museum'},
                  {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'},
                  {'name': 'Olympiahalle', 'value': [48.174927, 11.550053], 'subcategory': 'Concert Hall'},
                  {'name': 'Olympiaberg', 'value': [48.16976, 11.551545], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'BMW Museum', 'value': [48.176781, 11.558889], 'subcategory': 'Museum'},
                  {'name': 'Olympia-Eisstadion', 'value': [48.175093, 11.557058], 'subcategory': 'Stadium'},
                  {'name': 'Olympiapark SoccaFive Arena', 'value': [48.17497, 11.55615], 'subcategory': 'Stadium'},
                  {'name': 'SEA LIFE München', 'value': [48.173824, 11.556359], 'subcategory': 'Aquarium'},
                  {'name': 'Luitpoldpark', 'value': [48.172595, 11.57036], 'subcategory': 'Park'},
                  {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'Glyptothek', 'value': [48.146532, 11.565791], 'subcategory': 'History Museum'},
                  {'name': 'Königsplatz', 'value': [48.145951, 11.56525], 'subcategory': 'Plaza'},
                  {'name': 'Städtische Galerie im Lenbachhaus', 'value': [48.14676, 11.563966],
                   'subcategory': 'Museum'}, {'name': 'Paläontologisches Museum', 'value': [48.147529, 11.563557],
                                              'subcategory': 'History Museum'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]},
    "Simulated Annealing and Iterated Local Search": {
        'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Nymphenburger Kanal', 'value': [48.158724, 11.51708], 'subcategory': 'Canal'},
                  {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'},
                  {'name': 'Monopteros', 'value': [48.149863, 11.590922], 'subcategory': 'Monument'},
                  {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Bayerische Staatskanzlei', 'value': [48.142277, 11.58272], 'subcategory': 'Monument'},
                  {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'},
                  {'name': 'Dianatempel', 'value': [48.142975, 11.579994], 'subcategory': 'Monument'},
                  {'name': 'Antiquarium', 'value': [48.140547, 11.578958],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Max-Joseph-Platz', 'value': [48.139852, 11.578247], 'subcategory': 'Theater'},
                  {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'},
                  {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'},
                  {'name': 'Feldherrnhalle', 'value': [48.141743, 11.577155], 'subcategory': 'Monument'},
                  {'name': 'Kunsthalle München', 'value': [48.140042, 11.575858], 'subcategory': 'Art Museum'},
                  {'name': 'Denkmal-fuer-Michael-Jackson', 'value': [48.140281, 11.573416], 'subcategory': 'Monument'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Eisbach Wave (Eisbachwelle)', 'value': [48.143474, 11.587886], 'subcategory': 'Surf Spot'},
                  {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'},
                  {'name': 'Olympiahalle', 'value': [48.174927, 11.550053], 'subcategory': 'Concert Hall'},
                  {'name': 'Olympiaberg', 'value': [48.16976, 11.551545], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'BMW Museum', 'value': [48.176781, 11.558889], 'subcategory': 'Museum'},
                  {'name': 'Olympia-Eisstadion', 'value': [48.175093, 11.557058], 'subcategory': 'Stadium'},
                  {'name': 'Olympiapark SoccaFive Arena', 'value': [48.17497, 11.55615], 'subcategory': 'Stadium'},
                  {'name': 'SEA LIFE München', 'value': [48.173824, 11.556359], 'subcategory': 'Aquarium'},
                  {'name': 'Luitpoldpark', 'value': [48.172595, 11.57036], 'subcategory': 'Park'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Amalienburg', 'value': [48.155996, 11.500441], 'subcategory': 'Monument'},
                  {'name': 'Marstallmuseum', 'value': [48.15608, 11.50566], 'subcategory': 'History Museum'},
                  {'name': 'Ehrenhof', 'value': [48.158272, 11.504344], 'subcategory': 'Garden'},
                  {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469],
                   'subcategory': 'Museum'}, {'name': 'Botanischer Garten München-Nymphenburg (Botanischer Garten)',
                                              'value': [48.162651, 11.500261], 'subcategory': 'Garden'},
                  {'name': 'Gewächshäuser', 'value': [48.163716, 11.501614], 'subcategory': 'Garden'},
                  {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'},
                  {'name': 'New Town Hall (Neues Rathaus)', 'value': [48.137582, 11.575793], 'subcategory': 'Monument'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]},
    "Greedy Randomized Adaptive Search Procedures": {
        'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Karlsplatz', 'value': [48.139069, 11.565978], 'subcategory': 'Plaza'},
                  {'name': 'Kunsthalle München', 'value': [48.140042, 11.575858], 'subcategory': 'Art Museum'},
                  {'name': 'Rindermarkt', 'value': [48.13617, 11.574083], 'subcategory': 'Plaza'},
                  {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'},
                  {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'},
                  {'name': 'Olympiaberg', 'value': [48.16976, 11.551545], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'Bayerische Staatskanzlei', 'value': [48.142277, 11.58272], 'subcategory': 'Monument'},
                  {'name': 'Dianatempel', 'value': [48.142975, 11.579994], 'subcategory': 'Monument'},
                  {'name': 'Museum Brandhorst', 'value': [48.148144, 11.574342], 'subcategory': 'Art Museum'},
                  {'name': 'Antiquarium', 'value': [48.140547, 11.578958],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': "St. Michael's Church (St. Michael)", 'value': [48.138546, 11.570284],
                   'subcategory': 'Structure'},
                  {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'},
                  {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469],
                   'subcategory': 'Museum'},
                  {'name': 'Nymphenburger Kanal', 'value': [48.158724, 11.51708], 'subcategory': 'Canal'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Feldherrnhalle', 'value': [48.141743, 11.577155], 'subcategory': 'Monument'},
                  {'name': 'Isarufer an der Reichenbachbrücke', 'value': [48.126804, 11.576537],
                   'subcategory': 'Beach'},
                  {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Städtische Galerie im Lenbachhaus', 'value': [48.14676, 11.563966],
                   'subcategory': 'Museum'},
                  {'name': 'Königsplatz', 'value': [48.145951, 11.56525], 'subcategory': 'Plaza'},
                  {'name': 'Glyptothek', 'value': [48.146532, 11.565791], 'subcategory': 'History Museum'},
                  {'name': 'Alte Pinakothek', 'value': [48.148327, 11.569776], 'subcategory': 'Museum'},
                  {'name': 'Architekturmuseum der TU München', 'value': [48.14702, 11.572219],
                   'subcategory': 'Art Museum'},
                  {'name': 'Pinakothek der Moderne', 'value': [48.14719, 11.572348], 'subcategory': 'Art Gallery'},
                  {'name': 'Max-Joseph-Platz', 'value': [48.139852, 11.578247], 'subcategory': 'Theater'},
                  {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'},
                  {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'},
                  {'name': 'Eisbach Wave (Eisbachwelle)', 'value': [48.143474, 11.587886], 'subcategory': 'Surf Spot'},
                  {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]},
    "Ant Colony Optimization": {
        'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'New Town Hall (Neues Rathaus)', 'value': [48.137582, 11.575793], 'subcategory': 'Monument'},
                  {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'},
                  {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'},
                  {'name': 'Westermühlbach', 'value': [48.125982, 11.565144], 'subcategory': 'River'},
                  {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'},
                  {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'},
                  {'name': 'Deutsches Museum', 'value': [48.129902, 11.583512], 'subcategory': 'Museum'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Jüdisches Museum München', 'value': [48.134375, 11.572263],
                   'subcategory': 'History Museum'},
                  {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'},
                  {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469],
                   'subcategory': 'Museum'},
                  {'name': 'Ehrenhof', 'value': [48.158272, 11.504344], 'subcategory': 'Garden'},
                  {'name': 'Architekturmuseum der TU München', 'value': [48.14702, 11.572219],
                   'subcategory': 'Art Museum'},
                  {'name': 'Pinakothek der Moderne', 'value': [48.14719, 11.572348], 'subcategory': 'Art Gallery'},
                  {'name': 'Alte Pinakothek', 'value': [48.148327, 11.569776], 'subcategory': 'Museum'},
                  {'name': 'NS-Dokumentationszentrum', 'value': [48.145429, 11.567476],
                   'subcategory': 'History Museum'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}],
        'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'},
                  {'name': 'Wittelsbacherbrücke', 'value': [48.122642, 11.568007],
                   'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035],
                   'subcategory': 'Historic and Protected Site'},
                  {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'},
                  {'name': 'Feldherrnhalle', 'value': [48.141743, 11.577155], 'subcategory': 'Monument'},
                  {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'},
                  {'name': 'Galerie Hegemann', 'value': [48.135924, 11.570186], 'subcategory': 'Art Gallery'},
                  {'name': 'Karlsplatz', 'value': [48.139069, 11.565978], 'subcategory': 'Plaza'},
                  {'name': 'Museum Brandhorst', 'value': [48.148144, 11.574342], 'subcategory': 'Art Museum'},
                  {'name': 'Königsplatz', 'value': [48.145951, 11.56525], 'subcategory': 'Plaza'},
                  {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]}
}

routes_Bangalore = {
    "Iterated Local Search": {'Day 1': [
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'Start Point'},
        {'name': 'Chinnaswamy Stadium', 'value': [12.978861, 77.599418], 'subcategory': 'Stadium'},
        {'name': 'KSCA Club House', 'value': [12.977986, 77.600042], 'subcategory': 'Arts and Entertainment'},
        {'name': 'Lalbagh Botanical Garden', 'value': [12.955722, 77.578742], 'subcategory': 'Landmarks and Outdoors'},
        {'name': "Tippu's Summer Palace", 'value': [12.959469, 77.57366], 'subcategory': 'Park'},
        {'name': 'Cubbon Park', 'value': [12.977173, 77.595288], 'subcategory': 'Park'},
        {'name': 'Karnataka High Court', 'value': [12.977836, 77.592671],
         'subcategory': 'Law Enforcement and Public Safety'},
        {'name': 'Vidhana Soudha', 'value': [12.979105, 77.591783], 'subcategory': 'Capitol Building'},
        {'name': 'Bangalore Palace', 'value': [12.998409, 77.591948], 'subcategory': 'Monument'},
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'End Point'}]},
    "Ant Colony Optimization": {'Day 1': [
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'Start Point'},
        {'name': 'The Heritage Centre and Aerospace Museum', 'value': [12.955176, 77.680756], 'subcategory': 'Museum'},
        {'name': "Tippu's Summer Palace", 'value': [12.959469, 77.57366], 'subcategory': 'Park'},
        {'name': 'Bangalore Palace', 'value': [12.998409, 77.591948], 'subcategory': 'Monument'},
        {'name': 'Freedom Park', 'value': [12.978176, 77.58236], 'subcategory': 'Park'},
        {'name': 'Chinnaswamy Stadium', 'value': [12.978861, 77.599418], 'subcategory': 'Stadium'},
        {'name': 'KSCA Club House', 'value': [12.977986, 77.600042], 'subcategory': 'Arts and Entertainment'},
        {'name': 'Mahatma Gandhi Circle (ಮಹಾತ್ಮಾ ಗಾಂಧಿ ವೃತ್)', 'value': [12.976417, 77.599549], 'subcategory': 'Plaza'},
        {'name': 'Cubbon Park', 'value': [12.977173, 77.595288], 'subcategory': 'Park'},
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'End Point'}]},
    "Greedy Randomized Adaptive Search Procedures": {'Day 1': [
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'Start Point'},
        {'name': 'Bangalore Palace', 'value': [12.998409, 77.591948], 'subcategory': 'Monument'},
        {'name': 'Chinnaswamy Stadium', 'value': [12.978861, 77.599418], 'subcategory': 'Stadium'},
        {'name': 'KSCA Club House', 'value': [12.977986, 77.600042], 'subcategory': 'Arts and Entertainment'},
        {'name': 'Mahatma Gandhi Circle (ಮಹಾತ್ಮಾ ಗಾಂಧಿ ವೃತ್)', 'value': [12.976417, 77.599549], 'subcategory': 'Plaza'},
        {'name': 'Cubbon Park Train', 'value': [12.976051, 77.598155], 'subcategory': 'Garden'},
        {'name': 'Cubbon Park', 'value': [12.977173, 77.595288], 'subcategory': 'Park'},
        {'name': 'Freedom Park', 'value': [12.978176, 77.58236], 'subcategory': 'Park'},
        {'name': "Tippu's Summer Palace", 'value': [12.959469, 77.57366], 'subcategory': 'Park'},
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'End Point'}]},
    "Simulated Annealing and Iterated Local Search": {'Day 1': [
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'Start Point'},
        {'name': 'Chitra Kala Parishad', 'value': [12.989239, 77.581011], 'subcategory': 'Art Gallery'},
        {'name': 'Bangalore Palace', 'value': [12.998409, 77.591948], 'subcategory': 'Monument'},
        {'name': "Tippu's Summer Palace", 'value': [12.959469, 77.57366], 'subcategory': 'Park'},
        {'name': 'Lalbagh Botanical Garden', 'value': [12.955722, 77.578742], 'subcategory': 'Landmarks and Outdoors'},
        {'name': 'Vidhana Soudha', 'value': [12.979105, 77.591783], 'subcategory': 'Capitol Building'},
        {'name': 'Karnataka High Court', 'value': [12.977836, 77.592671],
         'subcategory': 'Law Enforcement and Public Safety'},
        {'name': 'Cubbon Park', 'value': [12.977173, 77.595288], 'subcategory': 'Park'},
        {'name': 'Chinnaswamy Stadium', 'value': [12.978861, 77.599418], 'subcategory': 'Stadium'},
        {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'End Point'}]}
}

distance_Munich = {
    "Iterated Local Search": {'Day 1': 13.71, 'Day 2': 5.45, 'Day 3': 14.16},
    "Simulated Annealing and Iterated Local Search": {'Day 1': 14.66, 'Day 2': 13.32, 'Day 3': 13.87},
    "Greedy Randomized Adaptive Search Procedures": {'Day 1': 13.65, 'Day 2': 13.36, 'Day 3': 12.41},
    "Ant Colony Optimization": {'Day 1': 14.25, 'Day 2': 14.45, 'Day 3': 14.03}}

distance_Bangalore = {
    "Iterated Local Search": {'Day 1': 9.46},
    "Ant Colony Optimization": {'Day 1': 34.66 },
    "Simulated Annealing and Iterated Local Search": {'Day 1': 11.77},
    "Greedy Randomized Adaptive Search Procedures": {'Day 1': 9.22275008606017}
}


def fetch_routes(city, hotel, categories, compulsory_pois, num_days, max_distance, max_locations):
    if city == "Munich":
        return routes_Munich, distance_Munich

    if city == "Bangalore":
        return routes_Bangalore, distance_Bangalore

    routes = dict()
    df = process_data(city, categories)
    distance_matrix = get_distance_matrix(df)
    profit_matrix = get_profit_table(df)
    distance = {}
    ils = ILS(distance_matrix, profit_matrix, num_days, compulsory_pois, \
                 hotel, df, city, max_distance, max_locations)
    ils_results = ils.iterated_local_search()
    routes["Iterated Local Search"] = ils_results.get('routes')
    distance['Iterated Local Search'] = ils_results.get('distance')

    sails = SAILS(distance_matrix, profit_matrix, num_days, compulsory_pois, \
                 hotel, df, city, max_distance, max_locations)
    sails_results =  sails.iterated_local_search()
    routes["Simulated Annealing and Iterated Local Search (SAILS)"] = sails_results.get('routes')
    distance["Simulated Annealing and Iterated Local Search (SAILS)"] = sails_results.get('distance')

    aco = AntColonyOptimization(distance_matrix, profit_matrix, num_days, compulsory_pois, \
                 hotel, df, city, max_distance, max_locations)
    aco_result = aco.optimize()
    routes["Ant Colony Optimization (ACO)"] = aco_result.get('routes')
    distance["Ant Colony Optimization (ACO)"] = aco_result.get('distance')

    grasp = GRASP(distance_matrix, profit_matrix, num_days, compulsory_pois, \
                 hotel, df, city, max_distance, max_locations)
    grasp_result = grasp.generate_multi_day_tours()
    routes["Greedy Randomized Adaptive Search Procedures"] = grasp_result.get('routes')
    distance["Greedy Randomized Adaptive Search Procedures"] = grasp_result.get('distance')

    return routes, distance

