T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())  # 화덕의 크기, 피자 수
    pizza_cheese = list(map(int, input().split()))  # 재료준비
    oven = []
    pizza = []

    # 피자만들기
    for i in range(M):
        pizza.append((i+1, pizza_cheese[i]))

    # 오븐에 피자 넣기
    while len(oven) != N and len(pizza) != 0:
        oven.append(pizza.pop(0))

    # 오븐에 최후의 피자 1개가 남을 때 까지 반복
    while len(oven) != 1:

        pizza_num, cheese = oven.pop(0)  # 일단 꺼내본다.
        cheese //= 2  # 넣으면서 한 바퀴 돌았다고 생각한다.

        if cheese == 0: # 치즈 다 녹았다
            if pizza:  # 대기중인 피자가 있다면 넣는다
                oven.append(pizza.pop(0))

        else:
            oven.append((pizza_num, cheese))  # 꺼냈던 피자를 다시 넣는다 (치즈는 절반)

    print('#{} {}'.format(test_case, oven[0][0]))