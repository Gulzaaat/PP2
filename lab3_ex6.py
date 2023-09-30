# «Наибольший элемент»
a = [int(i) for i in input().split()]
max_v=a[0]
max_i=0
for i in range(1, len(a)):
    if a[i] > max_v:
        max_v = a[i]
        max_i = i
print(max_v)
print(max_i)