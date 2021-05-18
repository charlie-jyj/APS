# 문자열 뒤집기

# 1번 새로운 빈 문자열 만들어 소스의 뒤에서부터 읽기
def my_reverse1(string):

    result = ''
    for i in range(len(string)-1, -1, -1):
        result += string[i]

    return result


# 2번 자기 문자열에서 뒤집기
def my_reverse2(string):

    arr = list(string)
    result = ''

    for i in range(len(string)//2):
        arr[i], arr[len(string)-1-i] = arr[len(string)-1-i], arr[i]

    # join
    for char in arr:
        result += char

    return result


if __name__ == '__main__':
    text = 'apple'
    print(my_reverse1(text))
    print(my_reverse2(text))