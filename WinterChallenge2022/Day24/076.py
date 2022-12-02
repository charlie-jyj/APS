num_string = "5 2"
N, K = list(map(int, num_string.split(" ")))

# DP Array => memoization 이용 (DP 기본)

# 선택 하지 않는 경우를 포함 해 N+1 * N+1 크기의 2차원 배열 선언
dp_array = [[0] * (N + 1) for _ in range(N + 1)]  # list comprehension

# 초기화
# i 개 중에 0 개 선택 [i][0] = 1
# i 개 중에 i 개 선택 [i][i] = 1
# i 개 중에 1개 선택 [i][1] = i

for i in range(N + 1):
    dp_array[i][0] = 1
    dp_array[i][i] = 1
    dp_array[i][1] = i

# 점화식 nCr = n-1Cr-1 + n-1Cr
# j의 경우 i 이상은 안 봐도 된다
for i in range(1, N + 1):
    for j in range(1, i):
        dp_array[i][j] = dp_array[i - 1][j - 1] + dp_array[i - 1][j]

print(dp_array[N][K])
