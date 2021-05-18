"""
2진수 목록을 만들고 (목록을 만들기가 상대적으로 간단하기 때문에)
3진수와 비교

자릿수 < 40
목록을 문자열로 만드는 것이 좋겠다?

어떻게 저장할까? => 나는 숫자로 저장
[1,0,1,0] ['1','0','1','0'] ['1010']

for i: o->len(A)
temp = [0]*4  사본을 만들어서 저장할까 => 나는 사본으로
A[i] = A[i]^1 원본을 수정할까
"""

# 2진수에서 10진수로 바꾸기
def from_2_to_10(arr):
    outcome = 0
    for i in range(len(arr)):
        if arr[len(arr)-1-i] == 1:
            outcome += 2**i
    return outcome


# 2진수에서 3진수로 바꾸기
def from_2_to_3(arr):
    outcome = []
    dec_num = from_2_to_10(arr)

    while dec_num > 0:
        outcome = [dec_num % 3] + outcome
        dec_num //= 3

    return outcome


T = int(input())
for tc in range(1, T+1):
    bin_num = list(map(int, list(input())))
    ter_num = list(map(int, list(input())))

    candidate = []
    answer = 0

    # 후보군을 뽑는다
    for i in range(len(bin_num)):
        temp = bin_num[:]
        temp[i] = bin_num[i]^1
        candidate.append(temp)

    # 후보를 하나하나 보기
    for i in range(len(candidate)):
        num = candidate[i]
        result = from_2_to_3(num)
        diff = 0

        # 후보를 3진수로 변환하고 비교했을 때, 차이가 1인 수를 찾는다
        if len(result) == len(ter_num):
            for j in range(len(result)):
                if result[j] != ter_num[j]:
                    diff += 1

            if diff == 1:
                answer = from_2_to_10(num)
                break

    print('#{} {}'.format(tc, answer))
