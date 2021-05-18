def find_goal(row, col):
    queue = [(row, col)]
    distance[row][col] = 0  # 출발점은 거리 0

    while queue:
        current_row, current_col = queue.pop(0)

        # 도착점을 찾았다면 더이상 헤매일 필요가 없다.
        if maze[current_row][current_col] == 3:
            break

        # 델타로 4 방향 순회
        for i in range(4):
            new_row = current_row + dr[i]
            new_col = current_col + dc[i]

            # 길이고 방문하지 않았다면
            if maze[new_row][new_col] != 1 and distance[new_row][new_col] == -1:
                distance[new_row][new_col] = distance[current_row][current_col] + 1  # 거리 기록
                queue.append((new_row, new_col))


T = int(input())
for test_case in range(1, T + 1):

    N = int(input()) # N*N의 미로

    # 미로 만들기와 벽두르기
    maze = [[1]*(N+2)]
    for _ in range(N):
        maze.append([1]+list(map(int, input()))+[1])
    maze.append([1]*(N+2))

    # 거리 기록
    distance = [[-1]*(N+2) for _ in range(N+2)]

    # 델타 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 출발점, 도착점 찾기
    start = ''
    end = ''
    for i in range(1, N+1):
        if 2 in maze[i]:
            start = (i, maze[i].index(2))
        elif 3 in maze[i]:
            end = (i, maze[i].index(3))

        if start != '' and end != '':
            break

    # 미로 찾기 go!
    find_goal(start[0], start[1])

    # 결과 확인
    result = distance[end[0]][end[1]]  # 출발점 ~ 도착점 거리

    # 지나가야하는 칸 수 = 거리 - 1
    print('#{} {}'.format(test_case, result-1 if result != -1 else 0))

