#Sum Of Digits - Python Program

num = int(input())
sum = 0

while num > 0:
    mod = num % 10
    sum = sum + mod
    num = num // 10

print(sum)
