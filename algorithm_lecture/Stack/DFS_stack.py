def DFS(v):
    stack.append(v)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v)

            for i in range(len(adj_arr[v])):
                if not visited[i] and adj_arr[v][i]:
                    stack.append(i)


V, E = map(int, input().split())

adj_arr = [[0]*V for _ in range(V)]
visited = [False] * V
stack = []

for _ in range(E):
    a, b = map(int, input().split())
    adj_arr[a][b] = adj_arr[b][a] = 1

DFS(0)