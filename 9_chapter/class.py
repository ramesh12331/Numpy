# ============================================================
# 🚀 NUMPY COMPLETE COURSE
# CHAPTER 9 - RESHAPING ARRAYS
# ============================================================
#
# Goal:
# Learn how to change the structure/dimensions of a NumPy
# array without changing the actual data.
#
# Topics:
#   1. What is Reshaping?
#   2. reshape()
#   3. Reshape 1D -> 2D
#   4. Reshape 1D -> 3D
#   5. Reshape rules
#   6. Reshape errors
#   7. -1 in reshape()
#   8. flatten()
#   9. ravel()
#   10. flatten() vs ravel()
#   11. transpose()
#   12. .T
#   13. Shape changes
#   14. resize()
#   15. reshape() vs resize()
#   16. Real-world examples
#   17. Practice
#   18. Mini coding exercise
#   19. Interview questions
#
# ============================================================


import numpy as np


# ============================================================
# 1. WHAT IS RESHAPING?
# ============================================================
#
# Reshaping means:
#
# Changing the SHAPE/STRUCTURE of an array
# without changing its DATA.
#
# Example:
#
# Original:
#
# [1 2 3 4 5 6]
#
# We can reshape it into:
#
# 2 x 3
#
# [[1 2 3]
#  [4 5 6]]
#
# Notice:
#
# The values are still:
#
# 1 2 3 4 5 6
#
# Only their arrangement changed.
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:")
print(arr)

# Output:
# [1 2 3 4 5 6]


# ============================================================
# 2. IMPORTANT RESHAPE RULE
# ============================================================
#
# The TOTAL NUMBER OF ELEMENTS must remain the same.
#
# Our array:
#
# [1 2 3 4 5 6]
#
# has:
#
# 6 elements.
#
# Therefore possible shapes include:
#
# 2 x 3 = 6       ✅
# 3 x 2 = 6       ✅
# 1 x 6 = 6       ✅
# 6 x 1 = 6       ✅
#
# But:
#
# 2 x 4 = 8       ❌
#
# because we only have 6 elements.
#
# ============================================================


# ============================================================
# 3. reshape()
# ============================================================
#
# Definition:
#
# reshape() changes the shape of an array while keeping
# the same elements.
#
# Syntax:
#
# array.reshape(rows, columns)
#
# OR:
#
# array.reshape((rows, columns))
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print("\nReshaped array:")
print(new_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]


# ============================================================
# 4. RESHAPE - DRY RUN
# ============================================================
#
# Original:
#
# [1 2 3 4 5 6]
#
# Number of elements:
#
# 6
#
# Requested shape:
#
# 2 x 3
#
# Calculate:
#
# 2 x 3 = 6
#
# Original size = 6
# New size      = 6
#
# Therefore reshape is possible.
#
# Result:
#
# 1  2  3
# 4  5  6
#
# ============================================================


# ============================================================
# 5. CHECK ORIGINAL AND NEW SHAPE
# ============================================================


arr = np.array([10, 20, 30, 40, 50, 60])

print("\nOriginal array:")
print(arr)

print("\nOriginal shape:")
print(arr.shape)

new_arr = arr.reshape(2, 3)

print("\nNew array:")
print(new_arr)

print("\nNew shape:")
print(new_arr.shape)

# Output:
#
# Original shape:
# (6,)
#
# New shape:
# (2, 3)


# ============================================================
# 6. RESHAPE 1D -> 3D
# ============================================================
#
# We can also create more dimensions.
#
# Example:
#
# 8 elements
#
# reshape(2, 2, 2)
#
# Because:
#
# 2 x 2 x 2 = 8
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2, 2, 2)

print("\n1D to 3D:")
print(new_arr)

print("\nShape:")
print(new_arr.shape)

# Output:
#
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
#
# Shape:
# (2, 2, 2)


# ============================================================
# 7. UNDERSTANDING 3D RESHAPE
# ============================================================
#
# Shape:
#
# (2, 2, 2)
#
# means:
#
# 2 layers
# 2 rows per layer
# 2 columns per row
#
# Visual:
#
# Layer 0:
#
# 1  2
# 3  4
#
#
# Layer 1:
#
# 5  6
# 7  8
#
# ============================================================


