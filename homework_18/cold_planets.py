from homework_18.class_planets import Planet

class ColdPlanets(Planet):
    def __init__(self, name: str, temperature: int, size: int, shape: str) -> None:
        super().__init__(name, temperature, size, shape)
        self.__burn_front_side = False

    def burning(self):
        self.__burn_front_side = True
        print("The Cold Planet burns just on front side to the Sun")

