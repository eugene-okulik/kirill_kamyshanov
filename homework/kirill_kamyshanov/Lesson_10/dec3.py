def art_int(func):
    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, '+')
        elif num1 < 0 or num2 < 0:
            return func(num1, num2, '*')
        elif num1 > num2:
            return func(num1, num2, '-')
        elif num2 > num1:
            return func(num1, num2, '/')
    return wrapper


@art_int
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
