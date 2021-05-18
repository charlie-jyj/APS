# 깊이 우선 탐색
def BFS(row, col):
    queue = list()
    queue.append((row, col))  # 큐에 출발점 저장
    visit[row][col] = 1  # 출발점 방문 체크

    while queue:  # 큐에 값이 있는 동안 반복
        current_row, current_col = queue.pop(0)

        if maze[current_row][current_col] == 3:  # 현재 방문 노드가 3이라면 성공!
            return 1

        # 델타로 사방 순회
        for i in range(4):
            new_row = current_row + dr[i]
            new_col = current_col + dc[i]

            # 테스트 케이스가 1로 둘러져 있어서 인덱스 에러가 나지 않을 것
            # 벽이 아니고 방문한 적이 없는 노드라면 큐에 저장
            if maze[new_row][new_col] != 1 and visit[new_row][new_col] == 0:
                queue.append((new_row,new_col))
                visit[new_row][new_col] = 1  # 방문 체크

    # 결국 찾지 못했다.
    return 0


for test_case in range(1, 10 + 1):
    tc = int(input())
    maze = []
    for _ in range(100):
        maze.append(list(map(int,input())))

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visit = [[0]*100 for _ in range(100)]

    print('#{} {}'.format(test_case, BFS(1,1)))