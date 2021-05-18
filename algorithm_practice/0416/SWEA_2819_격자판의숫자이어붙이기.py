"""
4*4
동서남북 이동
여섯 번 이동해 각 칸의 숫자를 이어붙여 7자리 수를 만든다
한 번 거쳤던 격자칸을 다시 거쳐도 된다
만들 수 잇는 일곱자리 수의 개수 (중복X)

[아이디어1]
배열 s에 7개의 숫자를 채운다
7자리의 숫자를 생성하고
set 에 추가해 중복을 제거한다
set의 크기를 출력

[아이디어2]  = > 나는 이걸 택하겠어
배열을 채우는 대신 숫자 s 를 만들어 다음단계에 전달
f(n+1, i, j , s*10+A[i][j]) 문자열로 전달해도 될 것 같은데...
"""


def make_seq(n, r, c, string):

    if n == 6:  # 7자리의 숫자 완성
        num_set.add(string)
        return

    for i in range(4):  # 동서남북으로 이동
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 4 and 0 <= nc < 4:  # 격자판을 벗어나지 않는다면
            make_seq(n+1, nr, nc, string+board[nr][nc])  # 이동 횟수 갱신, 현재 위치의 숫자 덧붙여서 갱신


T = int(input())
for tc in range(1, T+1):
    board = [input().split() for _ in range(4)]
    num_set = set()  # 중복을 피하기 위해 set 사용

    dr = [-1, 0, 1, 0]  # 상우하좌 이동
    dc = [0, 1, 0, -1]

    for i in range(4):
        for j in range(4):
            make_seq(0, i, j, board[i][j])  # 임의의 위치에서 시작하고자.. 시작점의 숫자를 담아 함수 호출

    print('#{} {}'.format(tc, len(num_set)))