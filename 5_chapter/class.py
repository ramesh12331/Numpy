# ============================================================
# NUMPY COMPLETE COURSE
# CHAPTER 5 - SLICING
# VS CODE NOTES WITH COMMENTED EXPLANATION
# ============================================================
#
# In Chapter 4:
# We learned INDEXING -> accessing ONE element / row / column.
#
# In Chapter 5:
# We learn SLICING -> accessing a RANGE / PORTION of an array.
#
# IMPORTANT MEMORY:
# Indexing -> ONE
# Slicing  -> RANGE
#
# Source: NumPy Chapter 5 - Slicing
# ============================================================


import numpy as np


# ============================================================
# 1. WHAT IS SLICING?
# ============================================================
#
# Slicing means extracting a part/range of an array.
#
# Example:
#
# Array:
# [10, 20, 30, 40, 50]
#
# If we want:
# [20, 30, 40]
#
# We can use:
# arr[1:4]
#
# IMPORTANT:
# The STOP index is NOT included.
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

print("\nSlicing arr[1:4]:")
print(arr[1:4])

# Output:
# [20 30 40]


# ============================================================
# INDEXING VS SLICING
# ============================================================
#
# Indexing:
#     Get ONE position
#
#     arr[2]
#
# Slicing:
#     Get a RANGE
#
#     arr[1:4]
#
# Easy memory trick:
#
#     Indexing -> ONE
#     Slicing  -> RANGE
# ============================================================

print("\nIndexing:")
print(arr[2])

# Output:
# 30

print("\nSlicing:")
print(arr[1:4])

# Output:
# [20 30 40]


# ============================================================
# 2. BASIC SLICING SYNTAX
# ============================================================
#
# Basic syntax:
#
#     array[start:stop]
#
# Full syntax:
#
#     array[start:stop:step]
#
#
# start -> where to start
# stop  -> where to stop
# step  -> how many positions to move
#
# VERY IMPORTANT:
# stop index is EXCLUDED.
#
# Example:
#
# arr[1:4]
#
# Start = 1
# Stop  = 4
#
# Takes:
# index 1
# index 2
# index 3
#
# Does NOT take index 4.
# ============================================================


# ============================================================
# 3. 1D ARRAY SLICING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

#
# Visual:
#
# Index:    0    1    2    3    4
#           ↓    ↓    ↓    ↓    ↓
# Array:   10   20   30   40   50
#


# ============================================================
# Example 1 - arr[1:4]
# ============================================================

print("\nExample 1 - arr[1:4]:")
print(arr[1:4])

# Output:
# [20 30 40]


# ============================================================
# DRY RUN
# ============================================================
#
# arr[1:4]
#
# Start = 1
# Stop  = 4
#
# Take:
#
# index 1 -> 20
# index 2 -> 30
# index 3 -> 40
#
# Stop before index 4.
#
# Result:
# [20 30 40]
# ============================================================


# ============================================================
# 4. START OMITTED
# ============================================================
#
# We can omit the start.
#
# arr[:3]
#
# Means:
#
# Start -> beginning
# Stop  -> 3
#
# Therefore:
#
# indexes 0, 1, 2
#
# ============================================================

print("\nExample 2 - arr[:3]:")
print(arr[:3])

# Output:
# [10 20 30]


# ============================================================
# DRY RUN
# ============================================================
#
# arr[:3]
#
# Beginning -> index 0
# Stop      -> index 3
#
# Take:
#
# 0 -> 10
# 1 -> 20
# 2 -> 30
#
# Do not take index 3.
# ============================================================


# ============================================================
# 5. STOP OMITTED
# ============================================================
#
# We can omit the stop.
#
# arr[2:]
#
# Means:
#
# Start -> index 2
# Stop  -> end
# ============================================================

print("\nExample 3 - arr[2:]:")
print(arr[2:])

# Output:
# [30 40 50]


# ============================================================
# DRY RUN
# ============================================================
#
# arr[2:]
#
# Start at index 2:
#
# 2 -> 30
# 3 -> 40
# 4 -> 50
#
# Continue until the end.
# ============================================================


