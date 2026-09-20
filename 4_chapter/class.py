# ============================================================
# NUMPY COMPLETE COURSE
# CHAPTER 4 - INDEXING
# VS CODE NOTES WITH COMMENTED EXPLANATION
# ============================================================

import numpy as np


# ============================================================
# 1. WHAT IS INDEXING?
# ============================================================

# Indexing means accessing a specific element
# from an array using its position/index.
#
# IMPORTANT:
# NumPy indexing starts from 0.
#
# Example:
#
# Value:  10   20   30   40   50
# Index:   0    1    2    3    4
#
# Therefore:
#
# arr[0] → 10
# arr[1] → 20
# arr[2] → 30
# arr[3] → 40
# arr[4] → 50


# ============================================================
# 2. 1D ARRAY INDEXING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

print("\nIndex 0:", arr[0])
print("Index 1:", arr[1])
print("Index 2:", arr[2])
print("Index 3:", arr[3])
print("Index 4:", arr[4])

# Output:
#
# Array:
# [10 20 30 40 50]
#
# Index 0: 10
# Index 1: 20
# Index 2: 30
# Index 3: 40
# Index 4: 50


# ============================================================
# 3. HOW TO UNDERSTAND INDEXING
# ============================================================

# Think:
#
# Index = Position starting from ZERO
#
#        0    1    2    3    4
#        ↓    ↓    ↓    ↓    ↓
#       10   20   30   40   50
#
#
# arr[3]
#
# means:
#
# "Give me the value at index 3."
#
# Answer:
#
# 40


print("\nValue at index 3:")
print(arr[3])

# Output:
# 40


# ============================================================
# 4. POSITIVE INDEXING
# ============================================================

# Positive indexing starts from the LEFT side.
#
#        0    1    2    3    4
#        ↓    ↓    ↓    ↓    ↓
#       10   20   30   40   50
#
#
# Examples:

print("\nPositive Indexing:")

print("arr[0]:", arr[0])
print("arr[2]:", arr[2])
print("arr[4]:", arr[4])

# Output:
#
# arr[0]: 10
# arr[2]: 30
# arr[4]: 50


# ============================================================
# 5. NEGATIVE INDEXING
# ============================================================

# Negative indexing starts from the RIGHT side.
#
#        -5   -4   -3   -2   -1
#         ↓    ↓    ↓    ↓    ↓
#        10   20   30   40   50
#
#
# -1 → Last element
# -2 → Second-last element
# -3 → Third-last element


print("\nNegative Indexing:")

print("arr[-1]:", arr[-1])
print("arr[-2]:", arr[-2])
print("arr[-3]:", arr[-3])

# Output:
#
# arr[-1]: 50
# arr[-2]: 40
# arr[-3]: 30


# ============================================================
# 6. POSITIVE vs NEGATIVE INDEXING
# ============================================================

# Positive:
#
#        0    1    2    3    4
#        ↓    ↓    ↓    ↓    ↓
#       10   20   30   40   50
#
#
# Negative:
#
#       -5   -4   -3   -2   -1
#        ↓    ↓    ↓    ↓    ↓
#       10   20   30   40   50
#
#
# Examples:
#
# arr[0]  → 10
# arr[-1] → 50
#
# arr[1]  → 20
# arr[-2] → 40


# ============================================================
# 7. 2D ARRAY INDEXING
# ============================================================

# A 2D array contains rows and columns.
#
# Example:
#
#             Column
#          0    1    2
#
#       ┌────┬────┬────┐
# Row 0 │ 10 │ 20 │ 30 │
#       ├────┼────┼────┤
# Row 1 │ 40 │ 50 │ 60 │
#       ├────┼────┼────┤
# Row 2 │ 70 │ 80 │ 90 │
#       └────┴────┴────┘


arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(arr)


# ============================================================
# 8. 2D INDEXING SYNTAX
# ============================================================

# For a 2D array:
#
# arr[row, column]
#
#
# Remember:
#
# FIRST  → Row
# SECOND → Column


# ============================================================
# 9. ACCESS A SPECIFIC ELEMENT
# ============================================================

# Suppose we want 50.
#
# 50 is located at:
#
# Row = 1
# Column = 1
#
# Therefore:
#
# arr[1, 1]

print("\nValue at row 1, column 1:")
print(arr[1, 1])

# Output:
# 50


# ============================================================
# 10. MORE 2D INDEXING EXAMPLES
# ============================================================

print("\nMore 2D Indexing:")

