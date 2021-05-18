def heap_push(value):  # 맨 끝 리프에서 시작
    global heap_size

    heap_size += 1
    heap[heap_size] = value  # 값을 push

    c = heap_size
    p = heap_size // 2

    # 자식에서 위를 향해 루트로 거슬러 올라가면서 heap 을 유지하도록 swap
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p  # 주목 노드를 부모로
        p = c//2


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 자연수 개수
    arr = list(map(int, input().split()))  # N 개의 자연수

    heap = [0] * (N+1)
    heap_size = 0

    # 맨 끝에서부터 노드를 추가한다.
    for v in arr:
        heap_push(v)

    ans = 0

    node = N//2 # 마지막 노드의 조상 노드들의 합이므로

    while node:
        ans += heap[node]
        node = node//2

    print('#{} {}'.format(tc, ans))




