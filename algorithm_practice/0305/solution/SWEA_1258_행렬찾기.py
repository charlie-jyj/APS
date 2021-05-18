# 화학물질을 빈 용기로 변환
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r+r_cnt):
        for j in range(c, c+c_cnt):
            arr[i][j] = 0


# 구역의 사이즈를 구한다
def search_size(r,c):
    r_cnt = 0
    c_cnt = 0

    # 너비
    for i in range(r, N):
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break

    # 높이
    for i in range(c, N):
        if arr[r][i] != 0:
            c_cnt += 1
        else:
            break

    ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
    init(r, c, r_cnt, c_cnt)


# 카운팅 정렬
def counting_sort(idx):
    cnt = [0] * 1001
    sort_ans = [0] * len(ans)

    # 1 카운팅 하는 과정
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1

    # 누적
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    # 정렬
    for i in range(len(ans)-1, -1, -1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1

        return sort_ans


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    # 행 우선 방식 순회하여 시작점을 구한다
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                search_size(i, j)

    ans = counting_sort(0) # 행정렬
    ans = counting_sort(2) # 행렬의 크기로 정렬


#####################################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j  # 시작점

                while r<N and arr[r][j] != 0:
                    r += 1
                while c<N and arr[i][c] != 0:
                    c += 1

                # r, c는 0이 아닐때까지 증가했다. r-i = 너비, c-j = 높이
                ans.append([r-i, c-j])

                # 초기화
                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0

    # 정렬
    ans.sort(key=lambda x: (x[0]*x[1], x[0]))