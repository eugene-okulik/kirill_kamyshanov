my_dict = {
        'tuple': ('some', 'words', 3, False, 2.456),
        'list': ['abobo', 4.56, ['willow', 'nose'], (45, 67, 78), {'props': 'yes', 'mater': 'leather'}],
        'dict': {'name': 'Yan', 'age' : 95, 'occupation': 'plumber', 'hobbies': 'booze', 'is_married': True},
        'set': {'no pain', 'no gain', 604, False, True}
}

print(my_dict['tuple'][-1]) # выведите на экран последний элемент

my_dict['list'].append('one_more]') # добавьте в конец списка еще один элемент
del my_dict['list'][1] # удалите второй элемент списка

my_dict['dict'][('i am a tuple',)] = 'really' # добавьте элемент с ключом ('i am a tuple',) и любым значением
del my_dict['dict']['hobbies'] # удалите какой-нибудь элемент

my_dict['set'].add(7) # добавьте новый элемент в множество
my_dict['set'].remove(False) # удалите элемент из множества

print(my_dict) # В конце выведите на экран весь словарь
