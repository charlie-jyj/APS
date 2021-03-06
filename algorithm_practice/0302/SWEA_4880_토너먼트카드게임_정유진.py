# 가위바위보
def battle(p1, p2):
    if p1[1] == p2[1]:  # 똑같은 패를 냈다면 학생 번호가 낮은 쪽이 승자
        return p1 if p1[0] < p2[0] else p2
    elif (p1[1] == 1 and p2[1] == 3) or (p1[1] == 2 and p2[1] == 1) or (p1[1] == 3 and p2[1] == 2):
        return p1
    else:
        return p2


def tournament(arr):

    if len(arr) == 1:  # 배열 길이가 1이면 배틀 할 사람이 없으니 돌려보낸다.

        return arr[0]

    elif len(arr) == 2: # 배열 길이가 2이면 가위바위보 시키고 승자를 돌려보낸다.
        p1 = arr[0]
        p2 = arr[1]

        return battle(p1, p2)

    else:

        # 절반으로 나누기 재귀 호출
        center = (len(arr)-1)//2
        left = tournament(arr[:center+1:])
        right = tournament(arr[center+1::])

        # 승자끼리 다시 배틀
        return tournament([left]+[right])


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    cards = list(map(int, input().split()))
    match = []  # ([학생번호, 카드 패])
    for i in range(N):
        match.append([i+1, cards[i]])

    result = tournament(match)

    print('#{} {}'.format(test_case, result[0]))

