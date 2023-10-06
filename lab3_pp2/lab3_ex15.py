# «Кегельбан»
a, b = [int(s) for s in input().split()]
c = ['I'] * a
for i in range(b):
    l, r = [int(s) for s in input().split()]
    for j in range(l - 1, r):
        c[j] = '.'
print(''.join(c))