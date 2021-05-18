def i_to_a(number):
    value = ''

    arr = []
    while number>0:
        remain = number%10
        arr.append(remain)
        number //= 10

    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]

    for n in arr:
        value += chr(n+ord('0'))
    return value


num = 1234
result = i_to_a(num)
print(result, type(result))