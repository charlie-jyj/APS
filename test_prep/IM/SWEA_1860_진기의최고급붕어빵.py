T = int(input())
for test_case in range(1, T + 1):

    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))  # 손님 방문 시간
    max_time = max(customer) # 마지막 방문 시간
    timetable = [0] * (max_time + 1)  # 방문 예약 시간표

    # 몇 시일 때, 몇 명의 손님이 오는지 count 한다.
    for c in customer:
        timetable[c] += 1

    is_possible = True
    time = 0
    product = 0
    people = 0

    # 손님 다 받을 때까지 반복
    while time <= max_time:

        product = (time//M)*K  # 붕어빵 만들기
        people += timetable[time]  # 손님 받기

        if product < people:  # 붕어빵 보다 손님이 더 많다
            is_possible = False
            break  # 장사 접는다.

        time += 1  # 1초가 흘렀다

    print('#{} {}'.format(test_case, 'Possible' if is_possible else 'Impossible'))
