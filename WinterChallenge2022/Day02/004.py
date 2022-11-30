condition = "4 3"
num1 = "1 2 3 4"
num2 = "2 3 4 5"
num3 = "3 4 5 6"
num4 = "4 5 6 7"
query1 = "2 2 3 4"
query2 = "3 4 3 4"
query3 = "1 1 4 4"

# 0을 붙여서 out of range 를 방지
N, QN = list(map(int, condition.split(" ")))
num_matrix = [[0]*(N+1)]
for num_string in [num1, num2, num3, num4]:
    arr = list(map(int, num_string.split(" ")))
    num_matrix.append([0]+arr)
sum_matrix = [[0]*(N+1) for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, N+1):
        sum_matrix[row][col] = sum_matrix[row-1][col] + sum_matrix[row][col-1] - sum_matrix[row-1][col-1] + num_matrix[row][col]

print(sum_matrix)



