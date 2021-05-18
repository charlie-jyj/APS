import heapq

"""
6 10
0 1 3
0 2 4
1 3 5
2 1 1
2 3 4
2 4 5
3 4 3
3 5 4
4 0 3
4 5 5
"""
v_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

V, E = map(int, input().split())
dist = [100 for _ in range(V)]  # 최소 비용 기록 배열
visit = [0 for _ in range(V)]  # 방문 체크 배열
heap = []
adj = [[0]*V for _ in range(V)]  # 이동 거리를 담은 인접 행렬 
for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w

# 시작 전 준비
dist[0] = 0  # 시작점에서 시작점으로 가는 비용은 0
heapq.heappush(heap, (0, 0))  # (비용:0, 인덱스:0) 시작점을 heap push

# 반복문 시작
while heap:  # 정점을 모두 방문하면 끝

    current = heapq.heappop(heap)  # 주목하는 원소 (최소비용 순서대로 방문)
    if dist[current[1]] < current[0]:  # 중복된 원소가 꺼내졌음을 의미, 이미 더 짧은 경로를 알고 있다면 지금 꺼낸 정점을 무시한다
        continue

    # current 정점에 연결된 정점 순회
    for j in range(V):
        # current 에서 j 정점으로 연결되어 있고, 아직 방문하지 않았고, current 를 거쳐가는 비용이 더 작을 때
        if adj[current[1]][j] > 0 and dist[j] > dist[current[1]] + adj[current[1]][j]:
            
            new_d = dist[current[1]] + adj[current[1]][j]
            dist[j] = new_d  # 비용 갱신
            heapq.heappush(heap, (new_d, j))  # 갱신된 정점 heap push

# 출력
for i in range(V):
    if i != 0:
        print('{} 정점에서 {} 정점으로 가는 최소 비용: {}'.format(v_dict[0],v_dict[i], dist[i]))

