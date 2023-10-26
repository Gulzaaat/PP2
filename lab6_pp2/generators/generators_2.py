n = int(input())
def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for index, b in enumerate(even(n)):
    if index < n // 2:
        print(b, end=', ')
    else:
        print(b)
