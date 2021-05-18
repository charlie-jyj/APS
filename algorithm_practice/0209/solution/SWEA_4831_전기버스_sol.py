T = int(input())
for test_case in range(1, T + 1):
    # K, N, M
    limit, destination, stops_length = map(int, input().split())
    # 충전기 설치된 정류장 번호
    charge = list(map(int, input().split()))
    # 정류장 표시
    bus_stops = [0] * (destination+1)

    for i in charge:
        bus_stops[i] = 1

    # 버스 위치
    bus = 0
    # 충전 횟수
    answer = 0

    # 1. 최대한 이동한다.
    while True:
        bus += limit

        if bus >= destination:  # 종점에 도착했다면 break
            break

    # 2. 뒤로 -1 씩 가면서 충전기가 있으면 충전한다.
        for i in range(bus, bus-limit, -1):
            if bus_stops[i]:
                answer += 1
                bus = i
                break
    # 3. 제자리로 돌아오면 종점까지 갈 수 없다는 뜻이므로 0을 반환한다.
        else:
            answer = 0
            break




    # 버스가 도착했다.
    print('#{} {}'.format(test_case, answer))