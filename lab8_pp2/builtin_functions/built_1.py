from functools import reduce 

def mult(a, b):
    return a * b

num = input()
n = [int(x) for x in num.split()]
ans = reduce(mult, n)
print(ans)

x = '*'.join(input().split())
print(eval(x))