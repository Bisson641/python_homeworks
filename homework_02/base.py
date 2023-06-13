from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    fuel = 0
    started = False
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low fuel please fill")

    def move(self, distance):
        expected_fuel = distance * self.fuel_consumption
        if expected_fuel > self.fuel:
            raise NotEnoughFuel("Not enough fuel to distance")
        else:
            self.fuel -= expected_fuel

