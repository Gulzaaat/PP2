a = int(input())
b = int(input())
def squares(a, b):
    for i in range(a, b+1):
        yield i * i
for i in squares(a, b):
    print(i)