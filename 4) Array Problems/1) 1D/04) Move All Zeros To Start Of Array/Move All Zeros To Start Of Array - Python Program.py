#Move All Zeros To Start Of Array - Python Program

#Logic 1 - Naive Approach Using Temporary Array
def move_zeros_to_start_1(arr, n):
    if ((n == 0) or (n == 1)):
        return arr
    
    #temp = [None] * n
    temp = list()
    for i in range(n):
        temp.append(None)
    
    count_zero = 0
    count_non_zero = 0
    
    for i in range(n):
        if (arr[i] != 0):
            temp[count_non_zero] = arr[i]
            count_non_zero = count_non_zero + 1
        else:
            count_zero = count_zero + 1
    
    for i in range(count_zero):
        arr[i] = 0
    
    j = 0
    for i in range(count_zero, n):
        arr[i] = temp[j]
        j = j+1
    
    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))
    
    result = move_zeros_to_start_1(arr, n)
    print(result)


#Logic 2 - Expected Approach Using Two Traversal (Swapping)
def move_zeros_to_start_2(arr, n):
    if ((n == 0) or (n == 1)):
        return arr
    
    end = -1
    
    for i in range(n-1, -1, -1):
        if (arr[i] == 0):
            end = i
            break
    
    for i in range(end-1, -1, -1):
        if (arr[i] != 0):
            arr[i], arr[end] = arr[end], arr[i]
            end = end-1
    
    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))
    
    result = move_zeros_to_start_2(arr, n)
    print(result)
