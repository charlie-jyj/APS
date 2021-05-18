for test_case in range(1, 10 + 1):
    tc = int(input())
    password = [0]*9  # 원형 큐, front를 비우기 위해 길이는 9 (비밀번호는 8자리)
    front = rear = 0
    minus = [1, 2, 3, 4, 5]  # 감소 값
    idx = 0 # 감소 값을 다루기 위한 인덱스

    for num in map(int, input().split()):
        rear = (rear+1) % 9
        password[rear] = num

    while password[rear] != 0:

        # pop하고 감소시킨다
        front = (front+1) % 9
        first = password[front]
        password[front] = 0  # 헷갈려서 pop한 자리 0으로 바꿈
        first -= minus[idx % 5]  # 감소시킨다.

        # 감소시킨 후의 값이 0보다 작아지거나 0일 경우 0으로 저장할 것
        if first <= 0:
            first = 0

        # append 한다
        rear = (rear+1) % 9
        password[rear] = first

        # minus 인덱스를 증가
        idx += 1

    # 비밀번호 출력
    if front < rear:
        print('#{} {}'.format(tc, ' '.join(map(str, password[front+1:rear+1]))))
    else:
        print('#{} {}'.format(tc, ' '.join(map(str, password[front+1::]+password[:rear+1:]))))



