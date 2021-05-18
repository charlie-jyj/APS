T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N):
        if not M >> i & 1:  # 2진수로 바꾼 M을 i 만큼 오른쪽으로 밀었을 때, 끝자리가 1이 아니면,
            print('#{} OFF'.format(tc))
            break
    else:  # break 없이 끝까지 순회했다 = 마지막 N 비트가 모두 1
        print('#{} ON'.format(tc))