print("arr[0, 0]:", arr[0, 0])
print("arr[0, 2]:", arr[0, 2])
print("arr[2, 0]:", arr[2, 0])
print("arr[2, 2]:", arr[2, 2])

# Output:
#
# arr[0, 0]: 10
# arr[0, 2]: 30
# arr[2, 0]: 70
# arr[2, 2]: 90


# ============================================================
# 11. 2D INDEXING DRY RUN
# ============================================================

# Question:
#
# arr[2, 1]
#
#
# Step 1:
#
# 2 → Row 2
#
#
# Step 2:
#
# 1 → Column 1
#
#
# Array:
#
#             0    1    2
#
#       ┌────┬────┬────┐
# Row 0 │ 10 │ 20 │ 30 │
#       ├────┼────┼────┤
# Row 1 │ 40 │ 50 │ 60 │
#       ├────┼────┼────┤
# Row 2 │ 70 │ 80 │ 90 │
#       └────┴────┴────┘
#                 ↑
#              column 1
#
#
# Answer:
#
# 80


print("\nDry Run - arr[2, 1]:")
print(arr[2, 1])

# Output:
# 80


# ============================================================
# 12. ALTERNATIVE 2D SYNTAX
# ============================================================

# You can also write:
#
# arr[1][2]
#
# This means:
#
# First select row 1
# Then select column 2

print("\nAlternative syntax:")
print(arr[1][2])

# Output:
# 60
#
#
# Standard NumPy style is:
#
# arr[1, 2]


# ============================================================
# 13. SELECT A COMPLETE ROW
# ============================================================

# To select a complete row:
#
# arr[row_index]
#
#
# Example:
#
# arr[1]
#
# means:
#
# Select row 1.


print("\nComplete Row 1:")
print(arr[1])

# Output:
#
# [40 50 60]


# ============================================================
# 14. SELECT OTHER COMPLETE ROWS
# ============================================================

print("\nRow 0:")
print(arr[0])

print("\nRow 1:")
print(arr[1])

print("\nRow 2:")
print(arr[2])

# Output:
#
# Row 0:
# [10 20 30]
#
# Row 1:
# [40 50 60]
#
# Row 2:
# [70 80 90]


# ============================================================
# 15. COMPLETE ROW USING :
# ============================================================

# We can also write:
#
# arr[1, :]
#
#
# : means:
#
# "Take everything"
#
#
# arr[1, :]
#
# means:
#
# Row 1
# All columns


print("\nRow 1 using colon:")
print(arr[1, :])

# Output:
#
# [40 50 60]


# ============================================================
# 16. SELECT A COMPLETE COLUMN
# ============================================================

# To select a complete column:
#
# arr[:, column_index]
#
#
# The colon means:
#
# ALL ROWS
#
#
# Example:
#
# arr[:, 1]
#
# means:
#
# All rows
# Column 1


print("\nColumn 1:")
print(arr[:, 1])

# Output:
#
# [20 50 80]


# ============================================================
# 17. COLUMN SELECTION VISUAL
# ============================================================

# Array:
#
#             0    1    2
#
#       ┌────┬────┬────┐
# Row 0 │ 10 │ 20 │ 30 │
#       ├────┼────┼────┤
# Row 1 │ 40 │ 50 │ 60 │
#       ├────┼────┼────┤
# Row 2 │ 70 │ 80 │ 90 │
#       └────┴────┴────┘
#              ↑
#           Column 1
#
#
# Result:
#
# [20 50 80]


# ============================================================
# 18. ROW vs COLUMN
# ============================================================

# COMPLETE ROW:
#
# arr[1, :]
#
# Result:
#
# [40 50 60]
#
# Meaning:
#
# Row 1
# All columns
#
#
# COMPLETE COLUMN:
#
# arr[:, 1]
#
# Result:
#
# [20 50 80]
#
# Meaning:
#
# All rows
# Column 1


# ============================================================
# 19. MOST IMPORTANT RULE
# ============================================================

# Remember:
#
# arr[row, column]
#
#
# For ROW:
#
# arr[1, :]
#
#       ↑
#     row
#
#       :
#     all columns
#
#
# For COLUMN:
#
# arr[:, 1]
#
#       :
#     all rows
#
#       ↑
#     column
#
#
# IMPORTANT:
#
# : means ALL


# ============================================================
# 20. NEGATIVE INDEXING IN 2D
# ============================================================

# Negative indexing also works with 2D arrays.
#
# Example:
#
#             0    1    2
#
#       ┌────┬────┬────┐
#       │ 10 │ 20 │ 30 │
#       ├────┼────┼────┤
#       │ 40 │ 50 │ 60 │
#       ├────┼────┼────┤
#       │ 70 │ 80 │ 90 │
#       └────┴────┴────┘
#
#
# Negative rows:
#
# -3 → first row
# -2 → second row
# -1 → last row


