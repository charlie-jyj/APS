T = int(input())
for test_case in range(1, T + 1):

    N, Q = map(int, input().split())

    # 박스 초기화
    boxes = [0] * N

    # 작업[L, R]을 순서대로 work 에 담는다, index 로 접근할 것이라 L-1, R-1 을 담는다.
    for i in range(Q):
        work = list(map(lambda x: int(x)-1, input().split()))

        # 배열의 L~R 구간에 i+1 로 채운다.
        for j in range(work[0], work[1]+1):
            boxes[j] = i+1

    print('#{} {}'.format(test_case, ' '.join(map(str, boxes))))
