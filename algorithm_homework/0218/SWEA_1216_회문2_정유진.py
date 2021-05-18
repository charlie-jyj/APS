# 문자열을 뒤집어 회문인지 판단하는 함수
def is_palindrome(word):
    reverse_word = ''

    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i]

    # 회문일 경우 True 반환하고 아닐 경우 False 반환
    return True if word == reverse_word else False


# 행과 열을 탐색해 회문을 찾는 함수
def find_max_palindrome(text):

    # 회문의 길이를 정한다 100~1
    for m in range(100, 0, -1):
        for i in range(100):
            for j in range(100-m+1):  # 회문의 길이만큼 구간을 잡는다.
                row_word = ''
                col_word = ''

                for k in range(m):  # 구간을 순회하며 char 를 하나씩 추가한다.
                    row_word += text[i][j+k]
                    col_word += text[j+k][i]

                # 행, 열 중에서 회문을 찾았을 경우 그 회문의 길이가 최댓값
                if is_palindrome(row_word) or is_palindrome(col_word):
                    return m

    return -1  # 회문을 찾지 못했다.


for test_case in range(1, 10 + 1):
    tc = int(input())
    origin_text = [list(input()) for i in range(100)]  # 글자판
    max_length = 0  # 회문의 최대 길이

    max_length = find_max_palindrome(origin_text)

    print('#{} {}'.format(tc, max_length))



