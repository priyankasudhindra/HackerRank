def jumpingOnClouds(c):
    start = 0
    jumps = 0

    while start < n - 1:
        if start + 2 < n and c[start+2] == 0:
            start = start + 2
            jumps += 1
        else:
            start = start + 1
            jumps += 1
    return jumps


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
