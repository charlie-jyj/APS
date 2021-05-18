N = 3

arr = [1, 2, 3]  # 우리가 활용할 데이터

sel = [0] * N  # a 리스트 (내가 해당 원소를 뽑았는지?) [0,0,0]


def power_set(idx):
    if idx == N:
        print(sel, ":", end=' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end='')
        print()

    else:
        # idx 자리의 원소를 뽑고 (True) 간다.
        sel[idx] = 1
        power_set(idx+1)

        # idx 자리의 원소를 안 뽑고(False) 간다.
        sel[idx] = 0
        power_set(idx+1)


power_set(0)

