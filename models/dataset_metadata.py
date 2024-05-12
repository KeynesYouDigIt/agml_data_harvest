from pydantic import BaseModel

class DatasetMetadata(BaseModel):
    name: str
    description: str