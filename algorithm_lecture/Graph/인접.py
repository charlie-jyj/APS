"""
5 (Vertex 갯수인지, 마지막 정점 번호인지 확인) 6 (Edge)
5 6
1 2 1 3 3 2 3 4 2 5 5 4

"""

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
adjList = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1  # 인접
    adj[n2][n1] = 1  # 무향 그래프 (저장 순간에 유향/무향 결정)

    adjList[n1].append(n2)
    adjList[n2].append(n1) # 무향 그래프

for i in range(1, V+1):
    for j in range(1, V+1):
        if adj[i][j]:
            print(i, j)

    for j in adjList[i]:
        print(i, j)


def bfs(s, V):  # 시작점 s, 정점 개수 V
    q = [s] # 큐 생성, 시작점 enqueue
    visited = [0]*(V+1)
    visited[s] = 1

    while q:  # front != rear
        t = q.pop(0)
        print(t)  # do(t)

        for u in range(1, V+1):
            if adj[t][u] == 1 and visited[u] == 0:
                q.append(u)
                visited[u] = visited[t] + 1  # 거리 정보 기록

    print(visited)


bfs(1, V)
