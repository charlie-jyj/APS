import sys
sys.stdin = open('input_1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 패딩 만들기
    puzzle = [list(map(int, input().split()))+[0] for _ in range(N)]
    puzzle.append([0]*(N+1))

    ans = 0

    for i in range(N):
        cnt = 0
        # 벽을 한 칸 더 둘렀기 때문에 1 추가
        for j in range(N+1):

            if puzzle[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

        for j in range(N+1):

            if puzzle[j][i]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(ans)


