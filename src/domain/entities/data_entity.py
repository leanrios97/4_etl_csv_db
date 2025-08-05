from pydantic import BaseModel

class DataEntity(BaseModel):
    id: int
    name: str
    value: float