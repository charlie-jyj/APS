def check_win(N, board):
    # 행 검사
    for i in range(N):
        row_count = 0
        for j in range(N):
            if board[i][j] == 'o':
                row_count += 1
                if row_count == 5:
                    return 'YES'
            else:
                row_count = 0

    # 열 검사
    for j in range(N):
        col_count = 0
        for i in range(N):
            if board[i][j] == 'o':
                col_count += 1
                if col_count == 5:
                    return 'YES'
            else:
                col_count = 0

    # 좌상우하 대각선
    for i in range(N):
        top = 0
        down = 0
        for j in range(0, i+1, 1):

            if i < 4:
                break

            if board[N-1-i+j][j] == 'o':
                down += 1
                if down == 5:
                    return 'YES'
            else:
                down = 0

            if board[j][N-1-i+j] == 'o':
                top += 1
                if top == 5:
                    return 'YES'
            else:
                top = 0

    # 우상좌하 대각선
    for i in range(N):
        top = 0
        down = 0
        for j in range(0, i+1, 1):

            if i < 4:
                break

            if board[j][i-j] == 'o':
                top += 1
                if top == 5:
                    return 'YES'
            else:
                top = 0

            if board[N-1-i+j][N-1-j] == 'o':
                down += 1
                if down == 5:
                    return 'YES'
            else:
                down = 0

    return 'NO'


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    answer = check_win(N, board)

    print('#{} {}'.format(test_case, answer))

