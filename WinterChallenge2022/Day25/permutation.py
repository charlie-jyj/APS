N = 4
numbers = [i for i in range(1, N + 1)]  # 1, 2, 3
result = [0 for i in range(N)]
total_cnt = 0
outcome = []


def permutation(k: int, visited: [int]):
    global numbers, total_cnt, outcome
    #print(k, result, visited)

    if k == N:
        total_cnt += 1
        #print(f"done with {result}, total: {total_cnt}")
        outcome.append(",".join(map(str, result)))

    else:
        for idx, is_visited in enumerate(visited):
            if not is_visited:
                #print(f"not visited {numbers[idx]}")
                visited[idx] = 1
                result[k] = numbers[idx]
                permutation(k + 1, visited)
                visited[idx] = 0


permutation(0, [0 for _ in range(N)])

print(outcome)