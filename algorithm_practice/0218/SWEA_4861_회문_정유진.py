# 회문인지를 판단하는 함수
def check_palindrome(origin):

    reverse_t = ''
    for i in range(len(origin)-1, -1, -1):
        reverse_t += origin[i]

    return True if origin == reverse_t else False


# 회문을 찾는 함수 (글자판, 글자판길이, 회문길이, 방향)
def scan_rows_cols(origin, n, m, direction):

    # 행 우선 순회
    for i in range(N):
        for j in range(N-M+1):
            word = ''
            for k in range(M):  # 정해진 구간 만큼 단어를 자른다.

                # 가로, 세로를 구분한다.
                if direction == 'row':
                    word += text[i][j+k]
                else:
                    word += text[j+k][i]

            # 정해진 구간만큼 자른 단어가 회문인지 판단한다.
            if check_palindrome(word):
                return word

    # 회문을 찾지 못했을 때 반환한다.
    return 'fail'


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    text = [list(input()) for i in range(N)]
    row_answer = ''  # 행에서 찾은 회문
    col_answer = ''  # 열에서 찾은 회문

    # 회문 찾기 함수 호출
    row_answer = scan_rows_cols(text, N, M, 'row')
    col_answer = scan_rows_cols(text, N, M, 'col')

    print('#{} {}'.format(test_case, row_answer if row_answer != 'fail' else col_answer))
