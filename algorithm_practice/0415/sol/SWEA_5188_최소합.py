"""
DP 이용
D[i][j] = min(D[i-1][j], D[i][j-1) + A[i][j] (i>0, j>0)
A[i][j] (i==0, j==0)
D[i-1][0] + A[i][0] (i>0, j==0)
D[0][j-1] + A[0][j] (i==0, j>0)

for i : 1 -> N-1
    for j 1 -> N-1
        D[i][j]
"""