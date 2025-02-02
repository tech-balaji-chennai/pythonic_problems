#Armstrong Number - Python Program

num = int(input())
result = 0
orig = num

while num:
    digit = num % 10
    result = result + (digit * digit * digit)
    num = num // 10

if result == orig:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
