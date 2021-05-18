T = int(input())
for tc in range(1, T+1):
    N = int(input())
    t = [list(map(int, input().split())) for i in range(N)]
    t.sort(key=lambda x:x[1])
    cnt = 1
    end = t[0][1]

    for i in range(N):
        if end <= t[i][0]:
            cnt += 1
            end = t[i][1]

    print(f'#{tc} {cnt}')