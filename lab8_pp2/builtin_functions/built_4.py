import math
import time

n = int(input())
ms = int(input())
time.sleep(ms/1000)
print('Square root of ', n, ' after ', ms, ' miliseconds is ', math.sqrt(n))