# ============================================================
# 8. RESHAPE WITHOUT CHANGING DATA
# ============================================================
#
# Original:
#
# [10 20 30 40 50 60]
#
# Reshape:
#
# 3 x 2
#
# Result:
#
# [[10 20]
#  [30 40]
#  [50 60]]
#
# The actual values did not change.
#
# Only the structure changed.
#
# ============================================================


arr = np.array([10, 20, 30, 40, 50, 60])

print("\nOriginal:")
print(arr)

print("\nReshaped:")
print(arr.reshape(3, 2))


# ============================================================
# 9. RESHAPE ERROR
# ============================================================
#
# Suppose:
#
# arr = [1 2 3 4 5 6]
#
# Size = 6
#
# Now:
#
# arr.reshape(2, 4)
#
# requires:
#
# 2 x 4 = 8
#
# But original size is only:
#
# 6
#
# Therefore NumPy raises:
#
# ValueError
#
# ============================================================


# The following code intentionally causes an error.
# Uncomment it to see the ValueError.
#
# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr.reshape(2, 4))


# ============================================================
# 10. RESHAPE GOLDEN RULE
# ============================================================
#
# Always remember:
#
# ORIGINAL SIZE = NEW SHAPE PRODUCT
#
# Example:
#
# 12 elements
#
# reshape(3, 4)
#
# 3 x 4 = 12
# ✅ Valid
#
#
# 12 elements
#
# reshape(5, 3)
#
# 5 x 3 = 15
# ❌ Invalid
#
# ============================================================


# ============================================================
# 11. -1 IN reshape()
# ============================================================
#
# -1 is a very useful NumPy feature.
#
# It means:
#
# "NumPy, calculate this dimension for me."
#
# Example:
#
# arr.reshape(2, -1)
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, -1)

print("\nreshape(2, -1):")
print(new_arr)

print("\nShape:")
print(new_arr.shape)

# Output:
#
# [[1 2 3]
#  [4 5 6]]
#
# Shape:
# (2, 3)


# ============================================================
# 12. HOW DOES -1 WORK?
# ============================================================
#
# Original size:
#
# 6
#
# We specify:
#
# 2 rows
#
# NumPy calculates:
#
# 6 / 2 = 3
#
# Therefore:
#
# reshape(2, -1)
#
# becomes:
#
# reshape(2, 3)
#
# ============================================================


# ============================================================
# 13. ANOTHER -1 EXAMPLE
# ============================================================
#
# np.arange(12)
#
# creates:
#
# [0 1 2 3 4 5 6 7 8 9 10 11]
#
# Total elements = 12
#
# reshape(3, -1)
#
# NumPy calculates:
#
# 12 / 3 = 4
#
# Therefore:
#
# reshape(3, 4)
#
# ============================================================


arr = np.arange(12)

print("\nOriginal:")
print(arr)

new_arr = arr.reshape(3, -1)

print("\nreshape(3, -1):")
print(new_arr)

# Output:
#
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]


# ============================================================
# 14. -1 MEMORY TRICK
# ============================================================
#
# -1 means:
#
# "NumPy, calculate this dimension for me."
#
# Example:
#
# reshape(2, -1)
# -> NumPy calculates columns
#
# reshape(3, -1)
# -> NumPy calculates columns
#
# ============================================================


# ============================================================
# 15. ONLY ONE -1
# ============================================================
#
# You should use only ONE -1.
#
# Correct:
#
# reshape(2, -1)
#
# Correct:
#
# reshape(-1, 3)
#
# Wrong:
#
# reshape(-1, -1)
#
# Why?
#
# NumPy cannot determine both dimensions automatically.
#
# ============================================================


# ============================================================
# 16. flatten()
# ============================================================
#
# Definition:
#
# flatten() converts a multi-dimensional array
# into a 1D array.
#
# Example:
#
# Before:
#
# [[1 2 3]
#  [4 5 6]]
#
# After flatten():
#
# [1 2 3 4 5 6]
#
# ============================================================


arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal 2D array:")
print(arr)

result = arr.flatten()

print("\nAfter flatten():")
print(result)

# Output:
# [1 2 3 4 5 6]


# ============================================================
# 17. flatten() VISUAL
# ============================================================
#
# Before:
#
# 1  2  3
# 4  5  6
#
#       ↓
#    flatten()
#       ↓
#
# [1 2 3 4 5 6]
#
# ============================================================


