def miniMaxSum(arr):
    arr = sorted(arr)
    minSum = 0
    maxSum = 0
    for i in range(0, len(arr)-1):
        minSum += arr[i]
    for i in range(1, len(arr)):
        maxSum += arr[i]
    print(minSum, maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
