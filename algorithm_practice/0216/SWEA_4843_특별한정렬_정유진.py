T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # flag 가 1일때는 최댓값, -1일때는 최솟값을 찾는다.
    flag = 1
    for i in range(0, len(numbers)-1):  # 정렬을 10개만 해도 된다.
        # 교환할 인덱스
        index = i
        for j in range(i+1, len(numbers)):
            if flag == 1:
                if numbers[index] < numbers[j]:
                    index = j
            elif flag == -1:
                if numbers[index] > numbers[j]:
                    index = j
        numbers[i], numbers[index] = numbers[index], numbers[i]
        # 다음 턴을 위해 flag 의 값을 바꾼다.
        flag *= -1

    # 출력 (리스트는 10개 까지 출력한다)
    print('#{}'.format(test_case), end=' ')
    for i in range(len(numbers)):
        if i == 10:
            break
        print('{}'.format(numbers[i]), end=' ')
    print()