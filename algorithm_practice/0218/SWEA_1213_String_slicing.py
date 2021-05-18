for test_case in range(1, 10 + 1):
    tc = int(input())
    pattern = input()  # 찾을 문자열
    text = input()  # 검색할 문자열

    match_count = 0  # pattern 을 찾은 횟수

    # 구간만큼 text 를 slicing 했을 때 pattern 과 같다면 count + 1 한다.
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            match_count += 1

    print('#{} {}'.format(tc, match_count))
