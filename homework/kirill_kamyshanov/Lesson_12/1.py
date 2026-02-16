class Flower:
    stem_color = 'green'

    def __repr__(self):
        return f'{self.name}. Цена: {self.price}, срок жизни: {self.lifetime}'


class Tulip(Flower):
    def __init__(self):
        self.name = 'Тюльпан'
        self.lifetime = 14
        self.price = 150
        self.stem_length = 18
        self.freshness = 3
        self.color = 'red'


class Chamomile(Flower):
    def __init__(self):
        self.name = 'Ромашка'
        self.lifetime = 10
        self.price = 40
        self.stem_length = 7
        self.freshness = 1
        self.color = 'yellow'


class Orchid(Flower):
    def __init__(self):
        self.name = 'Орхидея'
        self.lifetime = 30
        self.price = 250
        self.stem_length = 20
        self.freshness = 2
        self.color = 'pink'


class BunchOfFlowers:
    def __init__(self, name, *flowers):
        self.name = name
        self.flowers = list(flowers)

    def fading_time(self):
        time = [flower.lifetime for flower in self.flowers]
        fading_time = (sum(time) / len(time))
        return f'Время увядания: {fading_time}'

    def establish_cost(self):
        cost = sum([flower.price for flower in self.flowers])
        return f'Цена букета: {cost}'

    def find_by_attr(self, attr, value):
        flowers = [(flower.name, getattr(flower, attr))
                   for flower in self.flowers
                   if getattr(flower, attr) == value]
        if not flowers:
            return f'В букете нет цветов с {attr} == {value}'
        return flowers

    def sort_by_attr(self, attr):
        if not self.flowers:
            print('Букет пуст')
            return
        for flower in self.flowers:
            if not (hasattr(flower, attr)):
                print(f'Атрибут {attr} есть не у всех цветов')
                return
        sorted_flowers = sorted(self.flowers, key=lambda f: getattr(f, attr))
        print(f'Сортировка по {attr}:')
        for flower in sorted_flowers:
            print(flower.name, getattr(flower, attr))
        return


tulip1 = Tulip()
tulip2 = Tulip()
cham1 = Chamomile()
cham2 = Chamomile()
orchid1 = Orchid()
orchid2 = Orchid()

bunch1 = BunchOfFlowers('Первый букет', tulip1, tulip2, cham2, orchid1, orchid2)
