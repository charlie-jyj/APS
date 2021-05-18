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

    # 충전 횟수
    answer = 0

    # 전기 버스의 배터리
    battery = -1

    # 내가 지나친 충전기의 수
    passed_charger = 0

    # 버스가 0~ destination 까지의 길을 떠난다.
    for bus in range(destination+1):

        # 버스는 0에서 연료 만땅
        if bus == 0:
            battery = limit

        # 버스가 길을 가고있다. 1칸 갈 때마다 battery를 -1
        elif bus < destination:
            battery -= 1

            # 버스가 충전기를 만났고 이 충전기는 마지막 충전소가 아니다.
            if road[bus] > 0 and passed_charger < stops_length - 1:

                # 남은 배터리 < 지금 충전기에서 다음 충전기까지 남은 거리 이면 충전한다.
                if battery < stops[passed_charger+1] - stops[passed_charger]:
                    answer += 1
                    battery = limit
                # 충전소를 지나쳤다 +1
                passed_charger += 1

            # 버스가 마지막 충전기를 만났다.
            elif road[bus] > 0 and passed_charger == stops_length - 1:

                # 남은 배터리 < 지금 충전기에서 종착지까지 남은 거리 이면 충전한다.
                if battery < destination - stops[passed_charger]:
                    answer += 1
                    battery = limit

            # 버스가 충전기 없는 정류장에 도착했는데 battery 가 0이라면 여행을 마친다.
            else:
                if battery == 0:
                    answer = 0
                    break

    # 버스가 도착했다.
    print('#{} {}'.format(test_case, answer))