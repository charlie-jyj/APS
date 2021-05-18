import heapq


def dijkstra(adj, start, N):
    dist = [10000000] * (N + 1)
    dist[start] = 0
    heapq.heappush(heap, (0, start))  # 가중치, 정점번호
    while heap:
        d, v = heapq.heappop(heap)

        if dist[v] < d:
            continue

        for u in range(1, N + 1):
            if adj[v][u] != 0:  # 진출하는 간선이 있을 때
                cost = adj[v][u]
                if dist[u] > dist[v] + cost:
                    dist[u] = dist[v] + cost
                    heapq.heappush(heap, (dist[u], u))

    return dist


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())  # N 개의 집, M 개의 도로, X 인수의 집
    adj = [[0]*(N+1) for _ in range(N+1)] # 행: 출발, 열: 도착
    trans_adj = [[0] * (N + 1) for _ in range(N + 1)]  # (전치 행렬) 행:도착, 열: 출발
    heap = []

    for i in range(M):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # 진출 간선 표시
        trans_adj[e][s] = w  # 진입 간선 표시

    # 다익스트라 1 인수네 집에서 돌아가기
    dist_come = dijkstra(adj, X, N)

    # 다익스트라 2 인수네 집으로 가기
    dist_go = dijkstra(trans_adj, X, N)

    max_length = 0
    for i in range(1, N+1):
        sub_total = dist_come[i]+dist_go[i]
        max_length = max(max_length, sub_total)

    print('#{} {}'.format(tc, max_length))