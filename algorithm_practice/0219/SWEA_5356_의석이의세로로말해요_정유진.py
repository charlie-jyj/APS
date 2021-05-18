T = int(input())
for test_case in range(1, T + 1):
    words = [list(input()) for _ in range(5)]
    max_length = 0
    is_break = False

    for w in words:
        if max_length < len(w):
            max_length = len(w)

    answer = ''

    for j in range(max_length):
        for k in range(5):

            if j < len(words[k]):
                answer += words[k][j]

    print('#{} {}'.format(test_case, answer))




