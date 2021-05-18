T = int(input())
for test_case in range(1, T + 1):
    # N: 카드의 개수
    N = int(input())
    card = input()

    count = [0] * 10

    max_count = -1
    max_num = -1

    # 카드 숫자 세기
    # 이 때 count 의 max 를 알 수 있다면 추후에 나올 반복문에서 break를 할 수 있어서 편할 것
    for i in card:
        count[int(i)] += 1
        if max_count < count[int(i)]:
            max_count = count[int(i)]

    # for i in range(len(count)):
    #     if max_count <= count[i]:
    #         max_num = i
    #         max_count = count[i]

    for i in range(len(count)-1, -1, -1):
        if max_count == count[i]:
            max_num = i
            break

    print('#{} {} {}'.format(test_case, max_num, max_count))