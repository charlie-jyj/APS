arr = [1, 2, 3]
N = 3


def perm(idx):
    if idx == N:
        print(arr)

    else:
        for i in range(idx, N):  # 현재 위치(나)부터 N-1 까지 순회

            arr[idx], arr[i] = arr[i], arr[idx]  # 순서 바꾸기 0,0 바꿔보고 0,1 바꿔보고 0,2 바꿔보고...반복
            perm(idx+1)
            arr[idx], arr[i] = arr[i], arr[idx]  # 다음 반복문을 위해해 원상 복귀


perm(0)