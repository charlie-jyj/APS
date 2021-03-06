T = int(input())
for test_case in range(1, T + 1):

    case_length = int(input())
    cards = list(map(int, input()))

    # cards 를 정렬해서 max 를 구해보자
    for i in range(case_length-1, 0, -1):
        for j in range(0, i):
            if cards[j] > cards[j+1]:
                cards[j], cards[j+1] = cards[j+1], cards[j]

    # cards 중 최댓값을 찾아 counts 배열을 만들자
    max_value = cards[-1]
    counts = [0] * (max_value + 1)

    # cards를 순회하여 등장 횟수를 기록하자
    for card in cards:
        counts[card] += 1

    # counts를 순회하며 max_counts가 무엇이고 그 숫자값은 무엇인지 확인하자.
    max_value = -1
    max_counts = -1

    # max_value가 같을 때에 더 큰 인덱스가 덮어쓰게 한다.
    for idx in range(len(counts)):
        if counts[idx] >= max_counts:
            max_value = idx
            max_counts = counts[idx]

    print('#{} {} {}'.format(test_case, max_value, max_counts))