# ============================================================
# 18. flatten() WITH 3D ARRAY
# ============================================================
#
# A 3D array can also be flattened.
#
# 3D
#  ↓
# 2D
#  ↓
# 1D
#
# ============================================================


arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D array:")
print(arr)

print("\nFlattened 3D array:")
print(arr.flatten())

# Output:
# [1 2 3 4 5 6 7 8]


# ============================================================
# 19. ravel()
# ============================================================
#
# Definition:
#
# ravel() also converts an array into a 1D array.
#
# Example:
#
# [[1 2 3]
#  [4 5 6]]
#
# becomes:
#
# [1 2 3 4 5 6]
#
# ============================================================


arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = arr.ravel()

print("\nAfter ravel():")
print(result)

# Output:
# [1 2 3 4 5 6]


# ============================================================
# 20. flatten() vs ravel()
# ============================================================
#
# Both:
#
# flatten()
# ravel()
#
# can convert an array into 1D.
#
# Main difference:
#
# flatten()
# -> generally creates a COPY
#
# ravel()
# -> usually tries to return a VIEW when possible
#
# Therefore:
#
# flatten -> more memory usage
# ravel   -> can be more memory efficient
#
# We will study COPY vs VIEW in Chapter 13.
#
# ============================================================


# ============================================================
# 21. BEGINNER MEMORY TRICK
# ============================================================
#
# flatten
#     ↓
# flat + independent copy
#
# ravel
#     ↓
# flatten-like + view possible
#
# ============================================================


# ============================================================
# 22. transpose()
# ============================================================
#
# Definition:
#
# Transpose changes:
#
# rows -> columns
# columns -> rows
#
# Example:
#
# Original:
#
# 1  2  3
# 4  5  6
#
# After transpose:
#
# 1  4
# 2  5
# 3  6
#
# ============================================================


arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal array:")
print(arr)

transposed = np.transpose(arr)

print("\nTransposed array:")
print(transposed)

# Output:
#
# [[1 4]
#  [2 5]
#  [3 6]]


# ============================================================
# 23. TRANSPOSE SHAPE
# ============================================================
#
# Original shape:
#
# (2, 3)
#
# After transpose:
#
# (3, 2)
#
# Therefore:
#
# (2, 3) -> (3, 2)
#
# ============================================================


print("\nOriginal shape:")
print(arr.shape)

print("\nTransposed shape:")
print(transposed.shape)

# Output:
#
# Original shape:
# (2, 3)
#
# Transposed shape:
# (3, 2)


# ============================================================
# 24. arr.transpose()
# ============================================================
#
# We can also use the array method:
#
# arr.transpose()
#
# ============================================================


print("\nUsing arr.transpose():")
print(arr.transpose())


# ============================================================
# 25. .T SHORTCUT
# ============================================================
#
# NumPy provides a convenient shortcut:
#
# arr.T
#
# It performs transpose.
#
# ============================================================


print("\nUsing .T:")
print(arr.T)

# Output:
#
# [[1 4]
#  [2 5]
#  [3 6]]


# ============================================================
# 26. TRANSPOSE METHODS
# ============================================================
#
# Three common ways:
#
# 1. np.transpose(arr)
#
# 2. arr.transpose()
#
# 3. arr.T
#
# For a 2D array, they produce the same transpose.
#
# ============================================================


print("\nnp.transpose(arr):")
print(np.transpose(arr))

print("\narr.transpose():")
print(arr.transpose())

print("\narr.T:")
print(arr.T)


# ============================================================
# 27. SHAPE CHANGES
# ============================================================
#
# Suppose:
#
# arr = np.arange(12)
#
# Shape:
#
# (12,)
#
# We can reshape into:
#
# (3, 4)
# (2, 6)
# (4, 3)
# (2, 2, 3)
#
# because all contain 12 elements.
#
# ============================================================


arr = np.arange(12)

print("\nOriginal:")
print(arr)

print("\nShape:")
print(arr.shape)

print("\n3 x 4:")
print(arr.reshape(3, 4))

print("\n2 x 6:")
print(arr.reshape(2, 6))

print("\n4 x 3:")
print(arr.reshape(4, 3))

print("\n2 x 2 x 3:")
print(arr.reshape(2, 2, 3))


# ============================================================
# 28. VERIFY THE SHAPES
# ============================================================


arr = np.arange(12)

