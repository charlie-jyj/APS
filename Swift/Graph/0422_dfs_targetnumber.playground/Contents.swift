import Foundation

class Finder {
    var numbers: [Int]
    var target: Int
    var length: Int
    
    init(numbers: [Int], target: Int) {
        self.numbers = numbers
        self.target = target
        self.length = numbers.count
    }
    
    func doit() -> Int {
        let remain = numbers.reduce(0, +)
        return findTargetNumber(0, 0, remain, -remain)
    }
    
    func findTargetNumber(_ i: Int,_ temp_sum: Int,_ remain_max: Int,_ remain_min: Int) -> Int {
    
        if i < length, temp_sum + remain_max < target, target < temp_sum + remain_min {
            return 0
        }
        
        if i == length, temp_sum == target {
            return 1
        } else if i == length, temp_sum != target {
            return 0
        }
        
        return findTargetNumber(i+1, temp_sum + numbers[i], remain_max - numbers[i], remain_min + numbers[i]) + findTargetNumber(i+1, temp_sum - numbers[i], remain_max - numbers[i], remain_min + numbers[i])
        
}
}



func solution(_ numbers:[Int], _ target:Int) -> Int {
    return Finder(numbers: numbers, target: target).doit()
}
