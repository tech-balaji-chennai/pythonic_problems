#Find Positive Or Negative Number - 05 - Solution Code - Python.py

try:
    num = int(input())

    if (num > 0):
        print("Positive")
    elif (num < 0):
        print("Negative")
    else:
        print("Neither Positive Nor Negative")

except ValueError as e:
    print(f"Invalid input. Please enter an integer value")
