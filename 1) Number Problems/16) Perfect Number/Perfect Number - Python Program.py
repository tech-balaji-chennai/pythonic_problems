#Perfect Number - Python Program

import math

N = int(input())
result = 1
root = int(math.sqrt(N)) #root = int(N**0.5)

for i in range(2, root+1): #Square Root Factorization Method
    if (N % i) == 0:
        if (N / i) == i:
            result = result + i
        else:
            result = result + i + (N / i)

if result == N:
    print("Perfect Number")
else:
    print("Not Perfect Number")
