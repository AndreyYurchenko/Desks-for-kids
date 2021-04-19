from random import randint
lst = [randint(100,199) for _ in range(25)]
c = int(input('Рост нашего Петьки: '))
y = lst
y.sort(reverse=True)
x = 0
while x < len(y) and y[x] >= c:
    x += 1
print(lst)
print('Две недели Петька в строй стать не может! ты номер:',x + 1)
