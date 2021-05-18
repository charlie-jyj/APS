# BFS 로 어찌저찌 해보려 했는데..
# sort 를 할게 아니라 그냥 그때그때 가까운 애를 찾아야 해서... 다시 갈아엎어야겠다..ㅎ

def get_visit():
    global N
    return [ [-1]*N for _ in range(N) ]


def BFS(row, col, target, v):
    queue = [(row, col)]
    v[row][col] = 0

    while queue:
        curr_r, curr_c = queue.pop(0)

        if board[curr_r][curr_c] in target:
            zone.append((board[curr_r][curr_c], curr_r, curr_c, v[curr_r][curr_c]))

        for i in range(4):
            new_r = curr_r + dr[i]
            new_c = curr_c + dc[i]
            if 0<=new_r<N and 0<=new_c<N and v[new_r][new_c]<0 and board[new_r][new_c]!=1:
                queue.append((new_r, new_c))
                v[new_r][new_c] = v[curr_r][curr_c] + 1


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N) ]
    zone = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 1
                BFS(i, j, [3, 4, 5], get_visit())

    zone.sort(key=lambda x:(x[3], x[0]))
    print(zone)

    new_target = [(n, r, c) for n, r, c, d in zone]
    zone = [zone[0]]  # 새롭게 갱신하려
    for i in range(0, 2):
        r, c = new_target[i][1], new_target[i][2]
        BFS(r, c, [new_target[i+1][0]], get_visit())

    print('갱신:',zone)