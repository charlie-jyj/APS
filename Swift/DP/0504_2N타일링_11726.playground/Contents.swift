import Foundation

//let width: Int = Int(readLine()!)!

let width: Int = 9

/*
 점화식을 찾는다
 추측: p(n) = p(n-1) + p(n-2)
 p(1) = 1
 p(2) = 2
 
 길이 n+1 의 배열을 사용하여 풀이
 */

var testArray = Array(repeating: 0, count: 1001)
testArray[1] = 1
testArray[2] = 2

if width > 2 {
    for i in 3..<width+1 {
        testArray[i] = (testArray[i-1] + testArray[i-2])%10007
    }
}

print(testArray[width])

