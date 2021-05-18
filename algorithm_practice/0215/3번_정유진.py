T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = []

    # NxN 배열 만들기
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(0)
        result.append(temp)

    # 달팽이 델타
    pattern = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 행, 열, 패턴 인덱스
    i, j, p = 0, -1, 0
    # 정수
    num = 1

    while num <= N*N:
        temp_r = i + pattern[p%4][0]
        temp_c = j + pattern[p%4][1]
        # 델타 방향으로 증감시켰을 때 인덱스가 배열을 벗어나지 않고 이미 입력된 값이 없을 때,
        if 0 <= temp_r < N and 0 <= temp_c < N and result[temp_r][temp_c] == 0:
            pass
        # 회전한다.
        else:
            p += 1

        # 배열에 값 입력
        i += pattern[p % 4][0]
        j += pattern[p % 4][1]
        result[i][j] = num
        num += 1

    # 출력하기
    print('#{}'.format(test_case))
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=' ')
        print()

