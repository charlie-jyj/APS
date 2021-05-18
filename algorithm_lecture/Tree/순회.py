"""
5 4
2 1 2 4 4 3 4 5

그려보니 root가 1 아니고 2
"""


def preorder(n):
    if n > 0:
        print(n, end=' ')
        preorder(child1[n])
        preorder(child2[n])


V, E = map(int, input().split())
edge = list(map(int, input().split()))

child1 = [0] * (V+1)  # 부모를 인덱스로 왼쪽 자식 번호 저장
child2 = [0] * (V+1)  # 부모를 인덱스로 오른쪽 자식 번호 저장

parent = [0]*(V+1)  # 자식을 인덱스로 부모 번호 저장

for i in range(E):

    # 부모를 통해 자식 기록하기
    n1, n2 = edge[i*2], edge[i*2+1]
    if child1[n1] == 0:
        child1[n1] = n2
    else:
        child2[n1] = n2

    # 자식을 통해 부모 기록하기
    parent[n2] = n1

# root 찾기
root= 0
for i in range(1, V+1):
    if parent[i] == 0:
        root = i
        break

preorder(root)