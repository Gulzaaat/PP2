# «Четные индексы»
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    if i % 2 == 0:
        print(a[i])