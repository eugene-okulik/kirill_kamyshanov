example1 = 'результат операции: 42'
example2 = 'результат операции: 54'
example3 = 'результат работы программы: 209'
example4 = 'результат: 2'


def parse_and_increase(data):
    result = int(data.split()[-1]) + 10
    print(result)


parse_and_increase(example1)
parse_and_increase(example2)
parse_and_increase(example3)
parse_and_increase(example4)
