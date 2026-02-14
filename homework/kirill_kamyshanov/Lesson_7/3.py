example1 = 'результат операции: 42'
example2 = 'результат операции: 54'
example3 = 'результат работы программы: 209'
example4 = 'результат: 2'

answer_patterns = [example1, example2, example3, example4]


def parse_and_increase(data):
    for i in data:
        result = int(i.split()[-1]) + 10
        print(result)


parse_and_increase(answer_patterns)
