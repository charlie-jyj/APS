# 유효성 판단 함수
def is_valid_stack(stack, top):

    # 괄호문자를 처음부터 끝까지 순회한다.
    for member in members:

        # 열린 괄호일 경우 list 에 append 하고 top 을 1 증가 시킨다
        if member == '(':
            stack.append(member)
            top += 1
        elif member == '[':
            stack.append(member)
            top += 1
        elif member == '{':
            stack.append(member)
            top += 1
        elif member == '<':
            stack.append(member)
            top += 1

        # 닫힌 괄호일 경우 list 의 마지막 인덱스(top) 값을 확인한다.
        # 짝이 맞는 괄호이면 pop 하고 top 을 1 감소 시킨다.
        # 짝이 맞지 않을 경우 0 반환한다.
        if member == ')':
            if stack[top] == '(':
                stack.pop()
                top -= 1
            else:
                return 0
        elif member == ']':
            if stack[top] == '[':
                stack.pop()
                top -= 1
            else:
                return 0
        elif member == '}':
            if stack[top] == '{':
                stack.pop()
                top -= 1
            else:
                return 0
        elif member == '>':
            if stack[top] == '<':
                stack.pop()
                top -= 1

    # 반복문이 끝난 후에 남아있는 괄호가 있으면 짝이 없는 괄호이므로 0을 반환한다.
    if len(stack) > 0:
        return 0
    else:
        return 1


for tc in range(1, 10+1):
    N = int(input())
    members = list(input())
    stack = []
    top = -1

    answer = is_valid_stack(stack, top)
    print('#{} {}'.format(tc, answer))



