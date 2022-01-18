from homework_18.cold_planets import ColdPlanets
from homework_18.hot_planets import HotPlanets
"""The methods call here"""
if __name__ == "__main__":
    Venera = ColdPlanets("Venera", -300, 3000000, "circle")
    Mars = HotPlanets("Planet 767", 510, 450000, "oval")

    Mars.burning()
    Venera.burning()
    Mars.frozen()