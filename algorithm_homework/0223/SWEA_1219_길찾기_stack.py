def find_99(zero):

    # 시작 노드 0에 방문 표시하고 스택에 넣는다.
    visited[zero] = True
    stack = list()
    stack.append(zero)

    # 스택에 값이 있는 동안 반복
    while stack:

        # 방문할 노드를 스택에서 꺼낸다.
        current = stack.pop()

        # 방문할 노드에 연결되어 있는 다른 노드가 있는지 검색
        for i in range(2):

            # 노드가 연결되어 있고 그 노드에 방문한 적이 없다면 방문한다.
            if adj_arr[i][current] > 0 and not visited[adj_arr[i][current]]:
                if adj_arr[i][current] == 99:  # 방문할 노드가 99라면 길찾기 성공
                    return 1

                else:  # 도착하지 못했다면 연결된 노드를 모두 스택에 담는다 (방문 예정)
                    stack.append(adj_arr[i][current])

    # 결국 99에 도착하지 못했다.
    return 0


for test_case in range(1, 10 + 1):
    tc, N = map(int, input().split())
    numbers = list(map(int, input().split()))

    visited = [False]*100  # 출발 0 ~ 도착 99
    adj_arr = [[-1]*100 for _ in range(2)]  # 간선은 최대 2개

    # 연결된 노드 정보 기록하기
    for i in range(0, len(numbers)-2+1, 2):
        start = numbers[i]  # 시작 노드
        end = numbers[i+1]  # 도착 노드

        # 0행에 입력된 값이 있다면 1행에 입력한다.
        if adj_arr[0][start] > 0:
            adj_arr[1][start] = end
        else:
            adj_arr[0][start] = end

    answer = find_99(0)
    print('#{} {}'.format(test_case, answer))


