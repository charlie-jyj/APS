def hamburger(idx, temp_score, temp_cal):
    global N, L, max_sum

    # 칼로리 중간합이 칼로리 제한을 넘었을 경우 back
    if temp_cal > L:
        return

    # 조합이 결정되었을 때, 햄버거 점수 최댓값 갱신
    if idx == N:
        if temp_cal <= L:
            max_sum = max(temp_score, max_sum)
        return

    # 현재의 재료를 쓰지 않는다.
    hamburger(idx+1, temp_score, temp_cal)
    # 현재의 재료를 쓴다.
    hamburger(idx+1, temp_score+scores[idx], temp_cal+cals[idx])


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    scores= []  # 재료의 점수
    cals = []  # 재료의 칼로리
    for i in range(N):
        score, cal = map(int, input().split())
        scores.append(score)
        cals.append(cal)

    max_sum = 0  # 햄버거 점수의 최댓값

    hamburger(0, 0, 0)

    print('#{} {}'.format(tc, max_sum))