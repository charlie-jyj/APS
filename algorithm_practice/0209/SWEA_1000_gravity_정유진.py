# gravity
T = int(input())

for tc in range(1, T+1):
    # 방의 너비
    width = int(input())
    # 박스 기둥들
    boxes = list(map(int, input().split()))
    # 낙차를 기록할 list
    answers = [0] * width

    for idx in range(width):
        # 현재 내가 검사하고 있는 박스 기둥
        current = boxes[idx]
        # current <= value 인 박스 기둥의 개수를 기록할 변수
        longer = 0

        # 길이 비교를 하기 위한 반복문 (나를 제외)
        for num in range(idx+1, width):
            # 나(current)와 같은 높이거나 나보다 더 높은 기둥의 개수를 센다 (나의 낙하를 방해할 것이기 때문)
            if current <= boxes[num]:
                longer += 1

        # 나와 벽까지의 거리 - (나와 같은 높이거나 나보다 높은 상자 기둥의 수)
        answers[idx] = (width-1)-idx - longer

    # answers 에서 max 값을 찾아보자. (bubble sort 오름차순)
    for i in range(len(answers)-1, 0, -1):
        for j in range(0, i):
            if answers[j] > answers[j+1]:
                answers[j], answers[j+1] = answers[j+1], answers[j]

    print('#{} {}'.format(tc, answers[-1]))


