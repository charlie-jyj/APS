TC = int(input())
for tc in range(1, TC+1):

    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    total = 0

    # 처음에 center가 시작이자 끝
    # 중간까지는 center를 감소시키고 (범위 넓혀가기)
    # 중간 이후 부터는 center를 증가시킨다 (범위 좁혀가기)
    s = (N - 1) // 2
    e = (N - 1) // 2
    for i in range(N):

        for j in range(s, e+1, 1):
            total += board[i][j]

        if i >= (N-1)//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

    print('#{} {}'.format(tc, total))