print("\nLast row using negative indexing:")
print(arr[-1])

# Output:
#
# [70 80 90]


# ============================================================
# 21. NEGATIVE COLUMN INDEX
# ============================================================

# -1 means the LAST column.
#
# Therefore:
#
# arr[:, -1]
#
# means:
#
# All rows
# Last column


print("\nLast column:")
print(arr[:, -1])

# Output:
#
# [30 60 90]


# ============================================================
# 22. OTHER NEGATIVE COLUMN EXAMPLES
# ============================================================

print("\nSecond-last column:")
print(arr[:, -2])

# Output:
#
# [20 50 80]


print("\nFirst column using negative index:")
print(arr[:, -3])

# Output:
#
# [10 40 70]


# ============================================================
# 23. NEGATIVE INDEXING MEMORY TRICK
# ============================================================

# For 1D:
#
# -1 → last
# -2 → second last
# -3 → third last
#
#
# For 2D:
#
# arr[-1]
# → last row
#
# arr[:, -1]
# → last column
#
# arr[-1, -1]
# → last row + last column
# → last element


# ============================================================
# 24. LAST ELEMENT OF A 2D ARRAY
# ============================================================

print("\nLast element:")
print(arr[-1, -1])

# Output:
#
# 90


# ============================================================
# 25. FIRST ELEMENT OF A 2D ARRAY
# ============================================================

print("\nFirst element:")
print(arr[0, 0])

# Output:
#
# 10


# ============================================================
# 26. 3D ARRAY INDEXING
# ============================================================

# A 3D array can be understood as
# multiple 2D layers/tables.
#
#
# Example:
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


# ============================================================
# 27. 3D INDEXING SYNTAX
# ============================================================

# For a 3D array:
#
# arr[layer, row, column]
#
#
# Remember:
#
# FIRST  → Layer
# SECOND → Row
# THIRD  → Column


# ============================================================
# 28. GET A SPECIFIC VALUE FROM 3D
# ============================================================

# Suppose we want 6.
#
# 6 is located at:
#
# Layer = 1
# Row = 0
# Column = 1
#
#
# Therefore:
#
# arr_3d[1, 0, 1]


print("\nValue 6:")
print(arr_3d[1, 0, 1])

# Output:
#
# 6


# ============================================================
# 29. 3D INDEXING DRY RUN
# ============================================================

# Question:
#
# arr_3d[1, 0, 1]
#
#
# Step 1:
#
# 1 → Layer 1
#
#
# Step 2:
#
# 0 → Row 0
#
#
# Step 3:
#
# 1 → Column 1
#
#
# Layer 1:
#
#       0    1
#       ↓    ↓
#       5    6   ← Row 0
#       7    8   ← Row 1
#
#
# Column 1 = 6
#
# Answer:
#
# 6


# ============================================================
# 30. DIMENSIONS AND INDEXING
# ============================================================

# 1D:
#
# arr[index]
#
# Example:
#
# arr[2]
#
#
# 2D:
#
# arr[row, column]
#
# Example:
#
# arr[1, 2]
#
#
# 3D:
#
# arr[layer, row, column]
#
# Example:
#
# arr[1, 0, 1]


# ============================================================
# 31. EASY MEMORY TRICK
# ============================================================

# 1D → INDEX
#
# arr[index]
#
#
# 2D → ROW + COLUMN
#
# arr[row, column]
#
#
# 3D → LAYER + ROW + COLUMN
#
# arr[layer, row, column]


# ============================================================
# 32. REAL-WORLD EXAMPLE - STUDENT MARKS
# ============================================================

# Imagine:
#
# Rows    → Students
# Columns → Subjects
#
#
# Column 0 → Maths
# Column 1 → Science
# Column 2 → English


marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

print("\nStudent Marks:")
print(marks)


# ============================================================
# 33. GET SCIENCE MARK OF STUDENT 2
# ============================================================

# Student 2 is row 1.
#
# Science is column 1.
#
# Therefore:
#
# marks[1, 1]


print("\nScience mark of Student 2:")
print(marks[1, 1])

# Output:
#
# 88


# ============================================================
# 34. GET ALL SCIENCE MARKS
# ============================================================

# Science = column 1.
#
# All students = :
#
# Therefore:
#
# marks[:, 1]


print("\nAll Science marks:")
print(marks[:, 1])

