
def counting_sort(a, b, c):

# 입력 배열 a
# 정렬된 배열 b
# 카운트 배열 선언 c

# 카운트
    for i in a:
        c[i] += 1

    print(c)
# 누적합 구하기 1~len(c)-1 하면서 직전 인덱스 값과 더해서 누적
    for i in range(1, len(c)):
        c[i] += c[i-1]

    print(c)

# 마지막 인덱스~0 --1하면서 정렬
# count 배열의 값에서 1씩 깎고 b[index]에 a[index] 값을 넣는다.
    for i in range(len(a)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1


if __name__ == '__main__':
    a = [0, 4, 1, 3, 1, 2, 4, 1]
    b = [0] * len(a)
    c = [0]*(max(a)+1)
    counting_sort(a, b, c)
    print(a)
    print(b)