n = int(input())
def square(n):
    for i in range(n):
        if (i*i) <= n:
            yield i * i

for i in square(n):
    print (i)