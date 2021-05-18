import sys
sys.stdin = open('input_4864.txt', 'r')


def brute_force_1(t, p):
    for i in range(len(t) - len(p) + 1):
        for j in range(len(p)):
            if t[i + j] != p[j]:
                break
        else:  # for-else 구문을 사용하지 않을 경우, flag 를 사용하는 방법도 있다.
            return 1

        return 0


def brute_force_2(t, p):
    i = 0  # t를 컨트롤 하는 인덱스
    j = 0  #
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

    if j == len(p):
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(brute_force_1(str1, str2))
    print(brute_force_2(str1, str2))




