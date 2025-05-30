#Swap Two Numbers - Python Program

#Logic 1 - With Using Temporary Variable
a = int(input())
b = int(input())
temp = 0

temp = a
a = b
b = temp

print(a, b)


#Logic 2 - Without Using Temporary Variable (Arithmetic Operators)
a = int(input())
b = int(input())

a = a + b
b = a - b
a = a - b

print(a, b)


#Logic 3 - Without Using Temporary Variable (XOR Operator)
a = int(input())
b = int(input())

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)


#Logic 4 - Without Using Temporary Variable (Stack (Or) Tuple Unpacking)
a = int(input())
b = int(input())

a,b = b,a

print(a, b)
