# import sys
# sys.stdin = open("input.txt", "r")


def change_cards(n):  # n 번 만큼 교환을 하겠다.
    global max_value, size

    if n == 0:  # 교환 횟수를 다 사용했다.
        result = int(''.join(cards))
        max_value = max(max_value, result)  # 최댓값을 갱신한다.
        return

    for i in range(size):  # 앞에서부터 나 자신을 제외하고 내 다음 원소들과 교환한다 (순열과 비슷)
        for j in range(i+1, size):
            cards[i], cards[j] = cards[j], cards[i]  # 교환

            # 중복 검사 (dict 사용)
            key = ''.join(cards)
            if cards_dict.get((n, key), 1):  # 중복을 피하기 위한 검증, 현재 교환의 결과가 이전에 나온적이 있었나?(x in list 썼더니 시간초과)
                cards_dict[(n, key)] = 0  # n 회차에 이런 숫자 조합이 나왔다.
                change_cards(n-1)  # 이 숫자 조합을 가지고 다음 레벨로 이동

            cards[i], cards[j] = cards[j], cards[i]  # cards 를 재활용하기 때문에 원상복구


T = int(input())
for tc in range(1, T+1):
    N, L = input().split()
    cards = list(N)  # 숫자 하나씩 뜯어보려고 list 화
    limit = int(L)
    size = len(cards)  # 길이
    cards_dict = {}  # 중복 검사용 dict
    max_value = 0  # 갱신될 최댓값

    change_cards(limit)

    print('#{} {}'.format(tc, max_value))
