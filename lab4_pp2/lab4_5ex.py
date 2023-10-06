def a(b):
    print(len(b))
    print(*[str(item) for item in sorted(b)])

N, M = [int(s) for s in input().split()]
c1, c2 = set(), set()
for i in range(N):
    c1.add(int(input()))
for i in range(M):
    c2.add(int(input()))
    
a(c1 & c2)
a(c1 - c2)
a(c2 - c1)