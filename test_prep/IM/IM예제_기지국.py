# 1. 기지국을 만났을 때 범위 안의 영역을 모두 X로 바꾸고 변환 후의 배열을 순회하며 H의 개수를 세기
# 2. 집을 만났을 때 반경에 기지국이 있는지 확인하고 없을 경우 answer +1
def find_station(row, col):

    delta = [
        [(0, 1), (0, -1), (1, 0), (-1, 0)],
        [(0, 2), (0, -2), (2, 0), (-2, 0)],
        [(0, 3), (0, -3), (3, 0), (-3, 0)]
    ]

    station = ['A', 'B', 'C']

    for i in range(3):
        for j in range(4):
            temp_row = row + delta[i][j][0]
            temp_col = col + delta[i][j][1]

            if 0 <= temp_row < N and 0<= temp_col < N and city[temp_row][temp_col] in station[i:]:
                return True

    return False


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    city = [list(input()) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(N):
            if city[i][j] == 'H':
                if not find_station(i, j):
                    answer += 1

    print('#{} {}'.format(test_case, answer))