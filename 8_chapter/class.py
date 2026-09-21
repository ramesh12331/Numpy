# ============================================================
# 🚀 NUMPY COMPLETE COURSE
# CHAPTER 8 - STATISTICAL FUNCTIONS
# ============================================================
#
# Goal:
# Learn how to analyze numerical data using NumPy.
#
# We will learn:
#   1. np.sum()
#   2. np.mean()
#   3. np.median()
#   4. np.min()
#   5. np.max()
#   6. np.argmin()
#   7. np.argmax()
#   8. np.var()
#   9. np.std()
#   10. np.percentile()
#   11. axis=0
#   12. axis=1
#
# These concepts are very important for:
#   - Data Science
#   - Data Analysis
#   - Machine Learning
#   - AI
#   - Student/Sales/Employee datasets
#
# ============================================================


import numpy as np


# ============================================================
# 1. WHAT IS STATISTICS?
# ============================================================
#
# Statistics means:
# Collecting, analyzing, and understanding data.
#
# Example:
# Student marks:
#
# 60, 70, 80, 90, 100
#
# We may want to know:
#
#   Total marks?
#   Average marks?
#   Middle value?
#   Smallest mark?
#   Largest mark?
#   How spread out are the marks?
#
# NumPy provides statistical functions for these calculations.
# ============================================================


marks = np.array([60, 70, 80, 90, 100])

print("Student Marks:")
print(marks)

# Output:
# [ 60  70  80  90 100]


# ============================================================
# 2. CHAPTER 8 IMPORTANT FUNCTIONS
# ============================================================
#
# np.sum()       -> Total
# np.mean()      -> Average
# np.median()    -> Middle value
# np.std()       -> Standard deviation
# np.var()       -> Variance
# np.min()       -> Minimum value
# np.max()       -> Maximum value
# np.argmin()    -> Index of minimum value
# np.argmax()    -> Index of maximum value
# np.percentile()-> Percentile
# axis           -> Direction of calculation
#
# ============================================================


# ============================================================
# 3. np.sum()
# ============================================================
#
# Definition:
# np.sum() calculates the total/sum of all elements.
#
# Syntax:
#
# np.sum(array)
#
# ============================================================


total = np.sum(marks)

print("\nTotal Marks:")
print(total)

# Output:
# 400


# ============================================================
# 4. np.sum() - DRY RUN
# ============================================================
#
# marks = [60, 70, 80, 90, 100]
#
# 60 + 70 + 80 + 90 + 100
#
# = 400
#
# Therefore:
#
# np.sum(marks) -> 400
#
# ============================================================


# ============================================================
# 5. np.mean()
# ============================================================
#
# Definition:
# mean means average.
#
# Formula:
#
# Mean = Sum of all values / Number of values
#
# ============================================================


average = np.mean(marks)

print("\nAverage Marks:")
print(average)

# Output:
# 80.0


# ============================================================
# 6. np.mean() - DRY RUN
# ============================================================
#
# Data:
#
# 60, 70, 80, 90, 100
#
# Step 1:
# Sum = 400
#
# Step 2:
# Number of values = 5
#
# Step 3:
#
# Mean = 400 / 5
#      = 80
#
# NumPy returns:
#
# 80.0
#
# ============================================================


# ============================================================
# 7. np.sum() vs np.mean()
# ============================================================
#
# np.sum()  -> Total
# np.mean() -> Average
#
# Example:
#
# marks = [60, 70, 80, 90, 100]
#
# np.sum(marks)
# -> 400
#
# np.mean(marks)
# -> 80.0
#
# ============================================================


# ============================================================
# 8. np.median()
# ============================================================
#
# Definition:
# Median is the middle value after the data is arranged
# in sorted order.
#
# Example:
#
# 10, 20, 30, 40, 50
#
# Middle value = 30
#
# ============================================================


arr = np.array([10, 20, 30, 40, 50])

median_value = np.median(arr)

print("\nMedian:")
print(median_value)

# Output:
# 30.0


# ============================================================
# 9. MEDIAN - ODD NUMBER OF VALUES
# ============================================================
#
# Data:
#
# 5, 10, 15, 20, 25
#
# Number of values = 5
#
# Middle value = 15
#
# Therefore:
#
# Median = 15
#
# ============================================================


