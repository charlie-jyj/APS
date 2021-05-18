def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


for tc in range(1, 10+1):
    # N은 dump 횟수
    N =int(input())
    # 박스들
    box = list(map(int, input().split()))

    # N번 덤프하기
    for i in range(N):
        bubble_sort(box)
        box[0] += 1
        box[-1] -= 1

    bubble_sort(box)

    print('#{} {}'.format(tc, box[-1]-box[0]))