# ============================================================
# 6. BOTH START AND STOP OMITTED
# ============================================================
#
# arr[:]
#
# Means:
#
# Start -> beginning
# Stop  -> end
#
# Therefore, it selects the complete array.
# ============================================================

print("\nExample 4 - arr[:]:")
print(arr[:])

# Output:
# [10 20 30 40 50]


# ============================================================
# BASIC SLICING PATTERNS
# ============================================================
#
# arr[1:4] -> Index 1 to 3
# arr[:4]  -> Beginning to index 3
# arr[2:]  -> Index 2 to end
# arr[:]   -> Entire array
# ============================================================


# ============================================================
# 7. SLICING WITH STEP
# ============================================================
#
# Syntax:
#
#     arr[start:stop:step]
#
# Example:
#
# arr[0:6:2]
#
# Start = 0
# Stop  = 6
# Step  = 2
#
# Array:
#
# Index:   0   1   2   3   4   5
#          ↓   ↓   ↓   ↓   ↓   ↓
# Value:  10  20  30  40  50  60
#
# Take:
#
# 0 -> 10
# 2 -> 30
# 4 -> 50
# ============================================================

arr = np.array([10, 20, 30, 40, 50, 60])

print("\nExample 5 - arr[0:6:2]:")
print(arr[0:6:2])

# Output:
# [10 30 50]


# ============================================================
# 8. EVERY SECOND ELEMENT
# ============================================================
#
# arr[::2]
#
# Start -> beginning
# Stop  -> end
# Step  -> 2
#
# Therefore:
# Take every second element.
# ============================================================

print("\nExample 6 - arr[::2]:")
print(arr[::2])

# Output:
# [10 30 50]


# ============================================================
# 9. EVERY THIRD ELEMENT
# ============================================================
#
# arr[::3]
#
# Start -> beginning
# Stop  -> end
# Step  -> 3
#
# Index:
# 0 -> 10
# 3 -> 40
# ============================================================

print("\nExample 7 - arr[::3]:")
print(arr[::3])

# Output:
# [10 40]


# ============================================================
# 10. NEGATIVE SLICING
# ============================================================
#
# Negative indexes count from right to left.
#
# Example:
#
# Index:   -6   -5   -4   -3   -2   -1
#           ↓    ↓    ↓    ↓    ↓    ↓
# Array:   10   20   30   40   50   60
#
# For:
#
# arr[-3:]
#
# Start at the third-last element
# and continue to the end.
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print("\nExample 8 - arr[-3:]:")
print(arr[-3:])

# Output:
# [30 40 50]


# ============================================================
# 11. NEGATIVE START AND STOP
# ============================================================
#
# Example:
#
# arr[-4:-1]
#
# Negative indexes:
#
# -4 -> 20
# -3 -> 30
# -2 -> 40
# -1 -> stop
#
# Remember:
# STOP IS EXCLUDED.
# ============================================================

print("\nExample 9 - arr[-4:-1]:")
print(arr[-4:-1])

# Output:
# [20 30 40]


# ============================================================
# 12. REVERSE A 1D ARRAY
# ============================================================
#
# One of the MOST IMPORTANT slicing tricks:
#
#     arr[::-1]
#
# Step = -1
#
# Negative step means:
#
#     Move from RIGHT -> LEFT
#
# Original:
#
# [10 20 30 40 50]
#
# Reverse:
#
# [50 40 30 20 10]
# ============================================================

print("\nExample 10 - arr[::-1]:")
print(arr[::-1])

# Output:
# [50 40 30 20 10]


# ============================================================
# MEMORY TRICK
# ============================================================
#
# arr[::-1]
#
# means:
#
#     REVERSE THE ARRAY
# ============================================================


# ============================================================
# 13. 2D ARRAY SLICING
# ============================================================
#
# For a 2D array:
#
#     arr[row_slice, column_slice]
#
# General pattern:
#
#     arr[ROWS, COLUMNS]
#
# IMPORTANT:
#
# First part  -> ROWS
# Second part -> COLUMNS
# ============================================================

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\n2D Array:")
print(arr)

