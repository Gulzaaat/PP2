# «Уникальные элементы»
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j  and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')