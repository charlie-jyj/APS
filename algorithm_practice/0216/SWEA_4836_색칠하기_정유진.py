T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 영역의 개수
    board = [[0 for i in range(10)] for j in range(10)]  # 그림판
    colors = []  # 색칠 영역
    for i in range(N):
        colors.append(list(map(int, input().split())))
    purple = 0  # 보라색 칸의 수

    for color in colors:
        paint = color[-1]  # 칠할 색상 값

        x1 = color[0]  # 왼쪽 위 모서리 x
        y1 = color[1]  # 왼쪽 위 모서리 y
        x2 = color[2]  # 오른쪽 아래 모서리 x
        y2 = color[3]  # 오른쪽 아래 모서리 y

        # 그림판에 색칠하기
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] += paint

    # 그림판에 색칠된 값이 빨간색+파란색= 3 이상이면 보라색
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] >= 3:
                purple += 1

    print('#{} {}'.format(test_case, purple))