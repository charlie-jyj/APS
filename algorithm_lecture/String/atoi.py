def atoi(string):

    value = 0
    for i in range(len(string)):
        value = value*10 + ord(string[i])-ord('0')

    return value


num_str = '1234'
result = atoi(num_str)
print(result, type(result))