//: [Previous](@previous)

/*
 부모 노드의 왼쪽, 오른쪽 자식을 2차원 배열에 구현하여 순회하기
 */

import Foundation

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

func CharacterToIndex(char: String) -> Int {
    return Int(Character(char).asciiValue!) - Int(Character("A").asciiValue!) + 1
}

func IndexToCharacter(index: Int) -> String {
    return String(UnicodeScalar(index - 1 + Int(Character("A").asciiValue!))!)
}


// setup
var n = inputnumber
var children = Array(repeating: Array(repeating: "", count: 2), count: n+1)
var preArray: [String] = []
var inArray: [String] = []
var postArray: [String] = []

for line in inputmock {
    //if let group = readLine()?.split(separator: " ") {
    let group = line.split(separator: " ")
    print(group[0], group[1], group[2])
    
    let parent = CharacterToIndex(char: String(group[0]))
    children[parent][0] = String(group[1])
    children[parent][1] = String(group[2])
    //}
}

print(children)

func preorder(current: Int) {
    let node = IndexToCharacter(index: current)
    print("pre",current, node)
    
    preArray.append(node)

    if children[current][0] != "." {
        let left = CharacterToIndex(char: String(children[current][0]))
        print("pre left", left)
        preorder(current: left)
    }
    
    if children[current][1] != "." {
        let right = CharacterToIndex(char: String(children[current][1]))
        print("pre right", right)
        preorder(current: right)
    }
}

func inorder(current: Int) {
    let node = IndexToCharacter(index: current)
    print("in",current, node)
    
    if children[current][0] != "." {
        let left = CharacterToIndex(char: String(children[current][0]))
        inorder(current: left)
    }
    
    inArray.append(node)
    
    if children[current][1] != "." {
        let right = CharacterToIndex(char: String(children[current][1]))
        inorder(current: right)
    }
}

func postorder(current: Int) {
    let node = IndexToCharacter(index: current)
    print("post",current, node)
    
    if children[current][0] != "." {
        let left = CharacterToIndex(char: String(children[current][0]))
        postorder(current: left)
    }
    
    if children[current][1] != "." {
        let right = CharacterToIndex(char: String(children[current][1]))
        postorder(current: right)
    }
    
    postArray.append(node)
}

preorder(current: 1)
inorder(current: 1)
postorder(current: 1)

print("\(preArray.joined(separator: ""))\n\(inArray.joined(separator: ""))\n\(postArray.joined(separator: ""))")


//: [Next](@next)
