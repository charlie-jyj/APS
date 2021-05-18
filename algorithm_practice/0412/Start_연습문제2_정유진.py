"""
0F97A3
01D06079861D79F99F
"""

nums = list(input())

# dictionary 가 아니라 list와 index를 사용해도 좋겠다.
hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
binary_nums = []

for num in nums:
    dec_num = hex_dict[num]  # 16진수 = > 10진수
    bi_num = [0, 0, 0, 0]  # 16진수 1 자리 => 2진수 4자리이므로

    for i in range(3, -1, -1):  # 10진수를 2진수 변환
        bi_num[i] = dec_num % 2
        dec_num = dec_num//2

    binary_nums += bi_num  # 2진수를 누적시켜 하나의 배열로 완성

length = len(binary_nums)
for i in range((length+6)//7):  # length 가 7의 배수가 아닐 수 있어서
    sub_total = 0
    temp = []
    if i != (length+6)//7-1:  # 마지막 조각이 아니면
        temp = binary_nums[7*i:7*(i+1)]  # 7개의 비트가 1개의 조각
    else:
        temp = binary_nums[7*i:]  # 마지막 조각은 끝까지 slicing

    sub_length = len(temp)
    for j in range(sub_length):  # temp 를 뒤에서부터 읽으면서 2진수를 10진수로 변환
        sub_total += (2**j)*temp[sub_length-1-j]

    if i != (length+6)//7-1:
        print(sub_total, end=',')
    else:
        print(sub_total)


