def copy_origin_ladder(org):

    arr = list()
    for outer in range(len(org)):
        temp = []
        for inner in range(len(org[outer])):
            temp.append(org[outer][inner])
        arr.append(temp)

    return arr


for test_case in range(1, 11):
    number = int(input())
    origin = [list(map(int, input().split())) for i in range(100)]
    delta = [[0, 1], [0, -1]]  # 우 좌 (행, 열)
    dr = 0  # 행
    dc = 0  # 열
    answer = 0

    # 시작점 찾기
    for start in range(100):

        # 복사본으로 메모하면서 갈 것 (지나온 길을 표시하기 위해서)
        ladder = copy_origin_ladder(origin)

        if ladder[0][start] == 1:  # 시작점
            i = 0
            j = start

            # 사다리타기
            while True:
                # 바닥에 닿으면 break
                if i == 99:
                    break

                # 내가 지나간 길은 -1로 기록
                ladder[i][j] = -1

                # 델타로 좌우를 살핀다.
                for d in delta:
                    # 인덱스 에러나지 않도록 조건 부여
                    if 0 <= i+d[0] <= 99 and 0 <= j+d[1] <= 99:
                        # 좌우를 살폈을 때 값이 1이면 그 방향으로 가겠다.
                        if ladder[i+d[0]][j+d[1]] > 0:
                            dr = d[0]
                            dc = d[1]
                            break
                # 좌우로 갈 수 없다면 아래로 내려간다.
                else:
                    dr = 1
                    dc = 0

                i += dr
                j += dc

            # 바닥에 도착해 while 문이 종료하면 마지막 위치가 도착지(2)인지 확인한다.
            # 도착지 아니라면 start 의 위치를 옮겨 계속 반복한다.
            if origin[i][j] == 2:
                answer = start
                break

    print('#{} {}'.format(test_case, answer))