def factory(idx, cost):  # 내가 지금 주목하고 있는 공장, 현재까지의 생산 비용
    global min_cost

    if idx == N:  # 순열이 모두 결정되었다
        min_cost = min(min_cost, cost)  # 최소 생산 비용 갱신
        return

    if cost >= min_cost:  # 순열이 아직 결정되지 않았는데 이미 최소 생산 비용 초과 => 유망하지 않다
        return

    for i in range(N):  # N개의 제품
        if select[i] == -1:  # 아직 다른 공장이 만들지 않은 제품이라면
            select[i] = idx
            factory(idx+1, cost+price[i][idx])  # 제품 결정 + 생산 비용 추가 => 다음 공장
            select[i] = -1  # 초기화


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = [list(map(int, input().split())) for _ in range(N)]  # 각 공장의 상품 별 생산 비용
    select = [-1] * N  # i 상품을 j 공장이 만든다 라고 기록
    min_cost = 987654321  # 최소 생산 비용
    factory(0, 0)  # 0번째 공장으로 시작

    print('#{} {}'.format(tc, min_cost))