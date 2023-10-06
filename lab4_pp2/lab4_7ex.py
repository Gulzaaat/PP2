n = int(input())
sol = set(range(1, n + 1))
q = 0
while True:
    q = input()
    if q == "HELP":
        break
    else:
        a = set(list(map(int, q.split())))
        q = input()
        if q == "YES":
            sol = sol & a
        else:
            sol = sol - a
sol = sorted(sol)
print(*sol)