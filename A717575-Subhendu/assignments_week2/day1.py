import numpy as np

# 1. Create a one dimensional array with the following values 1, 4, 3 and print the values
arr1 = np.array([1, 4, 3])
print(arr1)

# 2. Create a one dimensional array with the following values 1, 4, 3 and print the type of the array
arr2 = np.array([1, 4, 3])
print(arr2.dtype)

# 3. Create a two dimensional array with the following format: [(1, 2, 3), (4, 5, 6)] and print the values
arr3 = np.array([(1, 2, 3), (4, 5, 6)])
print(arr3)

# 4. Create a two dimensional array with the following format: [(1, 2, 3), (4, 5, 6)] and print the type of the array
arr4 = np.array([(1, 2, 3), (4, 5, 6)])
print(arr4.dtype)

# 5. Create a one dimensional array with the following values 1, 4, 3 and print the dimension of the array
arr5 = np.array([1, 4, 3])
print(arr5.ndim)

# 6. For the same one dimensional array find the byte size of an each element
print(arr5.itemsize)

# 7. For the same one dimensional array find the data type of an each element
print(arr5.dtype)

# 8. For the same one dimensional array find the size of an array
print(arr5.size)

# 9. Create an array with np.zeros as 3, 3 values and print it
arr6 = np.zeros((3, 3))
print(arr6)

# 10. Create an array with np.ones as 3, 3 values and print it
arr7 = np.ones((3, 3))
print(arr7)

# 11. Find the shape of the array for the following values. [(1, 2, 3), (4, 5, 6)]
arr8 = np.array([(1, 2, 3), (4, 5, 6)])
print(arr8.shape)

# 12.  Find the re shape of the array for the following values. [(1, 2, 3), (4, 5, 6)] and reshape (4, 2) and print it.
arr9 = np.array([(1, 2, 3), (4, 5, 6)])
# print(arr9.reshape(4, 2)) # ValueError: cannot reshape array of size 6 into shape (4,2)

# 13. Find the slice of an array for the following values. [(1, 2, 3), (4, 5, 6)] and a [0:, 2] and print it. 
arr10 = np.array([(1, 2, 3), (4, 5, 6)])
print(arr10[0:, 2])

# 14. Print the linspace for the values (1, 2, 5)
arr11 = np.linspace(1, 2, 5)
print(arr11)

# 15. Find the sum, max, min of an array for the following values [(1,2,3),(3,4,5)].
arr12 = np.array([(1, 2, 3), (3, 4, 5)])
print(arr12.sum())
print(arr12.max())
print(arr12.min())

# 16. Find the column wise and row wise sum of an array for the following values [(1, 2, 3), (3, 4, 5)].
arr13 = np.array([(1, 2, 3), (3, 4, 5)])
print(arr13.sum(axis=0))
print(arr13.sum(axis=1))

# 17. Find the transpose of an array [[1,2,3],[3,4,5],[9,6,0]] and print it
arr14 = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
print(arr14.T)

# 18. Find the row wise sort and column wise sort for the following values [[1,4,2],[3,4,6],[0,-1,5]] and print it
arr15 = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]])
print(np.sort(arr15, axis=0))
print(np.sort(arr15, axis=1))

# 19. Find the horizontal split and vertical split for the following values [[1,3,5,7,9,11],[2,4,5,8,10,12]] and print it
arr16 = np.array([[1, 3, 5, 7, 9, 11], [2, 4, 5, 8, 10, 12]])
print(np.hsplit(arr16, 2))
print(np.vsplit(arr16, 2))

# 20.  Find the vstack and hstack for the following values 

a = np.array([(1,2,3),(3,4,5)]) 
b = np.array([(1,2,3),(3,4,5)])

print(np.vstack((a,b)))
print(np.hstack((a,b)))
