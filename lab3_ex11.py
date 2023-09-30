# «Удалить элемент»
a = input().split()
b = int(input())
for i in range(b+1, len(a)):
    a[i-1] = a[i]
a.pop()
print(*a)