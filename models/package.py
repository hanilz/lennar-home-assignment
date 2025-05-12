from pydantic import BaseModel, Field
from utils import calculate_volume

class Package(BaseModel):
    id: int = 0
    height: float = Field(gt=0, frozen=True)
    width: float = Field(gt=0, frozen=True)
    depth: float = Field(gt=0, frozen=True)
    volume: float = Field(default_factory=lambda data: calculate_volume(data['height'], data['width'], data['depth']), frozen=True)
    is_shipped: bool = False


