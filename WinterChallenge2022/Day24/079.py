# 조합 문제로 도출할 수 있는지가 핵심
# BOJ 1010

import sys
sys.stdin = open('079_text.txt')
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    # 0 < N <= M < 30
    N, M = list(map(int, input().split(" ")))
    bridge = [[0]*30 for _ in range(30)]

    # 초기화
    for i in range(0, 30):
        bridge[i][0] = 1
        bridge[i][1] = i
        bridge[i][i] = 1

    # 조합 구하기
    for i in range(1, 30):
        for j in range(2, i):
            bridge[i][j] = bridge[i-1][j-1] + bridge[i-1][j]

    print(bridge[M][N])