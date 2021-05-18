# 델타 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def DFS(row, col, num):
    global N

    stack = list()
    stack.append((row, col))

    while stack:
        curr_r, curr_c = stack.pop()

        if visited[curr_r][curr_c] == 0:
            visited[curr_r][curr_c] = num  # 인접한 화학물질을 같은 숫자로 바꾸어줄 것

            for i in range(4):
                new_r = curr_r + dr[i]
                new_c = curr_c + dc[i]

                if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
                    continue

                if matrix[new_r][new_c] != 0 and visited[new_r][new_c] == 0:
                    stack.append((new_r, new_c))


T = int(input())
for test_case in range(1, 10 + 1):
    N = int(input())  # 행렬 길이
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    type_num = 0  # 화학 물질의 수

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0 and visited[i][j] == 0:  # 비어있지 않고 방문한 적 없다면
                type_num += 1
                DFS(i, j, type_num)

    result = [0]*type_num

    # 너비*높이 알아내기
    for n in range(type_num):
        width = 0
        height = 0
        for i in range(N):
            if (n+1) in visited[i]:
                width = visited[i].count(n+1)
                s_col = visited[i].index(n+1)

                for j in range(N):
                    if visited[j][s_col] == n+1:
                        height += 1

                break

        result[n] = (height, width)

    # 정렬한다
    sorted_result = sorted(result, key = lambda x: (x[0]*x[1], x[0]))

    # 출력한다
    print('#{} {}'.format(test_case, type_num), end=' ')
    for h, w in sorted_result:
        print('{} {}'.format(h, w), end=' ')
    print()



