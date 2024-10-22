# 1. Library imports
import pickle

with open('utils/trf.pkl', 'rb') as archivo_pkl:
    scaler = pickle.load(archivo_pkl)

def func_transform(user_input):
    t1 = scaler.transform(user_input)
    return t1

def salida_pred(predicted):
    predicted = f'Prediccion del precio de la casa es de : {predicted[0]}'
    return predicted
