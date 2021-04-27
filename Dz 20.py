v = [
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


# y = []
# for i in v:
#     if i[-1]*item[-2] < 100:
#        y.append((i[0],i[-1]*i[-2]+10))
#     else:
#        y.append((i[0],i[-1]*i[-2]))
#
# print(y)
print(list(map(lambda i: (i[0],i[-1]) if i[-1] * i[-2] > 100 else i[-1] * i[-2] + 10, v)))
# Я так и не врубился куда round() вставлять.
# Времени нет так что хз или потом сам додумаюсь, или на уроке спрошу.