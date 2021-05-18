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

    # dictionary
    my_dict = {}
    for key in set(str1):
        my_dict[key] = 0

    for key in str2:
        if key in my_dict:
            my_dict[key] += 1

    ans = 0
    for i in my_dict.values():
        if ans < i:
            ans = i

    print(ans)

    # ASCII

    check_arr = [0]*26  # str1 해당 글자가 있는지 체크
    count_arr = [0]*26  # 해당 글자 카운트

    # str1을 순회하면서 알파벳 체크
    for i in str1:
        check_arr[ord(i)-ord('A')] = 1

    # 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord(i)-ord('A')]:
            count_arr[ord(i)-ord('A')] += 1

    print(max(count_arr))

