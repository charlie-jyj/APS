for test_case in range(1, 10 + 1):
    N = int(input())
    before = input()
    after = ''
    step1 = []
    step2 = []

    # step1 후위표기식으로 변환
    for token in before:
        if ord('0') <= ord(token) <= ord('9'):  # 숫자일 때 출력
            after += token
        else:  # 연산자일때 stack 에 저장

            while step1:  # 스택에 값이 있는 동안 반복
                if token == '+':  # + 연산자는 어떤 연산자를 만나더라도 모든 연산자를 pop 하고 출력
                    top = step1[-1]
                    after += step1.pop()

                elif token == '*':
                    top = step1[-1]
                    if top == '*':  # * 연산자는 * 연산자를 만났을 때 pop 하고 출력
                        after += step1.pop()
                    else:  # * 연산자는 + 연산자를 만나면 break
                        break

            step1.append(token)  # 연산자 저장

    # 스택에 남은 연산자가 있다면 출력
    while step1:
        after += step1.pop()

    # step2 연산하기
    for token in after:
        if ord('0') <= ord(token) <= ord('9'):  # 숫자는 스택에 저장
            step2.append(token)
        else:  # 연산자는 연산 시작
            b = step2.pop()  # 후입선출
            a = step2.pop()

            if token == '+':
                step2.append(int(a)+int(b))
            elif token == '*':
                step2.append(int(a)*int(b))

    print('#{} {}'.format(test_case, step2[-1]))