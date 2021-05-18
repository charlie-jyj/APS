arr = [1, 2, 3]
N = 3  # 몇개 길이의 순열을 만들지
sel = [0]*N  # 결과들이 저장될 리스트
check = [0]*N  # 해당 원소를 이미 사용했는지 안 했는지에 대한 체크


# idx 는 깊이를 의미하고 순열의 길이가 최대 깊이를 결정한다.
def perm(idx):

    # 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:  # 해당 원소를 아직 쓰지 않았다
                sel[idx] = arr[i]  # 값을 써라
                check[i] = 1  # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0  # 다음 반복문을 위한 원상복구


perm(0)