from typing import Union

import requests
import pandas as pd
from io import StringIO

from car import CarWithPrice, Car


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CarDataLoader(metaclass=Singleton):
    url = 'https://raw.githubusercontent.com/Murcha1990/MLDS_ML_2022/main/Hometasks/HT1/cars_test.csv'

    def __init__(self):
        cars_data = requests.get(self.url).text
        self.cars: list[CarWithPrice] = []
        data = pd.read_csv(StringIO(cars_data), sep=',').to_dict('records')

        for el in data:
            self.cars.append(CarWithPrice(**el))

    def get_car(self, car: Car) -> Union[CarWithPrice, None]:
        keys = car.__dict__.keys()
        current_keys = [v for v in keys if getattr(car, v, None) is not None]
        for car_in_data in self.cars:
            found = True
            for key in current_keys:
                if getattr(car, key, None) != getattr(car_in_data, key, None):
                    found = False
                    break
            if not found:
                continue
            return car_in_data
        return None
