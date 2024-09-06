# 1. Library imports
from pydantic import BaseModel

# 2. Class for models.
class Penguins(BaseModel):
    Mileage:float
    Year:float
    State:str
    Make:str
    Model:str