#
# Visual:
#
#           Columns
#        0    1    2     3
#
#  0   10   20   30    40
#  1   50   60   70    80
#  2   90  100  110   120
#
# ============================================================


# ============================================================
# 14. SELECT MULTIPLE ROWS
# ============================================================
#
# First two rows:
#
#     arr[0:2, :]
#
# 0:2 -> rows 0 and 1
# :   -> all columns
# ============================================================

print("\nExample 11 - First two rows:")
print(arr[0:2, :])

# Output:
# [[10 20 30 40]
#  [50 60 70 80]]


# ============================================================
# 15. SELECT MULTIPLE COLUMNS
# ============================================================
#
# Columns 1 and 2:
#
#     arr[:, 1:3]
#
# :   -> all rows
# 1:3 -> columns 1 and 2
# ============================================================

print("\nExample 12 - Columns 1 and 2:")
print(arr[:, 1:3])

# Output:
# [[ 20  30]
#  [ 60  70]
#  [100 110]]


# ============================================================
# 16. SELECT ROWS AND COLUMNS TOGETHER
# ============================================================
#
# Example:
#
#     arr[0:2, 1:3]
#
# Rows:
#     0, 1
#
# Columns:
#     1, 2
#
# Therefore:
#
# 20 30
# 60 70
# ============================================================

print("\nExample 13 - Rows 0,1 and Columns 1,2:")
print(arr[0:2, 1:3])

# Output:
# [[20 30]
#  [60 70]]


# ============================================================
# 17. SELECT A COMPLETE ROW USING SLICING
# ============================================================
#
# arr[1, :]
#
# 1 -> row 1
# : -> all columns
# ============================================================

print("\nExample 14 - Complete row 1:")
print(arr[1, :])

# Output:
# [50 60 70 80]


# ============================================================
# 18. SELECT A COMPLETE COLUMN USING SLICING
# ============================================================
#
# arr[:, 2]
#
# : -> all rows
# 2 -> column 2
# ============================================================

print("\nExample 15 - Complete column 2:")
print(arr[:, 2])

# Output:
# [ 30  70 110]


# ============================================================
# 19. SELECT A RANGE OF ROWS AND ALL COLUMNS
# ============================================================
#
# arr[1:3, :]
#
# Rows:
#     1 and 2
#
# Columns:
#     all
# ============================================================

print("\nExample 16 - Rows 1 and 2:")
print(arr[1:3, :])

# Output:
# [[ 50  60  70  80]
#  [ 90 100 110 120]]


# ============================================================
# 20. SELECT ALL ROWS AND A RANGE OF COLUMNS
# ============================================================
#
# arr[:, 1:4]
#
# Rows:
#     all
#
# Columns:
#     1, 2, 3
# ============================================================

print("\nExample 17 - Columns 1, 2, 3:")
print(arr[:, 1:4])

# Output:
# [[ 20  30  40]
#  [ 60  70  80]
#  [100 110 120]]


# ============================================================
# 21. 2D SLICING WITH STEP
# ============================================================
#
# arr[::2, :]
#
# Row slicing:
#     Start -> beginning
#     Stop  -> end
#     Step  -> 2
#
# Therefore:
#     Row 0
#     Row 2
#
# : -> all columns
# ============================================================

print("\nExample 18 - Every second row:")
print(arr[::2, :])

# Output:
# [[ 10  20  30  40]
#  [ 90 100 110 120]]


# ============================================================
# 22. REVERSE ROWS
# ============================================================
#
# arr[::-1, :]
#
# First part:
#     ::-1 -> reverse rows
#
# Second part:
#     : -> all columns
# ============================================================

print("\nExample 19 - Reverse rows:")
print(arr[::-1, :])

# Output:
# [[ 90 100 110 120]
#  [ 50  60  70  80]
#  [ 10  20  30  40]]


