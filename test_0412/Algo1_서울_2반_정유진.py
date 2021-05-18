def attack(r, c, p):  # 행, 열, 폭탄 범위
    global enemy, N

    enemy += ground[r][c]  # 폭탄이 터진 자리에 있는 군인 count
    ground[r][c] = 0

    for i in range(1, p+1):  # 폭탄 범위 결정
        for j in range(4):  # 델타 이동
            new_r = r + i*dr[j]
            new_c = c + i*dc[j]

            if 0 <= new_r < N and 0 <= new_c < N:  # 유효한 사정권 안에 있는지 확인한다.
                enemy += ground[new_r][new_c]  # 사정권 범위 내의 군인 count
                ground[new_r][new_c] = 0  # 중복 피해를 피하기 위해 해당 위치의 군인 수를 0으로 바꾼다.


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 지도의 크기, 폭탄의 수
    ground = [ list(map(int, input().split())) for _ in range(N) ] # 적군 정보
    bombs = [ list(map(int, input().split())) for _ in range(M) ]  # 폭탄 정보
    dr = [-1, 1, 1, -1]  # 대각선 델타
    dc = [1, 1, -1, -1]
    enemy = 0  # 반환할 피해 입은 적군 수

    for bomb in bombs:  # 폭탄의 정보를 통해 폭탄을 사용한다
        row, col, power = bomb
        attack(row, col, power)

    print('#{} {}'.format(tc, enemy))