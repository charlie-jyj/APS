for test_case in range(1, 10 + 1):
    tc = int(input())
    text = [list(input()) for i in range(100)]  # 글자판
    max_length = 0  # 회문의 최대 길이
    is_row_found = False
    is_col_found = False

    # 행 우선 검색
    # 회문의 길이 정하기 100 ~ 1
    for m in range(100, 0, -1):
        for i in range(100):
            for j in range(100-m+1):  # 회문의 길이를 구간으로 삼는다.

                for k in range(m):  # 구간 안의 문자열이 회문인지 판단한다. (양끝의 문자가 같은지 확인)
                    if text[i][j+k] != text[i][j+m-1-k]:  # 회문이 아니다.
                        break

                else:  # 반복문이 break 없이 종료되었다 = 구간 안의 문자열이 회문이었다는 뜻
                    is_row_found = True
                    max_length = m  # 구간을 내림차순으로 정하기 때문에 처음 등장한 회문 길이가 최댓값
                    break

            if is_row_found:  # 회문을 찾았다면 반복문을 빠져나간다.
                break

        if is_row_found:
            break

    # 열 우선 검색
    for m in range(100, 0, -1):
        for j in range(100):
            for i in range(100 - m + 1):

                for k in range(m):
                    if text[i+k][j] != text[i+m-1-k][j]:  # 회문이 아니다.
                        break
                else:
                    is_col_found = True
                    if max_length < m:  # 최댓값을 갱신한다.
                        max_length = m
                        break

            if is_col_found:
                break

        if is_col_found:
            break

    print('#{} {}'.format(tc, max_length))






