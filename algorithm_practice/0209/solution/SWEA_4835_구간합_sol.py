T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 구간 시작점
    for i in range(N-M+1):
        tmp = 0

        for j in range(M):
            tmp += numbers[i+j]

    if max_value < tmp:
        max_value = tmp

    if min_value > tmp:
        min_value = tmp
    
    # range_sums에서 max - min을 한다.
    print('#{} {}'.format(test_case, max_value-min_value))
    

