def get_luck(idx, sub):
    global max_luck
    if idx == N:  # 일의 분배가 끝났다
        max_luck = max(max_luck, sub)  # 최댓값 갱신
        return

    if sub <= max_luck:  # 확률은 곱할수록 작아질텐데 벌써 최댓값보다 작다면 가망이 없다
        return

    for j in range(N):  # 일의 후보
        if lucks[idx][j] != 0 and work[j] == -1:  # 성공 확률이 0인 일, 다른 사람이 이미 하는 일은 고르지 않는다
            work[j] = idx
            get_luck(idx+1, sub*lucks[idx][j]*(10**-2))  # 다음 사람에게 일을 할당하러
            work[j] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lucks = [list(map(int, input().split())) for _ in range(N)]
    work = [-1] * N  # 인덱스: 일, 값: 담당 직원
    max_luck = 0  # 성공 확률의 최댓값

    get_luck(0, 1)  # DFS

    # 소수점 6자리 까지 표시
    print('#{} {:.6f}'.format(tc, round(max_luck*(10**2), 6)))