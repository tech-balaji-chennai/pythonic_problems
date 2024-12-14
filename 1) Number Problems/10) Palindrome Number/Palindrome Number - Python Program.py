#Palindrome Number - Python Program

num = int(input())
orig = num
rev = 0

while (num > 0):
    mod = num % 10
    rev = (rev * 10) + mod
    num = num // 10

if (rev == orig):
    print("Palindrome")
else:
    print("Not Palindrome")
