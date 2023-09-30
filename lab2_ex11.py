x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (abs(x2-x1)==2 and abs(y2-y1)==1) or (abs(x2-x1)==1 and abs(y2-y1)==2):
    print('YES')
else:
    print('NO')
