# 예를 들어 길이 40을 채운다는 것은
# 길이 20에서 20을 늘리는 것이거나 (20은 10*20, 20*20 2가지 방법으로 늘릴 수 있다.)
# 길이 30에서 10을 늘리는 것 (10은 10*20 1가지)
# 따라서 길이 40 종이붙이기 경우의 수 = (20 종이붙이기 경우의 수 * 2) + 30 종이붙이기 경우의 수
# f(n) = 2 * f(n-2) + f(n-1)

def paper(n):

    if n >= 2 and len(memo) <= n:
        memo.append(2*paper(n-2)+paper(n-1))

    return memo[n]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())//10  # 편의를 위해 일의 자리로 만들었다.
    memo = [1, 1]

    answer = paper(N)

    print('#{} {}'.format(test_case,answer))