# ============================================================
# 23. REVERSE COLUMNS
# ============================================================
#
# arr[:, ::-1]
#
# First part:
#     : -> all rows
#
# Second part:
#     ::-1 -> reverse columns
# ============================================================

print("\nExample 20 - Reverse columns:")
print(arr[:, ::-1])

# Output:
# [[ 40  30  20  10]
#  [ 80  70  60  50]
#  [120 110 100  90]]


# ============================================================
# 24. REVERSE ENTIRE 2D ARRAY
# ============================================================
#
# arr[::-1, ::-1]
#
# First ::-1:
#     Reverse rows
#
# Second ::-1:
#     Reverse columns
#
# Therefore:
#
#     Reverse rows
#          +
#     Reverse columns
# ============================================================

print("\nExample 21 - Reverse entire 2D array:")
print(arr[::-1, ::-1])

# Output:
# [[120 110 100  90]
#  [ 80  70  60  50]
#  [ 40  30  20  10]]


# ============================================================
# 25. 3D ARRAY SLICING
# ============================================================
#
# A 3D array has:
#
#     layer
#     row
#     column
#
# General form:
#
#     arr[layer, row, column]
#
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

print("\n3D Array:")
print(arr)


# ============================================================
# CHECK SHAPE
# ============================================================

print("\n3D Array Shape:")
print(arr.shape)

# Output:
# (2, 2, 3)
#
# Meaning:
#
# 2 layers
# 2 rows per layer
# 3 columns per row


# ============================================================
# 26. SELECT ONE LAYER
# ============================================================
#
# arr[0]
#
# Selects layer 0.
# ============================================================

print("\nExample 22 - First layer:")
print(arr[0])

# Output:
# [[1 2 3]
#  [4 5 6]]


# ============================================================
# 27. SLICE ROWS FROM A 3D ARRAY
# ============================================================
#
# arr[:, 0, :]
#
# First :
#     all layers
#
# 0:
#     row 0
#
# Second :
#     all columns
# ============================================================

print("\nExample 23 - Row 0 from every layer:")
print(arr[:, 0, :])

# Output:
# [[1 2 3]
#  [7 8 9]]


# ============================================================
# 28. SLICE COLUMNS FROM A 3D ARRAY
# ============================================================
#
# arr[:, :, 1]
#
# First :
#     all layers
#
# Second :
#     all rows
#
# 1:
#     column 1
# ============================================================

print("\nExample 24 - Column 1 from every layer:")
print(arr[:, :, 1])

# Output:
# [[ 2  5]
#  [ 8 11]]


# ============================================================
# 29. SLICING CHEAT SHEET
# ============================================================
#
# -------------------------
# 1D ARRAY
# -------------------------
#
# arr[start:stop:step]
#
#
# -------------------------
# 2D ARRAY
# -------------------------
#
# arr[
#     row_start:row_stop:row_step,
#     col_start:col_stop:col_step
# ]
#
#
# -------------------------
# 3D ARRAY
# -------------------------
#
# arr[
#     layer_slice,
#     row_slice,
#     column_slice
# ]
# ============================================================


# ============================================================
# 30. REAL-WORLD EXAMPLE - SALES DATA
# ============================================================
#
# Imagine we have monthly sales data.
#
# Columns:
#
# Jan | Feb | Mar | Apr
#
# Rows can represent different stores.
# ============================================================

sales = np.array([
    [100, 200, 300, 400],
    [150, 250, 350, 450],
    [200, 300, 400, 500]
])

print("\nSales Data:")
print(sales)


# ============================================================
# GET JANUARY SALES
# ============================================================
#
# January is column 0.
#
# sales[:, 0]
#
# : -> all rows
# 0 -> column 0
# ============================================================

print("\nJanuary Sales:")
print(sales[:, 0])

# Output:
# [100 150 200]


# ============================================================
# GET JANUARY + FEBRUARY
# ============================================================
#
# sales[:, 0:2]
#
# :   -> all rows
# 0:2 -> columns 0 and 1
# ============================================================

