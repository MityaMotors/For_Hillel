class Zoo:
    def __init__(
            self,
            address: str,
            type_of: str,
            filming: int,
            foundation: int,
            staff: int,
            cages: float,
            herbivores: int,
            predators: int,
            birds: int,
            area: float,
            country: str,
            max_visitors_per_hour: int,
            price: float,
            rate: float,
    ) -> None:
        self.address = address
        self.type_of = type_of
        self.filming = filming
        self.foundation = foundation
        self.staff = staff
        self.cages = cages
        self.herbivores = herbivores
        self.predators = predators
        self.birds = birds
        self.area = area
        self.country = country
        self.max_visitors_per_hour = max_visitors_per_hour
        self.price = price
        self.rate = rate

    def avarage_square_of_cage(self) -> float:
        return self.area / self.cages


if __name__ == '__main__':
    My_Zoo = Zoo(
        type_of="Contact",
        address='Kyiv',
        filming=1,
        foundation=1995,
        staff=52,
        cages=510,
        herbivores=1850,
        predators=1200,
        birds=2508,
        area=12000,
        country="Ukraine",
        max_visitors_per_hour=10000,
        price=25,
        rate=4.7,
    )
    print(My_Zoo.area)
    print(My_Zoo.cages)
    print(My_Zoo.avarage_square_of_cage())
