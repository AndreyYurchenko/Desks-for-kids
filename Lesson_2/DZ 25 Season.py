def season(num):
    if num == 12 or 1 <= num <= 2:
        return ('Зима')
    elif 3 <= num <= 5:
        return ('Весна')
    elif 6 <= num <= 8:
        return ('Лето')
    elif 9 <= num <= 11:
        return ('Осень')
    else:
        return ('Введено неверное значение')


x = int(input('Введите 1-12: '))
season(x)