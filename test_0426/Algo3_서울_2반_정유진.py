def find_set(x):  # 배타 집합에서 대표 원소 반환
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(a, b):  # 배타 집합을 통합
    p[find_set(b)] = find_set(a)


def get_minimum():  # 아직 방문 안 한 정점 중 거리 값 최소 정점 찾기
    min_V = -1
    min_val = 987654321

    for i in range(1, V+1):
        if visit[i] == 0 and min_val > dist[i]:
            min_V = i
            min_val = dist[i]

    return min_V


T = int(input())
for tc in range(1, T+1):
    V, E, M = map(int, input().split())
    edges = []  # 간선
    result1 = []  # 최소 신장 트리 포함
    answer1 = 0  # plan A 결과
    p = [i for i in range(V+1)]  # 대표 원소

    adj = [[0]*(V+1) for _ in range(V+1)]  # 인접 행렬
    visit = [0] * (V+1)  # 방문 체크
    dist = [10000000] * (V+1)  # 최소 거리 표시
    queue = []
    result2 = set()  # 최소 신장 트리 포함
    answer2 = 0  # plan B 결과

    for i in range(E):  # 간선과 인접 행렬 값 채우기
        s, e, w = map(int, input().split())
        edges.append((w, s, e))
        adj[s][e] = w
        adj[e][s] = w

    edges.sort()  # 간선을 가중치로 오름차순 정렬
    for i in range(E):  # 사이클이 생기지 않는 최소 비용 간선 연결 : 크루스칼
        w, s, e = edges[i]
        if find_set(s) != find_set(e):
            result1.append(edges[i])
            answer1 += w
            union(s, e)

        if len(result1) == (V-1):
            break

    if answer1 <= M:
        print('#{} {}'.format(tc, M-answer1))
    else:  # 플랜 A 실패,
        # 다익스트라로 플랜 B
        dist[1] = 0
        result2.add(1)

        while len(result2) < V:  # 모든 정점 방문 시 까지
            current = get_minimum()
            visit[current] = 1
            result2.add(current)

            for j in range(1, V+1):  # 아직 방문하지 않았고 연결된 정점 중에 현재 정점을 거쳐갈 때에 비용이 더 작은 경우
                if adj[current][j] != 0 and visit[j] == 0 and dist[j] > dist[current]+adj[current][j]:
                    dist[j] = dist[current]+adj[current][j]

        answer2 = dist[V]
        if answer2 <= M:  # plan B 성공
            print('#{} {}'.format(tc, M-answer2))
        else:  # 모든 계획 실패 시
            print('#{} {}'.format(tc, -1))


