def find_set(x, p):
    while p[x] != x:
        x = p[x]
    return x


def kruskal(N):
    p = [i for i in range(N)]
    L2 = 0
    cnt = 0
    for w, u, v in edge:
        if find_set(u) != find_set(v):
            p[find_set(v)] = find_set(u)
            cnt += 1
            L2 += w
            if cnt == N -1 :  # N-1 개의 간선 선택 완료
                return L2

    return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # 완전 그래프 정리
    adj = [[0]*N for _ in range(N)]  # 인접 행렬
    for i in range(N):
        for j in range(N):
            adj[i][j] = (X[i]-X[j])**2 + (Y[i]-Y[j])**2
            adj[j][i] = adj[i][j]  # 무향 그래프

    edge = []
    for i in range(N):
        for j in range(i+1, N):
            edge.append(((X[i]-X[j])**2 + (Y[i]-Y[j])**2), i , j)
    edge.sort()

