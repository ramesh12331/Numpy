# ============================================================
# 3. CREATE A 2D ARRAY
# ============================================================
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(arr)

# ============================================================
# 4. ndim - NUMBER OF DIMENSIONS
# ============================================================
# ndim tells us how many dimensions
# an array has.
#
# Syntax:
#
# array.ndim

print("\nNumber of dimensions:")
print(arr.ndim)

# ============================================================
# 5. UNDERSTANDING ndim WITH 1D
# ============================================================
arr_1d = np.array([1, 2, 3])

print("\n1D Array:")
print(arr_1d)

print("\n1D Array:", arr_1d.ndim)
print(arr_1d)

# ============================================================
# 6. UNDERSTANDING ndim WITH 2D
# ============================================================
arr_2d = np.array([
    [1,2],
    [3,4]
])

print("\n 2D Array:", arr_2d.ndim)
print(arr_2d)

# ============================================================
# 7. UNDERSTANDING ndim WITH 3D
# ============================================================

arr_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print('\n 3D Array', arr_3d.ndim)
print(arr_3d)

# ============================================================
# 9. shape - SIZE OF EACH DIMENSION
# ============================================================

# shape tells us the size of the array
# in each dimension.
#
# Syntax:
#
# array.shape

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nShape:")
print(arr.shape)

# ============================================================
# 11. shape WITH 1D ARRAY
# ============================================================
arr = np.array([10, 20, 30, 40])

print("\n1D Shape:")
print(arr.shape)

# ============================================================
# 12. shape WITH 3D ARRAY
# ============================================================

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("\n3D Shape:")
print(arr.shape)

# ============================================================
# 13. size - TOTAL NUMBER OF ELEMENTS
# ============================================================

# size tells us the total number
# of elements in the array.
#
# Syntax:
#
# array.size


arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nTotal number of elements:")
print(arr.size)

# ============================================================
# 15. size WITH DIFFERENT SHAPES
# ============================================================
arr = np.zeros((4, 5))

print("\nShape:")
print(arr.shape)

print("Size:")
print(arr.size)

# ============================================================
# 16. dtype - DATA TYPE
# ============================================================

# dtype tells us the data type
# of the elements inside the array.
#
# Syntax:
#
# array.dtype

arr = np.array([10, 20, 30])

print("\ndtype:")
print(arr.dtype)

# ============================================================
# 17. dtype WITH FLOAT
# ============================================================

arr = np.array([10.5, 20.5, 30.5])

print("\nFloat dtype:")
print(arr.dtype)

# ============================================================
# 18. dtype WITH BOOLEAN
# ============================================================

arr = np.array([True, False, True])

print("\nBoolean dtype:")
print(arr.dtype)

# ============================================================
# 19. dtype WITH EXPLICIT DATA TYPE
# ============================================================

# We can specify the data type
# while creating the array.

arr = np.array([10, 20, 30], dtype="float64")

print("\nSpecified dtype:")
print(arr)
print(arr.dtype)

# ============================================================
# 20. itemsize - MEMORY USED BY ONE ELEMENT
# ============================================================

# itemsize tells us how many BYTES
# are used by ONE array element.
#
# Syntax:
#
# array.itemsize

arr = np.array([10, 20, 30, 40])

print("\nData type:")
print(arr.dtype)

print("Item size:")
print(arr.itemsize)

# ============================================================
# 22. nbytes - TOTAL MEMORY USED
# ============================================================

# nbytes tells us the total number
# of bytes used by the array's elements.
#
# Syntax:
#
# array.nbytes

arr = np.array([10, 20, 30, 40])

print("\nTotal memory:")
print(arr.nbytes)

# ============================================================
# 24. COMPLETE EXAMPLE
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n==============================")
print("COMPLETE ARRAY INFORMATION")
print("==============================")

print("Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Total elements:", arr.size)
print("Data type:", arr.dtype)
print("Memory per element:", arr.itemsize, "bytes")
print("Total memory:", arr.nbytes, "bytes")

# ============================================================
# 27. REAL-WORLD EXAMPLE - STUDENT MARKS
# ============================================================

# Suppose we have marks of:
#
# 3 students
# in
# 3 subjects

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

print("\n==============================")
print("STUDENT MARKS")
print("==============================")

print("Marks:")
print(marks)

print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Total marks:", marks.size)
print("Data type:", marks.dtype)
print("Memory per value:", marks.itemsize, "bytes")
print("Total memory:", marks.nbytes, "bytes")

# ============================================================
# 33. ATTRIBUTE vs METHOD EXAMPLE
# ============================================================

arr = np.array([
    [1, 2],
    [3, 4]
])

# Attributes:
print("\nAttributes:")
print("shape:", arr.shape)
print("size:", arr.size)
print("ndim:", arr.ndim)
print("dtype:", arr.dtype)
print("itemsize:", arr.itemsize)
print("nbytes:", arr.nbytes)

# Methods:
#
# arr.reshape()
# arr.flatten()
#
# These perform an ACTION,
# so parentheses are required.

# ============================================================
# 35. PRACTICE QUESTION
# ============================================================

# Given:

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\nPractice Array:")
print(arr)

print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)
print("itemsize:", arr.itemsize)
print("nbytes:", arr.nbytes)

# ============================================================
# 36. MINI EXERCISE
# ============================================================
# Create this array:

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

# Find:
#
# 1. ndim
# 2. shape
# 3. size
# 4. dtype
# 5. itemsize
# 6. nbytes
print("\n==============================")
print("MINI EXERCISE")
print("==============================")

print("Array:")
print(arr)

print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)
print("itemsize:", arr.itemsize)
print("nbytes:", arr.nbytes)