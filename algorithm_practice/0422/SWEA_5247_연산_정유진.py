from collections import deque


def compute(n, m):
    queue = deque([(n, 0)])  # 시작 노드, 연산 횟수
    visit = [0] * 1000001  # 내가 만날 수 있는 노드의 최댓값 1000000
    visit[n] = 1  # 시작점 방문 체크

    while queue:
        current = queue.popleft()

        if current[0] == m:  # 최초로 목표 노드를 만났을 때, 그 노드까지의 거리 = 연산의 최솟값
            return current[1]

        option = [current[0]+1, current[0]-1, current[0]*2, current[0]-10]  #  현재 노드에서 내가 갈 수 있는 노드 4개

        for i in range(4):
            if 0 < option[i] <= 1000000 and visit[option[i]] == 0:  # 그 노드가 백만 이하 자연수이고 방문한적 없는 노드라면
                queue.append((option[i], current[1]+1))  # 내가 방문할 노드와 누적 연산 횟수를 enqueue
                visit[option[i]] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N 을 M 으로 만들기
    print('#{} {}'.format(tc, compute(N, M)))  # BFS