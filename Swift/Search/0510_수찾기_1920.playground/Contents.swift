import Foundation

//let n = Int(readLine()!)!
//var source = readLine()!.components(separatedBy: " ").map { Int($0) }
//let m = Int(readLine()!)!
//var target = readLine()!.components(separatedBy: " ").map { Int($0) }

let n = 5
var source = "4 1 5 2 3".split(separator: " ").map { Int($0)! }.sorted(by: {first, second in return first < second})
let m = 5
var target = "1 3 7 9 5".split(separator: " ").map { Int($0)! }

print(source)
print(target)

struct Search {
    let n: Int
    let m: Int
    var sourceList: [Int]
    var targetList: [Int]
    
    func getResult() -> [Int] {
        var result = [Int]()
        for target in targetList {
            result.append(search(target: target, min: 0, max: n-1))
        }
                
        return result
    }
    
    // binary search
    func search(target: Int, min: Int, max: Int) -> Int {
        if min > max {
            return 0
        }
        
        let index = Int((min+max)/2)
        
        if sourceList[index] == target {
            return 1
        }
        
        if target < sourceList[index] {
            return search(target: target, min: min, max: index-1)
        } else {
            return search(target: target, min: index+1, max: max)
        }
    }
    
}

let soulution = Search(n: n, m: m, sourceList: source, targetList: target)
soulution.getResult().forEach {
    print($0)
}
