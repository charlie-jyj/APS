"""
output
#1 12
#2 10
#3 24
#4 31
#5 25
"""
def install(idx, temp_sum):
    global min_sum

    if temp_sum > min_sum:
        return

    if idx == len(cores): # 전선을 다 깔았다
        if temp_sum <= min_sum:
            min_sum = min(temp_sum, min_sum)

    # 이번 코어에 전선을 깔자

    curr_x, curr_y = cores[idx]
    visited[curr_x][curr_y] = idx + 1  # 코어 위치 표시


    for i in range(4):

        # 4방향으로 전선을 깔자
        while True:
            next_x = curr_x + dr[i]
            next_y = curr_y + dc[i]

            if 0 <= next_x < N+2 and 0 <= next_y < N+2:
                pass

    current_core = cores.pop(0)


T=int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[-1]*(N+2)]
    for i in range(N):
        board.append([-1]+list(map(int, input().split()))+[-1])
    board.append([-1]*(N+2))

    visited = [[0]*(N+2) for _ in range(N+2)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    min_sum = 987654321
    cores =[]

    for i in range(2, N):
        for j in range(2, N):
            if board[i][j] == 1:
                cores.append((i,j))

    install(0, 0)