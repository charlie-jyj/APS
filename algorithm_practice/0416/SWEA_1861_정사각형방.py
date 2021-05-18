"""
숫자는 모든 방에 대해 서로 다르기 때문에 나보다 1 큰 방은 아예 없거나 1개가 있을 것 (2개 이상은 아니라는 뜻)
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 방문할 수 있을까?

[아이디어]
1. 각 칸에서 재귀함수 사용해 이동한 칸 수 세기
2. N이 최대 1000, N*N 인 경우 최대 1000000 칸 이동 가능
=> 재귀 함수 사용 불가

1. 반복 구조의 탐색으로 이동해 본다.
2. N 개의 정수가 공백 하나로 구분되어 주어지고 모두 서로 다른 수
3. 갈림길이 생기지 않는다
4. 단순 반복으로 갈 수 있는 칸 만큼 이동한다.
5. 테스트 케이스는 통과해도 N= 1000 이면 시간초과

<효율성과 무관하게 단순반복, DFS, BFS 코드를 만들어보는 연습이 필요하다>

1. N*N 까지 인덱스를 가진 v 배열을 만들고 0으로 초기화
2. 모든 방을 돌면서 A[i][j] 주변에 A[i][j]+1 인 방이 있는지 확인한다
3. 해당하는 방이 있으면 v[A[i][j]] 를 1로 표시한다
4. 연속한 1의 개수 + 1 = 방문할 수 있는 방의 개수
5. max 값이 같을 때는 무시하고 갱신
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]  # 방의 숫자
    counting = [0]*(N*N+1)  # 이동 가능한지 여부를 기록
    dr = [-1, 0, 1, 0]  # 상우하좌 이동
    dc = [0, 1, 0, -1]

    for i in range(N):  # 행 우선 순회
        for j in range(N):
            for k in range(4):  # 현재의 방에서 상우하좌를 살폈을 때, 나의 숫자보다 1 큰 방이 있다면 기록 (이동할 수 있기 때문)
                nr = i + dr[k]
                nc = j + dc[k]

                if 0 <= nr < N and 0 <= nc < N and rooms[i][j] + 1 == rooms[nr][nc]:
                    counting[rooms[i][j]] = 1

    start = 0
    max_length = 0
    i = 0
    
    # 연속한 1의 길이를 세는 반복문
    while i <= N*N:

        if counting[i] == 1:  
            temp_length = 1  # 움직인 거리 + 1 = 방문한 방의 수
            while counting[i]:
                temp_length += 1
                i += 1
                
            # 최댓값 갱신 (최대값이 동일한 경우가 여럿이라면 시작하는 방의 숫자가 가장 작아야 하므로 최댓값이 같을 땐 갱신 X)
            if max_length < temp_length:
                start = i-(temp_length-1)  # 시작 숫자 찾기
                max_length = temp_length

        i += 1

    print('#{} {} {}'.format(tc, start, max_length))