x = input('Введите строку: ')
y = input('Введите символ: ')
b = -1
while True:
    b = x.find(y, b + 1)
    if b == -1:
        break
    else:
        print(b)
