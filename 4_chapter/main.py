import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

print("\nIndex 0:", arr[0])
print("Index 1:", arr[1])
print("Index 2:", arr[2])
print("Index 3:", arr[3])
print("Index 4:", arr[4])

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
print(arr[1,1])

# ============================================================
# 10. MORE 2D INDEXING EXAMPLES
# ============================================================

print("\nMore 2D Indexing:")

print("arr[0, 0]:", arr[0, 0])
print("arr[0, 2]:", arr[0, 2])
print("arr[2, 0]:", arr[2, 0])
print("arr[2, 2]:", arr[2, 2])

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

# ============================================================
# 14. SELECT OTHER COMPLETE ROWS
# ============================================================

print("\nRow 0:")
print(arr[0])

print("\nRow 1:")
print(arr[1])

print("\nRow 2:")
print(arr[2])

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

print("\nRow 0 using colon:")
print(arr[0, :])

print("\nRow 1 using colon:")
print(arr[1, :])

print("\nRow 2 using colon:")
print(arr[2, :])

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
print("\nColumn 0:")
print(arr[:,0])

print("\nColumn 1:")
print(arr[:, 1])

print("\nColumn 2:")
print(arr[:,2])

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

# ============================================================
# 22. OTHER NEGATIVE COLUMN EXAMPLES
# ============================================================

print("\nSecond-last column:")
print(arr[:, -2])

print("\nFirst column using negative index:")
print(arr[:, -3])

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

# ============================================================
# 25. FIRST ELEMENT OF A 2D ARRAY
# ============================================================

print("\nFirst element:")
print(arr[0, 0])

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

print(arr_3d[0, 0, 0])
print(arr_3d[1, 1, 1])
print(arr_3d[0,1,1])

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
print(marks[1,1])

# ============================================================
# 34. GET ALL SCIENCE MARKS
# ============================================================
print(marks[:,1])

# ============================================================
# 35. GET ALL MATHS MARKS
# ============================================================

print(marks[:,0])

# ============================================================
# 36. GET ALL ENGLISH MARKS
# ============================================================
print(marks[:,2])

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
print(arr[0,0])

# ============================================================
# 43. PRACTICE - LAST ELEMENT
# ============================================================
print(arr[2,3])
# OR
print(arr[-1,-1])

# ============================================================
# 44. PRACTICE - SECOND ROW
# ============================================================
print(arr[1])
# ============================================================
# 45. PRACTICE - THIRD ROW
# ============================================================
print(arr[2])
# ============================================================
# 46. PRACTICE - FIRST COLUMN
# ============================================================
print(arr[:,0])
# ============================================================
# 47. PRACTICE - SECOND COLUMN
# ============================================================
print(arr[:,1])
# ============================================================
# 48. PRACTICE - LAST COLUMN
# ============================================================
print(arr[:,-1])
# OR
print(arr[:,3])

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
print(students[0,0])
# ============================================================
# 51. GET 75
# ============================================================
print(students[1,2])
# ============================================================
# 52. GET COMPLETE SECOND ROW
# ============================================================
print(students[1,:])
# ============================================================
# 53. GET COMPLETE THIRD ROW
# ============================================================
print(students[2,:])
# ============================================================
# 54. GET FIRST COLUMN
# ============================================================
print(students[:,0])
# ============================================================
# 55. GET LAST COLUMN
# ============================================================
print(students[:,2])
# OR
print(students[:, -1])
# ============================================================
# 56. GET LAST ELEMENT
# ============================================================

print(students[-1,-1])
# OR
print(students[2,2])