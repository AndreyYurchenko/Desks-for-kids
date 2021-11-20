from random import randint
lst = [randint(10,99) for _ in range(30)]
x = lst
y = 0
for i in range(1, len(x) - 1):
    if x[i - 1] < x[i] > x[i + 1]:
        y += 1
print(lst)
print('Количество чисел которые больше своих соседей :',y)



