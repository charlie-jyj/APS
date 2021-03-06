T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    is_invalid_1 = False
    is_invalid_2 = False

    # 행, 열 검사
    for i in range(9):
        counting_row = [0] * 10
        counting_col = [0] * 10
        for j in range(9):
            if counting_row[board[i][j]]:
                answer = 0
                is_invalid_1 = True
                break
            else:
                counting_row[board[i][j]] += 1

            if counting_col[board[j][i]]:
                answer = 0
                is_invalid_1 = True
                break
            else:
                counting_col[board[j][i]] += 1

        if is_invalid_1:
            break

    # 구역 검사
    for i in range(0, 7, 3):  # 0, 3, 6
        for j in range(0, 7, 3):  # 0, 3, 6
            counting_block = [0]*10

            for x in range(3):  # 0, 1, 2
                for y in range(3):  # 0, 1, 2
                    if counting_block[board[i + x][j + y]]:
                        answer = 0
                        is_invalid_2 = True
                        break
                    else:
                        counting_block[board[i + x][j + y]] += 1
                if is_invalid_2:
                    break
            if is_invalid_2:
                break
        if is_invalid_2:
            break

    print('#{} {}'.format(test_case, answer))