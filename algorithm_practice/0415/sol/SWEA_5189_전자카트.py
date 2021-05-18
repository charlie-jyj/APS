"""
순열 만들때 , used 배열을 사용해서
[1] 배열부터 채우도록 하면
0으로 시작하는 순열을 만들 수 있다

"""


def f(i, n):
    global minV

    if i == n:
        s = 0
        for j in range(1, n):
            s += e[p[j-1]][p[j]]  # p[j-1] 에서 p[j]로 이동
        s += e[p[n-1]][0]  # 마지막 구역에서 사무실로 이동

        minV = min(minV, s)

    else:
        for j in range(1, n):
            if v[j] == 0:
                v[j] = 1
                p[i] = j
                f(i+1, n)
                v[j] = 0


T = int(input())
for tc in range(1,T+1):
    N= int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    p = [0]*N  # 순열
    v = [0]*N  # 이미 방문
    v[0] = 1
    minV = 1000  # 최대소모량*최대이동횟수
    f(1,N)
    print(f'#{tc} {minV}')