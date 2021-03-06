# 색깔 바꾸기 함수
def change_color(my_stack, color):

    while my_stack:
        s = my_stack.pop()
        s_row = s[0]
        s_col = s[1]
        board[s_row][s_col] = color


# 같은 편 찾기 함수
def find_friend(row, col, me):

    opponent = 2 if me == 1 else 1
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    # 8방향을 보면서 친구가 있는지 본다.
    for i in range(8):
        temp_row = row
        temp_col = col
        stack = []

        # 친구를 찾을 때 까지 반복
        while True:

            temp_row += dr[i]
            temp_col += dc[i]

            if 0 <= temp_row < N and 0 <= temp_col < N:

                if board[temp_row][temp_col] == opponent:  # 가는 길에 적을 발견했다면 좌표를 스택에 저장한다.
                    stack.append([temp_row, temp_col])
                elif board[temp_row][temp_col] == 0:  # 가는 길에 아무 것도 없다.
                    break
                elif board[temp_row][temp_col] == me:  # 친구 발견하면 이제까지 만났던 모든 적들의 색깔을 바꿀 수 있다.
                    change_color(stack, player)
                    break

            else:  # 인덱스를 벗어나면 살펴볼 필요 없다
                break


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0]*N for _ in range(N)]
    stone = [list(map(int, input().split())) for _ in range(M)]

    # 중앙에 돌 놓기
    center = N//2
    board[center][center] = board[center-1][center-1] = 2  # 백
    board[center-1][center] = board[center][center-1] = 1  # 흑

    # 오셀로 가자
    for i in range(len(stone)):
        stone_row = stone[i][1]-1
        stone_col = stone[i][0]-1  # col 값이 먼저 들어오고 배열에 맞추기 위해서는 1 빼야 하는 것 주의
        player = stone[i][2]

        if board[stone_row][stone_col] == 0:
            board[stone_row][stone_col] = player  # 돌을 놓는다.
            find_friend(stone_row, stone_col, player)

    # 돌 세기
    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(test_case, black, white))