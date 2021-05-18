T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 퍼즐의 길이, 단어의 길이
    puzzle = [list(map(int, input().split())) for i in range(N)]
    answer = 0  # 반환할 답

    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            # 행 순회
            # 행 안에서 1을 만났을 때
            if puzzle[i][j]:
                row += 1
            # 행 안에서 0을 만나서 가로막혔을 때, 이때까지 쌓인 row 의 값 = 넣을 수 있는 단어의 길이
            else:
                # K 와 비교하여 같다면 answer 1 증가
                if row == K:
                    answer += 1
                row = 0  # 가로막혔으니 다시 0에서 시작한다.

            # 열 순회
            if puzzle[j][i]:
                col += 1
            else:
                if col == K:
                    answer += 1
                col = 0

        # 한 행, 한 열 탐색을 마치면 이제까지 쌓인 row 값을 K와 비교한다.
        if row == K:
            answer += 1
        if col == K:
            answer += 1

    print('#{} {}'.format(test_case, answer))



