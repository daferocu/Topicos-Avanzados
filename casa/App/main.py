# 1. Library imports
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI
from enum import Enum
import json

import pickle
from Penguins_val import Penguins
from my_functions import func_transform, salida_pred


# 2. Create the app object
app = FastAPI()

lr = pickle.load(open('utils/model.pkl', 'rb'))

# 3. Index route, opens automatically on http://127.0.0.0:8000
@app.get('/')
def index():
    return {'message': 'Welcome to level 1 Topicos Avanzados Analitica PUJ, you can predict movie gender'}


@app.post('/predict')
def predict(data:Penguins):
    data = data.dict()
    MedInc = data['MedInc']
    HouseAge = data['HouseAge']
    AveRooms = data['AveRooms']
    AveBedrms = data['AveBedrms']
    Population = data['Population']
    AveOccup = data['AveOccup']
    Latitude = data['Latitude']
    Longitude = data['Longitude']

   # Estandarizar variables
    user_input = [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]
    user_input_scaled = func_transform([user_input])

    # Seleccionar modelo
    out_model = salida_pred(lr.predict(user_input_scaled)) 

    return {
        out_model
    }

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8989)
