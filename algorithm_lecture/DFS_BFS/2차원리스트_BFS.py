# N*N 크기의 배열이 주어졌을 때
# 하나의 시작 1로 부터 붙어져 있는 연속된 1의 개수를 세어보자 (BFS)

"""
7
0000011
0000000
0011100
0010111
0110010
0011100
0000000
"""

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(r,c):
    queue = [(r,c)]
    dist[r][c] = 1 # 출발!

    while queue:
        curr_r, curr_c = queue.pop(0)

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0<= nr <N and 0<= nc <N and arr[nr][nc] == 1 and dist[nr][nc] == 0:
                queue.append((nr, nc))
                dist[nr][nc] = dist[curr_r][curr_c]+1


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[0]*N for _ in range(N)]  # distance

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            BFS(i, j)

for i in dist:
    print(*i)