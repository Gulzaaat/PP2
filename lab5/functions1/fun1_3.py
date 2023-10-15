def solve():
    numheads = int(input())
    numlegs = int(input())
    a = int()
    b = int()
    b = (numlegs - 2*numheads) / 2
    a = numheads - b
    print(a, b)
solve()