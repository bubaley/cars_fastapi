from typing import Optional

from pydantic import BaseModel


class Car(BaseModel):
    name: Optional[str]
    year: Optional[int]
    km_driven: Optional[int]
    fuel: Optional[str]
    seller_type: Optional[str]
    transmission: Optional[str]
    owner: Optional[str]
    mileage: Optional[str]
    engine: Optional[str]
    max_power: Optional[str]
    torque: Optional[str]
    seats: Optional[float]


class CarWithPrice(Car):
    selling_price: float
