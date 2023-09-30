# «Шеренга»
h = [int(i) for i in input().split()]
x = int(input())
mesto = 1
for i in h:
    if i >= x:
        mesto += 1
    else:
        break
print(mesto)