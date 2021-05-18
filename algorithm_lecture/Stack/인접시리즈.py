# 정점의 수, 간선의 수
# 간선의 수 만큼 방복이 되면서 두 개의 정점이 주어진다.
# 정점의 시작 번호가 1 인지 0 인지를 신경써야 한다.


V, E = map(int, input().split())

# V*V 크기 0으로 초기화 된 2차원 리스트를 선언한다.
adj_arr = [[0]*V for _ in range(V)]

# V개의 빈리스트를 선언하여 사용한다.
adj_list = [[] for _ in range(V)]

for i in range(E):
    A, B = map(int, input().split())

    adj_arr[A][B] = 1
    adj_arr[B][A] = 1  # 유향일 때엔 생략

    adj_list[A].append(B)
    adj_list[B].append(A)  # 유향일 때엔 생략

for i in adj_arr:
    print(*i)