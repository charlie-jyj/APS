T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    answer = 1

    # set()에 값을 담고 length 가 9가 아니면 False
    # 행, 열 검사
    for i in range(9):
        check_row = set()
        check_col = set()
        for j in range(9):
            check_row.add(board[i][j])
            check_col.add(board[j][i])

        if len(check_row) != 9 or len(check_col) != 9:
            answer = 0
            break

    # 구역 검사
    for i in range(0, 7, 3):  # 0, 3, 6
        for j in range(0, 7, 3):  # 0, 3, 6
            check_block = set()

            for x in range(3):  # 0, 1, 2
                for y in range(3):  # 0, 1, 2
                    check_block.add(board[i + x][j + y])

            if len(check_block) != 9:
                answer = 0
                break

    print('#{} {}'.format(test_case, answer))