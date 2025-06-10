#Sum Of Digits - 05 - Solution Code - Python

num = int(input())
sum = 0
digit = 0

while (num > 0):
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(sum)
