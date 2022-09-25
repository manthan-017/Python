import array
A = array.array("i",[1,2,3,4,5,6,7])

i = int(input("enter value"))

if i in A:
    print(A.index(i))
else:
    print("enter valid index")