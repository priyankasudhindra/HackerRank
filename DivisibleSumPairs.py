def divisibleSumPairs(n, k, ar):
    ans = 0
    for i in range(0, n):
        for j in range(1, n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                ans += 1
    return ans



nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
print(result)