n, c = list(map(int, input().split()))

array = []
for _ in range(n):
    array.append(int(input()))
array= sorted(array)

start = array[1] - array[0]  # 최소 gap
end = array[-1] - array[0]  # 최대 gap
result = 0

while start <= end:
    mid = (start+end)//2  # gap
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:  # c개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1

print(result)


