T = int(input())


def BFS(sV):

    # 튜플로 만들면 거리를 수정할 수 없기 때문에 (immutable)
    Q = [[sV, 0]]
    visited = [False] * (V+1)
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)

        if v == eV:
            return  dist

        for i in range(1, V+1):
            if adj_arr[v][i] == 1 and visited[i] == False:
                Q.append([i, dist+1])
                visited[i] = True

    return 0


def BFS2(sV):

    # 튜플로 만들면 거리를 수정할 수 없기 때문에 (immutable)
    Q = [sV]
    visited = [False] * (V+1)
    visited[sV] = True

    dist = 0
    while Q:
        size = len(Q)

        for i in range(size):
            v = Q.pop(0)
            if v == eV:
                return dist

            for i in range(1, V+1):
                if adj_arr[v][i] == 1 and visited[i] == False:
                    Q.append(i)
                    visited[i] = True

        dist += 1

    return 0


for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    sV, eV = map(int, input().split())

    BFS(sV)