arr_odd = np.array([5, 10, 15, 20, 25])

print("\nMedian of odd number of values:")
print(np.median(arr_odd))

# Output:
# 15.0


# ============================================================
# 10. MEDIAN - EVEN NUMBER OF VALUES
# ============================================================
#
# Data:
#
# 10, 20, 30, 40
#
# Number of values = 4
#
# There are TWO middle values:
#
# 20 and 30
#
# Median:
#
# (20 + 30) / 2
# = 50 / 2
# = 25
#
# ============================================================


arr_even = np.array([10, 20, 30, 40])

print("\nMedian of even number of values:")
print(np.median(arr_even))

# Output:
# 25.0


# ============================================================
# 11. np.min()
# ============================================================
#
# Definition:
# np.min() returns the smallest value.
#
# Syntax:
#
# np.min(array)
#
# ============================================================


minimum = np.min(marks)

print("\nMinimum:")
print(minimum)

# Output:
# 60


# ============================================================
# 12. np.max()
# ============================================================
#
# Definition:
# np.max() returns the largest value.
#
# Syntax:
#
# np.max(array)
#
# ============================================================


maximum = np.max(marks)

print("\nMaximum:")
print(maximum)

# Output:
# 100


# ============================================================
# 13. MINIMUM vs MAXIMUM
# ============================================================
#
# min -> smallest value
# max -> largest value
#
# Example:
#
# [60, 70, 80, 90, 100]
#
# np.min() -> 60
# np.max() -> 100
#
# ============================================================


# ============================================================
# 14. np.argmin()
# ============================================================
#
# Definition:
# np.argmin() returns the INDEX/POSITION
# of the smallest value.
#
# Important:
#
# np.min()     -> value
# np.argmin()  -> index
#
# ============================================================


arr = np.array([50, 20, 80, 10, 60])

minimum_index = np.argmin(arr)

print("\nIndex of Minimum:")
print(minimum_index)

# Output:
# 3


# ============================================================
# 15. np.argmin() - DRY RUN
# ============================================================
#
# Index:
#
#    0   1   2   3   4
#
# Value:
#
#   50  20  80  10  60
#               ↑
#            minimum
#
# Minimum value = 10
#
# Index of 10 = 3
#
# Therefore:
#
# np.min(arr)
# -> 10
#
# np.argmin(arr)
# -> 3
#
# ============================================================


# ============================================================
# 16. np.argmax()
# ============================================================
#
# Definition:
# np.argmax() returns the INDEX/POSITION
# of the largest value.
#
# ============================================================


maximum_index = np.argmax(arr)

print("\nIndex of Maximum:")
print(maximum_index)

# Output:
# 2


# ============================================================
# 17. np.argmax() - DRY RUN
# ============================================================
#
# Index:
#
#    0   1   2   3   4
#
# Value:
#
#   50  20  80  10  60
#           ↑
#        maximum
#
# Maximum value = 80
#
# Index of 80 = 2
#
# Therefore:
#
# np.max(arr)
# -> 80
#
# np.argmax(arr)
# -> 2
#
# ============================================================


# ============================================================
# 18. VERY IMPORTANT DIFFERENCE
# ============================================================
#
# np.min()
#     -> Minimum VALUE
#
# np.argmin()
#     -> INDEX of minimum VALUE
#
# np.max()
#     -> Maximum VALUE
#
# np.argmax()
#     -> INDEX of maximum VALUE
#
#
# MEMORY TRICK:
#
# "arg" -> argument/index position
#
# min      -> value
# argmin   -> position
#
# max      -> value
# argmax   -> position
#
# ============================================================


# ============================================================
# 19. np.var() - VARIANCE
# ============================================================
#
# Variance measures how much data values are spread
# out from the mean.
#
# If values are close to the mean:
#
#     Low variance
#
# If values are far from the mean:
#
#     High variance
#
# ============================================================


# ============================================================
# 20. VARIANCE FORMULA
# ============================================================
#
# Population variance:
#
# Variance = Σ(x - mean)^2 / N
#
# Where:
#
# x     -> each value
# mean  -> average
# N     -> number of values
#
# ============================================================


