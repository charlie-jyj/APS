for tc in range(1, 10+1):
    # N은 dump 횟수
    N =int(input())
    # 박스들
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101

    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트 최고점과 최저점을 찾아보자.
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value-1:

        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value-1] += 1

        if h_cnt[min_value] == 0:
            min_value += 1

        if h_cnt[max_value] == 0:
            max_value -= 1

        N -= 1
        
    print('#{} {}'.format(tc, max_value-min_value))