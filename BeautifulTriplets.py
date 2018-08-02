n, d = map(int, input().split())
a = list(map(int, input().split()))
s = set(a)
ans = 0
for i in a:
    if i + d in s and i + 2*d in s:
        ans += 1
print(ans)