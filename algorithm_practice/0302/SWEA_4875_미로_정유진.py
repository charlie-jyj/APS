def find_goal(row, col):

    # 델타 이동
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    stack = list()
    stack.append([row, col]) # 출발점을 스택에 저장
    print(stack)

    while stack:
        current = stack.pop()  # 현재 위치
        r = current[0]  # 현재 위치의 행 값
        c = current[1]  # 현재 위치의 열 값

        if visit[r][c] == 0:  # 방문한 적이 없는 노드를 방문한다.
            visit[r][c] = 1

            for i in range(4):

                if maze[r+dr[i]][c+dc[i]] == 3:  # 델타로 사방을 둘러보았을 때 목적지 3이 있다면 성공
                    return 1

                elif maze[r+dr[i]][c+dc[i]] == 0 and visit[r+dr[i]][c+dc[i]] == 0:  # 방문하지 않았고 길이 연결 되어 있으면 방문
                    stack.append([r+dr[i], c+dc[i]])
                    print(stack)

    # 실패
    return 0


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())

    # 미로 만들기 (인덱스 검사 안 하려고 사방에 1로 벽을 둘렀다)
    maze = [[1] * (N+2)]
    for i in range(N):
        maze.append([1] + list(map(int, list(input()))) + [1])
    maze.append([1] * (N+2))

    visit = [[0]*(N+2) for _ in range(N+2)]  # 방문 체크
    is_end = False

    # 미로에서 2를 찾으면 출발
    for i in range(1, N+1):
        for j in range(1, N+1):
            if maze[i][j] == 2:
                result = find_goal(i, j)
                is_end = True
                break

        if is_end:
            break

    print('#{} {}'.format(test_case, result))