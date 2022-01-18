from homework_18.class_planets import Planet
"""Create a class of the hot planets"""
class HotPlanet(Planet):
    def __init__(self, name: str, temperature: int, size: int, shape: str) -> None:
        super().__init__(name, temperature, size, shape)
        self.__burn_front_side = False
        self.__burn_back__side = False
        self.__burn_left_side = False
        self.__burn_right_side = False

    def burn(self):
        self.__burn_front_side = True
        self.__burn_back__side = True
        self.__burn_left_side = True
        self.__burn_right_side = True
        print("The hot planet is burning now")











    # def __init__(self, name: str, temperature: int, size: int, shape: str) -> None:
    #     super().__init__(name, temperature, size, shape)
    #     self.__burn_front_side = False
    #     self.__burn_back__side = False
    #     self.__burn_left_side = False
    #     self.__burn_right_side = False
    #
    # def turn_around(self):
    #     self.__burn_front_side = True
    #     self.__burn_back__side = True
    #     self.__burn_left_side = True
    #     self.__burn_right_side = True
    #     print("The planet started burn")