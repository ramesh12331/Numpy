# ============================================================
# NUMPY COMPLETE COURSE
# CHAPTER 3 - ARRAY ATTRIBUTES
# VS CODE NOTES WITH COMMENTED EXPLANATION
# ============================================================

import numpy as np


# ============================================================
# 1. WHAT ARE ARRAY ATTRIBUTES?
# ============================================================

# Array attributes are properties that give us
# important information about a NumPy array.
#
# We can ask NumPy:
#
# 1. How many dimensions?
# 2. What is the shape?
# 3. How many total elements?
# 4. What is the data type?
# 5. How many bytes does one element use?
# 6. How many total bytes does the array use?
#
# Important NumPy attributes:
#
# ndim
# shape
# size
# dtype
# itemsize
# nbytes


# ============================================================
# 2. CHAPTER 3 MEMORY TRICK
# ============================================================

# Remember this order:
#
# ndim → shape → size → dtype → itemsize → nbytes
#
#
# ndim
# → Number of dimensions
#
# shape
# → Structure / size of each dimension
#
# size
# → Total number of elements
#
# dtype
# → Data type
#
# itemsize
# → Bytes used by ONE element
#
# nbytes
# → Total bytes used by the array


# ============================================================
# 3. CREATE A 2D ARRAY
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(arr)

# Output:
#
# [[10 20 30]
#  [40 50 60]]


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

# Output:
#
# 2
#
# Why?
#
# The array has:
#
# Rows + Columns
#
# Therefore it is 2D.


# ============================================================
# 5. UNDERSTANDING ndim WITH 1D
# ============================================================

arr_1d = np.array([1, 2, 3])

print("\n1D Array:")
print(arr_1d)

print("ndim:", arr_1d.ndim)

# Output:
#
# [1 2 3]
# ndim: 1
#
# A single sequence = 1 dimension.


# ============================================================
# 6. UNDERSTANDING ndim WITH 2D
# ============================================================

arr_2d = np.array([
    [1, 2],
    [3, 4]
])

print("\n2D Array:")
print(arr_2d)

print("ndim:", arr_2d.ndim)

# Output:
#
# [[1 2]
#  [3 4]]
#
# ndim: 2


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

print("\n3D Array:")
print(arr_3d)

print("ndim:", arr_3d.ndim)

# Output:
#
# 3
#
# There are multiple 2D arrays,
# so the array has 3 dimensions.


# ============================================================
# 8. ndim QUICK MEMORY
# ============================================================

# 1D → Line
#
# [1 2 3]
#
#
# 2D → Table
#
# [[1 2]
#  [3 4]]
#
#
# 3D → Stack of Tables
#
# [
#   [[1 2]
#    [3 4]],
#
#   [[5 6]
#    [7 8]]
# ]


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

# Output:
#
# (2, 3)
#
# For a 2D array:
#
# shape = (rows, columns)
#
# Therefore:
#
# 2 rows
# 3 columns


# ============================================================
# 10. UNDERSTANDING shape VISUALLY
# ============================================================

# Array:
#
#          3 columns
#       ↓    ↓    ↓
#
#       10   20   30   ← Row 1
#       40   50   60   ← Row 2
#
#       ↑
#     2 rows
#
#
# Therefore:
#
# shape = (2, 3)


# ============================================================
# 11. shape WITH 1D ARRAY
# ============================================================

arr = np.array([10, 20, 30, 40])

print("\n1D Shape:")
print(arr.shape)

# Output:
#
# (4,)
#
# This means:
#
# 4 elements in one dimension.


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

# Output:
#
# (2, 2, 3)
#
# Meaning:
#
# 2 matrices
# × 2 rows
# × 3 columns


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

# Output:
#
# 6


# ============================================================
# 14. size MATHEMATICAL DRY RUN
# ============================================================

# Our array has:
#
# 2 rows
# 3 columns
#
# Therefore:
#
# size = rows × columns
#
# size = 2 × 3
#      = 6
#
# So:
#
# arr.size = 6


# ============================================================
# 15. size WITH DIFFERENT SHAPES
# ============================================================

arr = np.zeros((4, 5))

print("\nShape:")
print(arr.shape)

print("Size:")
print(arr.size)

# Output:
#
# Shape:
# (4, 5)
#
# Size:
# 20
#
# Calculation:
#
# 4 × 5 = 20


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

# Possible output:
#
# int64
#
# Exact integer dtype can depend
# on your platform / NumPy build.


# ============================================================
# 17. dtype WITH FLOAT
# ============================================================

arr = np.array([10.5, 20.5, 30.5])

print("\nFloat dtype:")
print(arr.dtype)

# Common output:
#
# float64


# ============================================================
# 18. dtype WITH BOOLEAN
# ============================================================

arr = np.array([True, False, True])

print("\nBoolean dtype:")
print(arr.dtype)

# Output:
#
# bool


# ============================================================
# 19. dtype WITH EXPLICIT DATA TYPE
# ============================================================

# We can specify the data type
# while creating the array.

arr = np.array([10, 20, 30], dtype="float64")

