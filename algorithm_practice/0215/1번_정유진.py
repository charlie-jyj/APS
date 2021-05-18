import random

arr = []
N = 5
M = 5

# 무작위로 25개의 숫자로 5*5 배열 초기화
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(random.randint(1, 50))
    arr.append(temp)

# 델타 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 총합 선언
total = 0

# 행 우선 순회
for i in range(N):
    sub_total = 0
    for j in range(M):
        # 각 요소
        center = arr[i][j]
        # 이웃한 요소 순회
        for k in range(4):

            nr = i + dr[k]
            nc = j + dc[k]

            # 이웃한 요소 인덱스의 범위 제한 (벽에 있는 요소 때문에)
            if 0 <= nr < N and 0 <= nc < M:
                side = arr[nr][nc]
                # 차의 절대값의 합 구하기
                sub_total += int(((center - side)**2)**(1/2))
                
    # 총합 구하기
    total += sub_total

print(arr, total)