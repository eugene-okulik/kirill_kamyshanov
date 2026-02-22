import mysql.connector as mysql
import random

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

# 2 Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
book_titles = ['Как устроена экономика', 'Заповедники России', 'Основы геометрии']
book_data = [(book_title, student_id) for book_title in book_titles]
cursor.executemany(query, book_data)

# 3 Создайте группу (group) и определите своего студента туда
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('6Б', 'сентябрь 25', 'июнь 26')")
group_id = cursor.lastrowid
query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query, (group_id, student_id))

# 4 Создайте несколько учебных предметов (subjects)
subjects = ['Алгебра', 'Английский язык', 'Информатика']
subject_ids = []
for subject in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subject,))
    subject_ids.append(cursor.lastrowid)
subject1, subject2, subject3 = subject_ids

# 5 Создайте по два занятия для каждого предмета (lessons)
lessons = ['Теорема Пифагора', 'Квадратные уравнения', 'Прошедшие времена в английском',
           'Разговорная практика', 'Системы счисления', 'Основы веб-вёрстки']
subjects_for_lessons = [subject1, subject1, subject2, subject2, subject3, subject3]
lesson_ids = []
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
count = 0
for lesson in lessons:
    cursor.execute(query, (lesson, subjects_for_lessons[count]))
    count += 1
    lesson_ids.append(cursor.lastrowid)

# 6 Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
marks_data = [(random.randrange(2, 5), lesson_id, student_id) for lesson_id in lesson_ids]
cursor.executemany(query, marks_data)

# Получите информацию из базы данных:
# 1 Все оценки студента
query = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(query, (student_id,))
student_marks = cursor.fetchall()
print('student marks:')
for mark in student_marks:
    print(mark)

# 2 Все книги, которые находятся у студента
query = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(query, (student_id,))
student_books = cursor.fetchall()
print('student books:')
for book in student_books:
    print(book)

# 3 Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
query = """
SELECT g.title as group_title,
b.title as book_title,
subj.title as subject_title,
l.title as lesson_title,
m.value as mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON  b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects subj ON subj.id = l.subject_id
WHERE s.id = %s
"""

cursor.execute(query, (student_id,))
student_data = cursor.fetchall()
print('student data:')
for data in student_data:
    print(data)

db.commit()
db.close()
