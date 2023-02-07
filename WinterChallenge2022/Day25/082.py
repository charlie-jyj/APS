"""
1. 사전에서 다루는 문자열은 a, z
2. a N개 z M개
3. 핵심 아이디어 (N+M)개에서 N개를 뽑는 경우의 수 = (N+M)개에서 M개를 뽑는 경우의 수
"""
import sys
sys.stdin = open('082_text.txt')
input = sys.stdin.readline
N, M, K = list(map(int, input()))
D = [[0 for j in range(201)] for i in range(201)]  # 조합 테이블 200*200

for i in range(0, 201):
    for j in range(0, i+1):  # j는 i보다 클 수 없다
        if j == 0 or j == i:
            D[i][j] = 1
        elif j == 1:
            D[i][j] = i
        else:
            D[i][j] = D[i-1][j] + D[i-1][j-1]
            if D[i][j] > 1000000000:
                D[i][j] = 1000000001

if D[N+M][M] < K:
    print(-1)
else:
    while not (N==0 and M==0):
        if D[N-1][M] >= K:
            print("a", end="")
            N -= 1
        else:
            print("z", end="")
            M -= 1



