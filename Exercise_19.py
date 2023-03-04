# Libs in Python

import numpy as np

A = np.array([i for i in range(10)], float)

print(type(A))
print(A)
print(A[2 : 9 : 2])
print(A[3])

B = np.array([[i for i in range(11, 23)], [i for i in range(33, 45)]], float)

print(B)
print(len(B))       # Array first dimention
print(B.shape)      # Array dimention
print(B.dtype)      # Array data type
print(B[1, 5])
print(37 in B)

C = np.array(range(20), float)

print(C)

C = C.reshape(4, 5)     # Change array dimention
print(C)

B = B.flatten()      # Change array dimention
C = C.flatten()      # Change array dimention

print(A)
print(B)
print(C)

print(np.concatenate((A, B, C)))

print(np.identity(11, float))
