def find_set(v):
    if p[v] != v:
        p[v] = find_set(p[v])

    return p[v]


def union(parent, child):
    p[find_set(child)] = find_set(parent)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    answer = 0
    for i in range(M):
        leader, member = map(int, input().split())
        union(leader, member)

    for j in range(1, N+1):  # 팀 리더의 수를 센다
        if j == find_set(j):
            answer += 1

    print('#{} {}'.format(tc, answer))