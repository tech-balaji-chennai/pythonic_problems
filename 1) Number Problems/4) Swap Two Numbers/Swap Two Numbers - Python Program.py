#Swap Two Numbers - Python Program

a = int(input())
b = int(input())

#Logic 1 - With Using Temporary Variable
temp = a
a = b
b = temp
print(a, b)

#Logic 2 - Without Using Temporary Variable (Stack Or Tuple)
a,b = b,a
print(a, b)

#Logic 3 - With Using xor Operator
