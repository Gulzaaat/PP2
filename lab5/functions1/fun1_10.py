def unique(n):
    arr=[]
    for x in n:
        if x not in arr:
            arr.append(x)
    return arr

n=[int(x) for x in input().split()]
ans=unique(n)
print(ans)