print("\nJanuary + February Sales:")
print(sales[:, 0:2])

# Output:
# [[100 200]
#  [150 250]
#  [200 300]]


# ============================================================
# GET MARCH + APRIL
# ============================================================
#
# sales[:, 2:4]
#
# :   -> all rows
# 2:4 -> columns 2 and 3
# ============================================================

print("\nMarch + April Sales:")
print(sales[:, 2:4])

# Output:
# [[300 400]
#  [350 450]
#  [400 500]]


# ============================================================
# WHY SLICING IS IMPORTANT IN DATA SCIENCE
# ============================================================
#
# In real datasets, we often need only a portion of data.
#
# Examples:
#
#     Select specific rows
#     Select specific columns
#     Select months
#     Select features
#     Select records
#     Reverse data
#     Process part of a dataset
#
# Slicing is therefore extremely important in:
#
#     NumPy
#     Pandas
#     Data Science
#     Machine Learning
# ============================================================


# ============================================================
# 31. COMMON MISTAKE - STOP IS EXCLUDED
# ============================================================
#
# arr[1:4]
#
# Does NOT include index 4.
#
# It includes:
#
# 1, 2, 3
#
# Remember:
#
#     START -> INCLUDED
#     STOP  -> EXCLUDED
# ============================================================


# ============================================================
# 32. COMMON MISTAKE - INDEXING VS SLICING
# ============================================================
#
# arr[2]
#
# -> One element for a 1D array.
#
#
# arr[1:4]
#
# -> A range of elements.
#
#
# Easy memory:
#
#     arr[index]       -> ONE
#     arr[start:stop]  -> RANGE
# ============================================================


# ============================================================
# 33. COMMON MISTAKE - ROW VS COLUMN
# ============================================================
#
# For 2D arrays:
#
#     arr[row, column]
#
# NOT:
#
#     arr[column, row]
#
# Always remember:
#
#     ROW FIRST
#     COLUMN SECOND
# ============================================================


# ============================================================
# 34. COMMON MISTAKE - FORGETTING SECOND DIMENSION
# ============================================================
#
# For 2D arrays:
#
# Correct:
#
#     arr[0:2, 1:3]
#
# The comma separates:
#
#     rows , columns
#
# Without the comma, you are not specifying both dimensions.
# ============================================================


# ============================================================
# 35. PRACTICE PROGRAM
# ============================================================
#
# Run this complete program in VS Code.
# ============================================================

practice_arr = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

print("\n" + "=" * 60)
print("PRACTICE PROGRAM")
print("=" * 60)

print("\nOriginal Array:")
print(practice_arr)


# ------------------------------------------------------------
# 1. First two rows
# ------------------------------------------------------------

print("\n1. First two rows:")
print(practice_arr[:2, :])


# ------------------------------------------------------------
# 2. Last two rows
# ------------------------------------------------------------

print("\n2. Last two rows:")
print(practice_arr[-2:, :])


# ------------------------------------------------------------
# 3. First three columns
# ------------------------------------------------------------

print("\n3. First three columns:")
print(practice_arr[:, :3])


# ------------------------------------------------------------
# 4. Last two columns
# ------------------------------------------------------------

print("\n4. Last two columns:")
print(practice_arr[:, -2:])


# ------------------------------------------------------------
# 5. Rows 1 and 2, columns 2 and 3
# ------------------------------------------------------------

print("\n5. Rows 1 and 2, columns 2 and 3:")
print(practice_arr[1:3, 2:4])


# ------------------------------------------------------------
# 6. Reverse rows
# ------------------------------------------------------------

print("\n6. Reverse rows:")
print(practice_arr[::-1, :])


# ------------------------------------------------------------
# 7. Reverse columns
# ------------------------------------------------------------

print("\n7. Reverse columns:")
print(practice_arr[:, ::-1])


# ------------------------------------------------------------
# 8. Reverse everything
# ------------------------------------------------------------

print("\n8. Reverse everything:")
print(practice_arr[::-1, ::-1])


