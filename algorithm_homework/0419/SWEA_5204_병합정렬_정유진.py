# 병합과 오름차순 정렬
def merge(left, right):
    global cnt
    l_len = len(left)
    r_len = len(right)
    if left[l_len-1] > right[r_len-1]:  # 왼쪽 배열의 끝 원소 > 오른쪽 배열의 끝 원소 => 오른쪽 마지막 원소가 먼저 복사된다
        cnt += 1

    result = [0] * (l_len+r_len)  # 반환할 정렬 결과 배열
    idx = l_idx = r_idx = 0  # 결과 배열 인덱스, 왼쪽 배열 인덱스, 오른쪽 배열 인덱스

    while l_idx < l_len or r_idx < r_len:  # 왼쪽 배열과 오른쪽 배열 모두 다 복사할 때 까지 도는 반복문
        while l_idx < l_len and r_idx < r_len:  
            if left[l_idx] <= right[r_idx]:  # 왼쪽 배열의 원소가 오른쪽 배열 원소 보다 더 작은 경우
                result[idx] = left[l_idx]
                l_idx += 1
                idx += 1
            else:  # 오른쪽 배열의 원소가 왼쪽 배열 원소 보다 더 작은 경우
                result[idx] = right[r_idx]
                r_idx += 1
                idx += 1

        while l_idx < l_len:  # 왼쪽 배열에만 복사할 원소가 남아 있는 경우
            result[idx] = left[l_idx]
            l_idx += 1
            idx += 1

        while r_idx < r_len:  # 오른쪽 배열에만 복사할 원소가 남아 있는 경우
            result[idx] = right[r_idx]
            r_idx += 1
            idx += 1

    return result  # 복사 완료


# 분할
def merge_sort(a):
    if len(a) == 1:  # 더 이상 분할 할 수 없어 길이 1의 배열 반환
        return a

    mid = len(a) // 2  # 중앙값
    L = merge_sort(a[:mid])  # 분할+병합 정렬 => 왼쪽 부분 반환
    R = merge_sort(a[mid:])  # 분할+병합 정렬 => 오른쪽 부분 반환

    return merge(L, R)  # 병합하러 가기


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)

    print('#{} {} {}'.format(tc, result[N//2], cnt))