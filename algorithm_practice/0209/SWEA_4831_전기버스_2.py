T = int(input())
for test_case in range(1, T + 1):
    limit_destination_stops = list(map(int, input().split()))

    # 한 번 충전으로 이동할 수 있는 정류장 수
    limit = limit_destination_stops[0]
    # 종점
    destination = limit_destination_stops[1]
    # 충전기 설치된 정류장 수
    stops_length = limit_destination_stops[2]
    # 충전기 설치된 정류장 번호
    stops = list(map(int, input().split()))

    # 길을 만든다.
    road = [0] * (destination + 1)

    # 길에 충전기를 세운다.
    for stop in stops:
        road[stop] += 1

    # 배터리
    battery = limit

    # 버스
    bus = 0

    # 정답
    answer = 0

    # 버스는 종점에 도착하지 못했다면 계속 달린다.
    while bus < destination:

        # 버스가 갈 수 있는 만큼 간다
        bus += battery

        # 버스가 종점을 넘어섰다면 멈춘다
        if bus >= destination:
            break

        # 종점까지 아직 멀었다면
        # 현재 위치에 충전기가 있나? 있다면 충전한다.
        if road[bus] > 0:
            battery = limit
            answer += 1
        # 충전기가 없다면 내 뒤에 충전기가 있었나?
        else:
            # 현재 위치에서 -1씩, limit 한도 내에서 발견해야한다. 안 그러면 제자리걷기됨
            for i in range(bus, bus-limit, -1):
                if road[i] > 0:
                    # 내가 지나친 마지막 충전기로 이동, 충전한다.
                    bus = i
                    battery = limit
                    answer += 1
                    break
            # 충전기를 발견하지 못했다면 종점까지 갈 수 없다. while 문 break 한다.
            else:
                answer = 0
                break

    # 충전 횟수 확인
    print('#{} {}'.format(test_case, answer))