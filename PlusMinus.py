def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zero += 1
    pratio = round((positive / n), 6)
    nratio = round((negative / n), 6)
    zratio = round((zero / n), 6)
    print(pratio)
    print(nratio)
    print(zratio)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
