# 모듈러 연산 이용
# (A+B)%C = ((A%C) + (B%C)) % C

condition = "5 3"
num_string = "1 2 3 1 2"

N, M = list(map(int, condition.split(" ")))
numbers = list(map(int, num_string.split(" ")))
sum_array = [0 for _ in range(N)]
remainder_count = [0 for _ in range(M)]
sum_array[0] = numbers[0]
answer = 0

# 합 배열 만들기
for i in range(1, N):
    sum_array[i] = sum_array[i-1] + numbers[i]

# 나머지 연산
for j in range(N):
    remainder = sum_array[j] % M
    if remainder == 0:
        answer += 1  # (j,j) 인 경우는 조합에 포함되지 않기 때문에 따로 더해준다.
    remainder_count[remainder] += 1

# 조합 연산
for k in range(M):
    if remainder_count[k] > 1:
        answer += (remainder_count[k] * (remainder_count[k] - 1)) // 2

print(answer)
