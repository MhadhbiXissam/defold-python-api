from __future__ import annotations
from pydantic import BaseModel
from api.GameBaseModel import GameBaseModel
from pathlib import Path
class Camera(GameBaseModel):
    id: str
    aspect_ratio: float = 1.0
    fov: float = 0.7854
    near_z: float = 0.1
    far_z: float = 1000.0
    auto_aspect_ratio: bool = False
    orthographic_projection: bool = False
    orthographic_zoom: float = 1.0

    @property
    def uri(self) -> Path:
        return self._parent.uri / Path("#" + self.id)