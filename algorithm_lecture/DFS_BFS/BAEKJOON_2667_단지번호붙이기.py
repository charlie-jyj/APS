def DFS(row, col, num):  # 행, 열, 단지 번호

    visited[row][col] = num

    for i in range(4):
        new_row = row + dr[i]
        new_col = col + dc[i]

        if ground[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
            DFS(new_row, new_col, num)


N = int(input())

# 벽으로 둘렀다
ground = [[-1]*(N+2)]
for _ in range(N):
    ground.append([-1]+list(map(int, input()))+[-1])
ground += [[-1]*(N+2)]

# 방문 배열
visited = [[0]*(N+2) for _ in range(N+2)]

# 단지 번호
number = 0

# 델타
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 집 찾기
for i in range(1,N+1):
    for j in range(1, N+1):
        if ground[i][j] == 1 and visited[i][j] == 0:
            number += 1
            DFS(i,j, number)

# 단지 수 만큼 길이를 가진 정답 배열
answer = [0] * number

# 단지 counting
for i in range(N+2):
    for j in range(N+2):
        if visited[i][j] != 0:
            answer[visited[i][j]-1] += 1

# 오름차순 정렬
answer.sort()

# 출력
print(number)
for ans in answer:
    print(ans)
