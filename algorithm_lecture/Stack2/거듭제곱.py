# 반복문을 이용한 선형시간 O(n)

def iter_power(x, n):
    result = 1

    for i in range(1, n+1):
        result *= x

    return result

# 분할 정복을 이용한 거듭 제곱 O(logN)


def recur_power(x, n):
    if n == 1:
        return x

    if n%2 == 0:
        y = recur_power(x, n//2)
        return y*y
    else:
        y = recur_power((x, (n-1)//2))
        return y*y*x


iter_power(2, 10)
recur_power(2, 10)