def load_boxes(box, car, sub):  # 현재 화물 현황, 현재 트럭 현황, 중간 합계
    global max_weight

    if not car or box == [0]*N:  # 남아있는 트럭이 없거나 더이상 적재할 화물이 없을 때,
        max_weight = sub  # 결과를 보자
        return

    # 적재 가능
    curr_limit = cars.pop()  # 현재 주목하고 있는 차의 중량 제한
    idx = N-1  # 무거운 화물부터 (뒤에서부터) 순회한다
    while idx >= 0:  # 적재할 수 있는 화물이 있을 때 까지
        if box[idx] !=0 and box[idx] <= curr_limit:  # 이미 운송된 화물이 아니고 중량 제한보다 가벼운 화물일 때,
            sub += box[idx]  # 중간 합계를 화물 무게만큼 증량
            box[idx] = 0  # 화물을 운송했다는 뜻, 0으로 만든다
            break  # 1개의 컨테이너만 싣을 수 있으므로 break

        else:  # 더 가벼운 화물을 찾는다.
            idx -= 1

    load_boxes(box, car, sub)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    boxes = list(map(int, input().split()))  # 컨테이너
    cars = list(map(int, input().split()))  # 트럭
    boxes.sort()  # 오름차순 정렬 (무거운 화물부터 처리할 것 => 이게 greedy 한 것일까?)
    cars.sort()  # 오름차순 정렬 (많은 화물을 적재할 수 있는 트럭부터 사용할 것)
    max_weight = 0  # 이동한 화물 무게

    load_boxes(boxes, cars, 0)  # 화물을 적재한다
    print('#{} {}'.format(tc, max_weight))