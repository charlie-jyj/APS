def DFS(v):
    visited[v] = True

    for i in range(V):
        if adj_arr[v][i] and not visited[i]:
            DFS(i)


V, E = map(int, input().split())

adj_arr = [[0]*V for _ in range(V)]
visited = [False] * V

for _ in range(E):
    a, b = map(int, input().split())
    adj_arr[a][b] = adj_arr[b][a] = 1

DFS(0)