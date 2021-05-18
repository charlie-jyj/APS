T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    target = list(map(int, input().split()))  # 내가 찾을 숫자
    source = list(map(int, input().split()))  # 탐색할 숫자들
    counting = [0]*M  # 탐색 횟수 기록

    for i in range(M):  # 이진 탐색 
        goal = target[i]
        start = 0
        end = N-1
        is_found = False
        while start <= end:
            mid = (start+end)//2  # 중간 값
            if source[mid] == goal:
                counting[i] += 1
                is_found = True
                break
            elif source[mid] < goal:  # 찾을 값이 오른쪽에 있을 경우
                counting[i] += 1
                start = mid + 1
            elif goal < source[mid]:  # 찾을 값이 왼쪽에 있는 경우
                counting[i] += 1
                end = mid - 1

        if not is_found:  # 결국 찾지 못했을 때
            counting[i] = -1

    min_index = -1
    min_value = 987654321
    for i in range(M):  # 탐색 횟수가 최소인 원소를 찾는다.
        if counting[i] != -1 and min_value > counting[i]:
            min_index = i
            min_value = counting[i]

    print('#{} {} {}'.format(tc, target[min_index], min_value))