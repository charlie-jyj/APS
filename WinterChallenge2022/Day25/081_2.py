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

"""
Permutation81

nPn = n!
1…4, 사전 순서

1*1
1

2*1
12
21

3*2*1
123
132
213
231
312
321

4*3*2*1
(1)
1234
1243
1324
1342
1423
1432

(2)
2134
2143
2314
2341
2413
2431

(3)
3124
3142
3214
3241
3412
3421

(4)
4123
4132
4213
4231
4312
4321

Target = 1324
자릿수에 따른 경우의 수
[0,1,2,6,24]

N = 4
경우의 수 최대 24 는 K=3 보다 당연히 같거나 크기 때문에
N-1 = 3 부터 고려한다

내가 찾는 순열은 어느 range에 속할까.. _for i in range(3, -1, -1)

_i = 3
opt=선택할 수 있는 숫자의 개수: 4
arr[3] = 6
_step = 0
_for j in range(opt-1, -1, -1)
6*step3 = 18 > 3 _pass
6*step2 = 12 > 3 _pass
6*step1 = 6 > 3 _pass
6*step0 = 0 < 3 _break _step = 0
남은숫자 1,2,3,4 중 step번째 숫자 선택 => 1
K = K - arr[3]*(step) = 3 - 6*0 = 3
남은 숫자 2,3,4

_i = 2
opt=선택할 수 있는 숫자의 개수: 3
arr[2] = 2
_for j in range(opt-1, -1, -1)
2*step2 = 4 > 3 _pass
2*step1 = 2 < 3 _break _step = 1
남은 숫자 2,3,4 중 step번째 숫자 선택 => 3
K = K - arr[2]*(step) = 3- 2*1 = 1
남은 숫자 2,4

_i = 1
_opt =2
arr[i] = 1
_step = 0
_for j in range(opt-1, -1, -1):
1*step1 = 1 = 1 _pass
1* step0 = 0 < 1 _break _step = 0
남은 숫자 2,4 중 step번째 숫자 선택 => 2
K = K - arr[I]*step = 1 -0 = 1
남은 숫자 4

_i = 0
_opt = 1
arr[i] = 0
_step = 0
_for j in range(opt-1, 0, -1):
<x>
남은 숫자 4 중 step번째 숫자 선택 => 4
K = K - arr[I]*step = 1 - 0 = 1
남은 숫자 “”
"""
