import Foundation

struct Traffic {

func solution(_ lines:[String]) -> Int {
    for line in lines {
        let lineGroup = line.split(separator: " ")
        let sString = lineGroup[1].split(separator: ":")
        let tString = String(lineGroup[2]).replacingOccurrences(of: "s", with: "")
        let hour = Int(String(sString[0]))
        let mins = Int(String(sString[1]))
        let secs = Int(Double(String(sString[2]))!*1000)
        
        let responseMillisecs: Int = hour!*60*60*1000 + mins!*60*1000 + secs
        let processMillisecs: Int = Int(tString)!*1000
        let requestMillisecs: Int = responseMillisecs - processMillisecs + 1
            print(responseMillisecs, processMillisecs, responseMillisecs)
        
    }
    
    return 0
}
    
}





