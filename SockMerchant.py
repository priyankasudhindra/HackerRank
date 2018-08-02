from collections import Counter


def sockMerchant(n, ar):
    sock_pair = 0
    count_dict = Counter(ar)

    for value in count_dict.values():
        if value % 2 == 0 or value % 2 == 1:
            sock_pair += (value // 2)
    return sock_pair


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
