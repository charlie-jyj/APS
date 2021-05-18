T = int(input())
for test_case in range(1, T + 1):
    origin = input()
    N = len(origin)

    answer = 0
    flag = '1'  # 이전과 다른 숫자가 나오는 순간을 포착하기 위한 분기

    # 원본 bit 를 순회한다.
    for i in range(N):

        # flag 는 1, 0 순서로 바뀐다.
        # 초기화 값은 0으로 이루어져 있기 때문에 처음으로 1이 등장하는 시점이 최초로 고쳐야 하는 시점, 이후 flag 를 0으로 수정한다.
        # 이전과 다른 숫자가 등장하는 시점(flag 와 일치하는 값이 등장)이 고쳐야 하는 시점이므로 answer 에 +1 한다.
        if origin[i] == flag:
            answer += 1
            flag = '0' if flag == '1' else '1'

    print('#{} {}'.format(test_case, answer))