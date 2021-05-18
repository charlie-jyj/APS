def set_queens(idx):  # 현재 내가 주목하고 있는 행
    global answer

    if idx == N:  # N queen 배치가 끝났다
        answer += 1
        return

    for i in range(N):  # 퀸을 배치할 수 있는 후보 열
        is_able = True

        for j in range(idx):  # 나 이전에 놓여진 퀸의 위치 확인
            if i == queens[j]  or abs(idx-j) == abs(i-queens[j]):  # 열이 겹치거나 대각선으로 겹치면
                is_able = False
                break

        if is_able:
            queens[idx] = i  # i 열에 퀸을 배치한다
            set_queens(idx+1)  # 다음 퀸을 배치하러 간다
            queens[idx] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    queens = [-1]*N  # 인덱스 = 행, 값 = 열 (한 행에 한 개의 queen 을 놓을 수 있다)
    answer = 0
    set_queens(0)  # 0번째 행에 퀸을 놓는 것으로 시작

    print('#{} {}'.format(tc, answer))