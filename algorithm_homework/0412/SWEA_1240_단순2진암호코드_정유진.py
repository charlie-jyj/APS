T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 배열의 세로, 배열의 가로
    codes = []
    for _ in range(N):  # 배열을 이어붙여 한 줄로 만들었다.
        codes += list(input())
    pwd = [0, 0, 0, 0, 0, 0, 0, 0]  # 8자리의 암호코드
    pattern = {  # 숫자 그림으로 표시하기
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    idx = N*M-1
    while True:
        if codes[idx] == '1':  # 숫자 코드를 뒤에서 부터 읽어 1을 발견했을 때
            for i in range(8):  # 최초의 1부터 7자리씩 slicing
                pwd[7-i] = pattern[''.join(codes[idx-6:idx+1])]  # 암호패턴에서 값을 찾아 pwd 에 기록
                idx -= 7  # 구간을 앞으로 7 이동한다
            break

        else:
            idx -= 1

    answer = 0
    if not ((pwd[0]+pwd[2]+pwd[4]+pwd[6])*3+(pwd[1]+pwd[3]+pwd[5])+pwd[7]) % 10:  # 정상적인 암호라면 암호코드의 합을 반환한다.
        answer = sum(pwd)

    print('#{} {}'.format(tc, answer))