# 재귀로 순열 구현하기

# depth는 트리의 깊이
# n은 배열의 길이 (고정값), k는 순열의 길이 (고정값)
def perm(card, n, depth, k):

    if depth == k:
        print(card)
        return

    for i in range(depth, n):
        card[depth], card[i] = card[i], card[depth]
        perm(card, n, depth+1, k)
        card[depth], card[i] = card[i], card[depth]


if __name__ == '__main__':

    card = [4, 5, 6, ]
    perm(card, len(card), 0, 3)