# Fibonacci Number - 05 - Solution Code - Python

# Logic 1
N = int(input())
a = 0
b = 1
c = 0

if (N < 0):
    print("Not Fibonacci Number")
else:
    while (N > a):
        c = a + b
        a = b
        b = c
    if (N == a):
        print("Fibonacci Number")
    else:
        print("Not Fibonacci Number")

# Logic 2
import math

N = int(input())

if (N < 0):
    print("Not Fibonacci Number")

else:
    eq_1 = 5 * (math.pow(n, 2)) + 4  # (5*(N**2) + 4)
    eq_2 = 5 * (math.pow(n, 2)) - 4  # (5*(N**2) - 4)
    result_1 = math.pow(int(math.sqrt(eq_1)), 2)  # math.pow(int(math.pow(eq_1, 0.5)), 2) #int(eq_1 ** 0.5) ** 2
    result_2 = math.pow(int(math.sqrt(eq_1)), 2)  # math.pow(int(math.pow(eq_1, 0.5)), 2) #int(eq_2 ** 0.5) ** 2

    if (result_1 == eq_1) or (result_2 == eq_2):
        print("Fibonacci Number")
    else:
        print("Not Fibonacci Number")
