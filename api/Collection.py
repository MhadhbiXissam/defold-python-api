from __future__ import annotations
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Optional, Dict
from api.GameBaseModel import GameBaseModel
from api.GameObject import GameObject


class Collection(GameBaseModel):
    name: str
    gameObjects: Optional[Dict[Path, GameObject]] = Field(default_factory=dict)
    _ext = ".collection"

    @property
    def uri(self) -> Path:
        return self._uri

    @property
    def location(self) -> Path:
        return self._location / Path(self.name + self._ext)

    def addGameObject(self, id, **kwargs):
        o = GameObject(id=id, _parent=self, **kwargs)
        self.gameObjects[o.uri] = o
        return self.gameObjects[o.uri]