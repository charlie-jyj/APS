def find_set(child):
    if p[child] != child:
        p[child] = find_set(p[child])
    return p[child]


def union(parent, child):
    p[find_set(child)] = find_set(parent)


# 크루스칼 알고리즘 사용
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점의 수, 간선의 수
    p = [i for i in range(V+1)]  # make_set 상호 배타적 집합 생성
    edges = []
    for i in range(E):
        s, e, w = map(int, input().split())
        edges.append((w, s, e))  # 간선 정보 입력
    edges.sort(key=lambda x:x[0])  # 가중치로 오름차순 정렬

    total = 0
    cnt = 0
    for edge in edges:  # 간선을 순회하며 조건에 맞는 간선을 mst에 추가
        cost = edge[0]  # 가중치
        s, e = edge[1], edge[2]  # 정점1, 정점2

        if find_set(s) == find_set(e):  # 정점의 부모가 같다면 간선을 연결했을 때, 사이클이 되므로 무시
            continue

        union(s, e)  # 정점 연결
        total += cost  # 가중치의 합 갱신
        cnt += 1

        if cnt == V:
            break

    print('#{} {}'.format(tc, total))

    """
    prim 으로 풀기
    """

    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for j in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w
        adj[v][u] = w # 무향 그래프에서 MST 구성


    def extract_min(MST, key, v):
        minV = 10000000
        u = 0
        for i in range(1, V+1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]

        return u


    def prim(start, V):
        key = [10000000] * (V+1)
        key[start] = 0
        MST = [0] * (V+1)  # mst 에 포함되어 있는 정점 표시 (visit 처럼)
        pi = [0] * (V+1)

        for _ in range(V):  # 모든 정점이 MST에 포함될 때 까지

            # MST 에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
            u = extract_min(MST, key, V)
            MST[u] = 1
            for v in range(start, V+1):
                if MST[v] == 0 and adj[u][v] != 0:
                    if key[v] > adj[u][v]:
                        key[v] = adj[u][v]
                        pi[v] = u

        return sum(key[start:])

    print('#{} {}'.format(tc, prim(0, V)))





