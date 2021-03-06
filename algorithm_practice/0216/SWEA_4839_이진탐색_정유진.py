# 이진 탐색 함수 (찾을 페이지, 시작페이지, 끝페이지, 탐색 횟수)
def binary_search(page, start, end, n):

    left = start
    right = end
    center = int((left+right)/2)

    # 페이지를 찾으면 탐색 횟수를 반환한다.
    if center == page:
        return n
    # 페이지를 찾을 때까지 재귀로 호출한다.
    elif center < page:
        return binary_search(page, center, right, n+1)
    else:
        return binary_search(page, left, center, n+1)


T = int(input())
for test_case in range(1, T + 1):

    P, Pa, Pb = map(int, input().split())  # 전체 쪽 수, A가 찾을 쪽 번호, B가 찾을 쪽 번호
    winner = ''  # 이긴 사람

    a = binary_search(Pa, 1, P, 1)  # A의 수행 횟수
    b = binary_search(Pb, 1, P, 1)  # B의 수행 횟수

    # 각각의 수행 횟수 비교하여 승자를 정한다.
    if a == b:
        winner = '0'
    elif a < b:
        winner = 'A'
    else:
        winner = 'B'

    print('#{} {}'.format(test_case, winner))

