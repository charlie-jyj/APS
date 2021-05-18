def z(n, row, col, num):
    global cnt

    if n == 1:
        # for i in range(4):
        #     next_r = row + dr[i]
        #     next_c = col + dc[i]

        # for 문을 풀어헤쳤다.
        if row == R and col == C:
            print(num)
            return

        if row == R and col+1 == C:
            print(num+1)
            return

        if row+1 == R and col == C:
            print(num+2)
            return

        if row+1 == R and col+1 == C:
            print(num+3)
            return

        return

    if row <= R < row +(2**(n-1))  and col <= C < col +(2**(n-1)):
        z(n-1, row, col, num)
    elif row <= R < row +(2**(n-1)) and col +(2**(n-1)) <= C < 2**N:
        z(n-1, row, col+(2**(n-1)), num + 4**(n-1))
    elif row +(2**(n-1)) <= R < 2**N and col <= C < col +(2**(n-1)):
        z(n-1, row+(2**(n-1)), col, num + 4**(n-1)*2)
    elif row +(2**(n-1)) <= R < 2**N and col +(2**(n-1)) <= C < 2**N:
        z(n-1, row+(2**(n-1)), col+(2**(n-1)), num + 4**(n-1)*3)


N, R, C = map(int, input().split())
# dr = [0, 0, 1, 1]
# dc = [0, 1, 0, 1]


z(N,0,0,0)


