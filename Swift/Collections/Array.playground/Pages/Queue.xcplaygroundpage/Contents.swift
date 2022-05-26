//: [Previous](@previous)
import Foundation

public struct Queue<T> {
    private var data = [T]()
    
    public mutating func dequeue() -> T? {
        return data.removeFirst()
    }
    
    public func peek() -> T? { return data.first }
    
    public mutating func enqueue(_ element: T) {
        data.append(element)
    }
    
    public mutating func clear() {
        data.removeAll()
    }
    
    public var count: Int {
        return data.count
    }
    
    public var capacity: Int {
        get {
            return data.capacity
        }
        set {
            data.reserveCapacity(newValue)
        }
    }
    
    public var isFull: Bool {
        return count == data.capacity
    }
    
    public var isEmpty: Bool {
        return data.isEmpty
    }
}

//: [Next](@next)
