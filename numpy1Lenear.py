import numpy as np 

# Creating matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print('Matrix A:')
print(A)
print('Matrix B:')
print(B)

# Addition
add = A + B
print(add)

# Multi
mul = np.dot(A, B)
print(mul)

# Transpose
trans_A = A.T 
print(trans_A)

# Determinant
det_A = np.linalg.det(A)
print(det_A)

# Inverse
inv_A = np.linalg.inv(A)
print(inv_A)

# Solve Ax = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print(x)


# output
'''
Matrix A:
[[1 2]
 [3 4]]

Matrix B:
[[5 6]
 [7 8]]

A + B:
[[ 6  8]
 [10 12]]

A * B (dot product):
[[19 22]
 [43 50]]

Transpose of A:
[[1 3]
 [2 4]]

Determinant of A:
-2.0000000000000004

Inverse of A:
[[-2.   1. ]
 [ 1.5 -0.5]]

Solution to Ax = b where b = [5, 11]:
[1. 2.]
'''