# «Вставить элемент»
a = [int(s) for s in input().split()]
b, c = [int(s) for s in input().split()]
a.append(0)
for i in range(len(a) - 1, b, -1):
    a[i] = a[i-1]
a[b] = c
print(*a)