arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]
       ]

N, M = 3, 4

# # 행 우선 순회 방식
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])
#
# # 열 우선 순회 방식
# for j in range(M):
#     for i in range(N):
#         print(arr[i][j])
#
# # 행 역순회
# for i in range(N):
#     for j in range(M-1, -1, -1):
#         print(arr[i][j])

# 열 역순회
for j in range(M):
    for i in range(N-1, -1, -1):
        print(arr[i][j])
