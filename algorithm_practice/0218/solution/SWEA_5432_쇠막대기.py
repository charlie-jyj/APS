import sys
sys.stdin = open('input_5432.txt', 'r')

T = int(input())
# cnt 변수 사용
for tc in range(1, T+1):
    iron_bar = input()

    cnt = 0
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            cnt += 1
        else:
            cnt -= 1

            if iron_bar[i-1] == '(':
                ans += cnt
            else:
                ans += 1

    print(ans)

# 리스트 사용

    s = []
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            s.append('(')
        else:
            s.pop()

            if iron_bar[i-1] == '(':
                ans += len(s)

            else:
                ans += 1

    print(ans)