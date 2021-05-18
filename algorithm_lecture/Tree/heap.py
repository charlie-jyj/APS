import heapq


def heap_push(item):
    global heap_count
    heap_count += 1
    heap[heap_count] = item

    curr = heap_count
    parent = curr//2

    # 최소 힙을 만족하기 위해서 루트이면 멈추게 하고 부모와 자식 비교
    while parent and heap[curr] < heap[parent]:
        heap[parent], heap[curr] = heap[curr], heap[parent]
        curr = parent
        parent = curr//2


def heap_pop():
    global heap_count

    item = heap[1]  # root
    heap[1] = heap[heap_count]  # 마지막 원소를 루트 자리에 둔다
    heap[heap_count] = 0  # 마지막 원소 값을 0으로 갱신
    heap_count -= 1  # 마지막 원소가 사라진 것을 표현

    parent = 1  # 부모 노드 (루트에서 시작)
    child = 2*parent  # 자식 노드
    if child + 1 <= heap_count and heap[child] > heap[child + 1]:  # 오른쪽 자식이 존재하고, 오른쪽 자식의 값이 더 작을 때
        child += 1

    while child <= heap_count and heap[parent] > heap[child]:  # 자식이 유효 범위 내에 있고 부모 > 자식이면 계속 반복
        heap[parent], heap[child] = heap[child], heap[parent]  # 부모 자식의 값 갱신 (최소 힙 유지를 위해)
        parent = child  # 주목 노드를 자식으로 돌리고
        child = 2*parent
        if child+1 <= heap_count and heap[child] > heap[child+1]:
            child += 1


    return item


arr = [1, 8, 3, 9, 10, 2]
N = len(arr)

heap = [0]* (N+1)
heap_count = 0  # 가장 마지막 자리를 가리키는 인덱스

for i in arr:
    heap_push(i)

print(heap[1:heap_count])

heap_pop()

print(heap[1:heap_count])