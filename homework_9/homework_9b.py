"""Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата."""


def square_perimetr_diagonal(a):
    perimetr = a * 4
    s = a * a
    diagonal = (a ** 2) / 2
    diagonal = diagonal ** 0.5

    result = (perimetr, s, diagonal)

    return result


a = int(input('Please enter side lengh: '))
print(square_perimetr_diagonal(a))
