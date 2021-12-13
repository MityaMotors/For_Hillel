from homework_15.Class_Dog import Dog
from homework_15.Colors_of_dogs import Colors


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



if __name__ == "__main__":
    mastif = Mastif(5, 1, "Bulmastif", "Germany", 13, 1956, "Kind", Colors.Grey, "Chakki")
    mastif.jumping()
