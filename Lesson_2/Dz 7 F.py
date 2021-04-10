even = 0
odd = 0

while True:
    a = int(input('Введите число: '))
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    if a <= 0:
        break

print(even, odd)
