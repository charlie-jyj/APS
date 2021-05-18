def DFS(row, col):
    global is_goal

    visit[row][col] = 1

    if maze[row][col] == 3:
        is_goal = True
        return

    else:
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]

            if maze[new_row][new_col] != 1 and visit[new_row][new_col] == 0:
                DFS(new_row, new_col)


for test_case in range(1, 10 + 1):
    tc = int(input())
    maze = []
    for _ in range(100):
        maze.append(list(map(int,input())))

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    is_goal = False

    visit = [[0]*100 for _ in range(100)]
    DFS(1,1)

    print('#{} {}'.format(test_case, int(is_goal)))