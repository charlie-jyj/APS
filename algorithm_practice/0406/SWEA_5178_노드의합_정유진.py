def post_order(n):
    if n <= N:  # 노드가 N 이하이면 유효한 노드

        n1, n2 = 0, 0  # 자식이 없으면 반환 값이 없으므로 0 으로 초기화

        if 2*n <= N:
            n1 = post_order(2*n)  # 왼쪽 자식 노드의 값이 반환된다.

        if 2*n+1 <= N:
            n2 = post_order(2*n+1)  # 오른쪽 자식 노드의 값이 반환된다.

        tree[n] += (n1 + n2)  # 현재 노드의 값(0)에 자식 노드 값의 합을 더한다. 리프일 경우 0이 더해질 것

        return tree[n]  # 현재 노드 값을 반환한다.


T= int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # 노드의 개수, 리프의 개수, 출력할 노드 번호
    tree = [0]*(N+1)  # 완전 이진 트리

    for i in range(M):  # 리프의 값을 트리에 저장한다.
        node, value = map(int, input().split())
        tree[node] = value

    post_order(1)  # root 1 에서 후위 순회
    print('#{} {}'.format(tc, tree[L]))