T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321


    # 중복된 연산 피하기
    # 첫 구간의 값은 구한다.
    tmp = 0
    for i in range(M):
        tmp += numbers[i]

    max_value = tmp
    min_value = tmp

    for i in range(M, N):
        # 새로운 구간 합을 간단하게 구한다. 윈도우 슬라이딩
        tmp = tmp + numbers[i] - numbers[i-M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp
    
    # range_sums에서 max - min을 한다.
    print('#{} {}'.format(test_case, max_value-min_value))
    

