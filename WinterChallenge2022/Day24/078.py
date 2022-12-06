import sys
sys.stdin = open('078_text.txt')
input = sys.stdin.readline

T = int(input())
matrix = [[i for i in range(15)]]  # 0층 [0, 1, 2, 3, ..., 13, 14]
max_floor = 0
for _ in range(T):
    floor = int(input())
    room = int(input())
    if max_floor < floor:
        for i in range(max_floor+1, floor+1):
            temp_floor = [0 for _ in range(15)]
            for j in range(1, 15):
                temp_floor[j] = temp_floor[j-1] + matrix[i-1][j]  # 새로운 층 주민 입주
            matrix.append(temp_floor)
            max_floor += 1

    print(matrix[floor][room])


