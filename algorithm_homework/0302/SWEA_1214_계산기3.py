for test_case in range(1, 10 + 1):
    N = int(input())
    before = list(input())
    after = ''
    step1 = []
    step2 = []

    # 1 후위표기식 변환
    for token in before:
        if token.isdigit():  # 숫자라면 출력
            after += token
        else:
            if token == '(':  # 열린 괄호는 우선순위 0 스택에 무조건 저장 저장
                step1.append(token)

            elif token == '+':  # 더하기 연산자 우선순위 2, 우선순위가 더 낮은 연산자가 나올 때 까지 pop

                while True:
                    if step1[-1] == '(':  # 우선순위 3
                        step1.append(token)  # 우선 순위 낮은 연산자가 나오면 더하기를 스택에 저장
                        break
                    else:  # * 우선순위
                        after += step1.pop()

            elif token == '*':

                while True:
                    if step1[-1] in ['(', '+']:
                        step1.append(token)
                        break
                    else:
                        after += step1.pop()

            elif token == ')':  # 닫힌 괄호일 경우 열린 괄호가 stack 의 top 이 될 때 까지 pop

                while True:
                    if step1[-1] == '(':
                        step1.pop()
                        break
                    else:
                        after += step1.pop()

    # 연산하기
    for token in after:
        if token.isdigit():  # 숫자일 경우 스택에 저장
            step2.append(token)
        else:
            b = int(step2.pop())  # LIFO
            a = int(step2.pop())

            if token == '+':  # 연산 결과를 스택에 저장
                step2.append(a+b)
            elif token == '*':
                step2.append(a*b)

    # stack 의 top 의 값이 최종 결과
    print('#{} {}'.format(test_case, step2[-1]))

