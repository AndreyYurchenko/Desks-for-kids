def season(num):
    if num == 12 or 1 <= num <= 2:
        print('Зима')
    elif 3 <= num <= 5:
        print('Весна')
    elif 6 <= num <= 8:
        print('Лето')
    elif 9 <= num <= 11:
        print('Осень')
    else:
        print('Введено неверное значение')


x = int(input('Введите 1-12: '))
season(x)