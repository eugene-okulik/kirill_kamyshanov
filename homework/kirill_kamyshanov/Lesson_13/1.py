import os
import datetime

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
full_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(full_path, 'r', encoding='utf-8') as file:
    data = file.read().split('\n')
    for line in data:
        prepared_str = (line[3:line.index(' -')])
        date = datetime.datetime.strptime(prepared_str, "%Y-%m-%d %H:%M:%S.%f")
        if line.startswith('1'):
            print(date + datetime.timedelta(weeks=1))
        elif line.startswith('2'):
            print(date.strftime('%A'))
        elif line.startswith('3'):
            print((datetime.datetime.now() - date).days)
