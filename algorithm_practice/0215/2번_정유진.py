import random

arr = []  # 원본 배열
N = 10  # 정수의 개수
result = []  # 부분집합을 담을 리스트

# 10개의 정수를 가진 리스트 초기화
for i in range(N):
    arr.append(random.randint(-50, 50))

# 부분집합 구하기
for i in range(1 << N):
    temp = []
    for j in range(N):
        if i & (1 << j):
            temp.append(arr[j])

    result.append(temp)


print('원본: ', arr, '부분집합:', result)

# 부분집합의 합 구하기
# 합이 0이 되는 부분집합의 index 를 저장할 리스트
total_zero_index = []
for i in range(len(result)):
    temp = 0

    # 공집합이 아닌 부분집합의 합을 구한다.
    if len(result[i]) > 0:
        for j in range(len(result[i])):
            temp += result[i][j]
        # 부분집합의 합이 0일 경우 인덱스를 저장한다.
        if temp == 0:
            total_zero_index.append(i)

# 부분집합의 합이 0이 되는 부분집합 출력
for idx in total_zero_index:
    print('합이 0이 되는 부분 집합:', result[idx])


