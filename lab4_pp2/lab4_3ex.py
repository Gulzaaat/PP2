a = input().split()
b = input().split()
a = [int(x) for x in a]
b = [int(x) for x in b]
c = sorted(set(a) & set(b))
for i in c:
    print(i, end=" ")