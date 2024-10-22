# 1. Library imports
from pydantic import BaseModel

# 2. Class for models.
class Penguins(BaseModel):
    MedInc:float
    HouseAge:float
    AveRooms:float
    AveBedrms:float
    Population:float
    AveOccup:float
    Latitude:float
    Longitude:float
    