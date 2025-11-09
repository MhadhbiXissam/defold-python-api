from pydantic import BaseModel


class GameBaseModel(BaseModel):
    def __init__(self, **data):
        kwargs = {k: v for k, v in data.items() if not k.startswith("_")}
        super().__init__(**kwargs)
        {setattr(self, k, v) for k, v in data.items() if k.startswith("_")}