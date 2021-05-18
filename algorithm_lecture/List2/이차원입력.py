arr = [[1, 2, 3, 4.], [1, 2, 3]]

for i in arr:
    print(i)

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 1 2 3

# 1

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

# 2
arr1 = [0] * N

for i in range(N):
    arr1[i] = list(map(int, input().split()))

# 3
arr2 = [list(map(int, input().split())) for _ in range(N)]

for i in arr2:
    print(i)