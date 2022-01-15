a = int(input('Please enter the first argument: '))
b = int(input('Please enter the first argument: '))
operation = input('Please enter the operation (for example +, -, *, / ) : ')


def my_sum(func):
    def func_wrapper():
        print("The decorator of Sum:")
        func()

    return func_wrapper


def my_diff(func):
    def fun_wrapper():
        print("The decorator of Diff:")
        func()

    return fun_wrapper


@my_sum
def func_sum():
    if operation == "+":
        print(a + b)
    else:
        print("It's not a sum")


@my_diff
def fun_diff():
    if operation == "-":
        print(a - b)
    else:
        print("It's not a diff")


fun_diff()
func_sum()
