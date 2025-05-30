#Armstrong Number - Python Program

#import math
num = int(input())
orig = num
result = 0

while num:
    digit = num % 10
    result = result + (digit * digit * digit) #math.pow(digit, 3) #digit ** 3
    num = num // 10

if result == orig:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
