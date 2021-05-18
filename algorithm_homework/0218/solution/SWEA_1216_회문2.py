import sys
sys.stdin = open('input_1216.txt', 'r')


def my_find(M):

    for i in range(N):
        for j in range(N-M+1):

            # 가로 검사
            for k in range(M//2):
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                elif k == M//2-1:
                    return M

            # 세로 검사
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2-1:
                    return M
    return 0


def my_find_2(M):
    for i in range(N):
        for j in range(N-M+1):
            tmp = words[j][j:j+M]
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0


for tc in range(10):
    tc_num = int(input())

    N = 100

    words = [input() for _ in range(N)]
    zwords = list(zip(*words))

    for i in range(N, 0, -1):
        ans = my_find(i)

        if ans != 0:
            break

    print(ans)