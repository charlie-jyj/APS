def find_set(st):  # 대표원소 찾기
    if student[st] != st:  # 내가 나의 대표가 아닐 경우
        student[st] = find_set(student[st])

    return student[st]


def union(leader, member):  # 두 학생을 한 조로 만들기 = leader 통일하기
    student[find_set(member)] = find_set(leader)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 학생수, 신청서수
    student = [i for i in range(N+1)]  # 학생 목록
    forms = list(map(int, input().split()))
    for i in range(M):  # 신청서를 순회하며 각 학생을 한 조로 만든다
        st1, st2 = forms[2*i], forms[2*i+1]
        union(st1, st2)

    # 아직 리더가 갱신되지 않은 학생이 있을 것이기 때문에 전체 순회하며 리더 갱신
    for i in range(1, N+1):
        if student[i] != i:
            student[i] = find_set(student[i])

    print('#{} {}'.format(tc, len(set(student))-1))