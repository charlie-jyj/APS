# 순열 만들기

card = [4, 5, 6,]
N = 3

# baby_jin
run = False
tri = False

for i in range(N):
    for j in range(N):

        # 중복 순열 아니기 때문에
        if j == i: continue

        for k in range(N):

            if k != i and k != j:
                print(card[i], card[j], card[k])

                # run check
                if card[i]+1 == card[j] and card[i]+2 == card[j]:
                    run = True

                # triplet check
                # card[i] == card[j] == card[k] 라고 써도 된다.
                if card[i] == card[j] and card[j] == card[k]:
                    tri = True

                if run and tri:
                    print('baby-gin')