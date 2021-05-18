T = int(input())
for tc in range(1, T+1):

    N = float(input())  # 소수 입력
    bin_num = ''

    while N > 0:  # N이 0이 될때 멈춘다

        N *= 2  # N을 2배
        if N >= 1:  # 1이 넘으면 정수 부분 1 저장
            bin_num += '1'
            N -= 1
        else:  # 1을 넘지 않으면 0 저장
            bin_num += '0'

        if len(bin_num) > 12:
            bin_num = 'overflow'
            break

    print('#{} {}'.format(tc, bin_num))

