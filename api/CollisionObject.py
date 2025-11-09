from __future__ import annotations
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Optional, Dict
from api.GameBaseModel import GameBaseModel

class CollisionObjectType(Enum):
    COLLISION_OBJECT_TYPE_DYNAMIC = 0 #[(displayName) = "Dynamic"];
    COLLISION_OBJECT_TYPE_KINEMATIC = 1 #[(displayName) = "Kinematic"];
    COLLISION_OBJECT_TYPE_STATIC = 2 #[(displayName) = "Static"];
    COLLISION_OBJECT_TYPE_TRIGGER = 3 #[(displayName) = "Trigger"];


class CollisionObject(GameBaseModel):
    id : str 


