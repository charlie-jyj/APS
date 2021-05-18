for test_case in range(1, 10 + 1):
    N, numbers = input().split()  # 비밀번호 길이, 문자열
    stack = []

    # 문자열을 순회
    for number in numbers:
        if not stack:  # 스택이 비어있다면
            stack.append(number)
        elif stack[-1] == number:  # peek 했을 때 중복이면 pop
            stack.pop()
        elif stack[-1] != number:  # peek 했을 때 중복이 아니면 append
            stack.append(number)

    print('#{} {}'.format(test_case, ''.join(stack)))