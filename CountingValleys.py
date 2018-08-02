def countingValleys(n, s):
    s_num = []
    start = 0
    valley = 0
    for i in s:
        if i == 'U':
            start += 1
            s_num.append(start)
        else:
            start -= 1
            s_num.append(start)
    if s_num[0] == -1:
        valley += 1
    for j in range(1, n - 1):
        if s_num[j] == 0:
            if s_num[j + 1] < 0:
                valley += 1
    return valley


if __name__ == '__main__':
    n = int(input())
    s = input()

    result = countingValleys(n, s)
    print(result)
