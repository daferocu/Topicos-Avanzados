# 1. Library imports
from pydantic import BaseModel

# 2. Class for models.
class Penguins(BaseModel):
    summary:str
