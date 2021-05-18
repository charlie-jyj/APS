# gravity 다르게 풀어보기
# 나의 낙하를 방해하지 않는 기둥의 개수 = 낙차
# 낙차 max 를 갱신하여 max 찾기
T = int(input())

for tc in range(1, T+1):
    # 방의 너비
    width = int(input())
    # 박스 기둥들
    boxes = list(map(int, input().split()))
    # 낙차를 기록할 변수
    answer = 0

    for idx in range(width):
        # 현재 내가 검사하고 있는 박스 기둥
        current = boxes[idx]
        # current > value 인 박스 기둥의 개수를 기록할 변수 (낙하를 방해하지 않는다)
        shorter = 0

        # 길이 비교를 하기 위한 반복문 (나를 제외)
        for num in range(idx+1, width):
            # 나(current)보다 낮은 기둥의 개수를 센다
            if current > boxes[num]:
                shorter += 1

        # 낙차 = 나보다 짧은 박스 기둥의 개수
        answer = shorter if shorter > answer else answer

    print('#{} {}'.format(tc, answer))

