def DFS(v, d):  # 방문중 정점, 현재까지의 경로 길이
    global max_dist

    visit[v] = 1  # 정점 방문
    if max_dist < d:  # 최장 경로 갱신
        max_dist = d

    for j in range(1, N+1):  # 방문할 수 있는 정점 순회
        if adj[v][j] == 1 and visit[j] == 0:  # 인접하고 아직 방문하지 않은 정점
            DFS(j, d+1)

    visit[v] = 0  # 방문 가능한 모든 경로를 살펴보기 => 리턴하기 전 방문 체크 회수


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 정점의 수, 간선의 수
    adj = [[0]*(N+1) for _ in range(N+1)]  # 인접 행렬 => 인접 리스트면 좀더 빨라지나?
    for i in range(M):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1
    visit = [0]*(N+1)  # 방문 체크
    max_dist = 0  # 최장 거리

    for i in range(1, N+1):  # 모든 정점에서 출발해보자
        DFS(i, 1)

    print('#{} {}'.format(tc, max_dist))