# ============================================================
# 36. MINI CODING EXERCISE
# ============================================================
#
# Use slicing ONLY.
#
# Do NOT use individual indexes like:
#
#     students[0, 0]
#
# Use slicing such as:
#
#     students[:2, :]
#
# ============================================================

students = np.array([
    [80, 70, 90, 85],
    [60, 88, 75, 92],
    [95, 82, 89, 90],
    [72, 78, 85, 80]
])

print("\n" + "=" * 60)
print("MINI CODING EXERCISE")
print("=" * 60)

print("\nStudents:")
print(students)


# ============================================================
# QUESTION 1
# First two rows
# ============================================================

print("\n1. First two rows:")

# Answer:
print(students[:2, :])

# Output:
# [[80 70 90 85]
#  [60 88 75 92]]


# ============================================================
# QUESTION 2
# Last two rows
# ============================================================

print("\n2. Last two rows:")

# Answer:
print(students[-2:, :])

# Output:
# [[95 82 89 90]
#  [72 78 85 80]]


# ============================================================
# QUESTION 3
# First two columns
# ============================================================

print("\n3. First two columns:")

# Answer:
print(students[:, :2])

# Output:
# [[80 70]
#  [60 88]
#  [95 82]
#  [72 78]]


# ============================================================
# QUESTION 4
# Last two columns
# ============================================================

print("\n4. Last two columns:")

# Answer:
print(students[:, -2:])

# Output:
# [[90 85]
#  [75 92]
#  [89 90]
#  [85 80]]


# ============================================================
# QUESTION 5
# Rows 1 and 2, columns 1 and 2
# ============================================================

print("\n5. Rows 1 and 2, columns 1 and 2:")

# Answer:
print(students[1:3, 1:3])

# Output:
# [[88 75]
#  [82 89]]


# ============================================================
# QUESTION 6
# Reverse the rows
# ============================================================

print("\n6. Reverse the rows:")

# Answer:
print(students[::-1, :])

# Output:
# [[72 78 85 80]
#  [95 82 89 90]
#  [60 88 75 92]
#  [80 70 90 85]]


# ============================================================
# QUESTION 7
# Reverse the columns
# ============================================================

print("\n7. Reverse the columns:")

# Answer:
print(students[:, ::-1])

# Output:
# [[85 90 70 80]
#  [92 75 88 60]
#  [90 89 82 95]
#  [80 85 78 72]]


# ============================================================
# QUESTION 8
# Reverse the entire array
# ============================================================

print("\n8. Reverse the entire array:")

# Answer:
print(students[::-1, ::-1])

# Output:
# [[80 85 78 72]
#  [90 89 82 95]
#  [92 75 88 60]
#  [85 90 70 80]]


# ============================================================
# 37. INTERVIEW QUESTIONS
# ============================================================
#
# Q1. What is slicing?
#
# Answer:
# Slicing is used to extract a range or portion of an array.
#
#
# Q2. What is the syntax for slicing?
#
# Answer:
#
#     arr[start:stop:step]
#
#
# Q3. Is the stop index included?
#
# Answer:
# No.
#
# The stop index is excluded.
#
#
# Q4. How do you reverse a NumPy array?
#
# Answer:
#
#     arr[::-1]
#
#
# Q5. How do you select all rows from column 1?
#
# Answer:
#
#     arr[:, 1]
#
#
# Q6. How do you select rows 1 and 2?
#
# Answer:
#
#     arr[1:3, :]
#
#
# Q7. How do you select columns 1 and 2?
#
# Answer:
#
#     arr[:, 1:3]
#
#
# Q8. What does ::2 mean?
#
# Answer:
# Start from the beginning, go to the end,
# and move with a step of 2.
#
# Example:
#
#     arr[::2]
# ============================================================


