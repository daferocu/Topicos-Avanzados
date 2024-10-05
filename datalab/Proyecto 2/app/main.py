# 1. Library imports
import json
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI
from Penguins_val import Penguins
import pickle
from my_functions import func_transform, salida_pred
from enum import Enum

# 2. Create the app object
app = FastAPI()

lr = pickle.load(open('utils/cl_lr.pkl', 'rb'))
nb = pickle.load(open('utils/cl_nb.pkl', 'rb'))

# 3. Index route, opens automatically on http://127.0.0.0:8000
@app.get('/')
def index():
    return {'message': 'Welcome to level 1 Topicos Avanzados Analitica PUJ, you can predict movie gender'}

# @app.get('/examples')
# def index():      
#         json_data = json.load(open("examples.json"))
#         # Devolver el JSON como respuesta
#         return JSONResponse(content=json_data)

# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence

# class ModelOptions(str, Enum):
#     mod_1 = "Logistic Regression"
#     mod_2 = "MultinomialNB"

@app.post('/predict')
def predict(data:Penguins):
    data = data.dict()
    texto = data['summary']

   # Estandarizar variables
    user_input = [texto]
    user_input_scaled = func_transform(user_input)

    # Seleccionar modelo
    out_model = salida_pred(nb.predict(user_input_scaled)) 

    return {
        out_model
    }

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8989)
