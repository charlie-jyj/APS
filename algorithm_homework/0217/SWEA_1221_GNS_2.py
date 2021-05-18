T = int(input())
for test_case in range(1, T + 1):
    TC, L = map(str, input().split())  # 테스트케이스 번호, 테스트 케이스 길이
    length = int(L)
    text = input().split()
    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    counting = [0] * 10
    result = ''

    for i in range(len(text)):
        if text[i] == 'ZRO':
            counting[0] += 1
        elif text[i] == 'ONE':
            counting[1] += 1
        elif text[i] == 'TWO':
            counting[2] += 1
        elif text[i] == 'THR':
            counting[3] += 1
        elif text[i] == 'FOR':
            counting[4] += 1
        elif text[i] == 'FIV':
            counting[5] += 1
        elif text[i] == 'SIX':
            counting[6] += 1
        elif text[i] == 'SVN':
            counting[7] += 1
        elif text[i] == 'EGT':
            counting[8] += 1
        else:
            counting[9] += 1

    for i in range(len(order)):
        for j in range(counting[i]):
            result += order[i]+' '

    print(TC)
    print(result)