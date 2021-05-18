arr = [10, 15, 2, 19, 6, 14]

for i in range(0, len(arr)-1):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

    print('기준자리', i, arr)

print(arr)