T = int(input())
for test_case in range(1, T + 1):

    cards = input()  # 영준이 소유한 카드
    check = [[0]*13 for _ in range(4)]  # 카드 보유 수를 표시할 리스트
    answer = [0] * 4  # 가지지 않은 카드 수
    is_error = False  # 중복된 카드를 가졌는지

    for i in range(0, len(cards)-3+1, 3):  # 구간 3, step 3
        card = []
        for j in range(3):
            card.append(cards[i+j])  # card[0] = 카드 종류, card[1] = 십의 자리, card[2] = 일의 자리

        card_type = -1
        card_number = -1

        # 카드 종류를 확인한다
        if card[0] == 'S':
            card_type = 0
        elif card[0] == 'D':
            card_type = 1
        elif card[0] == 'H':
            card_type = 2
        else:
            card_type = 3

        # 카드 숫자를 확인한다.
        card_number = int(card[1])*10 + int(card[2])

        # 카드 보유를 표시한다.
        check[card_type][card_number-1] += 1

    # 카드 보유량을 확인하여 중복된 카드가 있을 경우 break, 그렇지 않을 경우 가지지 않은 카드의 수 출력
    for i in range(4):
        cnt = 0
        for j in range(13):
            if check[i][j] == 2:
                is_error = True
                break
            elif check[i][j] == 0:
                cnt += 1
        else:
            answer[i] = cnt

        if is_error:
            print('#{} {}'.format(test_case, 'ERROR'))
            break
    else:
        print('#{} {}'.format(test_case, ' '.join(map(str, answer))))