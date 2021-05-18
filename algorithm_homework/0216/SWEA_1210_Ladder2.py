for test_case in range(1, 11):
    number = int(input())
    ladder = []
    start = -1

    # 사다리를 그리면서, 도착지(2) 열의 값을 확인한다.
    for outer in range(100):
        temp = list(map(int, input().split()))
        ladder.append(temp)
        if outer == 99:
            for inner in range(100):
                if temp[inner] == 2:
                    start = inner

    delta = [[0, 1], [0, -1]]  # 우 좌 (행, 열)
    dr = 0  # 행
    dc = 0  # 열
    answer = 0
    i, j = 99, start

    # 사다리타기 (도착지에서 위로 올라간다)
    while True:
        # 맨 위에 닿으면 break
        if i == 0:
            break

        # 내가 지나간 길은 -1로 기록
        ladder[i][j] = -1

        # 델타로 좌우를 살핀다.
        for d in delta:
            # 인덱스 에러나지 않도록 조건 부여
            if 0 <= i + d[0] <= 99 and 0 <= j + d[1] <= 99:
                # 좌우를 살폈을 때 값이 1이면 그 방향으로 가겠다.
                if ladder[i + d[0]][j + d[1]] > 0:
                    dr = d[0]
                    dc = d[1]
                    break
        # 좌우로 갈 수 없다면 위로 올라간다.
        else:
            dr = -1
            dc = 0

        i += dr
        j += dc

    # 위에 도착했을 때 열의 위치를 확인한다.
    print('#{} {}'.format(test_case, j))

