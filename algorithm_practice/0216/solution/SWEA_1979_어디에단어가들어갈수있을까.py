import sys
sys.stdin = open('input_1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt = 0

        # 행을 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1

            if puzzle[i][j] or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열을 검사
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1

            if puzzle[i][j] or i == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(ans)