# ============================================================
# 21. VARIANCE - COMPLETE DRY RUN
# ============================================================
#
# Data:
#
# [10, 20, 30]
#
# ------------------------------------------------------------
# Step 1: Calculate Mean
# ------------------------------------------------------------
#
# Mean = (10 + 20 + 30) / 3
#
#      = 60 / 3
#
#      = 20
#
# ------------------------------------------------------------
# Step 2: Difference from Mean
# ------------------------------------------------------------
#
# 10 - 20 = -10
# 20 - 20 = 0
# 30 - 20 = 10
#
# ------------------------------------------------------------
# Step 3: Square the differences
# ------------------------------------------------------------
#
# (-10)^2 = 100
# (0)^2   = 0
# (10)^2  = 100
#
# ------------------------------------------------------------
# Step 4: Calculate average
# ------------------------------------------------------------
#
# Variance = (100 + 0 + 100) / 3
#
#          = 200 / 3
#
#          = 66.666...
#
# ============================================================


arr = np.array([10, 20, 30])

variance = np.var(arr)

print("\nVariance:")
print(variance)

# Output:
# 66.66666666666667


# ============================================================
# 22. np.std() - STANDARD DEVIATION
# ============================================================
#
# Standard deviation tells us how spread out values
# are from the mean.
#
# Formula:
#
# Standard Deviation = √Variance
#
# ============================================================


standard_deviation = np.std(arr)

print("\nStandard Deviation:")
print(standard_deviation)

# Output approximately:
# 8.16496581


# ============================================================
# 23. VARIANCE vs STANDARD DEVIATION
# ============================================================
#
# Variance
#     ↓
# Square of spread
#
# Standard Deviation
#     ↓
# Square root of variance
#
# Mathematically:
#
# std = √variance
#
# Therefore:
#
# np.std(arr)
# is approximately equal to
#
# np.sqrt(np.var(arr))
#
# ============================================================


print("\nCheck variance and standard deviation:")
print("Variance:", np.var(arr))
print("Standard Deviation:", np.std(arr))
print("Square Root of Variance:", np.sqrt(np.var(arr)))


# ============================================================
# 24. SIMPLE UNDERSTANDING OF VARIANCE
# ============================================================
#
# Dataset A:
#
# [50, 50, 50, 50]
#
# All values are identical.
#
# Mean = 50
# Variance = 0
# Standard deviation = 0
#
# There is NO spread.
#
# ============================================================


dataset_a = np.array([50, 50, 50, 50])

print("\nDataset A:")
print("Variance:", np.var(dataset_a))
print("Standard Deviation:", np.std(dataset_a))

# Output:
# Variance: 0.0
# Standard Deviation: 0.0


# ============================================================
# 25. MORE SPREAD = HIGHER VARIANCE
# ============================================================
#
# Dataset B:
#
# [10, 30, 50, 70, 90]
#
# Values are more spread out.
#
# Therefore:
#
# Variance -> larger
# Standard deviation -> larger
#
# ============================================================


dataset_b = np.array([10, 30, 50, 70, 90])

print("\nDataset B:")
print("Variance:", np.var(dataset_b))
print("Standard Deviation:", np.std(dataset_b))


# ============================================================
# 26. np.percentile()
# ============================================================
#
# Definition:
#
# A percentile tells us the value below which
# a certain percentage of observations fall.
#
# Syntax:
#
# np.percentile(array, percentile)
#
# ============================================================


arr = np.array([10, 20, 30, 40, 50])

percentile_50 = np.percentile(arr, 50)

print("\n50th Percentile:")
print(percentile_50)

# Output:
# 30.0


# ============================================================
# 27. 50th PERCENTILE = MEDIAN
# ============================================================
#
# The 50th percentile corresponds to the median.
#
# Therefore:
#
# 50th percentile = Median
#
# Example:
#
# [10, 20, 30, 40, 50]
#
# Median = 30
# 50th percentile = 30
#
# ============================================================


print("\nMedian:", np.median(arr))
print("50th Percentile:", np.percentile(arr, 50))


# ============================================================
# 28. COMMON PERCENTILES
# ============================================================
#
# 25th percentile -> Q1
# 50th percentile -> Median / Q2
# 75th percentile -> Q3
#
# ============================================================


