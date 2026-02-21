import argparse
import os
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("file", help='file or folder name')
parser.add_argument("-t" ,"--text", help='text of error')
parser.add_argument("-d", "--date", help='date for searching. Format: YYYY-MM-DD HH:MM')
args = parser.parse_args()
print(args.file, args.text, args.date)

# C:\user\data\logs --text WARN



def read_and_split_file(path):
    with open(path, 'r', encoding='utf8') as f:
        data = f.read()
        raw_data = data.split('\n20')
        entries = [raw_data[0]] + ['20' + log for log in raw_data[1:]]
        return entries


def show_context(target_log, text):
    pos = target_log.find(text)
    start = max(0, pos - 50)
    end = min(len(target_log), pos + 50)
    context = target_log[start:end]
    print(f'Контекст: ...{context}...')


def check_date(file_name, logs_list):
    for index, value in enumerate(logs_list, start=1):
        if args.date:
            date = datetime.datetime.strptime(args.date, "%Y-%m-%d %H:%M")
            log_time = datetime.datetime.strptime(value[:23], "%Y-%m-%d %H:%M:%S.%f")
            if date == log_time.replace(second=0, microsecond=0):
                if args.text in value:
                    print(f'Совпадение в файле {file_name}')
                    print(f'Совпадение в логе {index}')
                    print(f'Время: {log_time}')
                    show_context(value, args.text)
                    print('-' * 50)
    return


def search_match_file(file_name, logs_list):
    for index, value in enumerate(logs_list, start=1):
        if not args.text:
            print(value)
            return
        if args.date:
            return check_date(file_name, logs_list)
        if args.text in value:
            print(f'Совпадение в файле {file_name}')
            print(f'Совпадение в логе {index}')
            print(f'Время: {value[:23]}')
            show_context(value, args.text)
            print('-' * 50)





if '/' in args.file or '\\' in args.file:
    print('передана папка')
    files = os.listdir(args.file)
    for file in files:
        full_path = os.path.join(args.file, file)
        data = read_and_split_file(full_path)
        search_match_file(file, data)
else:
    print('передан файл')
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    full_path = os.path.join(base_path, 'eugene_okulik', 'data', 'logs', args.file)
    data = read_and_split_file(full_path)
    search_match_file(args.file, data)


# контекст по символам, а не пл словам
# не оптимизирован код
# поиск по логам верно ли??

# Также, программа должна вывести кусок ошибки, где был найден текст:
# 5 слов до найденного слова, найденное слово, 5 слов после найденного слова.




# команда с папкой и файлом для отладки
# python mad_logsearcher.py C:\Users\1\education\okulik_course\kirill_kamyshanov\homework\ # негативный тест. другая папка
# python mad_logsearcher.py rpe-api-error.2022-02-03.3.log

# файл, текст, дата
# python mad_logsearcher.py rpe-api-error.2022-02-03.3.log --text="Sql query answer" --date="2022-02-03 06:49"
# файл, текст
# python mad_logsearcher.py rpe-api-error.2022-02-03.3.log --text="Sql query answer"
# папка, текст
# python mad_logsearcher.py C:\Users\1\education\okulik_course\kirill_kamyshanov\homework\eugene_okulik\data\logs --text="Sql query answer"
# папка, текст, дата
# python mad_logsearcher.py C:\Users\1\education\okulik_course\kirill_kamyshanov\homework\eugene_okulik\data\logs --text="Sql query answer" --date="2022-02-03 06:49"

# 2022-02-03 01:05:40.459 формат начала (YYYY-MM-DD HH:MM) 16 символов





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