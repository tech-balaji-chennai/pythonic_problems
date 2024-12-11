#Swap Two Numbers - Python Program

#Logic 1 - With Using Temporary Variable
a = int(input())
b = int(input())

temp = a
a = b
b = temp
print(a, b)


#Logic 2 - Without Using Temporary Variable (Stack Or Tuple)
a = int(input())
b = int(input())

a,b = b,a
print(a, b)

#Logic 3 - With Using xor Operator
