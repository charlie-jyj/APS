arr = [1, 2, 3]
N = 3
sel = [0]*N  # 뽑은 결과를 적음


# 여기서 사용하는 check 는 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):

        # j 번째 원소를 활용을 했다면 그걸 쓰면 안 되지
        if check & (1 << j):
            continue

        sel[idx] = arr[j]
        perm(idx+1, check | (1 << j))  # 1회성 사용이라 원상복귀가 필요없다.


perm(0, 0)