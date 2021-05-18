from collections import deque
import sys


def result():
    global M,N,H
    answer = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 0:
                    return -1
                answer = max(answer, visited[h][n][m])
    return answer


def BFS():
    global M,N,H

    while queue:

        curr_f, curr_r, curr_c = queue.popleft()

        for i in range(6):
            new_floor = curr_f + dh[i]
            new_row = curr_r + dr[i]
            new_col = curr_c + dc[i]

            if 0 <= new_floor < H and 0 <= new_row < N and 0 <= new_col < M and tomato[new_floor][new_row][new_col] == 0 and visited[new_floor][new_row][new_col] == -1:
                visited[new_floor][new_row][new_col] = visited[curr_f][curr_r][curr_c] + 1  # 몇일째인지
                tomato[new_floor][new_row][new_col] = 1  # 토마토가 익는다
                queue.append((new_floor, new_row, new_col))


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[-1]*M for _ in range(N)] for _ in range(H)]
queue = deque()
# 델타, 위 아래 왼쪽 오른쪽 앞 뒤
dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, -1, 1, 0, 0]

is_break = False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1 and visited[h][n][m] == -1:  # 익은 토마토 발견
                queue.append((h,n,m))
                visited[h][n][m] = 0

BFS()

cnt = result()
print(-1 if cnt == -1 else cnt)