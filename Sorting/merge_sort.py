import random


def merge(left, right):

    # 정렬된 left, right 배열이 넘어온다.

    result = [0] * (len(left)+len(right))
    idx = 0  # result index

    l_idx = 0  # 왼쪽 배열 index
    r_idx = 0  # 오른쪽 배열 index

    while l_idx < len(left) or r_idx < len(right):  # 두 배열을 모두 result로 옮길 때 까지 반복
        if l_idx < len(left) and r_idx < len(right):  # 한 배열이라도 다 옮겨지면 elif 로 넘어갈 것
            if left[l_idx] <= right[r_idx]:
                result[idx] = left[l_idx]
                idx += 1
                l_idx += 1
            else:
                result[idx] = right[r_idx]
                idx += 1
                r_idx += 1
        elif l_idx < len(left):  # 옮길 left 배열이 아직 남아있다.
            result[idx] = left[l_idx]
            idx += 1
            l_idx += 1
        elif r_idx < len(right):
            result[idx] = right[r_idx]
            idx += 1
            r_idx += 1

    # left+right 가 merge 되고 result 배열이 완성되었다.
    return result


def merge_sort(a):
    # 리스트의 길이가 1이 될 때 까지 분할한다

    if len(a) == 1:
        return a

    # 리스트의 길이가 1이 아니라면 반으로 분할한다.
    mid = len(a)//2

    # python 스러운 분할
    left = a[:mid]
    right = a[mid:]

    # merge 된 배열이 반환될 것 (최초의 반환은 길이 1 배열이겠지만)
    new_left = merge_sort(left)
    new_right = merge_sort(right)

    # merge 한 배열을 반환하자
    return merge(new_left, new_right)


before = random.sample(range(100), 10)
print(before)

after=merge_sort(before)

# 정렬이 잘 된다.
print(after)