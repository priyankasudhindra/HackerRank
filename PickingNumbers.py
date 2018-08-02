from collections import Counter

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    d = Counter(a)
    best = 0
    for i in range(99):
        best = max(d[i] + d[i + 1], best)
    return best

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
