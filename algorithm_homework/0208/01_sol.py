# 내장함수를 내가 직접 구현한다.
def my_max(a, b):
    if a > b:
        return a
    else:
        return b


for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    answer = 0

    for idx in range(2, n-2):
        # my_max 전달인자로 2개를 가지니 왼쪽 2집, 오른쪽 2집 각각 뽑힌 집의 max를 다시 구한다
        max_h = my_max(my_max(building[idx-1], building[idx-2]), my_max(building[idx+1], building[idx+2]))

        if building[idx] > max_h:
            answer += building[idx] - max_h

    print('#{} {}'.format(tc, answer))

