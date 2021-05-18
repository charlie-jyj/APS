# 파일을 열어 input을 받을 수 있다. stdin = standard input, 'r'=read
import sys
sys.stdin = open('input.txt', 'r')


# print('test case의 개수?')
# n = int(input())
#
# for i in range(n):
#     print('리스트의 길이', end=':')
#     length = int(input())
#     print(length)
#     arr = [0] * length
#
#     print('리스트', end=':')
#     for idx, val in enumerate(map(int, input().split())):
#         arr[idx] = val
#
#     print(arr)


for tc in range(1, int(input())+1):
    N = int(input())
    box = list(map(int, input().split()))

    ans = 1
    print("#{} 길이의 배열: {}".format(N, box))