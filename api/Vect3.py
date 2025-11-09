from pydantic import BaseModel
from api.GameBaseModel import GameBaseModel


class Vect3(GameBaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0