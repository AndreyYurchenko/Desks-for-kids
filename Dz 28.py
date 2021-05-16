file = open('src_14.txt', encoding='utf-8')
counter = 0
summa = 0
for line in file:
    counter += 1
    x = len(line)
    for i in range(x):
        if line[i].isdigit():
            num = int(line[i])
            summa += num
            k = summa / num
            f = line.find(' ')
            if k < 5:
                print('{} {:18} {:19} {:20}'.format('Ученик двоечник:', line[f] + line[f: 20], line[0].capitalize() + '.', '%.2f' % k))
            break

y = summa / counter
print('Средний бал по классу', y)
