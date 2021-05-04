
def is_year_leap(year):
    return year % 4 == 0
    return year % 100 != 0
    return year % 400 == 0


x = int(input('Введите год: '))
print(is_year_leap(x))