T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # test case의 길이
    length = int(input())

    # test case 배열
    buildings = list(map(int, input().split()))

    # 문제 풀이 시작

    # 정답 변수 선언
    answer = 0

    # 양끝 2칸에는 건물이 지어지지 않으므로, i가 2~len(buildings)-3의 범위를, 1씩 증가하는 for문
    for i in range(2, length - 2):

        height = buildings[i]
        # 건물이 지어져있다면
        if height > 0:

            # 1번 풀이
            # 그 건물의 가장 꼭대기 세대가 거리 2 만큼의 조망권을 확보했다면
            # answer을 1 증가시키고, 1층 내려간다.
            # while buildings[i] > buildings[i - 1] and buildings[i] > buildings[i + 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 2]:
            #     # 해당 세대는 조망권을 확보했다.
            #     answer += 1
            #     # 해당 세대의 아래 세대도 조망권을 확보했는지 확인한다. (반복된다)
            #     buildings[i] -= 1

            # 2번 풀이
            # 이웃 건물의 max를 구한다.
            neighbors = buildings[i-2:i] + buildings[i+1:i+3]
            max_height = 0
            for j in neighbors:
                if max_height < j :
                    max_height = j

            # 3번 풀이
            # 왼쪽 건물, 오른쪽 건물나누어 최댓값을 구한다.
            # left_max = buildings[i-1] if buildings[i-1] > buildings[i-2] else buildings[i-2]
            #
            # if left_max >= height:
            #     continue
            #
            # right_max = buildings[i+1] if buildings[i+1] > buildings[i+2] else buildings[i+2]
            #
            # if right_max >= height:
            #     continue
            #
            # max_height = left_max if left_max > right_max else right_max

            # 현재 건물의 최고층 - 이웃 건물의 최고층 = 조망권 확보된 세대의 수
            answer += height - max_height

    # i가 끝에 도달하면 answer을 출력한다.
    print('#{} {}'.format(test_case, answer))
# ///////////////////////////////////////////////////////////////////////////////////
