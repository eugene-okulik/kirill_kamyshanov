a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'

separator = ': '
a = int(a[a.index(separator) + 2:]) + 10
b = int(b[b.index(separator) + 2:]) + 10
c = int(c[c.index(separator) + 2:]) + 10

print(a)
print(b)
print(c)
