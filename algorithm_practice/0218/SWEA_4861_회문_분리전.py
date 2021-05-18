def check_palindrome(origin):

    reverse_t = ''
    for i in range(len(origin)-1, -1, -1):
        reverse_t += origin[i]

    return True if origin == reverse_t else False


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    text = [list(input()) for i in range(N)]
    answer = ''
    is_answer = False

    # 행우선순회
    for i in range(N):
        for j in range(N-M+1):
            row_text = ''
            for k in range(M):
                row_text += text[i][j+k]
            is_answer = check_palindrome(row_text)
            if is_answer:
                answer = row_text
                break
        if is_answer:
            break

    # 열우선순회
    for j in range(N):
        for i in range(N-M+1):
            col_text = ''
            for k in range(M):
                col_text += text[i+k][j]
            is_answer = check_palindrome(col_text)
            if is_answer:
                answer = col_text
                break
        if is_answer:
            break

    print('#{} {}'.format(test_case, answer))
