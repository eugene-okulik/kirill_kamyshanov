import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1 Создайте студента (student)
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Андрей', 'Болконский', NULL)")
student_id = cursor.lastrowid
print(f'student_id: {student_id}') # убрать перед сдачей

# 2 Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(query, [
    ('Как устроена экономика', student_id),
    ('Заповедники России', student_id),
    ('Основы геометрии', student_id)
])
book_id1 = cursor.lastrowid
book_id2 = book_id1 - 1
book_id3 = book_id1 - 2
print(f'айди книг добавлены криво. book_id1: {book_id1}, book_id2: {book_id2}, book_id3: {book_id3}')

# 3 Создайте группу (group) и определите своего студента туда
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('6Б', 'сентябрь 25', 'июнь 26')")
group_id = cursor.lastrowid
print(f'group_id: {group_id}') # убрать перед сдачей
query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query, (group_id, student_id))

# 4 Создайте несколько учебных предметов (subjects)
subjects = ['Алгебра', 'Английский язык', 'Информатика']
subject_ids =[]
for subject in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subject,))
    subject_ids.append(cursor.lastrowid)
subject1, subject2, subject3 = subject_ids
print(f'subject1: {subject1}, subject2: {subject2}, subject3: {subject3}')


# 5 Создайте по два занятия для каждого предмета (lessons)
lessons = ['Теорема Пифагора', 'Квадратные уравнения', 'Прошедшие времена в английском',
           'Разговорная практика', 'Системы счисления', 'Основы веб-вёрстки']
lesson_ids = []
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

for subject in subject_ids:
    for lesson in lessons:
        # for count in range(2):
            cursor.execute(query, (lesson, subject))
            print(f'lesson: {lesson}, subject: {subject}')





# query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
# cursor.executemany(query, [
#     ('Теорема Пифагора', subject1),
#     ('Квадратные уравнения', subject1),
#     ('Прошедшие времена в английском', subject2),
#     ('Разговорная практика', subject2),
#     ('Системы счисления', subject3),
#     ('Основы веб-вёрстки', subject3)
# ])
# print('Лессоны не занесены в айдишники')


# 6 Поставьте своему студенту оценки (marks) для всех созданных вами занятий



# query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (2, 74773, 22289)"
# INSERT INTO marks (value, lesson_id, student_id) VALUES (2, 74773, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 74774, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 74775, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 74776, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 74777, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 74778, 22289)


db.close() # не забыть добавить коммит

# Важно: никакие id не хардкодить!
# Все нужные вашей программе id нужно сохранять в переменные сразу после добавления данных в базу
# и потом ими пользоваться.
# При получении данных, распечатывайте эти данные.




# 1 Создайте студента (student)
# INSERT INTO students (name, second_name, group_id) VALUES ('Wowa', 'Ivanov', NULL)
#
# 2 Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
# INSERT INTO books (title, taken_by_student_id) VALUES ('Как устроена экономика', 22289)
# INSERT INTO books (title, taken_by_student_id) VALUES ('Заповедники России', 22289)
# INSERT INTO books (title, taken_by_student_id) VALUES ('Основы геометрии', 22289)
#
# 3 Создайте группу (group) и определите своего студента туда
# INSERT INTO `groups` (title, start_date, end_date) VALUES ('6Б', 'сентябрь 25', 'июнь 26')
# UPDATE students SET group_id = 21985 WHERE student_id = 22289
#
#
# 4 Создайте несколько учебных предметов (subjects)
# INSERT INTO subjects (title) VALUES ('Алгебра')
# INSERT INTO subjects (title) VALUES ('Английский язык')
# INSERT INTO subjects (title) VALUES ('Информатика')
#
# 5 Создайте по два занятия для каждого предмета (lessons)
# INSERT INTO lessons (title, subject_id) VALUES ('Теорема Пифагора', 13815)
# INSERT INTO lessons (title, subject_id) VALUES ('Квадратные уравнения', 13815)
# INSERT INTO lessons (title, subject_id) VALUES ('Прошедшие времена в английском', 13816)
# INSERT INTO lessons (title, subject_id) VALUES ('Разговорная практика', 13816)
# INSERT INTO lessons (title, subject_id) VALUES ('Системы счисления', 13817)
# INSERT INTO lessons (title, subject_id) VALUES ('Основы веб-вёрстки', 13817)
#
# 6 Поставьте своему студенту оценки (marks) для всех созданных вами занятий
# INSERT INTO marks (value, lesson_id, student_id) VALUES (2, 74773, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 74774, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 74775, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 74776, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 74777, 22289)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 74778, 22289)
#
#
# Получите информацию из базы данных:
# 1 Все оценки студента
# SELECT * FROM marks WHERE student_id = 22289
#
# 2 Все книги, которые находятся у студента
# SELECT * FROM books WHERE taken_by_student_id = 22289
#
# 3 Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
# SELECT g.title , b.title , subj.title, l.title, m.value
# FROM `groups` g
# JOIN students s ON s.group_id = g.id
# JOIN books b ON  b.taken_by_student_id = s.id
# JOIN marks m ON m.student_id = s.id
# JOIN lessons l ON m.lesson_id = l.id
# JOIN subjects subj ON subj.id = l.subject_id
# WHERE s.id = 22289