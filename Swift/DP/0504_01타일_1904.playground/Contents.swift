import Foundation

//let N = Int(readLine()!)!
let N = 1000000

// N 만큼 수열을 만들어보자 1 <= N <= 1,000,000
var tilesArray = Array(repeating: 0, count: N+1)
tilesArray[1] = 1
tilesArray[2] = 2

if N < 3 {
    print(tilesArray[N])
} else {
    for i in 3..<N+1 {
        tilesArray[i] = (tilesArray[i-1] + tilesArray[i-2])%15746
    }
    print(tilesArray[N])
}


