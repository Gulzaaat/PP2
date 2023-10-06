a = 8
x = []
y = []
for i in range(a):
    first, second = [int(s) for s in input().split()]
    x.append(first)
    y.append(second)

true = True
for i in range(a):
    for j in range(i + 1, a):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            true = False

if true:
    print('NO')
else:
    print('YES')