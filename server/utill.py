import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath, balcony):
    load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    load_saved_artifacts()
    return __locations

def load_saved_artifacts():
    print("loading artifacts.............")
    global __data_columns
    global __locations
    global __model

    with open('columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open("banglore_home_price_model.pickle","rb") as f:
        __model = pickle.load(f)

    print("Done loading.............")


if __name__ == "__main__":
    load_saved_artifacts()
    get_location_names()
    print(get_estimated_price("1st Phase JP Nagar",1000.0, 2.0, 2.0, 0))
    print(get_estimated_price("Chikkabanavar",2460.0, 4.0, 7.0, 2.0))
    print(get_estimated_price("	Devarachikkanahalli",1250.0, 2.0, 2.0, 2.0))
    print(get_estimated_price("1st Phase JP Nagar",1000.0, 2.0, 3.0, 0))
    print(get_estimated_price("Ejipura",1000.0, 2.0, 2.0, 0))