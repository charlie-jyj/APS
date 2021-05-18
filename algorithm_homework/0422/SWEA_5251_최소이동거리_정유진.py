import heapq

def dijkstra(s, V):
    U = [0]*(V+1)
    U[s] = 1
    D = [100000]*(V+1)
    for v in range(V+1):
        D[v] = adj[s][v]

    while len(V) != V:
        for _ in range(V):
            minV = 1000000
            w = 0
            for i in range(V+1):
                if U[i] == 0 and minV > D[i]:
                    minV = D[i]
                    w = i
            U[w] = 1
            
            for v in range(V+1):
                if 0 < adj[w][v] < 1000000:
                    D[v] = min(D[v], D[w]+adj[w][v])


T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())  # 마지막 연결지점 N, 도로의 개수
    adj = [[-1]*(N+1) for _ in range(N+1)]  # 인접 행렬
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # 간선, 가중치 표시

    dist = [10000 for _ in range(N+1)]  # 최소 거리 기록
    heap = []  # 그리디적 접근을 위한 우선순위큐
    dist[0] = 0  # 시작점 초기화
    heapq.heappush(heap, (0, 0))

    while heap:
        d, curr = heapq.heappop(heap)

        if dist[curr] < d:  # 이미 최소 경로를 알고 있다면 지금 pop 한 원소를 무시한다 (중복을 피하는 것)
            continue

        for j in range(N+1):
            if adj[curr][j] != -1:  # 연결되어 있는 정점이라면
                cost = adj[curr][j]
                if dist[j] > dist[curr] + cost:  # 기존의 경로보다 현재 정점을 거쳐서 가는 경로가 더 최소 비용이라면
                    dist[j] = dist[curr] + cost  # 비용 갱신
                    heapq.heappush(heap, (dist[j], j))

    print('#{} {}'.format(tc, dist[N]))