print("\n25th Percentile:", np.percentile(arr, 25))
print("50th Percentile:", np.percentile(arr, 50))
print("75th Percentile:", np.percentile(arr, 75))

# Output:
# 25th Percentile: 20.0
# 50th Percentile: 30.0
# 75th Percentile: 40.0


# ============================================================
# 29. REAL-WORLD EXAMPLE - EXAM MARKS
# ============================================================
#
# Suppose students received:
#
# 35, 45, 50, 55, 60,
# 65, 70, 75, 80, 90
#
# ============================================================


marks = np.array([
    35, 45, 50, 55, 60,
    65, 70, 75, 80, 90
])

print("\n================ EXAM MARK STATISTICS ================")

print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))


# ============================================================
# 30. IMPORTANT CONCEPT - AXIS
# ============================================================
#
# axis is one of the MOST IMPORTANT concepts in NumPy.
#
# You will repeatedly use axis in:
#
#   - NumPy
#   - Pandas
#   - Data Science
#   - Machine Learning
#
# For a 2D array:
#
# axis=0
# axis=1
#
# ============================================================


# ============================================================
# 31. CREATE A 2D ARRAY
# ============================================================


arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(arr)


# ============================================================
# 32. UNDERSTANDING ROWS AND COLUMNS
# ============================================================
#
#             Columns
#             0   1   2
#
# Row 0      10  20  30
#
# Row 1      40  50  60
#
# Row 2      70  80  90
#
# ============================================================


# ============================================================
# 33. AXIS=0
# ============================================================
#
# Easy trick:
#
# axis=0 -> DOWN
#
# It moves down the rows.
#
# Result is calculated for EACH COLUMN.
#
# Visual:
#
#        ↓   ↓   ↓
#
#       10  20  30
#       40  50  60
#       70  80  90
#
# ============================================================


# ============================================================
# 34. AXIS=1
# ============================================================
#
# Easy trick:
#
# axis=1 -> ACROSS
#
# It moves across the columns.
#
# Result is calculated for EACH ROW.
#
# Visual:
#
#       10  20  30  ->
#       40  50  60  ->
#       70  80  90  ->
#
# ============================================================


# ============================================================
# 35. AXIS MEMORY TRICK
# ============================================================
#
# axis=0 -> vertical / DOWN
#         -> result for each COLUMN
#
# axis=1 -> horizontal / ACROSS
#         -> result for each ROW
#
# Remember:
#
# axis=0 -> column-wise result
# axis=1 -> row-wise result
#
# ============================================================


# ============================================================
# 36. np.sum() WITH axis=0
# ============================================================
#
# Array:
#
#       10  20  30
#       40  50  60
#       70  80  90
#
# Calculate each column:
#
# Column 0:
# 10 + 40 + 70 = 120
#
# Column 1:
# 20 + 50 + 80 = 150
#
# Column 2:
# 30 + 60 + 90 = 180
#
# ============================================================


sum_axis_0 = np.sum(arr, axis=0)

print("\nSum with axis=0:")
print(sum_axis_0)

# Output:
# [120 150 180]


# ============================================================
# 37. np.sum() WITH axis=1
# ============================================================
#
# Calculate each row:
#
# Row 0:
# 10 + 20 + 30 = 60
#
# Row 1:
# 40 + 50 + 60 = 150
#
# Row 2:
# 70 + 80 + 90 = 240
#
# ============================================================


sum_axis_1 = np.sum(arr, axis=1)

print("\nSum with axis=1:")
print(sum_axis_1)

# Output:
# [ 60 150 240]


# ============================================================
# 38. AXIS=0 vs AXIS=1
# ============================================================
#
# Original:
#
#       10  20  30
#       40  50  60
#       70  80  90
#
# ------------------------------------------------------------
# axis=0
# ------------------------------------------------------------
#
# 10 + 40 + 70 = 120
# 20 + 50 + 80 = 150
# 30 + 60 + 90 = 180
#
# Result:
#
# [120 150 180]
#
# ------------------------------------------------------------
# axis=1
# ------------------------------------------------------------
#
# 10 + 20 + 30 = 60
# 40 + 50 + 60 = 150
# 70 + 80 + 90 = 240
#
# Result:
#
# [60 150 240]
#
# ============================================================


