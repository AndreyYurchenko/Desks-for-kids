x = [int(y) for y in input().split()]
k = int(input())
for i in range(k + 1, len(x)):
    x[i - 1] = x[i]
x.pop()
print(' '.join([str(i) for i in x]))