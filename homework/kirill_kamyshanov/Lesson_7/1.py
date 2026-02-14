digit = 9

while True:
    random_digit = int(input('Enter a digit: '))
    if digit != random_digit:
        print('попробуйте снова')
        continue
    print('Поздравляю! Вы угадали!')
    break