# ============================================================
# 39. WHY DOES AXIS WORK THIS WAY?
# ============================================================
#
# Think about the dimension being collapsed.
#
# axis=0:
#
# Rows are collapsed.
# Calculation happens DOWN each column.
# Result -> one value for each column.
#
# axis=1:
#
# Columns are collapsed.
# Calculation happens ACROSS each row.
# Result -> one value for each row.
#
# ============================================================


# ============================================================
# 40. np.mean() WITH axis=0
# ============================================================
#
# Column 0:
#
# (10 + 40 + 70) / 3 = 40
#
# Column 1:
#
# (20 + 50 + 80) / 3 = 50
#
# Column 2:
#
# (30 + 60 + 90) / 3 = 60
#
# ============================================================


mean_axis_0 = np.mean(arr, axis=0)

print("\nMean with axis=0:")
print(mean_axis_0)

# Output:
# [40. 50. 60.]


# ============================================================
# 41. np.mean() WITH axis=1
# ============================================================
#
# Row 0:
#
# (10 + 20 + 30) / 3 = 20
#
# Row 1:
#
# (40 + 50 + 60) / 3 = 50
#
# Row 2:
#
# (70 + 80 + 90) / 3 = 80
#
# ============================================================


mean_axis_1 = np.mean(arr, axis=1)

print("\nMean with axis=1:")
print(mean_axis_1)

# Output:
# [20. 50. 80.]


# ============================================================
# 42. np.min() WITH axis
# ============================================================
#
# Minimum by COLUMN:
#
# Column 0 -> min(10,40,70) = 10
# Column 1 -> min(20,50,80) = 20
# Column 2 -> min(30,60,90) = 30
#
# ============================================================


print("\nMinimum by column:")
print(np.min(arr, axis=0))

# Output:
# [10 20 30]


# ============================================================
# 43. np.min() WITH axis=1
# ============================================================
#
# Minimum by ROW:
#
# Row 0 -> min(10,20,30) = 10
# Row 1 -> min(40,50,60) = 40
# Row 2 -> min(70,80,90) = 70
#
# ============================================================


print("\nMinimum by row:")
print(np.min(arr, axis=1))

# Output:
# [10 40 70]


# ============================================================
# 44. np.max() WITH axis=0
# ============================================================
#
# Maximum by COLUMN:
#
# Column 0 -> max(10,40,70) = 70
# Column 1 -> max(20,50,80) = 80
# Column 2 -> max(30,60,90) = 90
#
# ============================================================


print("\nMaximum by column:")
print(np.max(arr, axis=0))

# Output:
# [70 80 90]


# ============================================================
# 45. np.max() WITH axis=1
# ============================================================
#
# Maximum by ROW:
#
# Row 0 -> max(10,20,30) = 30
# Row 1 -> max(40,50,60) = 60
# Row 2 -> max(70,80,90) = 90
#
# ============================================================


print("\nMaximum by row:")
print(np.max(arr, axis=1))

# Output:
# [30 60 90]


# ============================================================
# 46. STATISTICAL FUNCTIONS WITH AXIS
# ============================================================
#
# Many NumPy statistical functions support axis.
#
# np.sum(arr, axis=...)
# np.mean(arr, axis=...)
# np.median(arr, axis=...)
# np.std(arr, axis=...)
# np.var(arr, axis=...)
# np.min(arr, axis=...)
# np.max(arr, axis=...)
#
# Example:
#
# np.mean(arr, axis=0)
#
# -> average of each column
#
# ============================================================


# ============================================================
# 47. REAL-WORLD EXAMPLE - STUDENT MARKS
# ============================================================
#
# Rows    -> Students
# Columns -> Subjects
#
# Suppose:
#
# Column 0 -> Maths
# Column 1 -> Science
# Column 2 -> English
#
# ============================================================


marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print("\n================ STUDENT MARKS ================")
print(marks)


# ============================================================
# 48. AVERAGE MARK FOR EACH SUBJECT
# ============================================================
#
# Subjects are represented by COLUMNS.
#
# Therefore:
#
# axis=0
#
# ============================================================


subject_average = np.mean(marks, axis=0)