shape_1 = arr.reshape(3, 4)
shape_2 = arr.reshape(2, 6)
shape_3 = arr.reshape(4, 3)
shape_4 = arr.reshape(2, 2, 3)

print("\nShapes:")
print(shape_1.shape)
print(shape_2.shape)
print(shape_3.shape)
print(shape_4.shape)

# Output:
#
# (3, 4)
# (2, 6)
# (4, 3)
# (2, 2, 3)


# ============================================================
# 29. resize()
# ============================================================
#
# Definition:
#
# resize() changes the shape of an array and CAN change
# the total number of elements.
#
# This is an important difference from reshape().
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6])

arr.resize(2, 3)

print("\nAfter resize(2, 3):")
print(arr)

# Output:
#
# [[1 2 3]
#  [4 5 6]]


# ============================================================
# 30. IMPORTANT: resize() MODIFIES ORIGINAL ARRAY
# ============================================================
#
# With reshape():
#
# new_arr = arr.reshape(2, 3)
#
# the original arr is not automatically replaced.
#
# With resize():
#
# arr.resize(2, 3)
#
# the original arr itself is modified.
#
# ============================================================


# ============================================================
# 31. resize() CAN CHANGE SIZE
# ============================================================
#
# Original:
#
# [1 2 3 4]
#
# Size = 4
#
# Now:
#
# arr.resize(2, 3)
#
# Requested size:
#
# 2 x 3 = 6
#
# Original size:
#
# 4
#
# NumPy needs 2 additional elements.
#
# For this numeric array, additional positions are filled
# with zeros.
#
# Result:
#
# [[1 2 3]
#  [4 0 0]]
#
# ============================================================


arr = np.array([1, 2, 3, 4])

arr.resize(2, 3)

print("\nresize() with larger size:")
print(arr)

# Output:
#
# [[1 2 3]
#  [4 0 0]]


# ============================================================
# 32. reshape() vs resize()
# ============================================================
#
# reshape()
# ------------------------------------------------------------
# Changes shape              -> YES
# Changes original directly  -> NO
# Must preserve size         -> YES
# Can change total size      -> NO
#
#
# resize()
# ------------------------------------------------------------
# Changes shape              -> YES
# Changes original directly  -> YES
# Must preserve size         -> NO
# Can change total size      -> YES
#
# ============================================================


# ============================================================
# 33. IMPORTANT reshape() EXAMPLE
# ============================================================
#
# Notice:
#
# arr.reshape(2, 3)
#
# alone does NOT replace arr.
#
# Example:
#
# arr = np.array([1,2,3,4,5,6])
#
# arr.reshape(2,3)
#
# print(arr)
#
# Original arr is still 1D.
#
# If we want to store the result:
#
# arr = arr.reshape(2,3)
#
# OR:
#
# new_arr = arr.reshape(2,3)
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 3)

print("\nOriginal remains unchanged after unused reshape:")
print(arr)

# Output:
# [1 2 3 4 5 6]


# Correct approach:
arr = arr.reshape(2, 3)

print("\nAfter assigning reshape result:")
print(arr)

# Output:
#
# [[1 2 3]
#  [4 5 6]]


# ============================================================
# 34. np.resize() NOTE
# ============================================================
#
# There is also:
#
# np.resize()
#
# This is different from:
#
# arr.resize()
#
# For beginner learning, first remember:
#
# arr.resize(...)
#
# because it modifies the original array and can change
# its size.
#
# ============================================================


# ============================================================
# 35. COMPLETE EXAMPLE
# ============================================================
#
# Let's use:
#
# reshape()
# reshape(-1)
# flatten()
# ravel()
# transpose()
# .T
#
# ============================================================


arr = np.array([1, 2, 3, 4, 5, 6])

print("\n================ COMPLETE EXAMPLE ================")

print("Original:")
print(arr)

print("\nReshape:")
print(arr.reshape(2, 3))

print("\nReshape with -1:")
print(arr.reshape(3, -1))

matrix = arr.reshape(2, 3)

print("\n2D array:")
print(matrix)

print("\nFlatten:")
print(matrix.flatten())

print("\nRavel:")
print(matrix.ravel())

print("\nTranspose:")
print(matrix.T)


# ============================================================
# 36. REAL-WORLD EXAMPLE - IMAGE DATA
# ============================================================
#
# Images are commonly represented as arrays.
#
# A grayscale image can be represented as:
#
# Height x Width
#
# Example:
#
# 28 x 28
#
# Number of pixels:
#
# 28 x 28 = 784
#
# So we can have:
#
# 1D pixel data
#       ↓
#    reshape
#       ↓
# 28 x 28 image matrix
#
# ============================================================


