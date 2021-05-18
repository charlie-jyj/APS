T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = sorted(list(map(int, input().split())))  # 입력값 정렬하기
    keys = list(map(int, input().split()))
    answer = 0

    for key in keys:  # key 를 이진 탐색으로 찾는다
        start = 0
        end = N - 1
        flag = 0  # 번갈아 선택했는지 확인용

        while start <= end:

            mid = (start+end)//2

            if data[mid] == key:
                answer += 1
                break

            elif data[mid] < key:  # 왼쪽 구간을 선택했을 때
                start = mid + 1
                if flag == 1:  # flag 가 1이라는 뜻 = 직전에도 왼쪽 구간을 선택했다는 뜻
                    break
                flag = 1

            elif key < data[mid]:  # 오른쪽 구간을 선택했을 때
                end = mid - 1
                if flag == -1:  # flag 가 -1 이라는 뜻 = 직전에도 오른쪽 구간을 선택했다는 뜻
                    break
                flag = -1

    print('#{} {}'.format(tc, answer))