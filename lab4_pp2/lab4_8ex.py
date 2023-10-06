a = int(input())
numbers = set(range(1, a+1))
sol = numbers
while True:
    b = input()
    if b=='HELP':
        break
    b = {int(x) for x in b.split()}
    if len(sol & b) >len(sol)/2:
        print('YES')
        sol = sol & b
    else:
        print('NO')
        sol = sol & numbers - b
print(' '.join([str(x) for x in sorted(sol)]))