T = int(input())
for test_case in range(1, T + 1):
    # 입력된 숫자
    number = int(input())
    # 소인수
    prime_numbers = [2, 3, 5, 7, 11]
    # 정답을 담을 list
    answers = []

    for prime_number in prime_numbers:
        # 지수를 count할 변수
        exp = 0
        # number가 소인수로 나누어진다면 반복
        while number % prime_number == 0:
            exp += 1
            number //= prime_number

        # 지수를 기록하고 다음 소인수로 넘어간다.
        answers.append(exp)

    print('#{} {}'.format(test_case, ' '.join(map(str, answers))))