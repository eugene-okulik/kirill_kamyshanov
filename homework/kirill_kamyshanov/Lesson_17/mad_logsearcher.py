import argparse
import os
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("file", help='file or folder name')
parser.add_argument("-t", "--text", help='text of error')
parser.add_argument("-d", "--date", help='date for searching. Format: YYYY-MM-DD HH:MM')
args = parser.parse_args()


# открытие файла, преобразование в список и получение данных с номерами строк
def read_and_split_file(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
        text = ''.join(lines)
    raw_data = text.split('\n20')
    entries = [raw_data[0]] + ['20' + log for log in raw_data[1:]]

    result = []
    current_line = 1
    for entry in entries:
        result.append((current_line, entry))
        current_line += entry.count('\n') + 1

    return result


# отображение контекста ошибки
def show_context(target_log, text):
    target_log = target_log.split()
    text = text.split()
    big_len = len(target_log)
    small_len = len(text)
    for i in range(big_len):
        if target_log[i: i + small_len] == text:
            start = max(0, i - 5)
            end = min(big_len, i + small_len + 5)
            context = ' '.join(target_log[start: end])
            print(f'Контекст: ...{context}...')


# проверка соответствия даты лога переданной дате
def check_date(date, value):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
    log_time = datetime.datetime.strptime(value[:23], "%Y-%m-%d %H:%M:%S.%f")
    if date == log_time.replace(second=0, microsecond=0):
        return True


def search_match_file(file_name, logs_list):
    for start_line, value in logs_list:
        log_time = datetime.datetime.strptime(value[:23], "%Y-%m-%d %H:%M:%S.%f")
        start = f'Совпадение в файле {file_name}\nСовпадение в строке №{start_line}'
        end = '-' * 120

        if not args.text and not args.date:  # нет текста и даты
            print(value)
            print(end)

        elif args.date:  # дата есть
            if check_date(args.date, value):
                print(start)
                print(f'Время: {log_time}')
                if args.text and args.text in value and args.date in value:  # дата с текстом
                    show_context(value, args.text)
                print(end)

        elif args.text and args.text in value and not args.date:  # только текст
            print(start)
            print(f'Время: {value[:23]}')
            show_context(value, args.text)
            print(end)


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
