"""
11 45 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0
"""


def lomuto_partition(arr, left, right):
    pivot = right
    i = left - 1

    for j in range(left, pivot):  # 맨 오른쪽 끝이 pivot 이므로 left 에서 pivot-1 까지
        if arr[j] <= arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]

    return i+1


def hoare_partition(arr, left, right):
    pivot = (left+right)//2
    while left < right:
        while left<right and arr[left] < arr[pivot] : left += 1
        while left<right and arr[pivot] <= arr[right] : right -= 1

        if left<right:
            if left == pivot:
                pivot = right
            arr[left], arr[right] = arr[right], arr[left]

    arr[pivot], arr[right] = arr[right], arr[pivot]

    return right


def quick_sort(arr, left, right):
    if left < right:
        # p = hoare_partition(arr, left, right)
        p = lomuto_partition(arr, left, right)
        quick_sort(arr, left, p-1)
        quick_sort(arr, p+1, right)


arr = list(map(int, input().split()))
n = len(arr)

quick_sort(arr, 0, n-1)

print(arr)


