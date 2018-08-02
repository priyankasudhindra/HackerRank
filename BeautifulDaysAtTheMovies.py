def beautifulDays(i, j, k):
    beautifulNum = []
    for l in range(i, j+1):
        m = l
        rev = 0
        while l > 0:
            rem = l % 10
            rev = (rev * 10) + rem
            l = l // 10
        if abs(rev - m) % k == 0:
            beautifulNum.append(m)
    return len(beautifulNum)


ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
result = beautifulDays(i, j, k)
print(result)