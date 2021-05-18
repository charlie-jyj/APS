# 1. 기지국을 만났을 때 범위 안의 영역을 모두 X로 바꾸고 변환 후의 배열을 순회하며 H의 개수를 세기
# 2. 집을 만났을 때 반경에 기지국이 있는지 확인하고 없을 경우 answer +1
def change(row, col):

    for k in range(1, ord(city[row][col])-ord('A')+2):
        # 동
        if 0 <= col + k < N and city[row][col+k] == 'H':
            city[row][col+k] = 'X'
        # 서
        if 0 <= col - k < N and city[row][col-k] == 'H':
            city[row][col-k] = 'X'
        # 남
        if 0 <= row + k < N and city[row+k][col] == 'H':
            city[row+k][col] = 'X'
        # 북
        if 0 <= row -k < N and city[row-k][col] == 'H':
            city[row-k][col] = 'X'


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    city = [list(input()) for _ in range(N)]
    station = ['A', 'B', 'C']
    answer = 0

    for i in range(N):
        for j in range(N):
            if city[i][j] in station:
                change(i, j)

    for i in range(N):
        for j in range(N):
            if city[i][j] == 'H':
                answer += 1

    print('#{} {}'.format(test_case, answer))
