from HW15.Class_Dog import Dog
from HW15.Colors_of_dogs import Colors
from enum import Enum


class Parameter_of_weight(Enum):
    Increase = 1
    Reduce = 1

class Parameter_of_height(Enum):
    Increase = 1
    Reduce = 2

class Mastif(Dog):

    def __init__(self,
                 weight: int,
                 height: int,
                 bread_type: str,
                 country_of_origin: str,
                 year_of_appearance_of_the_breed: int,
                 how_many_live: int,
                 character: str, color: Colors,
                 nickname: str):
        super().__init__(weight, height, bread_type, country_of_origin, year_of_appearance_of_the_breed, how_many_live,
                         character, color)
        self.__nickname = nickname

    def move(self, parameter_of_weight: Parameter_of_weight, amount: int ):
        if parameter_of_weight == Parameter_of_weight.Increase:
            self._weight += amount
        elif parameter_of_weight == Parameter_of_weight.Reduce:
                self._weight -= amount
        else:
            raise Exception ("Error Message")

    def move2(self, parameter_of_height: Parameter_of_height, amount2: int ):
        if parameter_of_height == Parameter_of_height.Increase:
            self._height += amount2
        elif parameter_of_height == Parameter_of_height.Reduce:
                self._height -= amount2
        else:
            raise Exception ("Error Message")

    @property
    def current_mass(self) -> int:
        return self._weight

    @property
    def current_height(self) -> int:
        return self._height

if __name__ == "__main__":
    mastif = Mastif(5, 1, "Bulmastif", "Germany", 13, 1956, "Kind", Colors.Grey, "Chakki")
    print(mastif.current_mass)
    mastif.move(Parameter_of_weight.Reduce, 1)
    print(mastif.current_mass)

    print(mastif.current_height)
    mastif.move2(Parameter_of_height.Increase, 3)
    print(mastif.current_height)