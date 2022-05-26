import Foundation

let id_list = ["muzi", "frodo", "apeach", "neo"]
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
let k = 2

//let id_list = ["con", "ryan"]
//let report = ["ryan con", "ryan con", "ryan con", "ryan con"]
//let k = 3

struct BlackList {
    private let id_list: [String]
    private let report: [String]
    private let limit: Int
    
    private var user_index: [String: Int] // user의 index 조회 용 딕셔너리
    private var emaillist: [Int]  // 반환할 result 배열
    private var visited: [[Int]]  // 신고 중복 방지용 2차원 배열
    private var candidates: [[Int]]  // 신고자 기록용 2차원 배열
    private var criminals: [Int]  // 범죄자 여부 기록용 배열 (1이면 범죄자 0이면 일반 유저)
    
    init(_ids: [String], _report: [String], _limit: Int) {
        self.id_list = _ids
        self.report = _report
        self.limit = _limit
        
        // 변수 초기화
        self.user_index = [:]
        self.emaillist = Array.init(repeating: 0, count: id_list.count)
        self.visited = Array.init(repeating: Array.init(repeating: 0, count: id_list.count), count: id_list.count)
        self.candidates = Array.init(repeating: [], count: id_list.count)
        self.criminals = Array.init(repeating: 0, count: id_list.count)
        
        // firstIndex 함수 대체 위해 dictionary 생성
        for i in 0..<id_list.count {
            user_index[id_list[i]] = i
        }
        
        // report 순회
        for doc in report {
            let group = doc.split(separator: " ")
            let challenger: Int = user_index[String(group[0])]!  // 신고자
            let defendent: Int = user_index[String(group[1])]!  // 예비 범죄자
            
            // 최초의 신고일 경우
            if visited[challenger][defendent] == 0 {
                // visited 기록
                visited[challenger][defendent] += 1
            
                // 이미 범죄자라면 나는 메일을 받는다.
                if criminals[defendent] > 0 {
                    emaillist[challenger] += 1
                    
                // 예비 범죄자라면 신고자 목록에 나를 추가한다.
                } else {
                    candidates[defendent].append(challenger)
                    
                    // 내가 신고하는 순간 범죄자로 확정되었다.
                    if candidates[defendent].count == limit {
                        criminals[defendent] += 1  // 범죄자로 등록
                        
                        // 나를 비롯하여 이전에 이 사람을 신고한 사람들은 메일을 받는다.
                        for j in candidates[defendent] {
                            emaillist[j] += 1
                        }
                    }
                }
            }
        }
    }
    
    public func getEmailList() -> [Int] {
        return emaillist
    }
}

print(BlackList(_ids: id_list, _report: report, _limit: k).getEmailList())