print("\nAverage for each subject:")
print(subject_average)

# Output:
# [78.33333333 81.66666667 84.33333333]
#
# Meaning:
#
# Maths average   -> 78.33...
# Science average -> 81.66...
# English average -> 84.33...


# ============================================================
# 49. AVERAGE MARK FOR EACH STUDENT
# ============================================================
#
# Students are represented by ROWS.
#
# Therefore:
#
# axis=1
#
# ============================================================


student_average = np.mean(marks, axis=1)

print("\nAverage for each student:")
print(student_average)

# Output:
# [80.         73.33333333 91.        ]
#
# Meaning:
#
# Student 1 average -> 80
# Student 2 average -> 73.33...
# Student 3 average -> 91
#
# This is why axis is very important in Data Science.
#
# ============================================================


# ============================================================
# 50. COMPLETE STATISTICAL ANALYSIS
# ============================================================
#
# Let's calculate many statistics together.
# ============================================================


print("\n================ COMPLETE STATISTICS ================")

print("Total:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))


# ============================================================
# 51. COMMON MISTAKE - min vs argmin
# ============================================================
#
# WRONG understanding:
#
# np.min(arr)
# -> index
#
# NO!
#
# np.min(arr)
# -> minimum VALUE
#
# np.argmin(arr)
# -> index of minimum VALUE
#
# ============================================================


example = np.array([50, 20, 80, 10, 60])

print("\nMinimum value:", np.min(example))
print("Minimum index:", np.argmin(example))


# ============================================================
# 52. COMMON MISTAKE - max vs argmax
# ============================================================
#
# np.max(arr)
# -> maximum VALUE
#
# np.argmax(arr)
# -> index of maximum VALUE
#
# ============================================================


print("\nMaximum value:", np.max(example))
print("Maximum index:", np.argmax(example))


# ============================================================
# 53. COMMON MISTAKE - VARIANCE vs STD
# ============================================================
#
# Variance:
#
# Measures spread using squared differences.
#
# Standard deviation:
#
# Square root of variance.
#
# Remember:
#
# std = √variance
#
# ============================================================


# ============================================================
# 54. COMMON MISTAKE - AXIS=0 vs AXIS=1
# ============================================================
#
# Remember:
#
# axis=0
#     ↓
# DOWN
#     ↓
# result for each COLUMN
#
# axis=1
#     →
# ACROSS
#     →
# result for each ROW
#
# ============================================================


# ============================================================
# 55. COMMON MISTAKE - MEDIAN
# ============================================================
#
# For understanding median:
#
# First think about the values in sorted order.
#
# Odd number:
# -> one middle value
#
# Even number:
# -> average of two middle values
#
# ============================================================


# ============================================================
# 56. PRACTICE PROGRAM
# ============================================================
#
# Run this program separately if you want to practice.
# ============================================================


practice_marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print("\n================ PRACTICE PROGRAM ================")

print("Marks:")
print(practice_marks)

print("\nTotal:")
print(np.sum(practice_marks))

print("\nMean:")
print(np.mean(practice_marks))

print("\nMedian:")
print(np.median(practice_marks))

print("\nMinimum:")
print(np.min(practice_marks))

print("\nMaximum:")
print(np.max(practice_marks))

print("\nVariance:")
print(np.var(practice_marks))

print("\nStandard Deviation:")
print(np.std(practice_marks))

print("\nColumn totals:")
print(np.sum(practice_marks, axis=0))

print("\nRow totals:")
print(np.sum(practice_marks, axis=1))

print("\nColumn averages:")
print(np.mean(practice_marks, axis=0))

print("\nRow averages:")
print(np.mean(practice_marks, axis=1))


# ============================================================
# 57. MINI CODING EXERCISE - SALES DATA
# ============================================================
#
# Create the following array:
#
#       100  200  300
#       150  250  350
#       200  300  400
#       250  350  450
#
# ============================================================


sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450]
])


# ============================================================
# 58. EXERCISE 1 - TOTAL SALES
# ============================================================
#
# Find the total of all sales.
#
# Answer:
# np.sum(sales)
#
# ============================================================


print("\nTotal Sales:")
print(np.sum(sales))


