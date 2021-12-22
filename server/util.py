import pickle
import json
import numpy as np

__provinsi = None
__data_columns = None
__model = None

def predict_ipm(provinsi,harapan_hidup,ppk,ls_mean,hls):
    try:
        loc_index = __data_columns.index(provinsi.upper()) # lower
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = harapan_hidup
    x[1] = ppk
    x[2] = ls_mean
    x[3] = hls
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __provinsi

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __provinsi = __data_columns[4:]

    global __model
    if __model is None:
        with open('./artifacts/hdi.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def nama_provinsi():
    return __provinsi

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(f" Prediksi nilai IPM Provinsi DI YOGYAKARTA adalah: {predict_ipm('DI YOGYAKARTA',75.04,14111,9.04,14.39)}")


