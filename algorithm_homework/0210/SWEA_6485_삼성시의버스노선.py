T = int(input())
for test_case in range(1, T + 1):
    # N 대의 버스
    N = int(input())
    # 버스 노선
    bus = []
    for i in range(N):
        bus.append(list(map(int, input().split())))
    # p 개의 버스정류장
    p = int(input())
    # 버스 노선 검사할 정류장
    c = []
    for j in range(p):
        c.append(int(input()))
    # 반환할 정답
    answer = [0] * p

    # 버스 정류장 목록을 순회하면서 정류장의 위치가 A, B 사이에 있으면 check 1 증가
    for idx in range(p):
        check = 0
        for route in bus:
            if route[0] <= c[idx] <= route[1]:
                check += 1
        answer[idx] = check

    print('#{} {}'.format(test_case, ' '.join(map(str, answer))))

