# Move All Zeros To End Of Array - 05 - Solution Code - Python

# Logic 1 - Naive Approach Using Temporary Array
def move_zeros_to_end_1(arr, n):
    if ((n == 0) or (n == 1)):
        return arr

    # temp = [None] * n
    temp = list()
    for i in range(n):
        temp.append(None)

    j = 0

    for i in range(n):
        if (arr[i] != 0):
            temp[j] = arr[i]
            j = j + 1

    for i in range(j, n):
        temp[i] = 0

    for i in range(n):
        arr[i] = temp[i]

    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))

    result = move_zeros_to_end_1(arr, n)
    print(result)


# Logic 2 - Two Traversals
def move_zeros_to_end_2(arr, n):
    if ((n == 0) or (n == 1)):
        return arr

    count = 0

    for i in range(n):
        if (arr[i] != 0):
            arr[count] = arr[i]
            count = count + 1

    for i in range(count, n):
        arr[i] = 0

    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))

    result = move_zeros_to_end_2(arr, n)
    print(result)


# Logic 3 - Expected Approach Using One Traversal (Swapping)
def move_zeros_to_end_3(arr, n):
    if ((n == 0) or (n == 1)):
        return arr

    count = 0

    for i in range(n):
        if (arr[i] != 0):
            arr[i], arr[count] = arr[count], arr[i]
            count = count + 1

    return arr


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))

    result = move_zeros_to_end_3(arr, n)
    print(result)
