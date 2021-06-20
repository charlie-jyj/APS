"""
idea
시간초과 나서 백트래킹 해보려고 했는데 어떻게 해야할지 모르겠음
"""

def sos(check, w, d, curr_height):
    global N, max_height

    if sum(check) == N:
        max_height = max(max_height, curr_height)
        return

    for p in range(N):
        if check[p] == 0:
            check[p] = 1
            a, b, c = boxes[p]
            impossible = True

            if (w >= b and d >= c) or (w >= c and d >= b):
                impossible = False
                sos(check, b, c, curr_height+a)

            if (w >= a and d >= c) or (w >= c and d >= a):
                impossible = False
                sos(check, a, c, curr_height+b)

            if (w >= a and d >= b) or (w >= b and d >= a):
                impossible = False
                sos(check, a, b, curr_height+c)

            if impossible:
                sos(check, w, d, curr_height)

            check[p] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    boxes = list()

    for _ in range(N):
        box = list(map(int, input().split()))
        boxes.append(box)

    max_height = 0
    sel = [0] * N
    for i in range(N):

        sel[i] = 1
        x, y, z = boxes[i]
        sos(sel, y, z, x)
        sos(sel, x, z, y)
        sos(sel, x, y, z)
        sel[i] = 0

    print('#{} {}'.format(tc, max_height))