def perm(idx, sub_sum):
    global  ans

    # 유망성 검사
    if sub_sum > N:
        return

    if idx == 3:
        if sub_sum == N:
            cnt = 0

            white = sel[0]
            blue = white + sel[1]

            # 흰색 칠하기
            for i in flag[:white]:
                for j in i:
                    if j!= 'W':
                        cnt += 1

            # 파란색 칠하기
            for i in flag[white:blue]:
                for j in i:
                    if j != 'B':
                        cnt += 1

            # 빨간색 칠하기
            for i in flag[blue::]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            ans = min(ans, cnt)

        return

    # 중복 순열 응용
    # 위 아래로 한 줄 씩 보장한다
    for i in range(1, N-1):
        sel[idx] = i
        perm(idx+1, sub_sum+i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N행, M열

    flag = [list(input()) for _ in range(N)]
    sel = [0] * 3
    ans = 987654321 # 색칠 최솟값

    # (시작 인덱스, 중간 합)
    perm(0, 0)

    print(ans)

################################################################
'''
W, B, R 열 * N 행
각각의 색깔이 아닌 개수를 세고 누적합
'''

for tc in range(1, int(input())+1):
    N. M = map(int, input().split())

    flag = [input() for _ in range(N)]  # 값을 수정할 것이 아니기 때문에 문자열로 둬도 좋다

    W = [0] * N
    B = [0] * N
    R = [0] * N

    # 행을 보면서 나와 다른 색깔의 개수를 카운팅한다.
    for i in range(N):
        for j in range(M):

            if flag[i][j] != 'W':
                W[i] += 1
            if flag[i][j] != 'B':
                B[i] += 1
            if flag[i][j] != 'R':
                R[i] += 1

    # 누적 시킨다
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]


    ans = 987654321

    # i로 흰색을 채울 텐데 파란색과 빨간색은 각각 적어도 1 줄 씩 가져야하기 때문에
    for i in range(N-2):
        # j로 파란색을 채울 것인데 흰색 다음줄부터~ 빨간색 (최소 1줄) 전 까지
        for j in range(i+1, N-1):
            w_cnt = W[i]
            b_cnt = B[j] - B[i]
            r_cnt = R[N-1] - R[j]

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt
