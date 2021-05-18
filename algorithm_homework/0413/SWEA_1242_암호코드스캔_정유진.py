import sys
sys.stdin = open("sample.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 배열의 세로, 배열의 가로
    codes = [ list(input()) for _ in range(N) ]  # 배열을 입력받았다
    hex = {'0': '0000',  # 16진수를 바로 2진수로 바꾸기 위한 dict
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111'
           }

    pattern = {'112': 0,  # 비율을 기록했다 뒤에서부터 읽었을 때, 1의 개수 : 0의 개수 : 1의 개수
               '122': 1,
               '221': 2,
               '114': 3,
               '231': 4,
               '132': 5,
               '411': 6,
               '213': 7,
               '312': 8,
               '211': 9,
    }

    # 16진수를 2진수로 바꾼다 => (길이가 4*M 인 2진수 문자열)이 N개
    bi_codes = ['']*N
    for i in range(N):
        for j in range(M):
            bi_codes[i] += hex[codes[i][j]]

    pwd = []  # 암호 코드
    pwd_list = []  # 암호 코드 중복을 피하기 위해
    answer = 0

    for i in range(N):  # 한 줄씩 배열을 보겠다
        cnt1 = cnt2 = cnt3 = 0  # 1 -> 0 -> 1 -> 0 (마지막 0들은 끝이 어딘지 몰라서 세지 않는다)
        if bi_codes[i] == '0'*(4*M):  # 0으로만 이루어진 배열은 무시한다
            continue

        for j in range(4*M-1, -1, -1):  # 2진수 문자열을 뒤에서 부터 보겠다.

            if cnt2 == 0 and cnt3 == 0 and bi_codes[i][j] == '1' and bi_codes[i-1][j] == '0':  # 1들을 만났다 (암호코드의 시작) + 중복 피하려 내 위에 칸이 0인지 확인
                cnt1 += 1
            elif cnt1 != 0 and cnt3 == 0 and bi_codes[i][j] == '0' and bi_codes[i-1][j] == '0' :  # 0들을 만났다
                cnt2 += 1
            elif cnt1 != 0 and cnt2 != 0 and bi_codes[i][j] == '1' and bi_codes[i-1][j] == '0':  # 다시 1들을 만났다
                cnt3 += 1
            elif cnt1 != 0 and cnt2 != 0 and cnt3 != 0 and bi_codes[i][j] == '0' and bi_codes[i-1][j] == '0':  # 다시 0을 만났으니 비율을 따질 수 있다.

                div = min(cnt1, cnt2, cnt3)  # 최솟값으로 각각을 나누어 주면 최소 비율을 알 수 있다
                ratio = str(cnt1//div) + str(cnt2//div) + str(cnt3//div)  # 1의 비율 : 0의 비율 : 1의 비율
                pwd = [pattern[ratio]] + pwd  # 암호 코드 => 숫자 변환 => 앞으로 누적시킨다

                cnt1 = cnt2 = cnt3 = 0  # 다음 숫자를 찾으러 간다. (8자리가 될 때 까지)

            if len(pwd) == 8:  # 8자리의 코드를 다 모았다
                check = (pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3 + pwd[1] + pwd[3] + pwd[5] + pwd[7]  # 암호 유효성 검사
                if check % 10 == 0 and pwd not in pwd_list:  # 10으로 나누어지는가? 중복이 아닌가?
                    pwd_list.append(pwd)
                    answer += sum(pwd)
                pwd = []  # pwd 를 초기화하고 새로운 암호 코드를 찾으러 간다

    print('#{} {}'.format(tc, answer))


