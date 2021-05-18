T = int(input())
for testcase in range(1, T+1):

    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 미래에서 오늘까지 가격의 최댓값을 갱신한다.
    for i in range(N-1, -1, -1):

        # 가격 최댓값 갱신
        if prices[i] > max_price:
            max_price = prices[i]

        # 최댓값 보다 작은 가격이라면 팔고 차액을 더한다.
        elif prices[i] < max_price:
            profit += max_price - prices[i]

    print('#{} {}'.format(testcase, profit))