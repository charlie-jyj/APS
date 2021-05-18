# 그냥 트리 만들어서 n 을 루트로 전위 순회든 중위 순회든 순회하면 되는거였구만ㅎ

def count_subtree(n):
    global visit_count

    # visit_count += 1  여기에 놓으면 전위 순회 (visit_count 를 0에서 시작해야)
    if not child[n]:  # 자식이 없다면 재귀 종료 (base)
        return

    for i in child[n]:  # 자식의 수 만큼 도는 반복문
        visit_count += 1  # 자식의 수를 센다
        count_subtree(i)  # 자식의 자식을 알기 위한 재귀 호출


T= int(input())
for tc in range(1, T+1):

    E, N = map(int, input().split())  # 간선, 시작할 root
    edge = list(map(int, input().split()))  # 부모, 자식 노드 입력
    child = [[] for _ in range(E+2)]  # 하나의 부모에 자식이 몇명이 있을지 몰라서 빈 배열을 가진 2차원 리스트를 선언했다.
    visit_count = 1  # 서브 트리의 노드 개수를 담을 변수 (root 자신을 포함하므로 1에서 시작한다)

    for i in range(E):  # 반복문을 순회하며 부모 인덱스를 통해 자식 인덱스를 저장한다.
        p, c = edge[2*i], edge[2*i+1]
        child[p].append(c)

    count_subtree(N)  # 자식 노드의 수를 세는 재귀 함수
    print('#{} {}'.format(tc, visit_count))