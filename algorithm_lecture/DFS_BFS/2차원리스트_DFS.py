# N*N 크기의 배열이 주어졌을 때
# 하나의 시작 1로 부터 붙어져 있는 연속된 1의 개수를 세어보자 (DFS)

"""
7
0000011
0000000
0011100
0010111
0110010
0011100
0000000
"""


def DFS(r,c):
    global cnt

    # 해당 arr[r][c] 자리 값이 1 이므로 방문 체크, 카운트 1 증가
    arr[r][c] = 0
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 1

        if nr < 0 or nr >= N or nc < 0 or nc >= N :  # 인덱스 에러 피하기
            continue
        if arr[nr][nc] == 0:  # 0일 때는 체크할 필요 없기 때문
            continue

        DFS(nr, nc)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            DFS(i,j)
            print(cnt)