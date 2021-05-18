def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


T = int(input())

for test_case in range(1, T + 1):
    case_length = int(input())
    numbers = list(map(int, input().split()))

    # 1
    # bubble_sort(numbers)

    # 2
    max_value = 0
    min_value = 1001

    for i in range(case_length):
        if max_value < numbers[i]:
            max_value = numbers[i]

        if min_value > numbers[i]:
            min_value = numbers[i]

    # print('#{} {}'.format(test_case, numbers[-1]-numbers[0]))
    print('#{} {}'.format(test_case, max_value - min_value))