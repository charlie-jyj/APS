def treat(k):
    global max_value
    # 방사선 범위가 k 일때, 치료가 가능한 종양의 수를 반환하자
    temp = []

    # 모든 좌표를 순회하면서 그 점에서 시작해볼까
    for i in range(max_value+1):
        for j in range(max_value+1):

            # 방사선의 범위
            startx, starty = i, j
            endx, endy = startx+k, starty+k
            temp_cnt = 0

            for t in tumors:
                x1, y1 = t[0]
                x2, y2 = t[1]

                if startx <= x1 <= endx and starty <= y1 <= endy and startx <= x2 <= endx and starty <= y2 <= endy:
                    temp_cnt += 1

            temp.append(temp_cnt)

    cnt = max(temp)
    return cnt


T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tumors = []
    result = 987654321  # 방사선 범위 최솟값
    max_value = 0

    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        max_value = max(max_value, x1, y1, x2, y2)
        tumor = [(x1, y1), (x2, y2)]
        tumors.append(tumor)

    min_length = 1
    max_length = max_value
    while min_length <= max_length:
        mid_length = (min_length+max_length)//2
        tumor_cnt = 0

        # 치료되는 종양의 수 세기
        tumor_cnt = treat(mid_length)

        if N - tumor_cnt <= M:   # 치료성공
            result = min(result, mid_length)  # 결과 기록
            max_length = mid_length -1  # 범위를 줄여보자
        else:
            min_length = mid_length +1  # 범위를 넓혀보자

    print('#{} {}'.format(tc, result))

