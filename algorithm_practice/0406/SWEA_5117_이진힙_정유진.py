def heap_sort(n):  # 자식 노드와 값을 비교하여 교환하는 함수
    global last

    if n <= last:

        if 2 * n <= last:
            if heap[n] > heap[2 * n]:
                heap[n], heap[2 * n] = heap[2 * n], heap[n]
            heap_sort(2 * n)  # 현재 주목 노드를 왼쪽 자식 노드로 돌린다

        if 2 * n + 1 <= last:
            if heap[n] > heap[2 * n + 1]:
                heap[n], heap[2 * n + 1] = heap[2 * n + 1], heap[n]
            heap_sort(2 * n + 1)  # 현재 주목 노드를 오른쪽 자식 노드로 돌린다


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 자연수 개수
    heap = [0]*(N+1)  # 트리
    nums = list(map(int, input().split()))  # N 개의 자연수
    last = 1  # 마지막 인덱스

    while last <= N:  # last 가 N 을 벗어나지 않으면 push 할 수 있다.
        heap[last] = nums[last-1]  # push
        if 1 <= last//2 and heap[last//2] > heap[last]: # 입력한 값이 부모보다 작은 값이면 최소 힙 유지 위해 부모와 교환
            heap[last//2], heap[last] = heap[last], heap[last//2]
        heap_sort(1)  # 전체 트리의 힙 유지를 위해 정렬하겠다
        last += 1  # 다음 추가를 위해 last 증가

    last = N  # last 가 N+1 이므로 다시 N으로 되돌린다.
    heap_sort(1)  # push 모두 끝난 후 최후의 정렬

    heap_sum = 0
    while last >= 1:
        last //= 2
        heap_sum += heap[last]

    print('#{} {}'.format(tc, heap_sum))
