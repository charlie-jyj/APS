def count_color():
    global M

    white = color[0]  # 흰색으로 칠할 행의 수
    blue = color[1]  # 파란색으로 칠할 행의 수
    red = color[2]  # 빨간색으로 칠할 행의 수
    cnt_change = 0  # 다시 칠한 칸의 개수

    # 흰색으로 칠하기
    for i in range(0, white):
        for j in range(M):
            if flag[i][j] != 'W':
                cnt_change += 1

    # 파란색으로 칠하기
    for i in range(white, white+blue):
        for j in range(M):
            if flag[i][j] != 'B':
                cnt_change += 1

    # 빨간색으로 칠하기
    for i in range(white+blue, N):
        for j in range(M):
            if flag[i][j] != 'R':
                cnt_change += 1

    return cnt_change


def repeat_perm(idx, temp_sum):
    global min_sum

    if temp_sum > N:  # 최대 N개의 행을 색칠할 수 있다. (가지치기)
        return

    if idx == 3: # base case (중복 순열이 완성되는 시점)
        if temp_sum == N:  # 순열의 합이 행의 개수와 같다
            min_sum = min(min_sum, count_color())  # 최솟값 갱신

        return  # 밑에 코드를 실행하지 않을 것

    # 모든 색깔이 최소 1 행을 가지고 최대 N-2 행까지 색칠할 수 있다. (3색이기 때문)
    for i in range(1, N-1):
        color[idx] = i  # 지금 다루고 있는 색상을 i 행만큼 색칠하겠다
        repeat_perm(idx+1, temp_sum+i)  # 다음 색상을 다루기 위해 재귀 함수 call

        # 중복 순열이므로 해당 값을 사용했는지의 여부 같은 것은 체크하지 않아도 된다.



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    color = [0]*3
    min_sum = 987654321

    # 시작 인덱스 (흰색:0), 중간 합 (현재까지 몇 행을 채웠는지)를 매개변수로 넘긴다.
    repeat_perm(0, 0)

    print('#{} {}'.format(test_case, min_sum))