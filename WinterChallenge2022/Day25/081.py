import sys
sys.stdin = open('081_text.txt')
input = sys.stdin.readline
T = int(input())


def permutation_81(curr_idx: int, visited: [int], temp_result: [int]):
    global N, numbers, issue_type, target, total_cnt

    if curr_idx == N:
        total_cnt += 1
        if issue_type == 1 and total_cnt == target[0]:
            print(" ".join(map(str, temp_result)))
        if issue_type == 2 and "".join(map(str, temp_result)) == "".join(map(str, target)):
            print(total_cnt)
        return

    for idx, is_visited in enumerate(visited):
        if not is_visited:
            temp_result[curr_idx] = numbers[idx]
            visited[idx] = 1
            permutation_81(curr_idx+1, visited, temp_result)
            visited[idx] = 0


for _ in range(T):
    N = int(input())
    numbers = [i for i in range(1, N+1)]
    test_case = list(map(int, input().split(" ")))
    issue_type = test_case[0]
    target = test_case[1:]
    total_cnt = 0
    permutation_81(0, [0 for _ in range(N)], [0 for _ in range(N)])


