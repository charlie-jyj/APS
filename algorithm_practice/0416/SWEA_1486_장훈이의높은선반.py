"""
부분집합의 합 응용
(중간에 걸러내지 않으면 2**N 개라서 많다 많아)

고려할 구간의 합 : S
남은 구간의 합 : rs
지금까지의 합 + 남은 구간의 합 < B OR 지금까지의 합 > 최솟값 이면, 고려할 필요가 없다(백트래킹)
f(0, 0, sum(A))
f(i, 고려할 구간의 합, 남은 구간의 합)

if i == n:
    최솟값 갱신
    return

elif B >= s and min <= s:  이미 최솟값은 아니니 끝까지 볼 필요가 없다
    return

elif s + rs < B:  # 남은 구간을 다 더해도 가망이 없다
    return

else:
    f(i+1, s+A[i], rs-A[i])  i 원소가 포함된다
    f(i+1, s, rs-A[i])  i 원소가 포함되지 않는다

"""


def power_set(idx, sub_sum, rest):  # 현재 내가 주목하고 있는 점원, 현재까지 점원 탑 높이, 남은 점원들 키의 합
    global min_sum, N, B

    if idx == N:  # 부분 집합 완성
        if sub_sum >= B:  # 탑의 높이가 선반 보다 같거나 높을 때 최솟값 갱신 
            min_sum = min(min_sum, sub_sum)
        return

    if sub_sum > min_sum:  # 아직 탑이 완성되지 않았지만 탑 높이 최솟값보다 크기 때문에 유망하지 않다
        return

    if sub_sum + rest < B:  # 아직 탑이 완성되지 않았지만 남은 직원의 키를 합쳐도 선반보다 작아 유망하지 않다.
        return

    power_set(idx+1, sub_sum+staffs[idx], rest-staffs[idx])  # 현재 주목하고 있는 점원을 탑에 포함시키고 다음으로
    power_set(idx+1, sub_sum, rest-staffs[idx])  # 현재 주목하고 있는 점원을 탑에 포함시키지 않고 다음으로


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())  # 점원의 수, 서랍의 높이
    staffs = list(map(int, input().split()))  # 점원의 키
    min_sum = 987654321  # 점원 탑의 높이 최솟값
    power_set(0, 0, sum(staffs))  

    print('#{} {}'.format(tc, min_sum-B))
