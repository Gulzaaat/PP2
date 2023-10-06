n, k = [int(i) for i in input().split()]
a = set()
for i in range(k):
    ai, bi = [int(j) for j in input().split()]
    for j in range(ai,n+1,bi):
        if j%7 == 6 or j%7 == 0:
            continue
        a.add(j)
print(len(a))