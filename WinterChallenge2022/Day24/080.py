import sys
sys.stdin = open('080_text.txt')
input = sys.stdin.readline

color_type = int(input())
rocks = list(map(int, input().split(" ")))
K = int(input())
N = sum(rocks)
combination = [[0]*(N+1) for _ in range(N+1)]
print("the number of rocks", N)
for i in range(N+1):
    combination[i][0] = 1
    combination[i][i] = 1
    combination[i][1] = i

for i in range(1, N+1):
    for j in range(2, i):
        combination[i][j] = combination[i-1][j-1] + combination[i-1][j]
print(combination)

divisor = combination[N][K]
total = 0
for rock in rocks:
    if K <= rock:
        print(combination[rock][K])
        total += combination[rock][K]
print(divisor, total)
print(total/divisor)