# ============================================================
# 59. EXERCISE 2 - AVERAGE SALES
# ============================================================
#
# Find the average of all sales.
#
# Answer:
# np.mean(sales)
#
# ============================================================


print("\nAverage Sales:")
print(np.mean(sales))


# ============================================================
# 60. EXERCISE 3 - MINIMUM SALES
# ============================================================
#
# Find the smallest sales value.
#
# ============================================================


print("\nMinimum Sales:")
print(np.min(sales))


# ============================================================
# 61. EXERCISE 4 - MAXIMUM SALES
# ============================================================
#
# Find the largest sales value.
#
# ============================================================


print("\nMaximum Sales:")
print(np.max(sales))


# ============================================================
# 62. EXERCISE 5 - TOTAL FOR EACH COLUMN
# ============================================================
#
# Columns:
#
# Column 0:
# 100 + 150 + 200 + 250
#
# Column 1:
# 200 + 250 + 300 + 350
#
# Column 2:
# 300 + 350 + 400 + 450
#
# Use:
#
# axis=0
#
# ============================================================


print("\nTotal for each column:")
print(np.sum(sales, axis=0))


# ============================================================
# 63. EXERCISE 6 - TOTAL FOR EACH ROW
# ============================================================
#
# Use:
#
# axis=1
#
# ============================================================


print("\nTotal for each row:")
print(np.sum(sales, axis=1))


# ============================================================
# 64. EXERCISE 7 - AVERAGE FOR EACH COLUMN
# ============================================================
#
# Use:
#
# np.mean(sales, axis=0)
#
# ============================================================


print("\nAverage for each column:")
print(np.mean(sales, axis=0))


# ============================================================
# 65. EXERCISE 8 - AVERAGE FOR EACH ROW
# ============================================================
#
# Use:
#
# np.mean(sales, axis=1)
#
# ============================================================


print("\nAverage for each row:")
print(np.mean(sales, axis=1))


# ============================================================
# 66. EXERCISE 9 - INDEX OF MINIMUM VALUE
# ============================================================
#
# Use:
#
# np.argmin(sales)
#
# Note:
# For a multi-dimensional array, without axis,
# NumPy considers the flattened positions for the result.
#
# ============================================================


print("\nIndex of minimum value:")
print(np.argmin(sales))


# ============================================================
# 67. EXERCISE 10 - INDEX OF MAXIMUM VALUE
# ============================================================
#
# Use:
#
# np.argmax(sales)
#
# ============================================================


print("\nIndex of maximum value:")
print(np.argmax(sales))


# ============================================================
# 68. CHAPTER 8 QUICK REVISION
# ============================================================
#
# np.sum()
#     -> Total
#
# np.mean()
#     -> Average
#
# np.median()
#     -> Middle value
#
# np.var()
#     -> Variance
#
# np.std()
#     -> Standard deviation
#
# np.min()
#     -> Minimum value
#
# np.max()
#     -> Maximum value
#
# np.argmin()
#     -> Index of minimum
#
# np.argmax()
#     -> Index of maximum
#
# np.percentile()
#     -> Percentile
#
# axis=0
#     -> DOWN
#     -> result for each column
#
# axis=1
#     -> ACROSS
#     -> result for each row
#
# ============================================================


# ============================================================
# 69. FINAL REVISION MAP
# ============================================================
#
#                  NUMPY STATISTICS
#                         |
#          ---------------+---------------
#          |              |              |
#       CENTRAL         SPREAD        POSITION
#      TENDENCY
#          |              |              |
#       mean          variance          min
#       median        std               max
#                                      argmin
#                                      argmax
#          |
#          |
#      percentile
#
# ============================================================


# ============================================================
# 70. MOST IMPORTANT FORMULAS
# ============================================================
#
# Mean:
#
#     Mean = Sum / Number of values
#
#
# Variance:
#
#     Variance = Average of squared differences from mean
#
#
# Standard Deviation:
#
#     Standard Deviation = √Variance
#
# ============================================================


# ============================================================
# 71. MOST IMPORTANT AXIS RULE
# ============================================================
#
# For a 2D array:
#
# axis=0
#     ↓
# DOWN the rows
#     ↓
# result for each COLUMN
#
#
# axis=1
#     →
# ACROSS the columns
#     →
# result for each ROW
#
#
# MEMORY:
#
# axis=0 -> column result
# axis=1 -> row result
#
# ============================================================


