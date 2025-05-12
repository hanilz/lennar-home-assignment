from pydantic import BaseModel, Field

from models.package import Package
from utils import calculate_volume


class Truck(BaseModel):
    id: int = 0
    height: float = Field(gt=0, frozen=True)
    width: float = Field(gt=0, frozen=True)
    depth: float = Field(gt=0, frozen=True)
    is_shipped: bool = False
    packages: list[Package] = []
    max_volume: float = Field(default_factory=lambda data: calculate_volume(data['height'], data['width'], data['depth']), frozen=True)
    filled_volume: float = 0
