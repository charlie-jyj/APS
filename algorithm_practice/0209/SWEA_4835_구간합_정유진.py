T = int(input())
for test_case in range(1, T + 1):

    case_length_range_length = list(map(int, input().split()))
    # 테스트 케이스의 길이
    case_length = case_length_range_length[0]
    # 구간합의 길이
    range_length = case_length_range_length[1]

    numbers = list(map(int, input().split()))

    # 구간합의 모음을 저장할 list
    range_sums = []

    # idx 처음부터 ~ (마지막 인덱스-구간길이+1) 만큼 증가시킨다.
    # 구간 길이 만큼 반복문을 돌려 구간합을 구하고 list에 값을 저장한다.
    for idx in range(0, case_length-range_length+1):

        range_sum = 0
        # i는 0에서 구간길이-1 까지 1씩 증가한다. 반복문은 총 (구간 길이) 번 반복한다.
        for i in range(range_length):
            range_sum += numbers[idx+i]

        range_sums += [range_sum]

    # 구간합의 모음인 range_sums를 정렬한다
    # bubble sort 오름차순
    for i in range(len(range_sums)-1, 0, -1):
        for j in range(0, i):
            if range_sums[j] > range_sums[j+1]:
                range_sums[j], range_sums[j+1] = range_sums[j+1], range_sums[j]

    
    # range_sums에서 max - min을 한다.
    print('#{} {}'.format(test_case, range_sums[-1]-range_sums[0]))
    

