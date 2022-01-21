from homework_18.cold_planets import ColdPlanet
from homework_18.hot_planets import HotPlanet
"""The methods call here"""

if __name__ == "__main__":
    Venera = ColdPlanet("Venera", -300, 3000000, "circle")
    Mars = HotPlanet("Planet 767", 510, 450000, "oval")

    Mars.burn()
    Venera.burn()
    Mars.froze()