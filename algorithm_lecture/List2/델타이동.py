arr = [
    [1, 2, 3,],
    [4, 5, 6,],
    [7, 8, 9],
]

# (1,1)
r = 1
c = 1
N = 3
M = 3

# 상하좌우 (고정되어 있지 않다)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 8방향 탐색 (knight 이동)


for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    # if nr < 0 or nr >= N or nc < 0 or nc >= M:
    #     continue
    # print(arr[nr][nc])

    if 0 <= nr < N and 0 <= nc < M:
        print(arr[nr][nc])