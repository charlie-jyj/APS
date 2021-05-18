def down_heap(n):
    global change_count

    if n <= N:

        if 2*n <= N:
            if heap[n] > heap[2*n]:
                heap[n], heap[2*n] = heap[2*n], heap[n]
                change_count += 1
            down_heap(2*n)

        if 2*n+1 <= N:
            if heap[n] > heap[2*n+1]:
                heap[n], heap[2*n+1] = heap[2*n+1], heap[n]
                change_count += 1
            down_heap(2*n+1)


def up_heap(n):
    global change_count

    if 1 <= n:

        if 1 <= n//2:
            if heap[n//2] > heap[n]:
                heap[n//2], heap[n] = heap[n], heap[n//2]
                change_count += 1
            up_heap(n//2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]*(N+1)
    nums = list(map(int, input().split()))
    change_count = -1

    for i in range(N):
        heap[i+1] = nums[i]

    while True:
        if change_count == 0:
            break
        change_count = 0
        down_heap(1)

    change_count = -1
    while True:
        if change_count == 0:
            break
        change_count = 0
        up_heap(N)

    heap_sum = 0

    while N >= 1:
        N //= 2
        heap_sum += heap[N]

    print('#{} {}'.format(tc, heap_sum))
