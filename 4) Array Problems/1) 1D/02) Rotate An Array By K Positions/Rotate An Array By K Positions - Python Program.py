#Rotate An Array By K Positions - Python Program

#Logic 1 - Normal Method
def right_rotate(arr, n):
    temp = arr[n-1]
    
    for i in range(n-1, 0, -1): #reversed(range(1, n, 1)):
        arr[i] = arr[i-1]
    
    arr[0] = temp

def array_rotate_1(arr, n, k):
    if (n == 0):
        return arr
    
    for i in range(1, k+1):
        right_rotate(arr,n)
    
    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))
    
    k = int(input())
    k = k%n
    
    result = array_rotate_1(arr, n, k)
    print(result)


#Logic 2 - Reversal Method
def reverse(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        start += 1
        arr[end] = temp
        end -= 1

def array_rotate_2(arr, n, k):
    if (n == 0):
        return arr
    
    reverse(arr, 0, n-k-1)
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-1)
    
    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))
    
    k = int(input())
    k = k%n
    
    result = array_rotate_2(arr, n, k)
    print(result)
