# 1. Library imports
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder

with open('data/encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

frecuencias = pd.read_csv('data/frecuencias.csv', sep = ',', decimal = '.', header = 0, encoding = 'utf-8')

# 2. Values to standardize variables.
max_year = np.array([2018])

# 3. Functions to standardize and predict.
def func_transform(user_input):

    data_c = pd.DataFrame(columns=['Mileage', 'Year', 'State', 'Make', 'Model'])
    data_c.loc[len(data_c)] = user_input

    # Eliminar espacios en blanco
    data_c['State'] = data_c['State'].str.strip()
    data_c['Make'] = data_c['Make'].str.strip()
    data_c['Model'] = data_c['Model'].str.strip()

    # Calculate older
    data_c['antiguedad'] = max_year - data_c['Year']  # Calcular la antiguedad del vehículo

    # frequency
    data_c = pd.merge(data_c, frecuencias, on=['Model'])
    data_c.drop(['Year', 'Model'], axis=1, inplace=True)
    data_c.rename(columns={'Valores':'Model'}, inplace=True)
    data_c = data_c.loc[:,['Mileage', 'State', 'Make', 'Model', 'antiguedad']]

    # Dummies
    categorical_features = ["State", "Make"]  # Ajusta según tus datos
    X_encoded = encoder.transform(data_c[categorical_features])
    data_c = pd.concat([data_c.drop(categorical_features, axis=1), pd.DataFrame(X_encoded.toarray())], axis=1)
    data_c.columns = data_c.columns.astype(str)
    
    return data_c

def salida_pred(predicted):

    predicted = f'Prediccion del precio del automovil es de : {predicted[0]}'
    
    return predicted
