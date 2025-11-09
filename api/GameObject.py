from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, Dict
from pathlib import Path
import inspect, os
from api.GameBaseModel import GameBaseModel
from api.Camera import Camera
from api.CollectionFactory import CollectionFactory
from api.CollectionProxy import CollectionProxy
from api.Vect3 import Vect3

class GameObject(GameBaseModel):
    id: str
    position: Vect3 = Vect3()
    rotation: Vect3 = Vect3()
    scale: Vect3 = Vect3(x=1.0, y=1.0, z=1.0)
    gameObjects: Optional[Dict[Path, GameObject]] = Field(default_factory=dict)
    components: Optional[Dict[Path, Camera |  CollectionProxy | CollectionFactory]] = Field(default_factory=dict)

    def __init__(self, **data):
        kwargs = {k: v for k, v in data.items() if not k.startswith("_")}
        super().__init__(**kwargs)
        {setattr(self, k, v) for k, v in data.items() if k.startswith("_")}

    @property
    def uri(self) -> Path:
        return self._parent.uri / self.id

    # add nested game object 
    def addGameObject(self, id, **kwargs):
        o = GameObject(id=id, _parent=self, **kwargs)
        self.gameObjects[o.uri] = o
        return self.gameObjects[o.uri]

    # add camera componenet
    def addCamera(self, id, aspect_ratio=1.0, fov=0.7854, near_z=0.1, far_z=1000.0,auto_aspect_ratio=False, orthographic_projection=False, orthographic_zoom=1.0):
        kwargs = {k: v for k, v in inspect.getargvalues(inspect.currentframe()).locals.items() if k != 'self'}
        cam = Camera(_parent=self, **kwargs)
        self.components[cam.uri] = cam
        return self.components[cam.uri]

    # add CollectionFactory componenet
    def addCollectionFactory(self,id : str , prototype : str = "" , load_dynamically : bool = False , dynamic_prototype  : bool = False):
        kwargs = {k: v for k, v in inspect.getargvalues(inspect.currentframe()).locals.items() if k != 'self'}
        collectionFactory = CollectionFactory(_parent=self, **kwargs)
        self.components[collectionFactory.uri] = collectionFactory
        return self.components[collectionFactory.uri]

    # add CollectionFactory componenet
    def addCollectionProxy(self,id : str  , collection : str = "" , exclude : bool = False ):
        kwargs = {k: v for k, v in inspect.getargvalues(inspect.currentframe()).locals.items() if k != 'self'}
        print(kwargs)
        collectionProxy = CollectionProxy(_parent=self, **kwargs)
        self.components[collectionProxy.uri] = collectionProxy
        return self.components[collectionProxy.uri]

GameObject.model_rebuild()