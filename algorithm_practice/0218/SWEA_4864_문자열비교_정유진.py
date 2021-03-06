# 고지식한 패턴 검색
def brute_force(p, t):

    pt = 0
    pp = 0
    while pt != len(t) and pp != len(p):

        if t[pt] == p[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return 1 if pp == len(p) else 0


T = int(input())
for test_case in range(1, T + 1):
    pattern = input()
    text = input()

    answer = brute_force(pattern, text)

    print('#{} {}'.format(test_case, answer))