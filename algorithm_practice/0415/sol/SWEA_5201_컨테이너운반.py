def f(N,M):
    moved = [0]*N  # 옮겨진 화물
    s = 0  # 옮겨진 화물 무게

    for i in range(M):  # 트럭 순서대로
        for j in range(N):
            if moved[j] == 0 and t[i]>=w[j]: # 남은 화물 중 큰 것 부터
                s += w[j]
                moved[j] = 1
                break  # 다음 트럭으로

    return s


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))  # 컨테이너
    t = list(map(int, input().split()))  # 트럭
    w.sort(reverse=True)
    t.sort(reverse=True)

    i = 0 # 트럭 인덱스
    j = 0 # 화물 인덱스
    s = 0

    while i < M and j < N:  # 트럭과 화물이 남아있으면면
        if t[i] >= w[j]:
            s += w[j]
            i += 1
            j += 1
        else:
            j += 1