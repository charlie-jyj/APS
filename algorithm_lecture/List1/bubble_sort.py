def bubble_Sort(a):
    for i in range(len(a)-1, 0, -1):
        # for j in range(0, i):
        #     if a[j] > a[j+1]:
        #         a[j], a[j+1] = a[j+1], a[j]

        for j in range(1, i+1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


if __name__ == '__main__':

    a = [5, 4, 3, 2, 1]
    bubble_Sort(a)

    print(a)
