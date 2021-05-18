arr = [4, 9, 11, 23, 19, 7]

key = 11

for i in range(len(arr)):
    if arr[i] == key:
        print(i, '에 위치한다')
        break
else:
    print('실패')


arr = [4, 7, 9, 11, 19, 23]

key = 10

for i in range(len(arr)):
    if arr[i] == key:
        print(i, '에 위치한다.')
        break
    elif arr[i] > key:
        print(i, '까지 탐색 후 실패')
        break