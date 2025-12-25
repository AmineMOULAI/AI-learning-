import numpy as np

# 1D array
print("############### 1D array ##############")
a = np.array([1, 2, 3])
print("a =", a)
print("a dim = ", a.ndim)
print("a shape =", a.shape)

## Slicing ##
print(a[1:])

b = np.array(['A', 'B', 'C']) 
print("b =", b)

print("\n")

# 2D array
print("############### 2D array ##############")
v1 = np.array([[1, 2, 3],
	      [4, 5, 6],
	      [7, 8, 9]])
print("v1 =", v1)
print("v1 dim = ", v1.ndim)
print("v1 shape =", v1.shape)
print("v1(1, 2) = ", v1[1, 2])

## Slicing ##

# Rows
print("### Rows")
print(v1[1:]) # row
print(v1[:-1]) # negative index 
print(v1[::-1]) # inverse the rows

print("\n")

# Columns
print("### Columns")
print(v1[:,1:]) # column
print(v1[:,:-1]) # negative index
print(v1[:,:-2])
print(v1[:, ::-1]) # inverse the columns
print("\n")


