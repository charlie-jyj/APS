"""
dp 기초
점화식
F(N) = min ( F(N-3), F(N-5) ) + 1
"""


def sugar(n):

    if n < 0:
        return 987654321

    if n >= 3 and memo[n] == 0:
        memo[n] = min(sugar(n-3), sugar(n-5)) + 1

    return memo[n]


N = int(input())
memo = [0] * (10000)
memo[1] = memo[2] = 987654321
answer = sugar(N)

if answer > 987654321:
    print(-1)
else:
    print(answer)