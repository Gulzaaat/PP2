a = input().split()
b = input().split()
c = set(b) & set(a)
print(len(c))