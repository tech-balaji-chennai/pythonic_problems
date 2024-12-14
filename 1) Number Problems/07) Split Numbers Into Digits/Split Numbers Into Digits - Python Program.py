#Split Numbers Into Digits - Python Program

num = int(input())
digit = 0

while (num > 0):
    digit = num % 10
    print(digit)
    num = num // 10
