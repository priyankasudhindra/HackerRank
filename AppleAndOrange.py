def countApplesAndOranges(s, t, a, b, apples, oranges):
    app = []
    orng = []
    app_count = 0
    orng_count = 0
    for i in apples:
        app.append(a + i)

    for j in oranges:
        orng.append(b + j)

    for x in app:
        if s <= x <= t:
            app_count += 1
        else:
            continue
    for y in orng:
        if s <= y <= t:
            orng_count += 1
        else:
            continue
    return (app_count, orng_count)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    result = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(result, end="\n")
