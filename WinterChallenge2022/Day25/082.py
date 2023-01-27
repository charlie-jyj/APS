"""
1. 사전에서 다루는 문자열은 a, z
2. a N개 z M개
3. 핵심 아이디어 (N+M)개에서 N개를 뽑는 경우의 수 = (N+M)개에서 M개를 뽑는 경우의 수
4. 중복 조합 n H r = n-1+r C n-1 = n-1+r C r
"""
import sys
sys.stdin = open('082_text.txt')
input = sys.stdin.readline
N, M, K = list(map(int, input()))