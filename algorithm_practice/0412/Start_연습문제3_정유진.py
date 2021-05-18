"""
0DEC
0269FAC9A0
"""

nums = list(input())
hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
binary_nums = []
pattern = {'001101': 0, '010011': 1, '111011': 2, '110001':3, '100011': 4, '110111': 5,
           '001011': 6, '111101': 7, '011001': 8, '101111': 9}  # 암호 비트 패턴

for num in nums:
    dec_num = hex_dict[num]  # 16진수 = > 10진수
    bi_num = [0, 0, 0, 0]  # 16진수 1 자리 => 2진수 4자리이므로

    for i in range(3, -1, -1):  # 10진수를 2진수 변환
        bi_num[i] = dec_num % 2
        dec_num = dec_num//2

    binary_nums += bi_num  # 2진수를 누적시켜 하나의 배열로 완성

print(binary_nums)
n = len(binary_nums)  # 2진수 배열 전체 길이
m = 6  # 패턴의 길이

# for i in range(n-m+1):  # 브루트포스로 하나하나 탐색
#     pwd = pattern.get(''.join(map(str,binary_nums[i:i+m])), -1)
#     if pwd >= 0:  # 패턴을 찾았다면 출력
#         print(pwd, end=' ')
#         for j in range(i, i+m):  # 패턴에 이미 사용된 숫자는 폐기 처분
#             binary_nums[j] = -1

idx = 0
while idx < n-m+1:
    pwd = pattern.get(''.join(map(str,binary_nums[idx:idx+m])), -1)
    if pwd >= 0:  # 패턴을 찾았다면 출력
        print(pwd, end=' ')
        idx += m  # 패턴 길이 만큼 건너뛴다

    else: # 패턴을 못 찾았으니 다음 인덱스 탐색
        idx += 1