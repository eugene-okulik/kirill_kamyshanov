import csv
import os
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
full_path = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(full_path, 'r', encoding='utf8', newline='') as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

query = """
SELECT s.name,
s.second_name,
g.title,
b.title,
subj.title,
l.title,
m.value
FROM `groups` g
JOIN students s ON s.group_id = g.id
JOIN books b ON  b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects subj ON subj.id = l.subject_id
"""


def read_db():
    cursor.execute(query)
    for line in cursor:
        yield line


file_set = set(tuple(row) for row in file_data)
found_in_db = set()

for db_row in read_db():
    db_row = tuple(db_row)
    if db_row in file_set:
        found_in_db.add(db_row)

missing_data = file_set - found_in_db

if missing_data:
    print('Данные, отсутствующие в БД:')
    for row in missing_data:
        print(row)
else:
    print('Все записи из файла есть в БД')
