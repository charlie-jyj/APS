T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 최댓값
    max_value = 0

    # 길이를 비교해 긴 문자열과 짧은 문자열을 정한다.
    longer = a if len(a) > len(b) else b
    shorter = b if len(a) > len(b) else a

    # 긴 문자열 기준으로 i를 옮긴다. 0~ 긴문자열 길이-짧은문자열 길이
    for i in range(0, len(longer)-len(shorter)+1):
        result = 0
        # 마주보는 위치의 숫자끼리 곱한다
        for j in range(len(shorter)):
            result += shorter[j] * longer[i+j]
        # 최댓값을 갱신한다.
        if max_value < result:
            max_value = result

    print('#{} {}'.format(test_case, max_value))


