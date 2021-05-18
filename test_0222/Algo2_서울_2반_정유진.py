T = int(input())
for tc in range(1, T+1):
    starter = input()  # 첫번째로 주사위를 굴리는 사람
    cubic = [list(map(int, input().split())) for _ in range(2)]  # A, B의 주사위 숫자
    N = len(cubic[0])  # 주사위를 굴리는 총 횟수

    round_num = -1  # 몇번째 라운드인지 기록할 변수
    current_first = 0  # 첫번째 주자의 위치 (출발 : 0, 도착 : 19)
    current_second = 0  # 두번째 주자의 위치

    # 보드 게임을 위한 반복문
    while True:

        # 새로운 round 가 시작된다.
        round_num += 1

        # 주사위를 다 굴렸는데 승부가 판가름 나지 않았다면 무승부로 생각하고 반복문 break
        if round_num >= N:
            answer = 'AB'
            break

        # starter 가 누구인지에 따라 first = starter 이고 second = starter 가 아닌 사람
        first = 0 if starter == 'A' else 1
        second = 1 if starter == 'A' else 0

        # first 가 주사위를 던진다, 임시로 위치를 이동시킨다.
        temp_first_position = current_first + cubic[first][round_num]

        # 임시 위치에 second 가 있었다면 (말을 잡았다) second 의 현재 위치를 0으로 갱신한다.
        if current_second == temp_first_position:
            current_second = 0

        # first 의 현재 위치를 확정한다.
        current_first += cubic[first][round_num]

        # second 가 주사위를 던진다. 임시로 위치를 이동시킨다.
        temp_second_position = current_second + cubic[second][round_num]

        # 임시 위치에 first 가 있었다면 (말을 잡았다) first 의 현재 위치를 0으로 갱신한다.
        if current_first == temp_second_position:
            current_first = 0

        # second 의 현재 위치를 확정한다.
        current_second += cubic[second][round_num]

        # 위치 확정 후 결과 확인
        if current_first >= 19 and current_second >= 19:  # first, second 모두 도착하거나 넘어갔다면 무승부 처리하고 break
            answer = 'AB'
            break
        elif current_first >= 19:  # first 가 도착하거나 넘어갔다면 first 가 누구인지 확인한 후 answer 에 기입하고 break
            answer = 'A' if first == 0 else 'B'
            break
        elif current_second >= 19:
            answer = 'A' if second == 0 else 'B'  # second 가 도착하거나 넘어갔다면 first 가 아닌 사람을 answer 에 기입하고 break
            break

    print('#{} {}'.format(tc, answer))
















