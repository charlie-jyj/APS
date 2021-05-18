def i_to_a(number):

    arr_number = []
    result = ''

    # 숫자를 뜯어서 리스트로 만들기
    while number:
        arr_number.append(number%10)
        number //= 10

    # 리스트 뒤집기
    for i in range(len(arr_number)//2):
        arr_number[i], arr_number[len(arr_number)-1-i] = arr_number[len(arr_number)-1-i], arr_number[i]

    # 리스트를 순회하며 int 를 string 으로 바꾸기
    for n in arr_number:
        result += chr(n + ord('0'))

    return result


if __name__ == '__main__':
    num = 123456
    answer = i_to_a(num)
    print(answer, type(answer))


