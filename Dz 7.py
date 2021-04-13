largest = None
smallest = None
sum_n = 0
n = 0
count = 0
even = 0
v = 0
while True:
    a = int(input('Введите число: '))
    if a == 0:
        break
    if smallest is None or smallest < a:
        smallest = a
    if largest is None or largest > a:
        largest = a
    if a == 0:
        break
    else:
        sum_n += a
        count += 1
    if a % 2 == 0:
        even += 1
    else:
        v += 1

print('Четное число: ',even)
print('нечетное число: ',v)
print('сумма: ', sum_n)
print('количество: ', count)
print('среднее значение:', sum_n / count)
print("Максимум ", largest)
print("Минимум ", smallest)
#Наконецто я зделал это задание (╥﹏╥) вроде все ок......
#Буду благодарен за доп литературу по циклам ибо мне с ними тяжело.
