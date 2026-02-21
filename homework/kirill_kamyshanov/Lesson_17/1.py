import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("file", help='file name')
parser.add_argument("-t" ,"--text", help='text of error')
parser.add_argument("-d", "--date", help='date for searching')
parser.add_argument("--full", help='get full log', action="store_true")
args = parser.parse_args()
print(args.file, args.text, args.date, args.full)

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
full_path = os.path.join(base_path, 'eugene_okulik', 'data', 'logs', args.file)
print(full_path) # путь к конкретному переданному файлу
# C:\user\data\logs --text WARN

def readfile(path):
    with open(path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            yield line


if '/' in args.file or '\\' in args.file:
    print('передана папка')
    files = os.listdir(full_path)
    for file in files:
        readfile(file)
else:
    print('передан файл')
    full_path = os.path.join(base_path, 'eugene_okulik', 'data', 'logs', args.file)
    for line in readfile(full_path):
        print(line)

# команда с папкой и файлом для отладки
# python 1.py C:\Users\1\education\okulik_course\kirill_kamyshanov\homework\eugene_okulik\data\logs
# python 1.py rpe-api-error.2022-02-03.3.log





# Этапы:
# 1 распознать аргументы, которые ввел пользователь
# 2 определить что указал пользователь: файл или папку
# 3 получить содержимое файла (файлов)
# 4 разбить содержимое на блоки и сохранить блоки в переменной
# 5 реализовать поиск по тексту
# 6 настроить удобный вывод результатов
#
# Подсказки:
# Для работы с файловой системой нужно использовать модуль “os”
# для работы с аргументами воспользуйтесь модулем argparse
# Каждый блок лога начинается с времени возникновения ошибки
# Блоки можно хранить в dict, где ключом будет время сообщения
# Для раскраски результатов (если хотите) можно использовать модуль "colorama"