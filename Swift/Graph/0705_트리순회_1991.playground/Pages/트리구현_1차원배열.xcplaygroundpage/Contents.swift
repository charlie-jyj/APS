/*
 index 계산해서 1차원 배열에 트리 구현하여 순회하기
 */

import Foundation

class Solution {
    var n: Int
    var tree: [String] = []  // n+1 배열에 기록
    
    var preArray: [String] = []
    var inArray: [String] = []
    var postArray: [String] = []
    
    init(n: Int, tree: [String]) {
        self.n = n
        self.tree = tree
    }
    
    func start() {
        let root = 1 // root는 항상 1
        preorder(node: root)
        inorder(node: root)
        postorder(node: root)
        
        // 출력
        print("\(preArray.joined(separator: ""))\n\(inArray.joined(separator: ""))\n\(postArray.joined(separator: ""))")
    }
    
    
    private func preorder(node: Int) {
        // 부모 없이는 자식도 없다
        if node <= n,
           tree[node] == "" {
            return
        }
        
        print(node)
        // 부모 방문 -> 왼쪽 자식 방문 -> 오른쪽 자식 방문
        if tree[node] != "" {
            preArray.append(tree[node])
        }
        
        if node*2 < n+1,
           tree[node*2] != "" {
            preorder(node: node*2)
        }
        
        if node*2+1 < n+1,
           tree[node*2+1] != "" {
            preorder(node: node*2+1)
        }
        
        
    }
    
    private func inorder(node: Int) {
        if node > n {
            return
        }
        
        // 왼쪽 자식 방문 -> 부모 방문 -> 오른쪽 자식 방문
        inorder(node: node*2)
        if tree[node] != "" {
            inArray.append(tree[node])
        }
        inorder(node: node*2+1)
    }
    
    private func postorder(node: Int) {
        if node > n {
            return
        }
        
        // 왼쪽 자식 방문 -> 오른쪽 자식 방문 -> 부모 방문
        postorder(node: node*2)
        postorder(node: node*2+1)
        if tree[node] != "" {
            postArray.append(tree[node])
        }
    }

    
}


// setup
//var n = Int(readLine()!)!
var inputnumber: Int = 7
var n = Int(truncating: NSDecimalNumber(decimal: pow(Decimal(2), inputnumber)-1))  // 트리가 완전히 편향된 이진트리일 수도 있기 때문에 배열의 크기는 2^n

var inputmock = [
    "A B C",
    "B D .",
    "C E F",
    "E . .",
    "F . G",
    "D . .",
    "G . ."
]

// tree
var tree = Array(repeating: "", count: n+1)

// root 는 tree[1] 이고 항상 A라는 조건
var pairs: [String: Int] = [
    "A":1
]

//for _ in 0..<n {
for line in inputmock {
    //if let group = readLine()?.split(separator: " ") {
    let group = line.split(separator: " ")
    print(group[0], group[1], group[2])
    
    let parent = pairs[String(group[0])]!
    print("parent \(parent) : \(group[0])")
    tree[parent] = String(group[0])
    
    if group[1] != "." {
        print("leftchild \(parent*2) : \(group[1])")
        tree[parent*2] = String(group[1])
        pairs[String(group[1])] = parent*2
    }
    
    if group[2] != "." {
        print("righttchild \(parent*2+1) : \(group[2])")
        tree[parent*2+1] = String(group[2])
        pairs[String(group[2])] = parent*2+1
    }
  
    //}
}

print(tree)
print(pairs)
Solution(n: n, tree: tree).start()





