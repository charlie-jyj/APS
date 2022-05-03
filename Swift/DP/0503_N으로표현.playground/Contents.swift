import Foundation

class Calculator {
    var memo = [Set<Int>]()
    var N: Int
    var number: Int
    
    init(N: Int, number: Int) {
        self.N = N
        self.number = number
        for _ in 0...8 {
            let set = Set<Int>()
            memo.append(set)
        }
        memo[1].update(with: N)
    }
    
    func execute() -> Int {
        
        // 0은 사용 안 함, index는 사용된 N의 숫자를 가르킨다.
        for i in 1...8 {
            
            // memo에 기록된 모든 경우의 수를 서로 사칙 연산한다.
            for j in 1...i {
                for elem1 in memo[j] {
                    for k in 1...i {
                        
                        // 8개 이상의 숫자를 사용할 경우 무시한다.
                        if j+k > 8 {
                            continue
                        }
                        
                        for elem2 in memo[k]{
                        
                            let plusResult = plus(elem1, elem2)
                            let timesResult = times(elem1, elem2)
                            
                            // 내가 간과했던 부분, minus/devide는 숫자의 순서에 따라 결과값이 다르므로
                            let minusResult1 = minus(elem1, elem2)
                            let minusResult2 = minus(elem2, elem1)
                            let devideResult1:Int? = devide(elem1, elem2)
                            let devideResult2:Int? = devide(elem2, elem1)
                            
                            if  plusResult == number ||
                                minusResult1 == number ||
                                minusResult2 == number ||
                                devideResult1 == number ||
                                devideResult2 == number ||
                                timesResult == number {
                                
                                // 사칙연산을 통해 값을 찾은 경우
                                return j + k
                                
                            } else {
                                // 발생할 수 있는 새로운 숫자를 메모한다.
                                [plusResult, minusResult1, minusResult2, timesResult].forEach {
                                    memo[j+k].update(with: $0)
                                }
                                
                                if devideResult1 != nil {
                                    memo[j+k].update(with: devideResult1!)
                                }
                                if devideResult2 != nil {
                                    memo[j+k].update(with: devideResult2!)
                                }
                            }
                        }
                    }
                }
            }
            
            // 숫자를 연달아 이어 붙여서 나올 수 있는 수
            var tempNum:String = ""
            for _ in 1...i {
                tempNum += String(N)
            }
            
            if Int(tempNum) == number {
                return i
            } else {
                // 일치하지 않을 경우 메모에 기록
                memo[i].update(with: Int(tempNum)!)
            }
        }
        // 8회차 내에 찾지 못한 경우 -1 반환한다.
        return -1
    }
    
    private func plus (_ a:Int, _ b: Int) -> Int {
        return a+b
    }
    
    private func minus (_ a:Int, _ b: Int) -> Int {
        return a-b
    }
    
    private func devide (_ a:Int, _ b: Int) -> Int? {
        guard b != 0 else { return nil }
        return a/b
    }
    
    private func times (_ a:Int, _ b: Int) -> Int {
        return a*b
    }
}

func solution(_ N:Int, _ number:Int) -> Int {
    if N == number {
        return 1
    }
    
    return Calculator(N: N, number: number).execute()
}
