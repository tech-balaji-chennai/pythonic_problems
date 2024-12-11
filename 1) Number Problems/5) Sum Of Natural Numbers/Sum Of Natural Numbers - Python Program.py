#Sum Of Natural Numbers - Python Program


#Logic 1
N = int(input())
sum = 0

for i in range(1,N+1):
    sum += i

print(sum)


#Logic 2
N = int(input())

sum = (N*(N+1)) // 2

print(sum)
