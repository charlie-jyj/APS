T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = input().split()

    # for i in range(M):
    #     # 반시계방향 회전 효과
    #     tmp = queue.pop(0)
    #     queue.append(tmp)

    M = M % N
    print(queue[M])