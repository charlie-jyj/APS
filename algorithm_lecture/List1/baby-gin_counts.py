# 완전 탐색 아닌 방법으로 baby-gin
# counts

def baby_gin_greedy(card, max_number):

    counts = [0] * (max_number+1)
    is_run = False
    is_triplet = False
    answer = []

    for num in card:
        counts[num] += 1

    print(counts)

    for num in range(1, len(counts)):
        counts[num] += counts[num-1]

    print(counts)

    for idx in range(0, len(counts)-2):
        if counts[idx] > 0 and counts[idx+1] > 0 and counts[idx+2] > 0:
            is_run = True
            answer += [idx, idx+1, idx+2]
            counts[idx] -= 1
            counts[idx+1] -= 1
            counts[idx+2] -= 1
            break

    for idx in range(len(counts)):
        if counts[idx] >= 3:
            is_triplet = True
            answer += [idx] * 3
            counts[idx] -= 3
            break

    if is_run and is_triplet:
        return answer
    else:
        return 'fail'


if __name__ == '__main__':
    card = [2, 5, 5, 4, 3, 5]
    print(baby_gin_greedy(card, max(card)))