print("\nSpecified dtype:")
print(arr)
print(arr.dtype)

# Output:
#
# [10. 20. 30.]
# float64


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

# Possible output:
#
# Data type:
# int64
#
# Item size:
# 8
#
# This means:
#
# ONE element = 8 bytes


# ============================================================
# 21. itemsize DRY RUN
# ============================================================

# Suppose:
#
# dtype = int64
#
# int64 normally uses:
#
# 8 bytes
#
# Array:
#
# [10, 20, 30, 40]
#
# Each value uses 8 bytes:
#
# 10 → 8 bytes
# 20 → 8 bytes
# 30 → 8 bytes
# 40 → 8 bytes


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

# If:
#
# size = 4
# itemsize = 8 bytes
#
# Then:
#
# nbytes = 4 × 8
#        = 32 bytes
#
# Output:
#
# 32


# ============================================================
# 23. IMPORTANT nbytes FORMULA
# ============================================================

# Very important:
#
# nbytes = size × itemsize
#
#
# Example:
#
# size = 4
# itemsize = 8
#
# nbytes = 4 × 8
#        = 32 bytes


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


# Expected output for a common int64 environment:
#
# Array:
# [[10 20 30]
#  [40 50 60]]
#
# Number of dimensions: 2
# Shape: (2, 3)
# Total elements: 6
# Data type: int64
# Memory per element: 8 bytes
# Total memory: 48 bytes


# ============================================================
# 25. COMPLETE EXAMPLE - DRY RUN
# ============================================================

# Array:
#
# [[10 20 30]
#  [40 50 60]]
#
#
# STEP 1 - ndim
#
# Rows + columns
#
# ndim = 2
#
#
# STEP 2 - shape
#
# 2 rows
# 3 columns
#
# shape = (2, 3)
#
#
# STEP 3 - size
#
# 2 × 3 = 6
#
# size = 6
#
#
# STEP 4 - dtype
#
# Values are integers.
#
# dtype = int64
#
#
# STEP 5 - itemsize
#
# int64 = 8 bytes
#
# itemsize = 8
#
#
# STEP 6 - nbytes
#
# nbytes = size × itemsize
#
# nbytes = 6 × 8
#        = 48 bytes


# ============================================================
# 26. ALL ATTRIBUTES TOGETHER
# ============================================================

# Attribute     Meaning
#
# ndim          Number of dimensions
#
# shape         Size of each dimension
#
# size          Total number of elements
#
# dtype         Data type
#
# itemsize      Bytes used by one element
#
# nbytes        Total bytes used


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


# Expected output in a common int64 environment:
#
# Dimensions: 2
# Shape: (3, 3)
# Total marks: 9
# Data type: int64
# Memory per value: 8 bytes
# Total memory: 72 bytes
#
#
# Why?
#
# 3 students
# × 3 subjects
# = 9 values
#
# 9 × 8 bytes
# = 72 bytes


# ============================================================
# 28. ATTRIBUTE vs METHOD
# ============================================================

# VERY IMPORTANT CONCEPT
#
# Some NumPy operations are ATTRIBUTES.
#
# Some are METHODS.
#
#
# ATTRIBUTES:
#
# arr.shape
# arr.size
# arr.ndim
# arr.dtype
# arr.itemsize
# arr.nbytes
#
# No parentheses are used.
#
#
# METHODS:
#
# arr.reshape()
# arr.flatten()
#
# Parentheses are used.


# ============================================================
# 29. COMMON MISTAKE - shape()
# ============================================================

# WRONG:
#
# arr.shape()
#
# Why?
#
# shape is an ATTRIBUTE.
#
#
# CORRECT:
#
# arr.shape


# ============================================================
# 30. COMMON MISTAKE - ndim()
# ============================================================

# WRONG:
#
# arr.ndim()
#
# CORRECT:
#
# arr.ndim
#
#
# ndim is an ATTRIBUTE.


# ============================================================
# 31. COMMON MISTAKE - size()
# ============================================================

# WRONG:
#
# arr.size()
#
# CORRECT:
#
# arr.size
#
#
# size is an ATTRIBUTE.


# ============================================================
# 32. COMMON MISTAKE - dtype()
# ============================================================

# WRONG:
#
# arr.dtype()
#
# CORRECT:
#
# arr.dtype
#
#
# dtype is an ATTRIBUTE.


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
# 34. EASY MEMORY TRICK
# ============================================================

# Property / Information
# → Usually access directly
#
# arr.shape
# arr.size
# arr.ndim
# arr.dtype
#
#
# Action / Operation
# → Usually call with ()
#
# arr.reshape()
# arr.flatten()
#
#
# Easy idea:
#
# ATTRIBUTE → "Tell me something"
#
# METHOD → "Do something"


# ============================================================
# 35. PRACTICE QUESTION
# ============================================================

# Given:

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# Before running, predict:
#
# ndim  = ?
# shape = ?
# size  = ?
#
#
# Hint:
#
# 3 rows
# 4 columns


print("\nPractice Array:")
print(arr)

