PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_dict = PRICE_LIST.split('\n')
my_dict = {item[:item.index(' ')]: int(item[item.index(' ') + 1 : -1]) for item in my_dict}
print(my_dict)
