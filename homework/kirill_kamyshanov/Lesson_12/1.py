class Flower:
    stem_color = 'green'

    def __init__(self, lifetime, stem_length, freshness, color):
        self.lifetime = lifetime
        self.stem_length = stem_length
        self.freshness = freshness
        self.color = color

    def __repr__(self):
        return f'{self.name}. Цена: {self.price}, срок жизни: {self.lifetime}'


class Tulip(Flower):
    def __init__(self, lifetime, stem_length, freshness, color):
        super().__init__(lifetime, stem_length, freshness, color)
        self.name = 'Тюльпан'
        self.price = 150


class Chamomile(Flower):
    def __init__(self, lifetime, stem_length, freshness, color):
        super().__init__(lifetime, stem_length, freshness, color)
        self.name = 'Ромашка'
        self.price = 40


class Orchid(Flower):
    def __init__(self, lifetime, stem_length, freshness, color):
        super().__init__(lifetime, stem_length, freshness, color)
        self.name = 'Орхидея'
        self.price = 250


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


tulip1 = Tulip(20, 15, 6, 'red')
tulip2 = Tulip(18, 19, 5, 'blue')
cham1 = Chamomile(10, 9, 4, 'yellow')
cham2 = Chamomile(11, 11, 3, 'white')
orchid1 = Orchid(39, 25, 2, 'scarlet')
orchid2 = Orchid(35, 29, 1, 'pink')

bunch1 = BunchOfFlowers('Первый букет', tulip1, tulip2, cham2, orchid1, orchid2)
