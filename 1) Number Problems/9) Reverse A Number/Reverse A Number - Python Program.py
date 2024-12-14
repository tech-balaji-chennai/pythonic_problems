#Reverse A Number - Python Program

num = int(input())
rev = 0

while (num > 0):
    mod = num % 10
    rev = (rev * 10) + mod
    num = num // 10

print(rev)
