def fact(n):
    if n >= 2 and n >= len(memo):
        memo.append(n*fact(n-1))

    return memo[n]


N = int(input())

memo = [1, 1]
print(fact(N))