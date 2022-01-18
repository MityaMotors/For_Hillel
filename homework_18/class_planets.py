from abc import ABC

class Planet(ABC):
    def __init__(self, name: str, temperature: int, size: int, shape: str) -> None:
        self.name = name
        self.temperature = temperature
        self.size = size
        self.shape = shape

    def burning(self):
       ...

    def frozen(self):
        raise Exception(f"Method {self.frozen.__name__} not implemented in {self.__class__.__name__}")

