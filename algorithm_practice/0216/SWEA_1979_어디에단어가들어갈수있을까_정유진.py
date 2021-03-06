T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 퍼즐의 길이, 단어의 길이
    puzzle = [list(map(int, input().split())) for i in range(N)]
    answer = 0  # 반환할 답

    # 행, 열에 넣을 수 있는 단어의 자리 수를 저장한다.
    word_length = []

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
                # 0 이상일 때만 자리 수를 저장한다
                if row > 0:
                    word_length.append(row)
                row = 0  # 가로막혔으니 다시 0에서 시작한다.

            # 열 순회
            if puzzle[j][i]:
                col += 1
            else:
                if col > 0:
                    word_length.append(col)
                col = 0

        # 한 행, 한 열 탐색을 마치면 이제까지 쌓인 row 값을 저장한다.
        if row > 0:
            word_length.append(row)
        if col > 0:
            word_length.append(col)

    # 저장한 단어의 길이와 K를 비교해 일치하면 answer 1 증가
    for length in word_length:
        if length == K:
            answer += 1

    print('#{} {}'.format(test_case, answer))



