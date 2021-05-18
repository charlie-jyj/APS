lst = input().split()

# 왼쪽 덱은 i=0 에서 시작하고
# 오른쪽 덱은 j= center 에서 시작하며 증가
# 카드의 개수가 홀수 일 때, 왼쪽 덱에 더 많은 카드를 할당하기 위해서 center = N+1 // 2
j = (len(lst)+1)//2


# 왼쪽 덱의 카드 숫자가 1장 더 많을 경우 j 가 리스트를 벗어날 수 있으므로 if 조건문으로 제어
for i in range(j):
    print(lst[i], end=' ')
    if j < len(lst):
        print(lst[j], end=' ')
        j += 1
