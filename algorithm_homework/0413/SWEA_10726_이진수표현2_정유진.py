T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N):
        if M % 2 == 0:
            print('#{} OFF'.format(tc))
            break
        else:
            M //= 2
    else:  # break 없이 끝까지 순회했다 = 마지막 N 비트가 모두 1
        print('#{} ON'.format(tc))