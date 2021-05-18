name = input('Файл: ')
f = open(name, 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()