# Output:
#
# [75 88 85]


# ============================================================
# 35. GET ALL MATHS MARKS
# ============================================================

# Maths = column 0.
#
# All students:
#
# marks[:, 0]


print("\nAll Maths marks:")
print(marks[:, 0])

# Output:
#
# [80 65 92]


# ============================================================
# 36. GET ALL ENGLISH MARKS
# ============================================================

# English = column 2.
#
# All students:
#
# marks[:, 2]


print("\nAll English marks:")
print(marks[:, 2])

# Output:
#
# [90 70 95]


# ============================================================
# 37. COMMON MISTAKE - ZERO INDEXING
# ============================================================

# Example:
#
# arr = [10, 20, 30]
#
# Index:
#
# 0 → 10
# 1 → 20
# 2 → 30
#
#
# Therefore:
#
# arr[1]
#
# gives:
#
# 20
#
# NOT 10.


arr = np.array([10, 20, 30])

print("\nZero-indexing example:")
print(arr[1])

# Output:
#
# 20


# ============================================================
# 38. COMMON MISTAKE - INVALID INDEX
# ============================================================

# Example:
#
# arr = np.array([10, 20, 30])
#
# Valid indexes:
#
# 0
# 1
# 2
#
#
# This is invalid:
#
# arr[3]
#
# Because index 3 does not exist.
#
# It causes:
#
# IndexError


# ============================================================
# 39. COMMON MISTAKE - ROW AND COLUMN CONFUSION
# ============================================================

# For a 2D array:
#
# arr[row, column]
#
#
# FIRST number = ROW
#
# SECOND number = COLUMN
#
#
# Do NOT reverse them.
#
#
# Example:
#
# arr[1, 2]
#
# means:
#
# Row 1
# Column 2


# ============================================================
# 40. INTERVIEW QUESTIONS
# ============================================================

# Q1. What is indexing?
#
# Answer:
#
# Indexing is the process of accessing
# a specific array element using its position.


# Q2. Does NumPy use zero-based indexing?
#
# Answer:
#
# Yes.
#
# The first element has index 0.


# Q3. How do you access an element
# from a 1D array?
#
# Answer:
#
# arr[index]


# Q4. How do you access an element
# from a 2D array?
#
# Answer:
#
# arr[row, column]


# Q5. How do you select the second row?
#
# Answer:
#
# arr[1]
#
# or:
#
# arr[1, :]


# Q6. How do you select the second column?
#
# Answer:
#
# arr[:, 1]


# Q7. What does : mean?
#
# Answer:
#
# : means select all elements along
# that axis.


# Q8. What does -1 mean?
#
# Answer:
#
# -1 represents the last index
# along the selected axis.


# Q9. How do you access a 3D array?
#
# Answer:
#
# arr[layer, row, column]


# ============================================================
# 41. PRACTICE ARRAY
# ============================================================

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\n==============================")
print("PRACTICE ARRAY")
print("==============================")

print("Array:")
print(arr)


# ============================================================
# 42. PRACTICE - FIRST ELEMENT
# ============================================================

print("\nFirst element:")
print(arr[0, 0])

# Output:
#
# 10


# ============================================================
# 43. PRACTICE - LAST ELEMENT
# ============================================================

print("\nLast element:")
print(arr[-1, -1])

# Output:
#
# 120


# ============================================================
# 44. PRACTICE - SECOND ROW
# ============================================================

print("\nSecond row:")
print(arr[1])

# Output:
#
# [50 60 70 80]


# ============================================================
# 45. PRACTICE - THIRD ROW
# ============================================================

print("\nThird row:")
print(arr[2])

# Output:
#
# [90 100 110 120]


# ============================================================
# 46. PRACTICE - FIRST COLUMN
# ============================================================

print("\nFirst column:")
print(arr[:, 0])

# Output:
#
# [10 50 90]


# ============================================================
# 47. PRACTICE - SECOND COLUMN
# ============================================================

print("\nSecond column:")
print(arr[:, 1])

# Output:
#
# [20 60 100]


# ============================================================
# 48. PRACTICE - LAST COLUMN
# ============================================================

print("\nLast column:")
print(arr[:, -1])

# Output:
#
# [40 80 120]


# ============================================================
# 49. MINI CODING EXERCISE
# ============================================================

students = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 88, 92]
])

print("\n==============================")
print("MINI CODING EXERCISE")
print("==============================")

print("Students:")
print(students)


# ============================================================
# 50. GET 80
# ============================================================

# 80 is:
#
# Row 0
# Column 0
#
# Answer:
#
# students[0, 0]


