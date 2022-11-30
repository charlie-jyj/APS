# 구간합

condition = "5 3"
number_string = "5 4 3 2 1"
group1 = "1 3"
group2 = "2 4"
group3 = "5 5"

N, M = list(map(int, condition.split(" ")))
numbers = list(map(int, number_string.split(" ")))
val = 0

#sum_set = [0 for _ in range(N)]

sum_set = [0]

# 누적 합 배열 구하기
for idx, number in enumerate(numbers):
    val += number
    #sum_set[idx] = val
    sum_set.append(val)

# 구간 합 구하기
for group in [group1, group2, group3]:
    i, j = list(map(int, group.split(" ")))

    # n 번째 = 인덱스 n-1
    #i -= 1
    #j -= 1

    # i~j 의 구간합 = sum_set[j] - sum_set[i-1]
    #print(sum_set[j] - (0 if i == 0 else sum_set[i-1]))
    print(sum_set[j] - sum_set[i-1])