T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ground = [list(map(int, list(input()))) for _ in range(N)]  # 농장

    center = (N-1)//2  # 가운데
    profit = 0  # 수익

    # 가운데를 기준으로 유효한 농작물을 수확한다.
    for i in range(N):
        delta = center - abs(center-i)

        for j in range(center-delta, center+delta+1):
            profit += ground[i][j]

    print('#{} {}'.format(test_case, profit))

