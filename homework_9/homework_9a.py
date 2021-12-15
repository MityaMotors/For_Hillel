""" Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
 которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
  / — разделить (первое на второе). В остальных случаях вернуть строку Not known operation: """


def arithmetic(first_arg: int, second_arg: int, third_arg) -> float:
    if third_arg == "+":
        return first_arg + second_arg
    elif third_arg == "-":
        return first_arg - second_arg
    elif third_arg == "*":
        return first_arg * second_arg
    elif third_arg == "/":
        return first_arg / second_arg
    else:
        return "Not known operation!!!"


first_arg = int(input('Please enter the first argument: '))
second_arg = int(input('Please enter the first argument: '))
third_arg = input('Please enter the operation (for example +, -, *, / ) : ')
print("The result is:", arithmetic(first_arg, second_arg, third_arg))
