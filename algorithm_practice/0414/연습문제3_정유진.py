
"""
부분집합의 합
모든 부분 집합 중 원소의 합이 0이 되는 부분 집합
-1 -3 -9 6 7 -6 1 5 4 -2
"""
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
result = []
N = 10
for i in range(1<<N):
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp.append(arr[j])
    if temp and sum(temp) == 0:
        result.append(temp)

for item in result:
    print(item)

# 재귀로 부분 집합 만들기