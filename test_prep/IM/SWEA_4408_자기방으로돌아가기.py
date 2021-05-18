def find_home(stack):

    wait = []  # 다음 차례를 기다려야 하는 학생들
    used = []  # 사용 되고 있는 복도 구간

    print(stack)

    if not stack:  # 돌아가야 하는 학생이 더 없다.
        return 0

    else:
        # 학생을 한 명 씩 보내보자.
        for i in range(len(stack)):
            temp = []  # 임시 복도
            room1 = (stack[i][0]-1)//2
            room2 = (stack[i][1]-1)//2
            start = room1 if room1 < room2 else room2    # 출발할 방이 놓인 열의 위치
            end = room2 if room1 < room2 else room1  # 도착할 방이 놓인 열의 위치
            print('start',start,':','end',end)

            # 학생이 사용해야 할 복도 구간
            for j in range(start, end+1):
                if j in used:  # 이미 그 구간을 누가 쓰고 있다면
                    wait.append(stack[i])  # 너는 대기
                    break
                else:  # 아직 겹치지 않는구나
                    temp.append(j)
            else:
                # 누구와도 구간이 겹치지 않고 도착했다.
                used += temp  # 사용중 구간에 추가
                print('사용중:',used)

    print('대기명단', wait)
    # 다음 차례 기다리는 학생들을 데리고 다시 반복
    return 1 + find_home(wait)


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())  # 학생 수
    student = [list(map(int, input().split())) for _ in range(N)]  # 학생 [현재 위치, 도착지]

    answer = find_home(student)

    print('#{} {}'.format(test_case, answer))