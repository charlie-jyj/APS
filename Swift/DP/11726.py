n = int(input())
quotient = 10007
testArray = [0 for _ in range(0, 1001)]
testArray[0] = 0
testArray[1] = 1
testArray[2] = 2

for i in range(3, n+1):
    testArray[i] = testArray[i-1] + testArray[i-2]

print(testArray[n]%quotient)