"""
13 12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""


def preorder(n): # 부모 노드가 매개변수로 들어온다
    if n > 0:  # 그 값이 존재한다면,
        print(n, end='') # 방문한다
        preorder(left_child[n])  # 왼쪽 자식 방문
        preorder(right_child[n])  # 오른쪽 자식 방문


def inorder(n):
    if n > 0:  # 그 값이 존재한다면,
        inorder(left_child[n])  # 왼쪽 자식 방문
        print(n, end='')  # 방문한다
        inorder(right_child[n])  # 오른쪽 자식 방문


def postorder(n):
    if n > 0:  # 그 값이 존재한다면,
        postorder(left_child[n])  # 왼쪽 자식 방문
        postorder(right_child[n])  # 오른쪽 자식 방문
        print(n, end='')  # 방문한다


T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점, 간선
    edge = list(map(int, input().split()))  # 부모, 자식 연결 관계

    left_child = [0]*(V+1)  # 왼쪽 자식 배열
    right_child = [0]*(V+1)  # 오른쪽 자식 배열
    parent = [0]*(V+1)  # 부모 배열

    # 부모와 자식 노드 관계 기록
    for i in range(E):
        p, c = edge[2*i], edge[2*i+1]

        # 부모로 자식 기록하기
        if left_child[p] == 0:
            left_child[p] = c
        else:
            right_child[p] = c

        # 자식으로 부모 기록하기
        parent[c] = p

    # root 찾기
    root = 0
    for i in range(1, V+1):  # 0은 쓰지 않으니 1 부터 시작
        if parent[i] == 0:  # 부모가 없는 자식이라면 == root
            root = i

    preorder(root)  # 전위순회
    print()
    inorder(root)  # 중위순회
    print()
    postorder(root)  # 후위순회

