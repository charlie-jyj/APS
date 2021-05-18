def binary_tree(n):  # 이진 탐색 트리를 중위 순회하면 수가 오름차순 되는 것을 이용한다.
    global num

    if n <= N:  # 현재 보고 있는 노드가 N 이하라면, 유효한 노드

        if 2*n <= N:  # 왼쪽 자식 노드
            binary_tree(2*n)

        tree[n] = num  # 트리에 자연수를 기록한다.
        num += 1  # 자연수 1 증가

        if 2*n + 1 <= N:  # 오른쪽 자식 노드
            binary_tree(2*n+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드의 수
    tree = [0] * (N+1)  # 이진 탐색 트리
    num = 1  # 트리에 기록할 자연수
    binary_tree(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))