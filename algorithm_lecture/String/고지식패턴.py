t = 'A pattern matching algorithm'
p = 'go'


def brute_force_for(t, p):
    n = len(t)
    m = len(p)
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break

        if cnt == m:
            return i
    return -1


def brute_force_while(t, p):
    n = len(t)
    m = len(p)
    i = 0
    j = 0

    while i < n and j < m :

        if t[i] != p[j]:
            i = i-j
            j = -1

        i += 1
        j += 1

    if j == m:
        return i-m  # 패턴이 일치하는 시작 인덱스 반환
    else:
        return -1  # 검색실패


if __name__ == '__main__':
    brute_force_for(t,p)
    brute_force_while(t,p)