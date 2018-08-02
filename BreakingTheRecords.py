def breakingRecords(scores):
    i = 0
    min_score = scores[i]
    max_score = scores[i]
    min_count = 0
    max_count = 0

    for i in range(1, n):
        if scores[i] < min_score:
            min_score = scores[i]
            min_count += 1
        elif scores[i] > max_score:
            max_score = scores[i]
            max_count += 1

    return max_count, min_count


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)
for i in result:
    print(i, end=" ")