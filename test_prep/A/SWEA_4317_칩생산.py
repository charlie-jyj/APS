"""
idea
나는 이걸 BFS 로 풀어보려다가 망해서 밀어버렸다
"""

for tc in range(1, int(input())+1):
    H, W = map(int, input().split()) # 세로 가로
    wafer = [list(map(int, input().split())) for _ in range(H)]