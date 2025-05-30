#Fibonacci Series - Python Program

N = int(input())
a = 0
b = 1
c = 0

for i in range(N):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
