from homework_15.Colors_of_dogs import Colors
class Dog:
    def __init__(
            self,
            weight: int,
            height: int,
            bread_type: str,
            country_of_origin: str,
            year_of_appearance_of_the_breed: int,
            how_many_live: int,
            character: str,
            color:Colors,
    ):
        self._weight = weight
        self._height = height
        self.bread_type = bread_type
        self.country_of_origin = country_of_origin
        self.year_of_appearance_of_the_breed = year_of_appearance_of_the_breed
        self.how_many_live = how_many_live
        self.character = character
        self.color = color

    def jumping(self):
        print("How can the dog jump?")

    def aggresive(self):
        print("Has the dog an agresive behavior?")

if __name__=="__main__":
    mass = Dog(66, 2, "Kolli","England", 1980, 15, "Good", Colors.Black)
    #print(mass.__weight) Closing for Global view Cannot Print
    #print(mass._weight) Protected Atribute, Can Print


