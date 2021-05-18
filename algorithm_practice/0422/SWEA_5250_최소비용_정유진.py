import heapq

def dijkstra(N):
    INF = 100000
    D = [[INF]*N for _ in range(N)]
    U = [[0]*N for _ in range(N)]
    D[0][0] = 0

    for _ in range(N*N):
        wi, wj = 0, 0
        minV = INF

        for i in range(N):
            for j in range(N):
                if U[i][j] == 0 and minV > D[i][j]:
                    minV = D[i][j]
                    wi, wj = i, j
        U[wi][wj] = 1

        for di, dj in [(0,1), (1,0), (0,-1), (-1, 0)]:
            ni, nj = wi + di, wj + dj
            if 0 <= ni < N and 0 <= nj < N and U[ni][nj] == 0 :
                diff = height[ni][nj] if height[ni][nj] > height[wi][wj] else 0
                D[ni][nj] = min(D[ni][nj], D[wi][wj]+diff+1)

        return D[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]  # 높이 정보
    dr = [-1, 0, 1, 0]  # 상우하좌 이동
    dc = [0, 1, 0, -1]
    dist = [[10000000]*N for _ in range(N)]  # 최소 비용 저장 배열
    visit = [[0]*N for _ in range(N)]  # 방문 체크
    heap = []

    dist[0][0] = 0
    heapq.heappush(heap, (0, 0, 0))  # 거리값, 행 인덱스, 열 인덱스

    while heap:  # heap 이 빌 때까지 
        d, r, c = heapq.heappop(heap)
        
        if dist[r][c] < d:  # 이미 짧은 경로를 알고 있다면 이번에 꺼낸 정점을 무시한다
            continue

        for i in range(4):  # 탐색
            nr = r + dr[i]  
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N :

                price = 1 + abs(height[r][c]-height[nr][nc]) if height[r][c] < height[nr][nc] else 1  # 높이 차이가 있을 때 비용이 증가
                if dist[nr][nc] > dist[r][c] + price:  # r,c 를 경유해서 가는 것이 더 유리할 때,
                    dist[nr][nc] = dist[r][c] + price  # 최소 비용을 갱신하고 heap 에 추가
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))

    print('#{} {}'.format(tc, dist[N-1][N-1]))