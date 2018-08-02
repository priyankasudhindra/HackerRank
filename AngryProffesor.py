def angryProfessor(k, a):
    late = 0
    on_time = 0
    for i in a:
        if i <= 0:
            on_time += 1
        else:
            late += 1
    if on_time >= k:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)