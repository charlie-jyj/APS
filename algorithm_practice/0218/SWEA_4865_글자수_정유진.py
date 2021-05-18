T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    counting = [0] * len(str1)  # str1의 각 char 의 출현 횟수를 기록할 리스트
    max_idx = 0  # counting 리스트의 최댓값 인덱스

    # str1을 순회하며 str1의 char 가 str2에 존재한다면 counting 리스트의 값 +1
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                counting[i] += 1

    # counting 정렬을 순회하며 최댓값 인덱스를 갱신한다.
    for i in range(len(counting)):
        if counting[max_idx] < counting[i]:
            max_idx = i

    print('#{} {}'.format(test_case, counting[max_idx]))