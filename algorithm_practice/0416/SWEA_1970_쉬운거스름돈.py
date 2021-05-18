"""
잔액을 각 금액으로 나누어서 몫이 1 이상이면 그 금액으로 몫만큼 주는 것
잔액을 갱신하고 다음 화폐 단위로 나눈다
잔액 갱신 = > N = N%bills[i]

"""
T = int(input())
for tc in range(1, T+1):
    change = int(input())
    cnt = [0] * 8  # 단위 당 사용할 개수
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # 화폐단위

    i = 0
    while change >= 10:  # 10 원 미만 금액은 거슬러줄 수 없다
        cnt[i] = change // money[i]  # 화폐단위로 나눈 몫 = 해당 단위로 거슬러 줄 수 있는 최대 수
        change %= money[i]  # 잔액 갱신
        i += 1  # 단위를 바꾼다

    print('#{}'.format(tc))
    for c in cnt:
        print('{}'.format(c), end=' ')
    print()