# 분할 정복을 이용한 거듭 제곱
def my_power(n, m):

    if n == 0 or m == 0:  # 밑이나 지수가 0 이면 1 반환
        return 1

    if m % 2:  # 홀수 일 경우
        return my_power(n, (m-1)//2)*my_power(n, (m-1)//2) * n
    else:  # 짝수 일 경우
        return my_power(n, m//2)*my_power(n, m//2)


for test_case in range(1, 10 + 1):
    tc = int(input())
    N, M = map(int, input().split())

    result = my_power(N, M)

    print('#{} {}'.format(tc, result))