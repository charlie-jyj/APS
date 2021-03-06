T = int(input())
for test_case in range(1, T + 1):
    origin = input()
    pipes = []  # 쇠막대기를 담을 배열
    pipe_number = 0  # 쇠막대기 전체 숫자
    count_laser = 0  # 쇠막대기가 레이저를 만난 횟수

    i = 0  # origin 을 순회할 인덱스
    while i < len(origin):

        if origin[i] == '(':  # 열린 괄호를 만났을 때,

            if origin[i:i+2] == '()':  # 레이저일 때
                if len(pipes) > 0:  # 쇠막대기가 존재할 때
                    count_laser += len(pipes)

                i += 2  # 인덱스를 2칸 오른쪽으로 민다.

            else:  # 쇠막대기의 시작일 때
                pipe_number += 1  # 쇠막대기 숫자 증가
                pipes.append(pipe_number)  # n번째 쇠막대기를 담는다.
                i += 1

        elif origin[i] == ')':  # 닫힌 괄호를 만났을 때, (쇠막대기의 끝을 의미한다)
            pipes.pop()  # 가장 마지막 쇠막대기를 꺼낸다. -> 리스트에는 아직 끝나지 않은 쇠막대기만 남는다.
            i += 1

    # 레이저를 만난 횟수 + 1 = 쇠막대기 조각의 수
    print('#{} {}'.format(test_case, count_laser + pipe_number))








