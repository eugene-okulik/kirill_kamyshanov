import sys

sys.set_int_max_str_digits(1000000)


def fibonacci_genetator(index=10000000):
    n1 = 1
    n2 = 1
    pos = 0
    while pos < index:
        if pos in [0]:
            yield 1
        else:
            n1, n2 = n2, n1 + n2
            yield n1
        pos += 1


count = 1
for i in fibonacci_genetator():
    if count in [5, 200, 1000]:
        print(i)
    elif count == 100000:
        print(i)
        break
    count += 1
