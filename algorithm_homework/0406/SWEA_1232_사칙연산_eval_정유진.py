def post_order(n):  # 후위순회를 통해 후위 표기법으로 problem을 작성한다.

    if n > 0:
        post_order(info[n][0])
        post_order(info[n][1])
        problem.append(info[n][2])


def calculate():
    stack = []  # 후위 표기법 계산을 위한 stack

    for item in problem:
        if item in ['+', '-', '*', '/']:  # 연산자일 경우 stack 의 값을 기반으로 연산한다.
            num2 = float(stack.pop())  # 후입선출, 중간 과정 연산은 실수 연산
            num1 = float(stack.pop())

            if item == '+':  # eval 을 썼다면 훨씬 간단했을까
                stack.append(num1+num2)
            elif item == '-':
                stack.append(num1-num2)
            elif item == '*':
                stack.append(num1*num2)
            elif item == '/':
                stack.append(num1/num2)

        else:  # 숫자일 경우 stack 에 저장
            stack.append(float(item))

    return int(stack[0])  # 스택에 남아있는 값이 최종 연산 결과, 정수부만 출력한다.


T = 10  # 테스트 케이스 10개
for tc in range(1, T+1):
    N = int(input())
    info = [[0, 0, ''] for _ in range(N+1)]  # 0: 왼쪽 자식 노드 번호  1: 오른쪽 자식 노드 번호  2: 연산자 혹은 양의 정수

    for i in range(1, N+1):
        temp = input().split()
        length = len(temp)

        if length == 4:  # 입력값의 길이가 4 == 부모 노드 번호, 연산자, 왼쪽 자식 노드 번호, 오른쪽 자식 노드 번호
            p, v, l, r = temp
            info[int(p)][0] = int(l)
            info[int(p)][1] = int(r)
            info[int(p)][2] = v
        elif length == 2:  # 입력값의 길이가 2 == 노드 번호, 양의 정수
            p, v = temp
            info[int(p)][2] = v

    problem = []  # 사칙연산 식의 결과를 담을 리스트
    post_order(1)  # 후위순회
    print('#{} {}'.format(tc, eval(''.join(problem))))  # SWEA에서 못쓴다.
