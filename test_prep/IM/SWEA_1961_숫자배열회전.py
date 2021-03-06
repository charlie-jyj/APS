T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    original = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = [[0]*N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):

            arr_90[j][N-1-i] = arr_180[N-1-i][N-1-j] = arr_270[N-1-j][i] = original[i][j]

    print('#{}'.format(test_case))
    for i in range(N):
        print(''.join(map(str, arr_90[i])), end=' ')
        print(''.join(map(str, arr_180[i])), end=' ')
        print(''.join(map(str, arr_270[i])), end=' ')
        print()
