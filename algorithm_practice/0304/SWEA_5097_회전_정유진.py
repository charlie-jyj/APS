T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N개의 자연수, M번의 작업
    numbers = list(map(int, input().split()))  # 수열

    # M번 작업한다.
    for _ in range(M):
        numbers.append(numbers.pop(0))  # 맨 앞의 숫자를 뒤에 보낸다.

    print('#{} {}'.format(test_case, numbers[0]))