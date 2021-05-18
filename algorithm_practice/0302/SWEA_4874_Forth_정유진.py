T = int(input())
for test_case in range(1, T + 1):
    problem = input().split()  # 연산 테스트 케이스
    stack = [0]*256  # 256자 이내의 연산 코드
    top = -1  # 스택의 top
    is_error = False  # error 여부

    for i in range(len(problem)-1):  # '.' 직전까지 순회

        if problem[i].isdigit():  # 숫자라면 stack 에 저장
            top += 1
            stack[top] = int(problem[i])

        else:  # 연산자라면

            if stack[top] != 0 and stack[top-1] != 0:  # 연산자 이전에 숫자가 2개 입력 되었는지 확인
                b = stack[top]  # LIFO
                a = stack[top-1]
                top -= 2
                oper = problem[i]

                # 연산자에 맞게 연산한다.
                if oper == '+':
                    top += 1
                    stack[top] = a+b
                elif oper == '-':
                    top += 1
                    stack[top] = a-b
                elif oper == '*':
                    top += 1
                    stack[top] = a*b
                elif oper == '/':
                    top += 1
                    stack[top] = a//b

            else:  # 연산자에 비해 숫자가 부족하다.
                is_error = True
                break

    # stack 에 남아있는 값이 1개 보다 많다면 연산자보다 숫자가 더 많이 입력된 경우, error
    if top != 0:
        is_error = True

    if is_error:
        print('#{} {}'.format(test_case, 'error'))
    else:
        print('#{} {}'.format(test_case, stack[top]))
