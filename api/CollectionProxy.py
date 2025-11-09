from __future__ import annotations
from pydantic import BaseModel
from api.GameBaseModel import GameBaseModel
from pathlib import Path

class CollectionProxy(GameBaseModel) :
    id : str
    collection : str = "" # must be difned to compile the game 
    exclude : bool = False 
    @property
    def uri(self) -> Path:
        return self._parent.uri / Path("#" + self.id)