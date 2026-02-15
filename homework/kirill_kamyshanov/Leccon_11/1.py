class Book:
    material = 'бумага'
    is_have_text = True

    def __init__(self, title, author, number_of_sheets, ISBN, is_reserved):
        self.title = title
        self.author = author
        self.number_of_sheets = number_of_sheets
        self.ISBN = ISBN
        self.is_reserved = is_reserved


book1 = Book('Вишнёвый сад', 'А.П.Чехов', '700', '0001', False)
book2 = Book('Долгая прогулка', 'С.Э. Кинг', '299', '0002', False)
book3 = Book('Война и мир', 'Л.Н. Толстой', '2351', '0003', False)
book4 = Book('На западном фронте без перемен', 'Э.М. Ремарк', '270', '0004', False)
book5 = Book('Крейсера', 'В.С.Пикуль', '480', '0005', False)

book5.is_reserved = True

books = [book1, book2, book3, book4, book5]

for book in books:
    if book.is_reserved:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.number_of_sheets}, '
              f'материал: {Book.material}, зарезервирована')
    else:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.number_of_sheets}, '
              f'материал: {Book.material}')


class Textbooks(Book):
    def __init__(self, title, author, number_of_sheets, ISBN, is_reserved, subject, group, have_tasks):
        super().__init__(title, author, number_of_sheets, ISBN, is_reserved)
        self.subject = subject
        self.group = group
        self.have_tasks = have_tasks


textbook1 = Textbooks('Обществознание для чайников', 'Е. Огурцов', '367', '6428',
                      False,'Обществознание', '6', True)
textbook2 = Textbooks('Занимательная математика', 'Д. Цифров', '791', '9410',
                      False,'Математика', '2', True)
textbook3 = Textbooks('История России (862-1480гг.)', 'Я. Иванов', '334', '7899',
                      False,'История', '5', False)
textbook4 = Textbooks('How are you doing?', 'К. Степанов', '231', '1152',
                      False,'Английский язык', '3', True)
textbook5 = Textbooks('Основы физики. Как стать поумнее', 'Э. Дроздов', '240', '8800',
                      False,'Физика', '7', True)

textbook3.is_reserved = True


textbooks = [textbook1, textbook2, textbook3, textbook4, textbook5]
for textbook in textbooks:
    if textbook.is_reserved:
        print(f'Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.number_of_sheets}, '
              f'предмет: {textbook.subject}, класс: {textbook.group}, зарезервирована')
    else:
        print(f'Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.number_of_sheets}, '
              f'предмет: {textbook.subject}, класс: {textbook.group}')
