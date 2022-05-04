import Foundation

// 입력값 받기
let testCaseNum = Int(readLine()!)!
var testCaseArray = Array(repeating: 0, count: testCaseNum)
for i in stride(from: 0, to: testCaseNum, by: 1) {
    testCaseArray[i] = Int(readLine()!)!
}

//var testCaseArray = [11,12,13,14]

// 점화식 구현
func solution (n: Int) -> Int {
    
    var waveArray: [Int] = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    
    if n < 11 {
        return waveArray[n]
    } else {
        for i in 11..<n+1 {
            waveArray.append(waveArray[i-2] + waveArray[i-3])
        }
        return waveArray[n]
    }
}

testCaseArray.forEach {
    print(solution(n: $0))
}


