"""
00000010001101
0000000111100000011000000111100110000110000111100111100111111001100111
"""


nums = list(map(int, list(input())))
length = len(nums)

for i in range((length+6)//7):  # length 가 7의 배수가 아닐 수 있어서
    sub_total = 0
    temp = []
    if i != (length+6)//7-1:  # 마지막 조각이 아니면
        temp = nums[7*i:7*(i+1)]  # 7개의 비트가 1개의 조각
    else:
        temp = nums[7*i:]  # 마지막 조각은 끝까지 slicing

    sub_length = len(temp)
    for j in range(sub_length):  # temp 를 뒤에서부터 읽으면서 2진수를 10진수로 변환
        sub_total += (2**j)*temp[sub_length-1-j]

    if i != (length+6)//7-1:
        print(sub_total, end=',')
    else:
        print(sub_total)

