def is_win(card_list):
    counting = [0]*10  # 카드 숫자의 빈도 수를 기록할 배열
    for card in card_list:
        counting[card] += 1

    for i in range(10):  # triplet 검사
        if counting[i] >= 3:
            return 1

    for i in range(10-3+1):  # run 검사
        if counting[i] > 0 and counting[i+1] > 0 and counting[i+2] > 0:
            return 1

    # 아무 것도 아닐 경우
    return 0


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    answer = 0

    A = []  # 플레이어 1 의 카드덱
    B = []  # 플레이어 2 의 카드덱

    for i in range(len(cards)):
        if i % 2:  # 홀수 번째 round == B 가 카드를 받을 차례
            B.append(cards[i])
        else:  # 짝수 번째 round == A 가 카드를 받을 차례
            A.append(cards[i])

        if i >= 4:  # round 4 부터 승부를 가릴 수 있다 (A의 카드가 3장이 되는 순간)
            if i % 2:  # 홀수 번째 round == B 의 승패 검사
                if is_win(B):
                    answer = 2
                    break  # 우승자가 나오면 반복문을 빠져나간다
            else:  # 짝수 번째 round == A 의 승패 검사
                if is_win(A):
                    answer = 1
                    break

    print('#{} {}'.format(tc, answer))
