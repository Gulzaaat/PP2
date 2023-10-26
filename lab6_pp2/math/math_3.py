import math
s = int(input('Input number of sides: '))
l = int(input('Input the length of a side: '))
area = round(s * (l**2)/(4 * math.tan(math.pi/s)))
print("The area of the polygon is: " + str(area))