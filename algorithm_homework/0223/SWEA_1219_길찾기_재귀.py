def find_99(v):

    visited[v] = True

    for i in range(2):
        if adj_arr[i][v] > 0 and not visited[adj_arr[i][v]]:
            find_99(adj_arr[i][v])


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

    find_99(0)
    print('#{} {}'.format(test_case, 1 if visited[99] else 0))