image = np.arange(784)

print("\nImage data:")
print(image)

print("\nOriginal image shape:")
print(image.shape)

image_2d = image.reshape(28, 28)

print("\n28 x 28 image shape:")
print(image_2d.shape)

# Output:
#
# Original image shape:
# (784,)
#
# 28 x 28 image shape:
# (28, 28)


# ============================================================
# 37. WHY IMAGE RESHAPING IS IMPORTANT
# ============================================================
#
# A machine-learning model may receive pixel data in a
# particular shape.
#
# Example:
#
# 784 pixel values
#
# can be represented as:
#
# (784,)
#
# or:
#
# (28, 28)
#
# Reshaping allows us to change the representation
# while keeping the same pixel values.
#
# ============================================================


# ============================================================
# 38. REAL-WORLD EXAMPLE - STUDENT DATASET
# ============================================================
#
# Suppose:
#
# 3 students
# 3 subjects
#
# Total values:
#
# 3 x 3 = 9
#
# ============================================================


marks = np.array([
    80, 75, 90,
    65, 88, 70,
    92, 85, 95
])

print("\nStudent marks in 1D:")
print(marks)

print("\nNumber of values:")
print(marks.size)


# ============================================================
# 39. RESHAPE STUDENT DATA
# ============================================================
#
# 9 values
#
# 3 students
# 3 subjects
#
# Therefore:
#
# reshape(3, 3)
#
# ============================================================


marks = marks.reshape(3, 3)

print("\nStudent marks in 3 x 3 form:")
print(marks)

# Output:
#
# [[80 75 90]
#  [65 88 70]
#  [92 85 95]]


# ============================================================
# 40. UNDERSTAND THE STUDENT DATA
# ============================================================
#
# Rows:
#     Students
#
# Columns:
#     Subjects
#
# Therefore:
#
# Row 0 -> Student 1
# Row 1 -> Student 2
# Row 2 -> Student 3
#
# Column 0 -> Subject 1
# Column 1 -> Subject 2
# Column 2 -> Subject 3
#
# This type of structure is very common in Data Science.
#
# ============================================================


# ============================================================
# 41. COMMON MISTAKE - WRONG NUMBER OF ELEMENTS
# ============================================================
#
# Example:
#
# arr = [1,2,3,4,5,6]
#
# arr.reshape(2,4)
#
# Why wrong?
#
# Original:
# 6 elements
#
# Requested:
# 2 x 4 = 8
#
# 6 != 8
#
# Therefore:
#
# ValueError
#
# ============================================================


# ============================================================
# 42. COMMON MISTAKE - FORGETTING TO STORE RESULT
# ============================================================
#
# Wrong:
#
# arr.reshape(2,3)
# print(arr)
#
# The original array is still unchanged.
#
#
# Correct:
#
# arr = arr.reshape(2,3)
#
# OR:
#
# new_arr = arr.reshape(2,3)
#
# ============================================================


# ============================================================
# 43. COMMON MISTAKE - TWO -1 VALUES
# ============================================================
#
# Wrong:
#
# arr.reshape(-1, -1)
#
# NumPy cannot calculate both dimensions.
#
# Correct:
#
# arr.reshape(2, -1)
#
# OR:
#
# arr.reshape(-1, 2)
#
# ============================================================


# ============================================================
# 44. COMMON MISTAKE - flatten() vs reshape(-1)
# ============================================================
#
# Both can produce a 1D representation:
#
# arr.flatten()
#
# arr.reshape(-1)
#
# But their memory/view behavior can differ.
#
# flatten() generally creates a copy.
#
# reshape(-1) may return a view when possible.
#
# Memory behavior will be studied in Chapter 13.
#
# ============================================================


