let items = ["A", "B", "A", "C", "A", "D"]

/*
 The indices that are valid for subscripting the collection, in ascending order.
 */
let filteredIndices = items.indices.filter {items[$0] == "A"}
print(filteredIndices)
