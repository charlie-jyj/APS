def post_order(n):

    if n > 0:

        num1 = post_order(info[n][0])  # 왼쪽 자식 노드로
        num2 = post_order(info[n][1])  # 오른쪽 자식 노드로

        if not info[n][2].isnumeric(): # 연산자라면, 반환값으로 연산한다.
            item = info[n][2]
            temp_result = 0
            if item == '+':
                temp_result = num1 + num2
            elif item == '-':
                temp_result = num1 - num2
            elif item == '*':
                temp_result = num1 * num2
            elif item == '/':
                temp_result = num1 / num2
            info[n][2] = temp_result  # 노드의 값을 연산자 => 연산 결과로 교체

        return float(info[n][2]) # 숫자값 반환 (실수 연산을 위해 float 으로 형변환)


T = 10  # 테스트 케이스 10개
for tc in range(1, T+1):
    N = int(input())
    info = [[0, 0, ''] for _ in range(N+1)]  # 0: 왼쪽 자식 노드 번호  1: 오른쪽 자식 노드 번호  2: 연산자 혹은 양의 정수

    for i in range(1, N+1):
        temp = input().split()  # 노드 정보 입력
        length = len(temp)

        if length == 4:  # 입력값의 길이가 4 == 부모 노드 번호, 연산자, 왼쪽 자식 노드 번호, 오른쪽 자식 노드 번호
            p, v, l, r = temp
            info[int(p)][0] = int(l)
            info[int(p)][1] = int(r)
            info[int(p)][2] = v
        elif length == 2:  # 입력값의 길이가 2 == 노드 번호, 양의 정수
            p, v = temp
            info[int(p)][2] = v

    print('#{} {}'.format(tc, int(post_order(1))))  # 후위 순회

