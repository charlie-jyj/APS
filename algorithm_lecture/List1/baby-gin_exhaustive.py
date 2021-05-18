# baby-gin 완전탐색으로

def baby_gin_exh(card):

    is_run = False
    is_triplet = False

    for i1 in range(len(card)):
        for i2 in range(len(card)):
            if i1 != i2:
                for i3 in range(len(card)):
                    if i1 != i2 != i3:
                        for i4 in range(len(card)):
                            if i1 != i2 != i3 != i4:
                                for i5 in range(len(card)):
                                    if i1 != i2 != i3 != i4 != i5:
                                        for i6 in range(len(card)):
                                            if i1 != i2 != i3 != i4 != i5 != i6:

                                                if card[i1] == card[i2] == card[i3]:
                                                    is_triplet = True
                                                    if card[i5] == card[i4] + 1 and card[i6] == card[i4] + 2:
                                                        is_run = True

                                                        return '{},{},{},{},{},{}'.format(card[i1], card[i2], card[i3],
                                                                                          card[i4], card[i5], card[i6])

                                                elif card[i4] == card[i5] == card[i6]:
                                                    is_triplet = True
                                                    if card[i2] == card[i1] + 1 and card[i3] == card[i1] + 2:
                                                        is_run = True

                                                        return '{},{},{},{},{},{}'.format(card[i1], card[i2], card[i3],
                                                                                          card[i4], card[i5], card[i6])

    return 'fail'


if __name__ == '__main__':
    card = [2, 5, 5, 4, 3, 5]
    print(baby_gin_exh(card))