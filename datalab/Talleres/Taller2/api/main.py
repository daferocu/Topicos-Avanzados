# 1. Library imports
import json
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI
from Penguins_val import Penguins
import pickle
from my_functions import func_transform, salida_pred

# 2. Create the app object
app = FastAPI()

model_rf = pickle.load(open('data/modelo.pkl', 'rb'))

# 3. Index route, opens automatically on http://127.0.0.0:8000
@app.get('/')
def index():
    return {'message': 'Welcome to level 0 Topicos, you can predict the price of a car'}

@app.get('/examples')
def index():      
        json_data = json.load(open("examples.json"))
        # Devolver el JSON como respuesta
        return JSONResponse(content=json_data)

# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence

@app.post('/predict')
def predict_price(data:Penguins):
    data = data.dict()
    Mileage = data['Mileage']
    Year = data['Year']
    State = data['State']
    Make = data['Make']
    Model = data['Model']

   # Estandarizar variables
    user_input = [Mileage, Year, State, Make, Model]
    user_input_scaled = func_transform(user_input)

    # Predecir
    out_model = salida_pred(model_rf.predict(user_input_scaled))
    # y_pred = model_rf.predict(user_input_scaled)
    # pre = f'lala {y_pred}'

    return {
        out_model
    }

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8989)
