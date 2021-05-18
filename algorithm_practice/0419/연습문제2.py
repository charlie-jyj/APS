nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)
power_set = []
power_set2 = []
sel = [0]*n


# 비트 연산자로 구하기
for i in range(1<<n):
    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(nums[j])
    if sum(temp) == 10:
        power_set.append(temp)

print(power_set)


def make_power_set(idx, sub_sum):
    global n

    if idx == n:
        if sub_sum == 10:
            temp = []
            for i in range(n):
                if sel[i] == 1:
                    temp.append(nums[i])
            power_set2.append(temp)
        return

    if sub_sum > 10:
        return

    sel[idx] = 0
    make_power_set(idx+1, sub_sum)
    sel[idx] = 1
    make_power_set(idx+1, sub_sum+nums[idx])


make_power_set(0, 0)
print(power_set2)
