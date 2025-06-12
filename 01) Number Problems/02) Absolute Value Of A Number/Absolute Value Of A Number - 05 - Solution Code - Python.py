#Absolute Value Of A Number - 05 - Solution Code - Python

try:
    num = int(input())

    if (num < 0):
        num = -num

    print(num)

except ValueError as e:
    print(f"Invalid input. Please enter an integer value")
