# Classes
# task 1
# class MyClass:
#     def getString(self):
#         self.word=input()
#     def printString(self):
#         print(self.word.upper())
# ans=MyClass()
# ans.getString()
# ans.printString()

# task 2
# class shape():
#     def area(self):
#         return 0

# class square(shape):
#     def __init__(self, length):
#         self.length = length
    
#     def area(self):
#         return self.length**2

# sh = shape()
# s = square(int(input()))
# print(sh.area())
# print(s.area())

# task 3
# class Shape():
#     def area(self):
#         return 0
    
# class rectangle(Shape):
#     def __init__ (self, l, w):
#         self.l = l
#         self.w = w
#     def area(self):
#         return self.l*self.w
    
# r = rectangle(int(input()), int(input()))
# print(r.area())

# task 4
# import math
# class Point():
#     def __init__ (self, x, y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(f"coordinates: ({self.x}, {self.y})")
#     def move(self, x2, y2):
#         self.x=x2
#         self.y=y2
#     def dist(self, point2):
#         dx = self.x - point2.x
#         dy = self.y - point2.y
#         distance = math.sqrt(dx**2 + dy**2)
#         return distance

# point1 = Point(int(input()), int(input()))
# point1.show()
# point1.move(int(input()), int(input()))
# point2 = Point(int(input()), int(input()))

# point1.show()
# point2.show()
# distance = point1.dist(point2)
# print(distance)

# task 5
# class Account:
#   def __init__(self):
#     self.balance = 0
#   def deposit(self):
#     deposit = float(input())
#     self.balance += deposit
#     print(deposit)
#   def withdraw(self):
#     summa = float(input())
#     if self.balance >= summa:
#       self.balance -= summa
#       print(summa)
#     else:
#       print("Insufficient balance")
#   def display(self):
#     print("\n Net Available Balance=", self.balance)
# a = Account()
# a.deposit()
# a.withdraw()
# a.display()

# task 6
def primes(n):
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
ans=list(filter(lambda x: primes(x), a))
print(ans)