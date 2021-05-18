T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    center = N//2+1 if N % 2 else N//2
    cards = input().split()

    result = [0] * N
    left = 0
    right = 1

    for i in range(N):

        if i < center:  # 절반 이전일 때
            result[left] = cards[i]
            left += 2
        else:  # 절반 이후일 때
            result[right] = cards[i]
            right += 2

    print('#{} {}'.format(test_case, ' '.join(result)))
