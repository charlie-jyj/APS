"""
순열로 구역의 방문 순서를 정한다
p[i] 가 정해질 때 마다 p[i] 까지의 배터리 사용량을 구한다
- p[i-1] 까지의 사용량 s 에 e[p[i-1]][p[i]]
p[N-1] 이 결정되면 e[N-1][0] 을 더해 총 사용량을 계산한다
최솟값과 비교하고 더 작으면 최솟값을 바꾼다
누적해나가는 정보가 있으면 백트래킹 을 할 수 있다 (익숙해지도록 하자)
"""


def f2(i, n, s):
    global minV

    if i == n:  # 중복 연산이 줄어든다
        s += e[p[n-1]][0]
        if minV > s:
            minV = s

    elif minV <= s:  # 백트래킹
        return

    else:
        for j in range(1, n):  # 다음에 갈 구역 결정
            if v[j] == 0:
                v[j] = 1
                p[i] = j
                f2(i+1, n, s+e[p[i-1]][j])
                v[j] = 0


T = int(input())
for tc in range(1,T+1):
    N= int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    p = [0]*N  # 순열
    v = [0]*N  # 이미 방문
    v[0] = 1
    minV = 1000  # 최대소모량*최대이동횟수
    f2(1, N, 0)
    print(f'#{tc} {minV}')