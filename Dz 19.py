from random import randint
lst1 = [randint(10, 200) for _ in range(10)]
lst2 = [randint(10, 200) for _ in range(10)]
print(lst1)
print(lst2)
print(len(set(lst1) & set(lst2)))


print(len(set(input().split()) & set(input().split())))
