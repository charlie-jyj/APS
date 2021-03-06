T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for i in range(N)]  # 파리 수가 담긴 2차원 배열
    max_sum = 0  # 반환할 파리 수

    # 파리가 있는 2차원 배열을 행 우선으로 순회하면서 M 구간 안에 있는 파리의 수를 더한다.
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_max = 0
            for k in range(M):
                for l in range(M):
                    temp_max += fly[i+k][j+l]
            # 구간의 총합을 구하고 최댓값을 갱신한다.
            if max_sum < temp_max:
                max_sum = temp_max

    print('#{} {}'.format(test_case, max_sum))