print("\n80:")
print(students[0, 0])

# Output:
#
# 80


# ============================================================
# 51. GET 75
# ============================================================

# 75 is:
#
# Row 1
# Column 2
#
# Answer:
#
# students[1, 2]


print("\n75:")
print(students[1, 2])

# Output:
#
# 75


# ============================================================
# 52. GET COMPLETE SECOND ROW
# ============================================================

# Second row = index 1.
#
# Answer:
#
# students[1, :]


print("\nComplete second row:")
print(students[1, :])

# Output:
#
# [60 85 75]


# ============================================================
# 53. GET COMPLETE THIRD ROW
# ============================================================

# Third row = index 2.
#
# Answer:
#
# students[2, :]


print("\nComplete third row:")
print(students[2, :])

# Output:
#
# [95 88 92]


# ============================================================
# 54. GET FIRST COLUMN
# ============================================================

# First column = index 0.
#
# All rows:
#
# students[:, 0]


print("\nFirst column:")
print(students[:, 0])

# Output:
#
# [80 60 95]


# ============================================================
# 55. GET LAST COLUMN
# ============================================================

# Last column = -1.
#
# All rows:
#
# students[:, -1]


print("\nLast column:")
print(students[:, -1])

# Output:
#
# [90 75 92]


# ============================================================
# 56. GET LAST ELEMENT
# ============================================================

# Last row = -1
# Last column = -1
#
# Therefore:
#
# students[-1, -1]


print("\nLast element:")
print(students[-1, -1])

# Output:
#
# 92


# ============================================================
# 57. CHAPTER 4 SUMMARY
# ============================================================

# 1D indexing:
#
# arr[i]
#
# → Access one element


# 2D indexing:
#
# arr[row, column]
#
# → Access one element


# 3D indexing:
#
# arr[layer, row, column]
#
# → Access one element


# Positive indexing:
#
# 0, 1, 2, 3...
#
# → Left to right
# → Top to bottom


# Negative indexing:
#
# -1, -2, -3...
#
# → Right to left
# → Bottom to top


# Complete row:
#
# arr[row, :]
#
# → All columns


# Complete column:
#
# arr[:, column]
#
# → All rows


# Colon:
#
# :
#
# → ALL


# ============================================================
# 58. FINAL REVISION MAP
# ============================================================

#                 NUMPY INDEXING
#                       |
#         +-------------+-------------+
#         |             |             |
#         ↓             ↓             ↓
#        1D            2D            3D
#         |             |             |
#      arr[i]      arr[row,col]   arr[layer,row,col]
#         |             |             |
#         ↓             ↓             ↓
#      One value   Row + Column  Layer + Row + Column
#
#
# Positive Index:
#
# 0 → First
# 1 → Second
# 2 → Third
#
#
# Negative Index:
#
# -1 → Last
# -2 → Second last
# -3 → Third last
#
#
# 2D:
#
# arr[1, :] → Complete row
#
# arr[:, 1] → Complete column
#
# : → ALL


# ============================================================
# 59. CHAPTER 4 QUIZ
# ============================================================

# Try answering these WITHOUT looking at the answers.
#
#
# 1. What is the index of the first element?
#
#
# 2. What does arr[-1] return?
#
#
# 3. What does arr[2, 1] mean?
#
#
# 4. How do you select all rows from column 2?
#
#
# 5. How do you select row 1 and all columns?
#
#
# 6. What does : mean?
#
#
# 7. What is the indexing format for a 3D array?


# ============================================================
# 60. CHAPTER 4 CHECKLIST
# ============================================================

# Make sure you understand:
#
# ☑ What is indexing
# ☑ Zero-based indexing
# ☑ 1D indexing
# ☑ Positive indexing
# ☑ Negative indexing
# ☑ 2D indexing
# ☑ row, column
# ☑ Complete row
# ☑ Complete column
# ☑ Colon :
# ☑ Negative indexing in 2D
# ☑ 3D indexing
# ☑ layer, row, column
# ☑ Real-world student example
# ☑ Common mistakes
# ☑ Interview questions
# ☑ Practice
# ☑ Mini coding exercise
# ☑ Quiz


# ============================================================
# CHAPTER 4 - COMPLETE
# ============================================================

# NEXT:
#
# CHAPTER 5 - NUMPY SLICING
#
# Topics:
#
# start : stop : step
# 1D slicing
# Positive slicing
# Negative slicing
# Reverse arrays
# 2D row slicing
# 2D column slicing
# 2D sub-arrays
# 3D slicing
# Visual dry runs