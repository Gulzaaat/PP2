n = int(input())
def div(n):
    for i in range(n):
        if (i % 3 == 0) and (i % 4 == 0):
            yield i

for i in div(n):
    print(i, end=' ')