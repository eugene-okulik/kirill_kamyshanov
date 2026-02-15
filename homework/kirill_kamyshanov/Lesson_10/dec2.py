def repeat_me(func):
    def wrapper(*args, count=2):
        rep = 1
        while rep <= count:
            func(*args)
            rep += 1
    return wrapper


@repeat_me
def mult(a, b):
    print(a * b)


mult(2, 3, count = 4)


def count(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator


@count(count=4)
def sub(a, b):
    print(a - b)


sub(2, 3)
