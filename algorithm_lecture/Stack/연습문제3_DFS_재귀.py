def dfs_recursive(v):
    visit[v] = 1
    path.append(str(v))

    for i in range(len(matrix[v])):
        if matrix[v][i] > 0 and visit[i] < 0:
            dfs_recursive(i)


N, M = map(int, input().split())  # 정점수, 간선수
visit = [-1] * (N+1)  # 방문 여부 표시 1~N
visit[0] = 0  # 0은 쓰지 않는다.
matrix = [[0]*(N+1) for _ in range(N+1)]  # 인접 행렬
start = 1  # 시작할 정점
path = []

# 인접 행렬 만들기 (양방향)
for _ in range(M):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1

dfs_recursive(start)
print(path)