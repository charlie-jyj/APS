//: [Previous](@previous)

/*
 트리를 구조체로 구현하여 보자
 */

class Node {
    let data: String
    var leftNode: Node?
    var rightNode: Node?

    init(value: String) {
        data = value
        leftNode = nil
        rightNode = nil
    }
    
    func addLeft(node: Node) {
        leftNode = node
    }
    
    func addRight(node: Node) {
        rightNode = node
    }
}

class Tree {
    static var shared = Tree()
    var count: Int = 0
    static var preorderLine: String = ""
    static var inorderLine: String = ""
    static var postorderLine: String = ""
    
    init() {}
    
    func addNode(data: String) -> Node {
        let node = Node(value: data)
        Tree.shared.count += 1
        return node
    }
    
    func preorder(node: Node?) {
        guard let current = node else { return }
        Tree.preorderLine += current.data
        preorder(node: current.leftNode)
        preorder(node: current.rightNode)
    }
    
    func inorder(node: Node?) {
        guard let current = node else { return }
        inorder(node: current.leftNode)
        Tree.inorderLine += current.data
        inorder(node: current.rightNode)
    }
    
    func postorder(node: Node?) {
        guard let current = node else { return }
        postorder(node: current.leftNode)
        postorder(node: current.rightNode)
        Tree.postorderLine += current.data
    }
}

func CharacterToIndex(char: String) -> Int {
    return Int(Character(char).asciiValue!) - Int(Character("A").asciiValue!) + 1
}

func IndexToCharacter(index: Int) -> String {
    return String(UnicodeScalar(index - 1 + Int(Character("A").asciiValue!))!)
}


var inputnumber: Int = 7
var inputmock = [
    "A B C",
    "B D .",
    "C E F",
    "E . .",
    "F . G",
    "D . .",
    "G . ."
]

var n = inputnumber
// node를 재활용하기 위해
var nodes: [Node?] = Array(repeating: nil, count: n+1)
var children = Array(repeating: Array(repeating: "", count: 2), count: n+1)

// nodes 생성
for line in inputmock {
    //if let group = readLine()?.split(separator: " ") {
    let group = line.split(separator: " ")
    let parent = CharacterToIndex(char: String(group[0]))
    nodes[parent] = Tree.shared.addNode(data: String(group[0]))
    children[parent][0] = String(group[1])
    children[parent][1] = String(group[2])
    //}
}

//node 연결
for i in 1...n {
    let parent = nodes[i]!
    
    if children[i][0] != ".",
       let left = nodes[CharacterToIndex(char: children[i][0])]{
        parent.addLeft(node: left)
    }
    
    if children[i][1] != ".",
       let right = nodes[CharacterToIndex(char: children[i][1])]{
        parent.addRight(node: right)
    }
    
    nodes[i] = parent
}

Tree.shared.preorder(node: nodes[1])
Tree.shared.inorder(node: nodes[1])
Tree.shared.postorder(node: nodes[1])

print(Tree.preorderLine)
print(Tree.inorderLine)
print(Tree.postorderLine)

//: [Next](@next)
