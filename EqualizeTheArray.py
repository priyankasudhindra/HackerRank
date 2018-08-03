def equalizeArray(arr):

    best = 0

    for i in arr:
        if arr.count(i) > best:
            best = arr.count(i)
            number = i

    while number in arr:
        arr.remove(number)

    return len(arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)