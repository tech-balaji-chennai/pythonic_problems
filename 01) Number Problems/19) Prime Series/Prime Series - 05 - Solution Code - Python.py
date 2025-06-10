#Prime Series - 05 - Solution Code - Python

import math
N = int(input())

for i in range(2, N+1):
    f=0
    root = int(math.sqrt(i)) #int(math.pow(i, 0.5)) #int(i**0.5)
    for j in range(2, root+1):
        if (i%j)==0:
            f=1
            break
    if f==0:
        print(i, end = " ")