# ============================================================
# 45. INTERVIEW QUESTIONS
# ============================================================
#
# Q1. What is reshaping?
#
# Answer:
# Changing the shape/structure of an array without changing
# its data.
#
#
# Q2. What is the main rule of reshape()?
#
# Answer:
# The total number of elements must remain the same.
#
# old size = new shape product
#
#
# Q3. What does -1 mean in reshape()?
#
# Answer:
# NumPy automatically calculates that dimension.
#
#
# Q4. What does flatten() do?
#
# Answer:
# Converts an array into a 1D array and generally creates
# a copy.
#
#
# Q5. What does ravel() do?
#
# Answer:
# Converts an array into a 1D array and generally tries
# to return a view when possible.
#
#
# Q6. What does transpose do?
#
# Answer:
# It swaps axes.
#
# For a 2D array:
#
# rows become columns
# columns become rows
#
#
# Q7. What is .T?
#
# Answer:
# A convenient transpose attribute.
#
# Example:
#
# arr.T
#
#
# Q8. Difference between reshape() and resize()?
#
# Answer:
#
# reshape()
# -> shape changes
# -> size must stay the same
#
# resize()
# -> shape can change
# -> size can also change
#
# ============================================================


# ============================================================
# 46. PRACTICE PROGRAM
# ============================================================
#
# Run this complete program in VS Code.
#
# ============================================================


arr = np.arange(12)

print("\n================ PRACTICE PROGRAM ================")

print("Original:")
print(arr)

print("\nOriginal shape:")
print(arr.shape)

matrix = arr.reshape(3, 4)

print("\n3 x 4:")
print(matrix)

print("\nShape:")
print(matrix.shape)

print("\nTranspose:")
print(matrix.T)

print("\nFlatten:")
print(matrix.flatten())

print("\nRavel:")
print(matrix.ravel())


# ============================================================
# 47. MINI CODING EXERCISE
# ============================================================
#
# Create:
#
# numbers = np.arange(1, 13)
#
# This creates:
#
# [1 2 3 4 5 6 7 8 9 10 11 12]
#
# Total = 12 elements
#
# ============================================================


numbers = np.arange(1, 13)

print("\n================ MINI EXERCISE ================")

print("Numbers:")
print(numbers)


# ============================================================
# EXERCISE 1
# ============================================================
# Reshape into 3 x 4.
# ============================================================


result_1 = numbers.reshape(3, 4)

print("\n1. 3 x 4:")
print(result_1)


# ============================================================
# EXERCISE 2
# ============================================================
# Reshape into 4 x 3.
# ============================================================


result_2 = numbers.reshape(4, 3)

print("\n2. 4 x 3:")
print(result_2)


# ============================================================
# EXERCISE 3
# ============================================================
# Reshape into 2 x 2 x 3.
#
# Check:
#
# 2 x 2 x 3 = 12
# ============================================================


result_3 = numbers.reshape(2, 2, 3)

print("\n3. 2 x 2 x 3:")
print(result_3)


# ============================================================
# EXERCISE 4
# ============================================================
# Use -1 to create 3 x 4.
#
# Hint:
#
# numbers.reshape(3, -1)
# ============================================================


result_4 = numbers.reshape(3, -1)

print("\n4. Using -1:")
print(result_4)


# ============================================================
# EXERCISE 5
# ============================================================
# Convert the 3 x 4 array into 1D using flatten().
# ============================================================


result_5 = result_1.flatten()

print("\n5. flatten():")
print(result_5)


# ============================================================
# EXERCISE 6
# ============================================================
# Convert the 3 x 4 array into 1D using ravel().
# ============================================================


result_6 = result_1.ravel()

print("\n6. ravel():")
print(result_6)


# ============================================================
# EXERCISE 7
# ============================================================
# Transpose the 3 x 4 array.
# ============================================================


result_7 = result_1.T

print("\n7. Transpose:")
print(result_7)


# ============================================================
# EXERCISE 8
# ============================================================
# Check the shape after transpose.
#
# Original:
# (3, 4)
#
# After transpose:
# (4, 3)
# ============================================================


print("\n8. Shape after transpose:")
print(result_7.shape)

# Output:
# (4, 3)


# ============================================================
# 48. MINI EXERCISE - EXPECTED RESULTS
# ============================================================
#
# numbers:
#
# [1 2 3 4 5 6 7 8 9 10 11 12]
#
# ------------------------------------------------------------
# 3 x 4:
#
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
#
# ------------------------------------------------------------
# 4 x 3:
#
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
#
# ------------------------------------------------------------
# 2 x 2 x 3:
#
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
#
# ------------------------------------------------------------
# flatten():
#
# [1 2 3 4 5 6 7 8 9 10 11 12]
#
# ------------------------------------------------------------
# ravel():
#
# [1 2 3 4 5 6 7 8 9 10 11 12]
#
# ------------------------------------------------------------
# transpose of 3 x 4:
#
# [[ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]]
#
# Shape:
#
# (4, 3)
#
# ============================================================


