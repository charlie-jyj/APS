def baby_gin(arr):  # 트리플렛과 런이 하나씩 있는지 확인하는 함수
    tri = False
    run = False

    for i in range(10-3+1):
        if arr[i]>0 and arr[i+1]>0 and arr[i+2]:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            tri = True
            break

    for i in range(10):
        if arr[i] >= 3:
            arr[i] -= 3
            run = True
            break

    if tri and run:
        return 1
    else:
        return 0


def double_tri(arr):  # 트리플렛이 두 세트 존재하는지 확인하는 함수
    chk1 = False
    chk2 = False

    for i in range(10-3+1):
        if arr[i]>0 and arr[i+1]>0 and arr[i+2]:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            chk1 = True
            break

    for i in range(10-3+1):
        if arr[i]>0 and arr[i+1]>0 and arr[i+2]:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            chk2 = True
            break

    if chk1 and chk2:
        return 1
    else:
        return 0


def double_run(arr):  # 런이 두 세트 있는지 확인하는 함수
    chk1 = False
    chk2 = False

    for i in range(10):
        if arr[i] >= 3:
            arr[i] -= 3
            chk1 = True
            break

    for i in range(10):
        if arr[i] >= 3:
            arr[i] -= 3
            chk2 = True
            break

    if chk1 and chk2:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, list(input())))
    counting = [0]*10
    answer = 0
    for card in cards:
        counting[card] += 1  # 카드의 숫자를 확인 후 개수 증가

    result1 = baby_gin(counting.copy())  # 런과 트리플렛이 하나씩 있는가?
    result2 = double_tri(counting.copy())  # 트리플렛이 두 번 있는가?
    result3 = double_run(counting.copy())  # 런이 두 번 있는가?

    if result1 == 1 or result2 == 1 or result3 == 1:  # 셋 중 하나라도 해당되면 베이비진
        answer = 1
    else:
        answer = 0

    print('#{} {}'.format(tc, answer))
