T = int(input())
for test_case in range(1, T + 1):
    TC, L = map(str, input().split())  # 테스트케이스 번호, 테스트 케이스 길이
    length = int(L)
    text = input().split()  # 테스트 케이스
    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = []

    # order 를 순회하며 text 의 값과 order 값이 일치하면 리스트에 추가한다.
    # 순서대로 추가된다 ZRO ONE TWO...
    for i in range(len(order)):
        for j in range(length):
            if order[i] == text[j]:
                result.append(order[i])

    print(TC)
    print(*result)