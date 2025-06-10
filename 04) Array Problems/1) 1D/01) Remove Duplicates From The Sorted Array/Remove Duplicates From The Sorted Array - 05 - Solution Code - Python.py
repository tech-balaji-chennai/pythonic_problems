# Remove Duplicates From The Sorted Array - 05 - Solution Code - Python

def remove_duplicates(arr, n):
    if ((n == 0) or (n == 1)):
        return n

    len = 0

    for i in range(n - 1):
        if (arr[i] != arr[i + 1]):
            arr[len] = arr[i]
            len += 1

    arr[len] = arr[n - 1]
    len += 1

    return len


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        arr = []
    else:
        arr = list(map(int, input().split(',')))

    result = remove_duplicates(arr, n)
    print(result)
