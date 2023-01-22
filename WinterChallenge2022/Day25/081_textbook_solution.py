import sys
sys.stdin = open('081_text.txt')
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())  # 순열의 길이
    F = [0]*21  # 자리 별로 만들 수 있는 경우의 수 (팩토리얼)
    S = [0]*21  # 1번 소문제 정답 순열을 담는 리스트
    visited = [False]*21  # 숫자 사용 여부 저장
    F[0] = 1

    for i in range(1, N+1):
        F[i] = F[i-1] * i  # 자릿수에서 만들 수 있는 경우의 수 구하기

    # F[1] = 1, F[2] = 2, F[3] = 6, F[4] = 24

    inputList = list(map(int, input().split()))
    if inputList[0] == 1:
        K = inputList[1]
        # 1~N 자릿수 변수 i
        for i in range(1, N+1):
            cnt = 1  # 몇 번째 숫자를 사용할 지 결정 변수
            for j in range(1, N+1):  # visited를 순회
                if visited[j]:
                    continue
                if K <= cnt * F[N-i]:
                    K -= (cnt-1) * F[N-i]
                    S[i] = j
                    visited[j] = True
                    break
                cnt += 1
        for i in range(1, N+1):
            print(S[i], end='')
    else:
        K = 1
        for i in range(1, N+1):
            cnt = 0  # 미사용 숫자
            for j in range(1, inputList[i]):  #1, 13, 132, 1324
                if not visited[j]:
                    cnt += 1
            K += cnt * F[N-i]  # 사용된 수의 개수 * (현재 자릿수 - 1)의 경우의 수
            visited[inputList[i]] = True
        print(K)

