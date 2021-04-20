from random import randint
lst = [randint(10,40) for _ in range(20)]
x = lst
print(lst)
k = int(input('Введите индекс: '))
for i in range(k + 1, len(x)):
    x[i - 1] = x[i]
x.pop()
print(x)

