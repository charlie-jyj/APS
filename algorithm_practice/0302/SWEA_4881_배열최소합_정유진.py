import time

def get_min_sum(idx):
    global min_sum, temp_sum

    if min_sum < temp_sum:  # 지금까지 합한 임시 총합이 기존 최솟값 보다 크다면 더 볼 필요없다.
        return

    if idx == N:  # 순열 완성, 최솟값을 갱신한다.

        if temp_sum < min_sum:
            min_sum = temp_sum
            return

    else:
        # 현재 idx 행에서 순회하며 열을 결정한다.
        for j in range(N):
            if visit[j] == 0:  # 아직 사용하지 않은 열

                visit[j] = 1  # 사용 체크
                temp_sum += numbers[idx][j]  # 해당 열을 사용한다면, 그 값을 임시 총합에 더한다.
                get_min_sum(idx+1)  # 다음 행으로
                visit[j] = 0  # 다음 반복문을 위해 사용 여부를 초기화
                temp_sum -= numbers[idx][j]  # 임시 총합도 초기화


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N  # 방문 여부 체크 idx가 0에서 N-1 까지 재귀호출 되므로 열 사용 여부만 체크
    min_sum = 987654321  # 반환할 최솟값
    temp_sum = 0  # 현재까지의 합을 담을 임시 변수

    get_min_sum(0)

    print('#{} {}'.format(test_case, min_sum))

    # time.time()