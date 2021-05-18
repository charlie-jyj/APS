def BFS(v):
    queue = []  # 큐
    route = []  # 경로

    queue.append(v)  # 출발지 큐에 저장
    visited[v] = 1  # 출발지 방문 체크
    route.append(v)  # 출발지 경로에 저장

    while queue:  # 큐에 값이 있는 동안 반복

        current = queue.pop(0)  # 현재 방문 중인 노드

        # 노드와 간선으로 연결되어 있는 다른 노드를 순회
        for j in range(len(adj_matrix[current])):

            # 연결되어 있고 방문하지 않았다면
            if adj_matrix[current][j] == 1 and visited[j] == 0:
                queue.append(j)  # 방문을 위해 큐에 저장
                visited[j] = 1  # 방문 체크
                route.append(j)  # 경로 저장

    # 방문 경로 반환
    return route

"""
1
7,8
1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split(','))  # 정점 수, 간선 수
    numbers = list(map(int, input().split(',')))  # 간선 목록

    # 방문 체크 배열
    visited = [0]*(N+1)

    # 인접 행렬
    adj_matrix = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        adj_matrix[numbers[2*i]][numbers[2*i+1]] = 1

    print(BFS(1))