# ============================================================
# 49. CHAPTER 9 QUICK SUMMARY
# ============================================================
#
# reshape()
#     -> Change shape while preserving number of elements
#
# -1
#     -> NumPy automatically calculates one dimension
#
# flatten()
#     -> Convert to 1D
#     -> Generally creates a copy
#
# ravel()
#     -> Convert to 1D
#     -> May return a view
#
# transpose()
#     -> Swap axes
#
# .T
#     -> Shortcut for transpose
#
# resize()
#     -> Change shape
#     -> Can change total number of elements
#
# ============================================================


# ============================================================
# 50. FINAL REVISION MAP
# ============================================================
#
#                    ARRAY RESHAPING
#                           |
#          -----------------+-----------------
#          |                |                |
#          ↓                ↓                ↓
#      reshape()         flatten()         ravel()
#          |                |                |
#    change shape         -> 1D            -> 1D
#    same size            copy generally   view possible
#          |
#          ↓
#         -1
#          |
#          ↓
#    NumPy calculates
#       dimension
#
#
#                  2D ARRAY
#                      |
#                      ↓
#                transpose / .T
#                      |
#                      ↓
#                 rows <-> columns
#
#
# resize()
#     ↓
# can change shape AND size
#
# ============================================================


# ============================================================
# 51. MUST REMEMBER
# ============================================================
#
# reshape() -> change structure
#
# flatten() -> make 1D copy
#
# ravel()   -> make 1D, view possible
#
# .T        -> transpose
#
# resize()  -> can change size
#
# -1        -> NumPy calculates dimension
#
# ============================================================


# ============================================================
# 52. CHAPTER 9 QUIZ
# ============================================================
#
# Try to answer WITHOUT looking at the answers.
#
# 1. What is reshaping?
#
# 2. What is the main rule of reshape()?
#
# 3. Can an array of 12 elements be reshaped to (3, 4)?
#
# 4. Can an array of 12 elements be reshaped to (5, 3)?
#
# 5. What does -1 mean in reshape()?
#
# 6. What does flatten() do?
#
# 7. What is the main difference between flatten() and ravel()?
#
# 8. What does .T do?
#
# 9. What happens to a (2, 3) array after transpose?
#
# 10. What is the difference between reshape() and resize()?
#
# ============================================================


# ============================================================
# 53. QUIZ ANSWERS
# ============================================================
#
# 1. Reshaping changes the structure/shape without changing
#    the data.
#
# 2. Total number of elements must remain the same.
#
# 3. YES
#
#    3 x 4 = 12
#
# 4. NO
#
#    5 x 3 = 15
#
# 5. -1 tells NumPy to automatically calculate that dimension.
#
# 6. Converts an array into 1D and generally creates a copy.
#
# 7. Both convert to 1D, but flatten generally creates a copy
#    while ravel may return a view when possible.
#
# 8. .T performs transpose.
#
# 9. (2, 3) becomes (3, 2).
#
# 10. reshape() must preserve total size, while resize() can
#     change both shape and size.
#
# ============================================================


# ============================================================
# 🎯 CHAPTER 9 COMPLETE
# ============================================================
#
# You have now learned:
#
# [x] Reshaping
# [x] reshape()
# [x] 1D -> 2D
# [x] 1D -> 3D
# [x] Reshape size rule
# [x] Reshape ValueError
# [x] -1 in reshape()
# [x] flatten()
# [x] ravel()
# [x] flatten vs ravel
# [x] transpose()
# [x] .T
# [x] Shape changes
# [x] resize()
# [x] reshape vs resize
# [x] Image data example
# [x] Student dataset example
#
# ============================================================
#
# NEXT:
#
# 🚀 CHAPTER 10 - JOINING ARRAYS
#
# Topics:
#
#   np.concatenate()
#   np.vstack()
#   np.hstack()
#   np.stack()
#   np.dstack()
#
# We will understand:
#
#   - Joining arrays
#   - Row-wise joining
#   - Column-wise joining
#   - Axis in joining
#   - Shape changes
#   - Visual diagrams
#   - Difference between concatenate/vstack/hstack/stack/dstack
#
# ============================================================