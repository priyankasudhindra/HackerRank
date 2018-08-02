def diagonalDifference(arr):
    primary_row = 0
    primary_column = 0
    secondary_row = 0
    secondary_column = n - 1
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in arr:
        primary_diagonal += arr[primary_row][primary_column]
        primary_row += 1
        primary_column += 1

    for j in arr:
        secondary_diagonal += arr[secondary_row][secondary_column]
        secondary_row += 1
        secondary_column -= 1

    return abs(primary_diagonal - secondary_diagonal)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
