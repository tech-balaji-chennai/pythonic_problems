#Split Numbers Into Digits - Python Program

num = int(input())

while (num > 0):
    mod = num % 10
    print(mod)
    num = num // 10
