def pre_order(n):  # 전위 순회
    global count_child

    if n > 0:  # 유효한 노드
        count_child += 1  # 노드를 방문하면 count 를 + 1 한다
        pre_order(child_left[n])  # 왼쪽 자식으로 주목 노드를 바꾼다
        pre_order(child_right[n])  # 오른쪽 자식으로 주목 노드를 바꾼다


T = int(input())
for tc in range(1, T+1):
    V, N = map(int, input().split())

    child_left = [0]*(V+1)
    child_right = [0]*(V+1)

    edge = list(map(int, input().split()))
    for i in range(V-1):  # 부모 노드를 통해 연결된 자식 노드를 기록한다.
        p, c = edge[2*i], edge[2*i+1]

        if child_left[p] == 0:
            child_left[p] = c
        else:  # 이미 왼쪽 자식에 기록된 자식이 있다면 오른쪽 자식에 기록한다.
            child_right[p] = c

    count_child = -1  # 시작 root 를 빼고 세기 위해 -1 에서 시작
    pre_order(N)

    print('#{} {}'.format(tc, count_child if count_child>0 else 0))  # 이거 안 써서 망하겠다..ㅎ