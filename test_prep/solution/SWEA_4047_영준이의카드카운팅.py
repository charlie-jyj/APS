TC = int(input())
for tc in range(1, TC+1):
    str = input()
    res = ''
    card = [[0]*14 for _ in range(4)]
    for i in range(0, len(str), 3):
        value = int(str[i+1:i+3])  # 숫자

        # dictionary 이용하면 더 쉬울 것
        if str[i] == 'S':
            row = 0
        elif str[i] == 'D':
            row = 1
        elif str[i] == 'H':
            row = 2
        else:
            row = 3

        if str[row][value] == 1:
            res = 'ERROR'
            break
        str[0][value] = 1

    # for 문이 끝나서 오는 경우
    if res == 'ERROR':
        print('error')
    else:
        print('수량체크')
