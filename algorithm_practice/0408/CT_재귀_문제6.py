def preorder(n):
    global root, N

    if n <= N:
        if n == root:
            print(f'[{value[n]}]--', end='')
        elif parent[n] == root:
            if children[root].index(n) == 0:
                print(f'+--[{value[n]}]', end='' if children[n] else '\n')
            elif children[root].index(n) == len(children[root])-1:
                print(f'       L--[{value[n]}]', end='' if children[n] else '\n')
            else:
                print(f'       +--[{value[n]}]', end='' if children[n] else '\n')
        elif not children[n]:
            print(f'-----[{value[n]}]')

        for child in children[n]:
            preorder(child)


N = 6
children = [[],[2,3,4],[5],[],[6],[],[]]
parent = [0, 0, 1, 1, 1, 2, 4]
value = ['000', '030', '054', '002', '045', '001', '123']
root = 1
preorder(root)