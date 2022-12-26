# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input()) # 노드수
graph = [list() for _ in range(N+1)] # 연결리스트
visit = [0 for _ in range(N+1)]
cycle = list()
found = -2 

for _ in range(N):
	a, b = list(map(int, input().split()))
	graph[a].append(b)
	graph[b].append(a)
	
def findCycle(node, parent):
	global found
	
	if visit[node] != 0:
		found = node
		# 이미 방문한 노드를 찾았다면 cycle을 발견
		if node not in cycle:
			cycle.append(node)
		return
	
	# 방문 표시
	visit[node] = 1
		
	for next_node in graph[node]:
		if next_node == parent:
			continue
		
		findCycle(next_node, node)
		
		if found == -1:
			# 이미 탐색 끝 
			return 
		
		if found == node:
			# 나로 돌아왔다는건 cycle을 한 바퀴 돌고 끝났다는 것
			found = -1
			return 
		
		if found >= 0:
			# next_node가 cycle이었다는건 그 직전의 나도 cycle이라는 뜻
			if node not in cycle:
				cycle.append(node)
			return
			
findCycle(1,1)
print(len(cycle), end="\n")
print(" ".join(map(str,sorted(cycle))))