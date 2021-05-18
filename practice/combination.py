def combination(idx): # 부분집합 만들기 재귀 코드를 약간 응용했다. (idx = 현재 주목하고 있는 원소)
    global sel_num

    if idx == len(source): # base case
        temp = []
        for i in range(len(select)):  # select 배열을 봤을 때 값이 1 이다 == 해당 원소를 사용한다는 뜻
            if select[i] == 1:
                temp.append(source[i])  # 사용하는 원소를 담는다
        if len(temp) == sel_num:  # 원소의 수가 원하는 조합의 수와 같다면,
            result.append(temp)
        return

    for i in range(2):
        select[idx] = i  # 현재 idx 번째 원소를 사용한다면 1, 해당 원소를 사용하지 않는다면 0을 기록 (이 2가지 경우로 각각 재귀 호출)
        combination(idx+1)  # 다음 원소로 넘어간다.


source = [i for i in range(10)] # 원본 [0, 1, 2, 3 ...9]
sel_num = 2  # 조합 원소의 수
select = [0]* 10 # 사용여부 체크
result = [] # 결과

combination(0)

# 작은 것부터 출력하기 위해 reverse 했는데 stack 이라고 생각하고 뒤에서부터 꺼내도 같은 결과
# result.reverse()
# for idx in range(len(result)):
#     if idx == len(result)-1:
#         print(result[idx], end='$')
#     else:
#         print(result[idx], end=',')

length = len(result)
for idx in range(length):
    if idx == length-1:
        print(result.pop(), end='$')
    else:
        print(result.pop(), end=',')