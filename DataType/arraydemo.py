import array
arr = array.array("i",[1,2,3,4])
print(arr)

arr.insert(3,10)
arr.insert(4,10)
print(arr)

arr.append(20)
print(arr)

print(len(arr))

print(arr.count(10))

arr.pop(2)
print(arr)

print(arr[4])

print(arr[1:4])