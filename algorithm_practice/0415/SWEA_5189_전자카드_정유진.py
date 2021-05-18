def perm(idx):

    if idx == len(route):
        temp_route = [1] + route + [1]  # 시작(사무실) + 경로 + 종료(사무실) 하여 경로를 완성한다
        route_list.append(temp_route)

    for i in range(idx, len(route)):
        route[idx], route[i] = route[i], route[idx]
        perm(idx+1)
        route[idx], route[i] = route[i], route[idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery_usage = [list(map(int, input().split())) for _ in range(N)]
    route = [i+1 for i in range(N)][1:]  # 앞의 1 빼고 2,3,4,...N
    route_list = []  # 가능한 경로를 모두 담을 리스트

    perm(0)  # [2,3,4...,N] 으로 순열을 만든다.

    min_sum = 987654321
    for r in route_list:  # 가능 경로를 하나하나 들여다 본다.
        temp_sum = 0
        for i in range(len(r)-1):  # 경로를 이동하는데 소모되는 배터리의 양을 더한다
            temp_sum += battery_usage[r[i]-1][r[i+1]-1]
        min_sum = min(min_sum, temp_sum)  # 배터리 소모량의 최솟값을 갱신한다

    print('#{} {}'.format(tc, min_sum))