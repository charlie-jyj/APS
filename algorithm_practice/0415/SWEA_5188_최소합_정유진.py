def travel(row, col, sub_sum):
    global N, min_sum

    sub_sum += board[row][col]  # 내가 방문한 곳의 숫자를 더한다

    if row == N-1 and col == N-1:  # 오른쪽 아래에 도달했다.
        min_sum = min(min_sum, sub_sum)  # 이동 거리 합 최솟값 갱신
        return

    if sub_sum > min_sum: # 이 길은 유망하지 않으니 돌아간다
        return

    for i in range(2):  # 아직 가능성이 있는 길이므로 갈 수 있는 곳을 모두 탐색
        new_row = row + dr[i]
        new_col = col + dc[i]

        if 0 <= new_row < N and 0 <= new_col < N:  # 숫자판을 벗어나지 않는다면
            travel(new_row, new_col, sub_sum)  # 갱신한 sub_sum을 가지고 다른 위치로 이동


T = int(input())
for tc in range(1, T+1):
    N= int(input())
    board = [list(map(int, input().split())) for _ in range(N)]  # 숫자가 적힌 판
    dr = [0, 1]  # 우, 하 로만 이동할 수 있다. (좌, 상으로 갈 수 없으니 돌고 돌 일이 없어 visit 검사는 필요없다)
    dc = [1, 0]
    min_sum = 987654321  # 갱신될 최솟값
    travel(0, 0, 0)  # 여행을 떠난다

    print('#{} {}'.format(tc, min_sum))