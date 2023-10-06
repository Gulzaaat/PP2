a = []
l = set()
one = set()
for i in range(int(input())):
    k = int(input())
    lan = {input() for j in range(k)}
    one.update(lan)
    if i == 1:
        l.update(lan)
    else:
        l &= lan
print(len(l))
print('\n'.join(sorted(l)))
print(len(one))
print('\n'.join(sorted(one)))
