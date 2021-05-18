# 수직 체크, 대각선 체크
def is_available(candidate, current_col):
    # 현재 내가 다루고 있는 행 == 이제까지 배치된 퀸의 수
    current_row = len(candidate)
    for queen_row in range(current_row):
        # candidtae[queen_row] 현재까지 배치된 퀸의 컬럼 번호
        if candidate[queen_row] == current_col or abs(candidate[queen_row]-current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):  # board의 길이, 현재 다루고 있는 행, 현재까지 배치된 퀸, 최종 배치
    if current_row == N:  # 배치가 끝났다
        final_result.append(current_candidate[:])  # 가능한 배치를 저장, shallow copy
        return  # 아래 부분 실행하지 않고 return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()  # 배치했거나 배치할 수 없을 경우 return -> 해당 후보를 제거한다. -> 다음 후보 점검


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


print(solve_n_queens(4))