def in_order(n):  # 중위 순회
    global answer

    if n > 0:
        in_order(info[n][0])
        answer += info[n][3]  # 알파벳 누적
        in_order(info[n][1])


T = 10
for tc in range(1, T+1):
    N = int(input())
    info = [[0, 0, 0, ''] for _ in range(N+1)]  # 0: 왼쪽 자식, 1: 오른쪽 자식, 2: 부모, 3: 알파벳
    answer = ''

    for _ in range(N):
        temp =input().split()
        length = len(temp)

        if length == 2:  # 길이가 2 => 부모 값, 알파벳 값
            p, ch = temp
            info[int(p)][3] = ch
        elif length == 3:  # 길이가 3 => 부모 값, 알파벳 값, 왼쪽 자식 값
            p, ch, l = temp
            info[int(p)][3] = ch
            info[int(p)][0] = int(l)
            info[int(l)][2] = int(p)
        elif length == 4:
            p, ch, l, r = temp  # 길이가 4 => 부모 값, 알파벳 값, 왼쪽 자식 값, 오른쪽 자식 값 (완전 이진트리니까 왼오 순서 고정)
            info[int(p)][3] = ch
            info[int(p)][0] = int(l)
            info[int(p)][1] = int(r)
            info[int(l)][2] = int(p)
            info[int(r)][2] = int(p)

    # root 찾기
    root = 0
    for i in range(1, N+1):
        if info[i][2] == 0:
            root = i
            break

    in_order(root)

    print('#{} {}'.format(tc, answer))