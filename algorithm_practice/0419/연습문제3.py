"""
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""


def pre_order(n):
    if n > 0:
        print(n, end=' ')
        pre_order(child1[n])
        pre_order(child2[n])


def in_order(n):
    if n > 0:
        in_order(child1[n])
        print(n, end=' ')
        in_order(child2[n])


def post_order(n):
    if n > 0:
        post_order(child1[n])
        post_order(child2[n])
        print(n, end=' ')


E = int(input())
N = E+1
edges = list(map(int, input().split()))
child1 = [0] * (N+1)
child2 = [0] * (N+1)
parent = [0] * (N+1)
for i in range(E):
    p, c = edges[2*i], edges[2*i+1]
    if child1[p] == 0:
        child1[p] = c
    else:
        child2[p] = c

    parent[c] = p

root = 0
for p in range(N+1):
    if parent[p] == 0:
        root = p

pre_order(root)
print()
in_order(root)
print()
post_order(root)
