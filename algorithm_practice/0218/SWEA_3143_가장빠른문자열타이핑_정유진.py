T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()

    i = 0  # 문자열 A를 탐색할 인덱스
    answer = 0

    while True:

        if i == len(A):  # 문자열 A를 끝까지 탐색했다면 break
            break

        if A[i:i+len(B)] == B:  # 인덱스 i를 시작으로 B의 길이만큼 문자열을 잘랐을 때 B와 같다면
            answer += 1
            i += len(B)  # B의 길이만큼 i를 오른쪽으로 민다.
        else:
            answer += 1
            i += 1  # 같지 않다면 i를 오른쪽으로 1 만큼 민다.

    print('#{} {}'.format(test_case, answer))

