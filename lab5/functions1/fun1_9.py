import math
def volume(r):
    volume=(4/3)* math.pi *(r**3) # volume=(4/3)* 3.14 *(r**3)
    return volume

ans=volume(int(input()))
print (ans)