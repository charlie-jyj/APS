T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 부분집합의 원소의 수, 부분집합의 합
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 집합 A
    answer = 0  # 반환할 정답

    # 부분집합 만들기
    for i in range(1<<12):
        sum_result = 0
        count_result = 0
        for j in range(12):
            if i & (1<<j):
                count_result += 1
                sum_result += A[j]
        # N, K와 일치하면 answer 1 증가
        if count_result == N and sum_result == K:
            answer += 1

    print('#{} {}'.format(test_case, answer))

