"""
Car
"""

class Car():
    """ Base class for Cars"""
    def __init__(self, model:str, color:str, age:int, mileage:int|float) -> None:
        self._model = model
        self._color = color
        self._age = age
        self._mileage = mileage

    @property
    def model(self) -> str:
        """ Car model """
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        self._model = new_model

    @property
    def color(self) -> str:
        """ Car color """
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        self._color = new_color

    @property
    def age(self) -> str:
        """ Car age """
        return self._age

    @age.setter
    def age(self, new_age: str) -> None:
        self._age = new_age

    @property
    def mileage(self) -> str:
        """ Car mileage in miles (m) """
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage: str) -> None:
        self._mileage = new_mileage

    @property
    def mileage_km(self) -> float:
        """ Car's Mileage in kilometers """
        return self._mileage * 1.609344


if __name__ == "__main__":
    car = Car("Toyota", "Red", 10, 100)

    print(f"This color {car.color} {car.model} has run for {car.mileage_km}km in a span of {car.age} years.")
