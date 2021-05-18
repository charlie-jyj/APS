T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pascal = []

    for i in range(N):
        temp = []
        for j in range(0, i+1, 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(pascal[i-1][j-1]+pascal[i-1][j])
        pascal.append(temp)

    print('#{}'.format(test_case))
    for numbers in pascal:
        result = ''
        for number in numbers:
            result += str(number) + ' '
        print('{}'.format(result))


