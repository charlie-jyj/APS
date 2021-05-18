N = 5
R = 3

arr = [1, 2, 3, 4, 5]
sel = [0] * R


def combination(idx, sidx):  # idx = arr 에서의 인덱스, sidx = 조합에서의 인덱스

    if sidx == R:  # if 문 순서 바뀌지 않도록 주의
        print(sel)
        return

    if idx == N:
        return

    sel[sidx] = arr[idx]  # 지금 조합의 인덱스에 이번 arr index 를 사용하겠다
    combination(idx+1, sidx+1)  # 이번에 뽑고 다음 조합을 고르러 가자
    combination(idx+1, sidx)  # 이번에 안 뽑았고 다음 조합을 고르러 가자


def combination2(idx, sidx):
    if sidx == R:
        print(sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination2(i+1, sidx+1)


# combination(0, 0)
combination2(0, 0)