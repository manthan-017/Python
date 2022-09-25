import numpy
arr = numpy.array([1,2,3,4,5])
print(arr)

#version
import numpy as np
print(np.__version__)

#0-D arrays
import numpy as np
arr = np.array(42)
print(arr)

#1-D array
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

#2-D array
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#3-D array
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

#access array element
import numpy
arr = numpy.array([1,2,3,4,5])
print(arr[1])

#sum of index
import numpy
arr = numpy.array([1,2,3,4,5])
print(arr[1]+arr[2])

#access of 2-D array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row',arr[0,1])

#access of 3-D array
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)

#slicing array
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

#negative slicing
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])

#step slicing
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])

#slicing 2-D array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 1:4])

#sorting array
import numpy as np
arr = np.array([3,4,0,1])
print(np.sort(arr))

#arithmetic operation

#add operation
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
newarr = np.add(arr1,arr2)
print(newarr)

#sub operation
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
newarr = np.subtract(arr1,arr2)
print(newarr)

#mul operation
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
newarr = np.multiply(arr1,arr2)
print(newarr)

#div operation
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
newarr = np.divide(arr1,arr2)
print(newarr)

#power function
import numpy as np
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])
newarr = np.power(arr1,arr2)
print(newarr)

#absolute values
import numpy as np
arr1 = np.array([-1,-2,1,2,3,-4])
newarr = np.absolute(arr1,arr2)
print(newarr)

#LCM(Lowest Common Multiple)
import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1,num2)
print(x)

#GCD(Greatest Common Denominator)
import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1,num2)
print(x)

#Max() and Min() in array
arr = numpy.array([1,2,3,4,5])
print(numpy.max(arr))
print(numpy.min(arr))

#searching in array
import numpy as np
arr = np.array([1,2,3,4,5])
n = 1
if n in arr:
    print("found")
else:
    print("not found")