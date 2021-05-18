# step 1 중위표기식 -> 후위표기식
before = '(6+5*(2-8)/2)'
step1_stack = []
after = ''

for token in before:

    if ord('0') <= ord(token) <= ord('9'):  # 숫자일때 출력
        after += token

    else:  # 연산자 일때 stack 에 append

        if token == '(':  # 우선 순위 3
            step1_stack.append(token)

        elif token == '*' or token == '/':  # 우선순위 2

            while step1_stack:  # stack 에서 우선순위 낮은 연산자 발견할 때 까지 반복

                peek = step1_stack[-1]

                if peek == '+' or peek == '-' or peek == '(':  # 우선순위 1,0
                    step1_stack.append(token)
                    break
                else:
                    after += step1_stack.pop()  # 현재 token 보다 우선순위가 높은 연산자는 출력

        elif token == '+' or token == '-':

            while step1_stack:

                peek = step1_stack[-1]

                if peek == '(':  # 우선순위 0
                    step1_stack.append(token)
                    break
                else:
                    after += step1_stack.pop()

        elif token == ')':

            while step1_stack:

                peek = step1_stack[-1]

                if peek == '(':  # 여는 괄호를 만나면 여는 괄호 pop 하고 break
                    step1_stack.pop()
                    break
                else:  # 여는 괄호 만날 때 까지 출력
                    after += step1_stack.pop()

print(after)

# step 2 연산하기
step2_stack = []
answer = 0

for token in after:

    if ord('0') <= ord(token) <= ord('9'):  # 숫자일 때 stack 에 append
        step2_stack.append(token)

    else:  # 연산자 일때
        b = step2_stack.pop()  # LIFO
        a = step2_stack.pop()

        # 연산자에 따라서 연산
        if token == '+':
            step2_stack.append(int(a)+int(b))
        elif token == '-':
            step2_stack.append(int(a)-int(b))
        elif token == '*':
            step2_stack.append(int(a)*int(b))
        elif token == '/':
            step2_stack.append(int(a)/int(b))

# stack 에 남아있는 값이 연산 결과
answer = step2_stack[-1]
print(answer)