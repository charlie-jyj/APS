import Foundation

let A: Int = Int(Character("A").asciiValue!)
let jump = 3
let jumpfromA = String(UnicodeScalar(3 + A)!)

print(jumpfromA)