# ============================================================
# 72. INTERVIEW QUESTIONS
# ============================================================
#
# Q1. What does np.sum() do?
#
# Answer:
# It returns the sum/total of array elements.
#
#
# Q2. What does np.mean() calculate?
#
# Answer:
# Arithmetic average.
#
# Formula:
#
# mean = sum / number of values
#
#
# Q3. Difference between np.min() and np.argmin()?
#
# Answer:
#
# np.min()    -> minimum value
# np.argmin() -> index of minimum
#
#
# Q4. Difference between np.max() and np.argmax()?
#
# Answer:
#
# np.max()    -> maximum value
# np.argmax() -> index of maximum
#
#
# Q5. What is variance?
#
# Answer:
# A measure of how much values are spread around the mean.
#
#
# Q6. What is standard deviation?
#
# Answer:
# Square root of variance.
#
#
# Q7. What is the 50th percentile?
#
# Answer:
# It corresponds to the median.
#
#
# Q8. What does axis=0 mean for a 2D array?
#
# Answer:
# It calculates down the rows and produces a result
# for each column.
#
#
# Q9. What does axis=1 mean?
#
# Answer:
# It calculates across the columns and produces a result
# for each row.
#
#
# Q10. Why is axis important in Data Science?
#
# Answer:
# Datasets commonly contain rows and columns, and we often
# need calculations per row or per column.
#
# ============================================================


# ============================================================
# 73. CHAPTER 8 QUIZ
# ============================================================
#
# Try to answer these WITHOUT looking at the answers above.
#
# 1. What is the difference between np.sum() and np.mean()?
#
# 2. What is the median of:
#       [10, 20, 30, 40, 50]
#
# 3. What is the median of:
#       [10, 20, 30, 40]
#
# 4. What does np.argmin() return?
#
# 5. What does np.argmax() return?
#
# 6. What is the relationship between variance
#    and standard deviation?
#
# 7. What does the 50th percentile represent?
#
# 8. What does axis=0 do?
#
# 9. What does axis=1 do?
#
# 10. If rows represent students and columns represent
#     subjects, which axis calculates the average
#     of each subject?
#
# ============================================================


# ============================================================
# 74. QUIZ ANSWERS
# ============================================================
#
# 1. np.sum() -> total
#    np.mean() -> average
#
# 2. 30
#
# 3. 25
#
# 4. Index of minimum value
#
# 5. Index of maximum value
#
# 6. std = √variance
#
# 7. Median
#
# 8. Calculates DOWN -> result for each column
#
# 9. Calculates ACROSS -> result for each row
#
# 10. axis=0
#
# ============================================================


# ============================================================
# 75. GOLDEN MEMORY TABLE
# ============================================================
#
# Function             Meaning
# ------------------------------------------------------------
# np.sum()             Total
# np.mean()            Average
# np.median()          Middle value
# np.var()             Variance
# np.std()             Standard deviation
# np.min()             Minimum value
# np.max()             Maximum value
# np.argmin()          Index of minimum
# np.argmax()          Index of maximum
# np.percentile()      Percentile
# ------------------------------------------------------------
#
# axis=0               DOWN -> column result
# axis=1               ACROSS -> row result
#
# ============================================================


# ============================================================
# 🎯 CHAPTER 8 COMPLETE
# ============================================================
#
# You have now learned:
#
# [x] np.sum()
# [x] np.mean()
# [x] np.median()
# [x] np.min()
# [x] np.max()
# [x] np.argmin()
# [x] np.argmax()
# [x] np.var()
# [x] np.std()
# [x] np.percentile()
# [x] axis=0
# [x] axis=1
# [x] Statistical analysis
# [x] Student marks analysis
# [x] Sales data analysis
#
# ============================================================
#
# NEXT:
#
# 🚀 CHAPTER 9 - RESHAPING ARRAYS
#
# Topics:
#
#   reshape()
#   resize()
#   flatten()
#   ravel()
#   transpose()
#   .T
#   Changing dimensions
#   Shape calculations
#   Visual transformations
#   Step-by-step dry runs
#
# ============================================================