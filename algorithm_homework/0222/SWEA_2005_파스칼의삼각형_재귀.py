def triangle(n):

    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(0, len(result)-1, 1):
            new_row.append(last_row[i]+last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pascal = []

    pascal = triangle(N)

    print('#{}'.format(test_case))
    for numbers in pascal:
        answer = ''
        for number in numbers:
            answer += str(number) + ' '
        print('{}'.format(answer))


