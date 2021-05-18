# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


def BFS(r, c):
    # 선형 큐
    Q = [0]*1000000
    front = -1
    rear = 0
    Q[rear] = (r,c)

    dist = [[-1]*(N) for _ in range(N)]
    dist[r][c] = 0

    while front!=rear:
        front += 1
        curr_r, curr_c = Q[front]

        if maze[curr_r][curr_c] == '3':
            return dist[curr_r][curr_c] - 1

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >=N:
                continue

            if maze[nr][nc] != '1' and dist[nr][nc] == -1:
                rear += 1
                Q[rear] = (nr, nc)

    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    stR, stC = search()
    print('#{} {}'.format(tc, BFS(stR, stC)))