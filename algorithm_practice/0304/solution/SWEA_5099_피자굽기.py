T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    pizza = list(map(int, input().split()))  # 피자
    firepot = list()  # 화덕

    for i in range(N):
        firepot.append((i+1, pizza[i]))

    next_pizza = N  # 다음 피자는 N 번부터 넣어야 한다
    last_pizza = -1

    while firepot:
        num, cheeze = firepot.pop(0)

        cheeze//=2
        last_pizza = num

        # 치즈 양이 남아있다
        if cheeze:
            firepot.append((num, cheeze))
        else:
            if next_pizza < M:
                firepot.append((next_pizza+1, pizza[next_pizza]))

                next_pizza += 1

    print('#{} {}'.format(tc, last_pizza))