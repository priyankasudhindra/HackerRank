def solve(s, d, m):
    ans = 0
    for i in range(n - m + 1):
        if sum(s[i:m+i]) == d:
            ans += 1
    return ans

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    dm = input().split()
    d = int(dm[0])
    m = int(dm[1])

    result = solve(s, d, m)
    print(result)