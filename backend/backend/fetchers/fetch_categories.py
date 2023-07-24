from data.distance_matrix import get_data

category_dict = {
  "Arts and Entertainment" : [10000, 12101, 17065],
  "Landmarks and Outdoors" : [16000],
  "Events" : [14000],
  "Retail" : [17000],
  "Sports and Recreation": [18000],
  "Dining" : [13000],
  #"Hotels" : [19014]
}


def fetch_categories(city):

    categories = [{'label': key, 'value': value} for key, value in category_dict.items()]
    #categories = [{'label' : label, 'value' : idx} for idx, label in enumerate(labels)]

    return categories

def fetch_subcategories(city):
    data = get_data(city)
    subcategories = list(set(data['subcategory']))

    return subcategories

