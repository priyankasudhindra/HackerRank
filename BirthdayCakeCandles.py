def birthdayCakeCandles(ar):
    ar = sorted(ar)
    length = len(ar)
    maxCandle = ar[length - 1]
    numberOfCandles = ar.count(maxCandle)
    return numberOfCandles

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(result)
