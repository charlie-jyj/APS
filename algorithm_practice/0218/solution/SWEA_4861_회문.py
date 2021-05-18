import sys
sys.stdin = open('input_4861.txt', 'r')


def my_reverse(line):
    r_line = []
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])

    return r_line


def my_find():
    for i in range(N):
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[i][j+k])

            if tmp == my_reverse(tmp):
                return tmp

        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])

            if tmp == my_reverse(tmp):
                return tmp
    return []


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]

    answer = my_find()

    print(answer)
