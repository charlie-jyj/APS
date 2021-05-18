def DFS(row, col):
    stack = list()
    stack.append((row, col))

    while stack:
        current_row, current_col = stack.pop()

        if maze[current_row][current_col] == 3:
            return 1

        if visit[current_row][current_col] == 0:
            visit[current_row][current_col] = 1

            for i in range(4):
                new_row = current_row + dr[i]
                new_col = current_col + dc[i]

                if maze[new_row][new_col] != 1 and visit[new_row][new_col] == 0:
                    stack.append((new_row,new_col))

    return 0


for test_case in range(1, 10 + 1):
    tc = int(input())
    maze = []
    for _ in range(16):
        maze.append(list(map(int,input())))

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visit = [[0]*16 for _ in range(16)]

    print('#{} {}'.format(test_case, DFS(1,1)))