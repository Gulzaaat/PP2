def reversed(w):
    s = w.split()[::-1]
    l = []
    for i in s:
        l.append(i)
    return " ".join(l)
w = input()
print(reversed(w))