print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)
print("itemsize:", arr.itemsize)
print("nbytes:", arr.nbytes)


# Expected:
#
# ndim = 2
#
# shape = (3, 4)
#
# size = 3 × 4
#      = 12
#
# If dtype is int64:
#
# itemsize = 8
#
# nbytes = 12 × 8
#        = 96 bytes


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


# Expected in a common int64 environment:
#
# ndim:
# 2
#
# shape:
# (4, 2)
#
# size:
# 8
#
# dtype:
# int64
#
# itemsize:
# 8
#
# nbytes:
# 64


# ============================================================
# 37. CHAPTER 3 SUMMARY
# ============================================================

# NumPy Array
#      |
#      +-------------------------------+
#      |                               |
#     ndim                           shape
#      |                               |
# Dimensions                     Structure
#      |                               |
#      2                            (2, 3)
#
#
#      +-------------------------------+
#      |
#     size
#      |
# Total elements
#      |
#      6
#
#
#      +-------------------------------+
#      |
#     dtype
#      |
# Data type
#      |
# int64
#
#
#      +-------------------------------+
#      |
#   itemsize
#      |
# Bytes per element
#      |
# 8 bytes
#
#
#      +-------------------------------+
#      |
#    nbytes
#      |
# Total memory
#      |
# 48 bytes


# ============================================================
# 38. MUST REMEMBER
# ============================================================

# ndim
# → How many dimensions?
#
# shape
# → What is the structure?
#
# size
# → How many total values?
#
# dtype
# → What type of values?
#
# itemsize
# → How many bytes per value?
#
# nbytes
# → How many total bytes?


# ============================================================
# 39. QUICK REVISION
# ============================================================

# Example:
#
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
#
#
# ndim:
# 2
#
# shape:
# (2, 3)
#
# size:
# 6
#
# dtype:
# int64   # commonly
#
# itemsize:
# 8 bytes # for int64
#
# nbytes:
# 48 bytes
#
#
# Formula:
#
# nbytes = size × itemsize
#
#        = 6 × 8
#
#        = 48 bytes


# ============================================================
# 40. CHAPTER 3 QUIZ
# ============================================================

# QUESTION 1
#
# What does ndim represent?
#
# A. Number of elements
# B. Number of dimensions
# C. Data type
# D. Memory size
#
# Answer:
# B. Number of dimensions


# QUESTION 2
#
# If:
#
# arr.shape
#
# returns:
#
# (5, 4)
#
# How many total elements?
#
# Answer:
#
# 5 × 4 = 20


# QUESTION 3
#
# Which attribute gives the data type?
#
# A. type
# B. dtype
# C. datatype()
# D. data
#
# Answer:
# B. dtype


# QUESTION 4
#
# What does itemsize represent?
#
# Answer:
#
# Number of bytes used by ONE element.


# QUESTION 5
#
# If:
#
# size = 20
# itemsize = 8
#
# Calculate nbytes.
#
# Formula:
#
# nbytes = size × itemsize
#
# nbytes = 20 × 8
#        = 160 bytes


# QUESTION 6
#
# Which is correct?
#
# A. arr.shape()
# B. arr.shape
#
# Answer:
# B. arr.shape
#
# Because shape is an attribute.


# QUESTION 7
#
# What is the difference between
# an attribute and a method?
#
# Attribute:
# Gives information/property.
#
# Example:
# arr.shape
#
# Method:
# Performs an action.
#
# Example:
# arr.reshape()


# ============================================================
# 41. FINAL MEMORY MAP
# ============================================================

#                NUMPY ARRAY
#                     |
#                     ↓
#                  ndim
#                     |
#             How many dimensions?
#                     |
#                     ↓
#                  shape
#                     |
#              What structure?
#                     |
#                     ↓
#                   size
#                     |
#             How many values?
#                     |
#                     ↓
#                  dtype
#                     |
#               What data type?
#                     |
#                     ↓
#                itemsize
#                     |
#             Bytes per value
#                     |
#                     ↓
#                  nbytes
#                     |
#               Total bytes


# ============================================================
# 42. CHAPTER 3 CHECKLIST
# ============================================================

# Make sure you understand:
#
# ☑ ndim
# ☑ shape
# ☑ size
# ☑ dtype
# ☑ itemsize
# ☑ nbytes
# ☑ ndim vs shape
# ☑ shape vs size
# ☑ itemsize vs nbytes
# ☑ Attribute vs method
# ☑ Memory calculation
# ☑ nbytes = size × itemsize
# ☑ Common mistakes
# ☑ Real-world example
# ☑ Practice questions
# ☑ Mini exercise
# ☑ Interview questions
# ☑ Quiz


# ============================================================
# CHAPTER 3 - COMPLETE
# ============================================================

# NEXT CHAPTER:
#
# Chapter 4 - NumPy Indexing
#
# Topics:
#
# 1. 1D indexing
# 2. Positive indexing
# 3. Negative indexing
# 4. 2D indexing
# 5. Row selection
# 6. Column selection
# 7. Complete rows
# 8. Complete columns
# 9. 3D indexing
# 10. Visual dry runs