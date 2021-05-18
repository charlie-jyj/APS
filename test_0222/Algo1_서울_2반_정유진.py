T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    trees = [list(map(int, input().split())) for _ in range(N)]

    total_cost = 0  # 총 비용
    total_tree_count = 0  # 심은 나무의 수
    max_tree_cost = 0  # 가장 비싼 나무의 가격
    max_tree_col = 0  # 비싼 나무가 심어진 열

    # 열 우선 순회 (열의 숫자 고정 후 반복문으로 행을 순회하고 열의 숫자를 +1 하며 순회한다)
    for j in range(M):  # 열의 수 만큼 도는 반복문
        for i in range(N):  # 행의 수 만큼 도는 반복문

            if j % 2 == 0:  # 나무는 한 줄 씩 띄어서 심는다. 나무가 심어지는 열은 j가 짝수 인덱스를 가진다.
                total_cost += trees[i][j]  # 총 비용을 증가시킨다.
                total_tree_count += 1  # 심은 나무의 수를 1씩 증가시킨다.

                if max_tree_cost <= trees[i][j]:  # 나무 가격의 최댓값을 갱신하는데 같은 가격일 경우 열 인덱스가 더 큰 값으로 갱신된다.
                    max_tree_cost = trees[i][j]
                    max_tree_col = j+1  # 나무가 심어진 열은 열 인덱스 + 1 (0 행 -> 1 번째 열에 나무)

    print('#{} {} {} {} {}'.format(tc, total_cost, total_tree_count, max_tree_cost, max_tree_col))

