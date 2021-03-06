T = int(input())
for test_case in range(1, T + 1):
    chars = list(input())  # 입력 받은 문자열
    stack = []

    for char in chars:

        if not stack:  # stack 이 비어있을 때 일단 넣는다.
            stack.append(char)

        elif stack[-1] == char:  # stack 을 peek 해봤더니 넣으려는 char 와 같다 == 중복이므로 pop
            stack.pop()

        elif stack[-1] != char:  # 중복되지 않는 char 이므로 append
            stack.append(char)

    # stack 에 남아있는 char 의 수 = 중복 되지 않는 문자의 수
    print('#{} {}'.format(test_case, len(stack)))