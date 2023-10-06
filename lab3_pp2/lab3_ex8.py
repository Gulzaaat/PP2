# «Количество различных элементов»
a = [int(i) for i in input().split()]
cnt = 0
for i in range(len(a)):
    if i==0 or a[i] != a[i-1]:
        cnt+=1
print(cnt)