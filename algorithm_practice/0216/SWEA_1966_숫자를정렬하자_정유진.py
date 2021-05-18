# 선택 정렬
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(0, len(numbers)-1):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print('#{} {}'.format(test_case, ' '.join(map(str,numbers))))
