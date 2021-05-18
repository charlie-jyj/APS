def fibo1(n):

    # memo 0, 1, 은 구현하지 않고 len(memo)가 n 보다 작을 때 구현한다
    # len(memo) 가 n 보다 크다면 이미 memo 값이 구해져 있다는 뜻
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1)+fibo1(n-2))
    return memo[n]


# 현재 len(memo) = 2
memo = [0, 1]

fibo1(35)
print(memo)



def fibo2(n):
    if n >= 2 and memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)

    return memo2[n]


memo2 = [-1] * 21
memo2[0] = 1
memo2[1] = 1

print(fibo2(5))
print(memo2)