from abc import ABC
"""The abstract class for all planets"""
class Planet(ABC):
    def __init__(self, name: str, temperature: int, size: int, shape: str) -> None:
        self.name = name
        self.temperature = temperature
        self.size = size
        self.shape = shape

    def burn(self):
       ...

    def froze(self):
        raise Exception(f"Method {self.froze.__name__} not implemented in {self.__class__.__name__}")

