def charge(idx, cnt):  # 현재 내가 주목하고 있는 정류장, 현재까지의 충전 횟수
    global min_cnt

    if idx >= N:  # 도착
        min_cnt = min(min_cnt, cnt)
        return

    if cnt >= min_cnt:  # 아직 도착하지 않았지만 충전 횟수가 최솟값 보다 크기 때문에 유망하지 않다
        return

    fuel = battery[idx]  # 내가 이 정류장에서 갈 수 있는 최대 이동 수
    for i in range(fuel, 0, -1):  # 가장 멀리가는 것 ~ 1씩 감소시켜 이동
        charge(idx+i, cnt+1)  # 이동 거리만큼 인덱스 증가, 충전 횟수 증가,


T = int(input())
for tc in range(1,T+1):
    battery = list(map(int, input().split()))
    N = battery[0]
    min_cnt = 987654321
    charge(1, -1)  # 출발지는 충전에서 제외하기 때문에 -1로 시작

    print('#{} {}'.format(tc, min_cnt))