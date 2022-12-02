# 모듈러 연산 이용
# ((A mod C) + (B mod C)) mod C = (A+B) mod C


num_string = "5 2"
N, K = list(map(int, num_string.split(" ")))
dp_array = [[0] * (N + 1) for _ in range(N + 1)]
C = 10007
for i in range(N + 1):
    dp_array[i][0] = 1
    dp_array[i][i] = 1
    dp_array[i][1] = i

for i in range(1, N+1):
    for j in range(1, i):
        dp_array[i][j] = dp_array[i-1][j-1] + dp_array[i-1][j]  # 각각의 항은 이미 %10007 divmod한 값으로 초기화 되어 있다.
        dp_array[i][j] %= C

print(dp_array[N][K])