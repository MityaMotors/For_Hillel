def squere_pairs(numbers: int):
    counter = 0

    while counter < numbers:
        yield counter
        counter +=2

generator = squere_pairs(10)

for counter in generator:
    print(counter**2)