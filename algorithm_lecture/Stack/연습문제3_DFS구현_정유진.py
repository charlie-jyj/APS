def dfs_stack(v):
    stack = []
    result = ''  # 방문 경로

    stack.append(v)  # 시작 정점을 stack 에 담는다
    visit[v] = 1  # 시작 정점 방문
    result += str(v)  # 경로 표시

    while len(stack) != 0:  # stack 비어있을 때 까지 반복

        while visit[v] > 0:  # v에 방문중일 때

            # v와 연결된 간선 중에서 숫자가 더 작은 정점으로 이동한다.
            for i in range(len(matrix[v])):
                if matrix[v][i] > 0 and visit[i] < 0:  # 연결되어 있고, 방문하지 않은 정점 i
                    w = i
                    visit[w] = 1  # i를 방문했다
                    result += str(w)  # 방문 경로를 추가한다.
                    stack.append(w)  # i를 스택에 추가한다. (나중에 돌아올 수 있게)
                    v = w  # i를 현재 방문중으로 갱신
                    break

            # break 없이 반복문이 종료했다 = 연결된 노드에 모두 방문했다.
            else:
                v = stack.pop()  # 스택에 담긴 직전 분기점으로 돌아간다.
                break

    # 스택이 비었다면 탐색 끝, 방문 경로를 반환한다.
    return result


N, M = map(int, input().split())  # 정점수, 간선수
visit = [-1] * (N+1)  # 방문 여부 표시 1~N
visit[0] = 0  # 0은 쓰지 않는다.
matrix = [[0]*(N+1) for _ in range(N+1)]  # 인접 행렬

# 인접 행렬 만들기 (양방향)
for _ in range(M):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1

# 함수 호출 (시작값)
answer = dfs_stack(7)
print(answer)

