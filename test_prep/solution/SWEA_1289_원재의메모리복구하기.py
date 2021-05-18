lst = input()

# 원본이 1에서 시작할 경우 0000... -> 1111... 로 바꾸고 시작하기 때문에 시작 cnt = 1 이다
cnt = 0
if lst[0] == '1':
    cnt = 1

# 숫자의 종류가 달라지는 순간 포착
for i in range(len(lst)-1):
    if lst[i] != lst[i+1]:
        cnt += 1