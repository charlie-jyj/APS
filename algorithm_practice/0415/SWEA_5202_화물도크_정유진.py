T=int(input())
for tc in range(1, T+1):
    N = int(input())  # 신청서의 수
    forms = []

    # 회의 신청서를 작성한다
    for i in range(N):
        s, e = map(int, input().split())
        forms.append((s,e))

    # 종료시간을 기준으로 오름차순 정렬하여 종료시간이 가장 빠른 회의를 [0] 에 둔다
    forms.sort(key=lambda x:x[1])

    avail = 1  # 적어도 1개의 회의는 유효 (forms[0])
    end = forms[0][1]  # 첫 번째 회의의 끝나는 시간 => 갱신해나갈 것
    idx = 0  # forms 을 순회할 인덱스

    while True:
        idx += 1  # 다음 회의를 살펴본다

        if idx >= N:  # 모든 회의를 다 살펴보았으니 반복문을 빠져나간다
            break

        if end <= forms[idx][0]:  # 회의의 시작시간이 직전 회의의 종료시간 이후인가?
            avail += 1  # 그렇다면 개최할 수 있는 회의
            end = forms[idx][1]  # 회의 종료 시간을 갱신한다

    print('#{} {}'.format(tc, avail))

