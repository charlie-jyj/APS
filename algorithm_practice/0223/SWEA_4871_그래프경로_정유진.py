def find_route(s, e):

    stack = list()
    stack.append(s)  # 시작 노드를 스택에 저장

    while stack:  # 스택에 값이 있다면 반복

        v = stack.pop()  # 방문할 노드를 스택에서 꺼낸다.
        for idx in range(len(adj_matrix[v])):  # 방문 노드와 연결되어 있는 노드를 찾는다.
            if adj_matrix[v][idx] == 1:
                if idx == end:  # 도착 노드와 연결되어 있다면 return 1
                    return 1
                else:  # 도착 노드로 바로 갈 수 없다면 연결된 노드를 모두 스택에 담고 반복한다.
                    stack.append(idx)

    # 스택을 다 비울 때까지 end 노드를 만나지 못했다면 연결되어 있지 않다는 뜻
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # 정점과 간선
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]  # 인접행렬

    for _ in range(E):
        i, j = map(int, input().split())
        adj_matrix[i][j] = 1  # 방향 있을 유

    start, end = map(int, input().split())  # 시작 노드와 종료 노드

    answer = find_route(start, end)

    print('#{} {}'.format(test_case, answer))