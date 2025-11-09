from __future__ import annotations
from pydantic import BaseModel
from pathlib import Path
from api.GameBaseModel import GameBaseModel


class CollectionFactory(GameBaseModel) :
    id : str 
    prototype : str = "" # must be defind to compile the game , it refer to local collection file in the project 
    load_dynamically : bool = False
    dynamic_prototype  : bool = False
    @property
    def uri(self) -> Path:
        return self._parent.uri / Path("#" + self.id)