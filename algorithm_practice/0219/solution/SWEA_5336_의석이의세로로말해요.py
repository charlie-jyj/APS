T =int(input())

for tc in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())

        if len(word[i]) > max_len:
            max_len = word[i]


    for i in range(max_len):
        for j in range(5):

            if i < len(word[j]):
                word[i][j]
