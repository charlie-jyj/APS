T = int(input())
for test_case in range(1, T + 1):

    N = int(input())  # 학생 수
    student = [list(map(int, input().split())) for _ in range(N)]  # 학생 [현재 위치, 도착지]
    corridor = [0] * 400

    for i in range(len(student)):
        room1 = (student[i][0] - 1) // 2
        room2 = (student[i][1] - 1) // 2  # room1, room2 의 번호의 대소 관계는 정해져 있지 않다.
        start = room1 if room1 < room2 else room2  # 출발할 방이 놓인 열의 위치
        end = room2 if room1 < room2 else room1  # 도착할 방이 놓인 열의 위치

        # 학생이 사용한 복도의 count 를 증가 시킨다.
        for j in range(start, end+1):
            corridor[j] += 1

    # 복도 구간 사용의 최댓값 = 소요된 총 시간
    print('#{} {}'.format(test_case, max(corridor)))