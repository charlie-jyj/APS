T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    center = N//2+1 if N % 2 else N//2
    cards = input().split()

    left = []
    right = []
    result = []

    # 절반으로 나누어 left, right 에 담는다
    for i in range(N):
        if 0 <= i < center:
            left.append(cards[i])
        else:
            right.append(cards[i])

    # left, right 의 길이를 넘지 않는 한도 내에서, 하나씩 꺼내어 result 에 append
    i = 0
    while True:
        # left 의 길이 가 right 보다 항상 같거나 크기 때문에, i 가 left 의 길이와 같아지면 break
        if i == len(left):
            break

        if i < len(left):
            result.append(left[i])

        if i < len(right):
            result.append(right[i])

        i += 1

    print('#{} {}'.format(test_case, ' '.join(result)))