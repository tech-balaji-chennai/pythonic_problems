#Palindrome Number - 05 - Solution Code - Python

#Logic 1
num = int(input())
orig = num
rev = 0
digit = 0

while (num > 0):
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

if (rev == orig):
    print("Palindrome")
else:
    print("Not Palindrome")


#Logic 2
num = input()
orig = num
rev = ''

rev = orig[::-1]

if (rev == orig):
    print("Palindrome")
else:
    print("Not Palindrome")
