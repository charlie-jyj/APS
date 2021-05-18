def run(count):
    for i in range(8):
        if count[i] >= 1 and count[i+1] >= a and count[i+2] >=1:
            return 1


def game():
    count1 = [0 for i in range(10)]
    count2 = [0 for i in range(10)]

    for i in range(12):
        n = card[i]
        if i%2 == 0:
            count1[n] += 1
            if count1 [n] == 3:
                return 1
            if run(count1):
                return 1
        else:
            count2[n] += 1
            if count2[n] == 3:
                return 2
            if run(count2):
                return 2

    return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    game()
    