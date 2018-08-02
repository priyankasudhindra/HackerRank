def migratoryBirds(ar):
    bird_count = 0
    bird_id = 0
    for i in range(1,6):
        if ar.count(i) > bird_count:
            bird_count = ar.count(i)
            bird_id = i
        elif ar.count(i) == bird_count:
            bird_id = min(bird_id, i)
        else:
            continue
    return bird_id

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)
    print(result)