# ============================================================
# 38. SLICING CHEAT SHEET
# ============================================================
#
# 1D ARRAY
#
# arr[1:4]
#     -> Range from index 1 to 3
#
# arr[:4]
#     -> Beginning to index 3
#
# arr[2:]
#     -> Index 2 to end
#
# arr[:]
#     -> Entire array
#
# arr[::2]
#     -> Every second element
#
# arr[::-1]
#     -> Reverse array
#
#
# 2D ARRAY
#
# arr[1:3, :]
#     -> Selected rows
#
# arr[:, 1:3]
#     -> Selected columns
#
# arr[::-1, :]
#     -> Reverse rows
#
# arr[:, ::-1]
#     -> Reverse columns
#
# arr[::-1, ::-1]
#     -> Reverse everything
# ============================================================


# ============================================================
# 39. FINAL REVISION
# ============================================================
#
# REMEMBER THIS FORMULA:
#
#     START : STOP : STEP
#
#
# For 2D:
#
#     ROWS , COLUMNS
#
#
# Example:
#
#     arr[1:3, 2:4]
#
# Means:
#
#     Rows    -> 1, 2
#     Columns -> 2, 3
#
#
# Example:
#
#     arr[::-1, ::-1]
#
# Means:
#
#     Reverse rows
#          +
#     Reverse columns
# ============================================================


# ============================================================
# 40. MOST IMPORTANT SLICING PATTERNS
# ============================================================
#
# arr[1:4]          -> range
#
# arr[:4]           -> beginning
#
# arr[2:]           -> end
#
# arr[::2]          -> every 2nd element
#
# arr[::-1]         -> reverse
#
# arr[1:3, :]       -> rows
#
# arr[:, 1:3]       -> columns
#
# arr[::-1, :]      -> reverse rows
#
# arr[:, ::-1]      -> reverse columns
#
# arr[::-1, ::-1]   -> reverse everything
# ============================================================


# ============================================================
# 41. CHAPTER 5 QUIZ
# ============================================================
#
# Try answering these WITHOUT looking at the answers above.
#
# 1. What is the difference between indexing and slicing?
#
# 2. In arr[1:5], is index 5 included?
#
# 3. What does arr[:3] return?
#
# 4. What does arr[2:] return?
#
# 5. What does arr[::2] mean?
#
# 6. How do you reverse a 1D array?
#
# 7. How do you select all rows from column 2?
#
# 8. How do you select rows 1 and 2 from a 2D array?
#
# 9. What does arr[::-1, :] do?
#
# 10. What does arr[:, ::-1] do?
# ============================================================


# ============================================================
# CHAPTER 5 SUMMARY
# ============================================================
#
# SLICING:
#     Extract a range/portion of an array.
#
# BASIC SYNTAX:
#     arr[start:stop]
#
# FULL SYNTAX:
#     arr[start:stop:step]
#
# MOST IMPORTANT RULE:
#     STOP IS EXCLUDED.
#
# 1D:
#     arr[1:4]
#
# START OMITTED:
#     arr[:4]
#
# STOP OMITTED:
#     arr[2:]
#
# EVERYTHING:
#     arr[:]
#
# STEP:
#     arr[::2]
#
# REVERSE:
#     arr[::-1]
#
# 2D:
#     arr[rows, columns]
#
# ROWS:
#     arr[1:3, :]
#
# COLUMNS:
#     arr[:, 1:3]
#
# REVERSE ROWS:
#     arr[::-1, :]
#
# REVERSE COLUMNS:
#     arr[:, ::-1]
#
# REVERSE EVERYTHING:
#     arr[::-1, ::-1]
#
#
# ============================================================
# GOLDEN RULE
# ============================================================
#
#     1D  -> START : STOP : STEP
#
#     2D  -> ROWS , COLUMNS
#
#     3D  -> LAYERS , ROWS , COLUMNS
#
#
# ⭐ MOST IMPORTANT:
#
#     START -> INCLUDED
#     STOP  -> EXCLUDED
#
#
# Chapter 5 - COMPLETE ✅
#
# Next:
# Chapter 6 - NumPy Array Operations
#
# Topics:
#     Addition
#     Subtraction
#     Multiplication
#     Division
#     Modulus
#     Power
#     Comparisons
#     Logical Operations
# ============================================================