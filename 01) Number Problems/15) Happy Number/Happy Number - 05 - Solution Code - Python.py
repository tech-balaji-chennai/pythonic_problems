# Happy Number - 05 - Solution Code - Python

N = int(input())
digit = 0
visit = set()

while N not in visit:
    visit.add(N)
    # print(visit)

    result = 0

    while (N > 0):
        digit = N % 10
        result = result + (digit * digit)
        N = N // 10

    N = result

    if N == 1:
        print("Happy Number")
        break

else:
    print("Not Happy Number")
