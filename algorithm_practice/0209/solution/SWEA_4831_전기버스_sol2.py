T = int(input())
for test_case in range(1, T + 1):
    # K, N, M
    limit, destination, stops_length = map(int, input().split())
    # 충전기 설치된 정류장 번호
    charge = list(map(int, input().split()))

    # 마지막 위치
    last = 0
    # 충전 횟수
    answer = 0

    charge = [0] + charge + [destination]

    # 충전소에 출발점과 도착지를 넣어 놓았으므로
    for i in range(1, stops_length+2):

        # 내가 연료를 다 태워도 못가는구나
        if charge[i] - charge[i-1] > limit:
            answer = 0
            break

        # 갈 수 있다면 아무 작업 하지 않는다.
        # 갈 수 없다면 내 바로 직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + limit:
            last = charge[i-1]
            answer += 1

    # 버스가 도착했다.
    print('#{} {}'.format(test_case, answer))