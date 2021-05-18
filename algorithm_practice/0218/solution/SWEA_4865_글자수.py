import sys
sys.stdin = open('input_2865.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = [0] * len(str1)

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str[i] == str2[j]:
                cnt[i] += 1

    ans = 0
    for i in range(len(cnt)):
        if ans < cnt[i]:
            ans = cnt[i]

    print(ans)