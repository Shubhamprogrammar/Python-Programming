import numpy as np

arr = np.array([1, 2, 3, 4, 5,6,7,8,9,10,11,12])

print(arr)
print(arr.ndim)
print(type(arr))
print(arr[0])
print(arr[1:5])
print(arr[1:5:2])
print(arr.dtype)
x = arr.copy()
print(x)
y = arr.view()
print(y)
newarr = arr.reshape(4, 3)
print(newarr)


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print(arr.shape)

print(arr.ndim)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
x = np.where(arr%2 == 0)
print(x)

arr = np.array([3,8, 2, 0, 1])
print(np.sort(arr))