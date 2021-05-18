import sys
sys.stdin = open()


def check():
    
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            pos = BRD[i][j]
            if cnt[pos] == 1:
                return 0

        cnt = [0] * 10
        for j in range(9):
            pos = BRD[j][i]
            if cnt[pos] == 1:
                return 0
        
        # 마무리
        for c in range(0, 9, 3):
            cnt = [0] * 10
            for i in range(c, c+3):
                for j in range(c, c+3):
                    pos = BRD[c+i][c+j]
                    if cnt[pos] == 1:
                        return 0
                    
TC = int(input())
for tc in range(1, TC+1):
    BRD = [list(map(int, input())) for _ in range(9)]
    
    