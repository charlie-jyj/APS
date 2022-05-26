var array = [1, 2, 3, 4, 5]
print(array[array.indices])

/*
 <cf> indices (instance property)
 the indices that are valid for subscriptin the collection, in ascending order
 a collection's indices property can hold a strong reference to the collection itself,
 causing the collection to be nonuniquely referenced
 */

/*
 <cf> ArraySlice
 Instead of copying over the elements of a slice to new storage,
 an arrayslice instance presents a view onto the storage of a larger array
 arrayslice presents the same interface as array, you can perform the same operation as you could on the array
 */

let absences = [0, 2, 0, 4, 0, 3, 1, 0]
let midpoint = absences.count / 2

// neither the firstHalf nor secondHalf slices allocate any new storage of their own
let firstHalf = absences[..<midpoint]
let secondHalf = absences[midpoint...]

let firstHalfSum = firstHalf.reduce(0, +)
let secondHalfSum = secondHalf.reduce(0, +)

if firstHalfSum > secondHalfSum {
    print("More absences in the first half.")
} else {
    print("More absences in the second half.")
}

/*
 long-term storage of arrayslice instances is discouraged
 a slice holds a reference to the entire storage of a larger array, not just to the portion it presents,
 even after the original array's lifetime ends.
 */
