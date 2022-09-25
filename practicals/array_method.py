import array
A = array.array("i",[1,2,3,4])

A.append(78)
print(A)

A.insert(3,10)
A.insert(4,78)
print(A)

A.remove(10)
print(A)

A.pop(2)
print(A)

print(A[3])

print(A.count(78))