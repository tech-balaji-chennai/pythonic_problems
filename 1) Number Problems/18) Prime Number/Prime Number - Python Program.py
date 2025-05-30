#Prime Number - Python Program

#Logic 1
N = int(input())

if N < 2:
    print("Not Prime Number")
else:
    flag = 0
    for i in range(2, N):
        if (N % i) == 0:
            flag = 1
            break
    
    if flag == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")


#Logic 2 - Trial Division Method
import math
N = int(input())

if N < 2:
    print("Not Prime Number")
else:
    flag = 0
    root = int(math.sqrt(N)) #root = int(math.pow(N, 0.5)) #root = int(N**0.5)
    for i in range(2, root+1):
        if (N % i) == 0:
            flag = 1
            break
    
    if flag == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")
