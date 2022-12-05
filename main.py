from fastapi import FastAPI
from typing import List, Union

from car import Car, CarWithPrice
from cars_data_factory import CarDataLoader

app = FastAPI()


@app.post("/predict_item")
def predict_item(item: Car) -> float:
    cars_data_loader = CarDataLoader()
    result = cars_data_loader.get_car(item)
    return result.selling_price if result else None


@app.post("/predict_items")
def predict_items(items: List[Car]) -> List[Union[CarWithPrice, None]]:
    cars_data_loader = CarDataLoader()
    results = []
    for item in items:
        result = cars_data_loader.get_car(item)
        results.append(result)
    return results
