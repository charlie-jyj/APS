def BFS(s, e):
    queue = list()
    queue.append(s)
    distance[s] = 0 # 시작점은 거리가 0

    while queue:  # 큐에 값이 있다면 반복

        current = queue.pop(0) # 현재 내가 방문하고 있는 노드

        if current == end:  # 방문하고 있는 노드가 끝점이라면 return 거리
            return distance[end]

        # 방문 노드와 연결되어 있는 노드를 순회한다.
        for j in range(len(adj_matrix[current])):
            if adj_matrix[current][j] == 1 and distance[j] == -1:  # 연결되어 있고 아직 방문하지 않은 노드라면?
                distance[j] = distance[current] + 1  # 출발점 ~ 현재 방문 노드 사이의 거리 + 1
                queue.append(j)  # 방문 예정 노드 저장

    # 결국 끝점에 도달하지 못했다.
    return 0


T = int(input())
for test_case in range(1, T + 1):

    V, E = map(int, input().split())  # 노드 개수, 간선 개수

    adj_matrix = [[0]*(V+1) for _ in range(V+1)]  # 인접 행렬
    for _ in range(E):
        i, j = map(int, input().split())
        adj_matrix[i][j] = 1  # 무방향
        adj_matrix[j][i] = 1

    start, end = map(int, input().split())  # 시작점, 끝점
    distance = [-1]*(V+1)  # 거리 기록용

    print('#{} {}'.format(test_case, BFS(start, end)))



