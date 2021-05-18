N = 10  # 원소의 수
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 원본 배열
check = [0]*N  # 원소가 사용되었는지 안 되었는지 체크할 배열
answer = []  # 조건에 맞는 부분 집합을 담을 배열


def power_set(idx):

    # base case, 부분집합이 하나 완성된 시점이므로 출력
    if idx == N:
        temp = []
        temp_sum = 0
        for i in range(len(check)):
            if check[i]:  # 원소가 사용되었다면 temp 배열에 저장, temp_sum 에 가산
                temp_sum += arr[i]
                temp.append(arr[i])

        if temp_sum == 10:  # 부분집합의 합이 10이라면 answer 배열에 저장
            answer.append(temp)

    # 부분 집합이 아직 완성되지 않았다
    else:
        check[idx] = 0  # 현재의 원소를 사용하지 않는다
        power_set(idx+1)  # 다음 원소의 인덱스를 매개변수로 함수 실행

        check[idx] = 1  # 현재의 원소를 사용한다.
        power_set(idx+1)


# 인덱스 0에서 시작하여 부분집합 만들러 go
power_set(0)
print(answer)