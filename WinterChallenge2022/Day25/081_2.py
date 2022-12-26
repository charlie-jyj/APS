# 재귀 쓰지 않고 풀기
# memoize
# functools is for higher-order function that act on or return other functions
import functools
import sys
sys.stdin = open('081_text.txt')
input = sys.stdin.readline
T = int(input())
factorial_memo = [1, 1]


def factorial(n) -> int:
    global factorial_memo
    if n > 1:
        for i in range(2, n+1):
            factorial_memo.append(factorial_memo[i-1]*i)
    return factorial_memo[n]


print(factorial(10))

# 처음 한 번은 재귀를 타서 값을 구할 수 밖에 없다. 그 값은 cached 되어 다음 연산 부터 사용
@functools.cache
def factorial2(n) -> int:
    return n*factorial2(n-1) if n else 1


for _ in range(T):
    N = int(input())
    numbers = [i for i in range(1, N+1)]
    test_case = list(map(int, input().split(" ")))
    issue_type = test_case[0]
    target = test_case[1:]
    cnt_list = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        cnt_list[i] = factorial(i)  # i번째 자리

    if issue_type == 1:
        print(f"{target[0]}번째 순열?")

    if issue_type == 2:
        print(f"{target}은 몇 번째 순열?")