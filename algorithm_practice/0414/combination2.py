def f(i, n, k):

    if i == k:
        print(p)
    else:
        for j in range(n):
            if u[j] == 0:
                u[j] = 1
                p[i] = j
                f(i+1, n, k)
                u[j] = 0


N = 5
K = 3

p = [0]*K
u = [0]*K
f(0, N, K)