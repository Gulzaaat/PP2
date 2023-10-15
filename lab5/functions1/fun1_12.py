def histogram(h):
    for i in range(h):
        print("*", end='')
    print('')
h=[int(x) for x in input().split()]
for i in range (len(h)):
    histogram(h[i])