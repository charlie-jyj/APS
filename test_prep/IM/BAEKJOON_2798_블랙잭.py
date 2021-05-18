def black_jack(idx, temp_sum):
    global N, M, max_sum

    if temp_sum > M:  # 중간합이 M을 넘는다면 더 볼 이유가 없다.
        return

    if idx == 3:  # 순열이 결정되었다.
        if temp_sum <= M:  # 최종 합이 M 보다 같거나 작아야 한다.
            max_sum = max(temp_sum, max_sum)  # 최댓값 갱신
            return

    for i in range(N):
        if used[i] == 0:  # 사용하지 않은 카드라면 (중복을 허용하지 않기 때문에)
            used[i] = 1
            black_jack(idx+1, temp_sum+cards[i])
            used[i] = 0  # 사용 여부를 원상복구 하지 않는다면 다음 반복문에서 쓸 카드가 점점 없어질 것


N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0  # 최대 카드의 합
used = [0] * N  # 카드 사용 여부 체크 배열

black_jack(0, 0)  # depth, 중간합
print(max_sum)