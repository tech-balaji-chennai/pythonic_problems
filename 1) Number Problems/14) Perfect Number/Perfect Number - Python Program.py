#Perfect Number - Python Program

import math

n = int(input())
result = 1
root = int(math.sqrt(n))

for i in range(2, root+1):
    if n % i == 0:
        if n / i == i:
            result = result + i
        else:
            result = result + i + (n / i)

if result == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
