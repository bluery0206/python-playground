"""
Person file
"""

class Person:
    """ Base class for every person """
    def __init__ (self, name:str, age:int, address:str, gender:str) -> None:
        self._name      = name
        self._age       = age
        self._address   = address
        self._gender    = gender

    @property
    def name(self) -> str:
        """ Person's Name """
        return self._name

    @name.setter
    def name(self, name:str) -> None:
        self._name = name

    @property
    def age(self) -> str:
        """ Person's age """
        return self._age

    @age.setter
    def age(self, age:int) -> None:
        self._age = age

    @property
    def address(self) -> str:
        """ Person's address """
        return self._address

    @address.setter
    def address(self, address:str) -> None:
        self._address = address

    @property
    def gender(self) -> str:
        """ Person's gender """
        return self._gender

    @gender.setter
    def gender(self, gender:str) -> None:
        self._gender = gender

    @property
    def details(self) -> str:
        """ Person's Details """
        return f"name:{self._name}, gender:{self._gender}, age:{self.age}, addess:{self.address}"
