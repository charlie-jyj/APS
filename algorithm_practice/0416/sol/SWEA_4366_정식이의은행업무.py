"""
2진수 10진수로 바꾸기
for x in binary:
result = 2*result + int(x)

3진수 10진수로 바꾸기
for x in ternary:
result = 3*result + int(x)

3진수 각 자리를 바꾸기
ternary = ['2','1','2']
num1 = 0
num2 = 0
for i in range(len(ternary)):  # 잘못된 위치 결정
    for j in range(len(ternary)):
        if i==j:
            num1 = num1*3 + (int(ternary[j])+1)%3
            num2 = num2*3 + (int(ternary[j])+2)%3

"""


def f(b,t):
    # bint=int(b,2)
    bint = 0
    for x in b:  # 10 진수로 바꾸기
        bint = bint*2 + int(x)
        
    # 가능한 수의 후보
    binary = []
    for i in range(len(b)):
        binary.append(bint ^ (1 << i))  # 2진수의 1비트 씩을 바꿔서 저장
        
    # 3진수 각 자리 바꾸기
    for i in range(len(t)):
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if i != j:  # 안 바꾸는 자리
                num1 = num1 * 3 + int(t[j])
                num2 = num2 * 3 + int(t[j])
            else:  # 바꾸는 자리
                num1 = num1 * 3 + (int(t[j])+1) % 3
                num2 = num2 * 3 + (int(t[j]) + 2) % 3
        
        if num1 in binary:
            return num1
        if num2 in binary:
            return num2