from api.GameBaseModel import GameBaseModel
from api.Collection import Collection
from pydantic import BaseModel, Field
from typing import Optional, Dict
from pathlib import Path


class Project(GameBaseModel):
    folder: Path = Path("/")
    Collections: Optional[Dict[Path, Collection]] = Field(default_factory=dict)

    def newCollection(self, name: str, location: Path = Path("/")):
        x = Collection(name=name, _uri=Path("/"), _parent=self, _location=location)
        self.Collections[x.location] = x
        return self.Collections[x.location]