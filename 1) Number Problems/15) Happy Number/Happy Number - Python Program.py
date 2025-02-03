#Happy Number - Python Program

n = int(input())
digit = 0
visit = set()

while n not in visit:
    #adding resulting number to 'visit' set during the beginning of every iteration
    visit.add(n)
    #print(visit)
    
    #result is initialized to 0 at first
    #resetting result to 0 during the beginning of every iteration
    result = 0

    #finding sum of squares of all digits of resulting number
    while (n > 0):
        digit = n % 10
        result = result + (digit * digit)
        n = n // 10

    #updating n with resulting number for next iteration
    n = result
    
    if n == 1:
        print("Happy Number")
        break

else:
    print("Not Happy Number")
