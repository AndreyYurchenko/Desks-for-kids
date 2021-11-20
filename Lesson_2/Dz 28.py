# Это фиаско ничего не работает как и мой мозг сейчас.Где-то я повернул не туда,а времени с нуля делать нет.(╥﹏╥)
file = open('src_14.txt', encoding='utf-8')
counter = 0
summa = 0
lst = []
for line in file:
    counter += 1
    x = len(line)
    for i in range(x):
        if line[i].isdigit():
            num = int(line[i])
            summa += num
            k = summa / num
            f = line.find(' ')
            j = '{:} {:18} {:<10} {:^30}'.format('Ученик двоечник:', line[f] + line[f: 20], line[0].capitalize() + '.', '%.2f' % k)
            y = '{:1} {:<1} {:>10}'.format(line[f] + line[f: 20], line[0].capitalize() + '.', '%.2f' % k)
            if k < 5:
                lst.append(y.strip('\n'))
                print(j)

            else:
                lst.append(y.strip('\n'))
            break

y = summa / counter
print('Средний бал по классу', y)
# print(lst)
# for f in lst:
#     print('{:1}'.format(f))
file = open('src_14.txt', encoding='utf-8')
counter = 0
summa = 0
lst = []
for line in file:
    counter += 1
    x = len(line)
    for i in range(x):
        if line[i].isdigit():
            num = int(line[i])
            summa += num
            k = summa / counter
            f = line.find(' ')
            if k != 0:
                print('{:18} {:19} {:20}'.format(line[f] + line[f: 20], line[0].capitalize() + '.', '%.2f' % k))
            break
file.close()





