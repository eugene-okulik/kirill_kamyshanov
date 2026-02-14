import random

salary = int(input('Enter your salary:'))
bonus = random.choice([True, False])
bonus_amount = random.randint(1,10000)

if bonus == True:
    increased_salary = salary + bonus_amount
    print(f"{salary}, {bonus} - '${increased_salary}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
