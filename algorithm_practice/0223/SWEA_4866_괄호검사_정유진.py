T = int(input())
for test_case in range(1, T + 1):
    codes = input()
    stack = []
    is_valid = False  # 유효한 괄호인지

    # 입력 받은 코드를 처음부터 끝까지 순회한다.
    for code in codes:
        # 여는 괄호는 stack 에 append 한다
        if code == '(':
            stack.append(code)
        elif code == '{':
            stack.append(code)

        # 닫힌 괄호가 나왔을 때 검사해야할 것 1. stack 이 비어있는가? 2. 직전 괄호가 짝이 맞는가? (단축평가 순서 주의)
        # 위의 조건 중 하나라도 해당된다면 유효하지 않은 괄호이므로 break
        if code == ')':
            if len(stack) == 0 or stack[-1] != '(':
                break
            else:
                stack.pop()  # 비어있지 않고 짝이 맞는 괄호라면 pop 한다.
        elif code == '}':
            if len(stack) == 0 or stack[-1] != '{':
                break
            else:
                stack.pop()

    # break 되지 않고 반복문이 끝까지 돌았을 때,
    else:
        if stack:  # stack 에 값이 남아있다면 짝이 맞지 않는 것이므로 유효하지 않다.
            is_valid = False
        else:  # stack 이 비어있다면 괄호 검사 통과라는 뜻
            is_valid = True

    if is_valid:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))
