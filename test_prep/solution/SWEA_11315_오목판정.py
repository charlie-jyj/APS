# 행 우선 순회하다가 'o'를 만날 경우 델타로 우,아래,좌우대각선 확인

def chk(row, col):
    dr = [0, 1, 1, 1, -1, -1] # 우, 하, 좌하대각선, 우하대각선, 좌상대각선, 우상대각선
    dc = [1, 0, -1, 1, -1, 1]

    # 델타 이동 할 때마다 row, col, cnt 값 초기화
    for i in range(6):
        idx_row = row
        idx_col = col
        cnt = 1

        while 0 <= idx_row + dr[i] < N and 0 <= idx_col + dc[i] < N and BRD[idx_row+dr[i]][idx_col+dc[i]] == 'o':
            idx_row += dr[i]
            idx_col += dc[i]

            cnt += 1
            if cnt >= 5:
                return True

    return False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    BRD = [input() for _ in range(N)]
    is_check = False

    for r in range(N):
        for c in range(N):
            if BRD[r][c] == 'o':
                is_check = chk(r, c)
                if is_check:
                    break

        if is_check:
            break

    if is_check:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))