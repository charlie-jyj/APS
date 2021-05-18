def hoare_partition(a:list, left, right):

    pivot = (left+right)//2  # 피봇: 가운데 값

    while left < right:  # left==right 일 때 까지 도는 반복문
        while left < right and a[left] < a[pivot] : left += 1  # pivot 과 같거나 큰 값을 만나면 멈춘다
        while left < right and a[pivot] <= a[right] : right -= 1  # pivot 보다 작은 값을 만나면 멈춘다

        if left < right:
            if left == pivot:  # left가 pivot 위치에서 멈췄다면 pivot이 right 자리로 옮겨지므로 pivot 인덱스 갱신
                pivot = right
            a[left], a[right] = a[right], a[left]  # 각자가 멈춘 자리에서 값을 교환 (피봇을 중심으로 작은 값, 큰 값 자리 찾기)

    a[pivot], a[right] = a[right], a[pivot]  # left== right 인 시점, 피봇이 있어야 할 자리를 찾아준다.

    return right  # 피봇의 위치를 반환한다


def lomuto_partition(a:list, left, right):
    pivot = a[right]  # 피봇 : 오른쪽 맨 끝 값
    i = left - 1  # j를 따라갈 인덱스

    for j in range(left, right):  # 시작 인덱스~ 끝 - 1 인덱스 까지 j 이동
        if a[j] <= pivot:  # pivot 값 보다 작거나 같을 경우 i 증가, i는 pivot 이하인 원소들의 가장 끝 인덱스
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[right] = a[right], a[i+1]  # pivot 자리 찾아주기, i + 1

    return i+1


def quick_sort(a:list, left, right):

    if left < right:  # 분할하면서 바로 정렬한다
        p = hoare_partition(a, left, right)
        # p = lomuto_partition(a, left, right)
        quick_sort(a, left, p-1)  # 피봇을 제외하고 왼쪽 분할
        quick_sort(a, p+1, right)  # 피봇을 제외하고 오른쪽 분할


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)

    print('#{} {}'.format(tc, arr[N//2]))