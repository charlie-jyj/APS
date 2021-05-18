# def fibo(n):
#     if n < 1:
#         return 0
#     elif n == 1:
#         return 1
#
#     return fibo(n-1) + fibo(n-2)

def fibo(n):
    if 1 < n and n >= len(memo):
        memo.append(fibo(n-1)+fibo(n-2))

    return memo[n]


N = int(input())
memo = [0, 1, ]
answer = 0

answer=fibo(N)

print(answer)