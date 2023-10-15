def filter_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range (2,n):
        if n%i==0:
            return False
            break
    return True

a=[int(x) for x in input().split()]
for i in range (len(a)):
    if filter_prime(a[i]):
        print (a[i], end=" ")
