from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: None
    max_cargo: None

    def __init__(self, weight, fuel, fuel_consumption,  max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, loaded):
        if self.cargo + loaded > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += loaded

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result

