"""Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата."""


def square_perimetr_diagonal(a: int):
    perimetr = a * 4
    square = a * a
    diagonal = 2 ** (0.5) * a

    result = (perimetr, square, diagonal)

    return result


a = int(input('Please enter side lengh: '))
print(square_perimetr_diagonal(a))
