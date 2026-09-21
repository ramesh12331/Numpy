import numpy as np

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450]
])

# ============================================================
# 58. EXERCISE 1 - TOTAL SALES
# ============================================================
print(np.sum(sales))
# ============================================================
# 59. EXERCISE 2 - AVERAGE SALES
# ============================================================
print(np.average(sales))
print(np.mean(sales))

# ============================================================
# 60. EXERCISE 3 - MINIMUM SALES
# ============================================================
print(np.min(sales))

# ============================================================
# 61. EXERCISE 4 - MAXIMUM SALES
# ============================================================
print(np.max(sales))
# ============================================================
# 62. EXERCISE 5 - TOTAL FOR EACH COLUMN
# ============================================================
print(np.sum(sales, axis=0))
# ============================================================
# 63. EXERCISE 6 - TOTAL FOR EACH ROW
# ============================================================
print(np.sum(sales, axis=1))
# ============================================================
# 64. EXERCISE 7 - AVERAGE FOR EACH COLUMN
# ============================================================
print(np.mean(sales, axis=0))
# ============================================================
# 65. EXERCISE 8 - AVERAGE FOR EACH ROW
# ============================================================
print(np.mean(sales, axis=1))

# ============================================================
# 66. EXERCISE 9 - INDEX OF MINIMUM VALUE
# ============================================================
print(np.argmin(sales))

# ============================================================
# 67. EXERCISE 10 - INDEX OF MAXIMUM VALUE
# ============================================================
print(np.argmax(sales))

# ============================================================
# 73. CHAPTER 8 QUIZ - ANSWERS
# ============================================================


# ============================================================
# 1. What is the difference between np.sum() and np.mean()?
# ============================================================

# np.sum()  -> Adds all the values.
# np.mean() -> Calculates the average of all the values.

import numpy as np

arr = np.array([10, 20, 30])

print(np.sum(arr))
# Output: 60

print(np.mean(arr))
# Output: 20.0


# ============================================================
# 2. What is the median of:
#       [10, 20, 30, 40, 50]
# ============================================================

# There are 5 values.
# The middle value is 30.

arr = np.array([10, 20, 30, 40, 50])

print(np.median(arr))
# Output: 30.0


# ============================================================
# 3. What is the median of:
#       [10, 20, 30, 40]
# ============================================================

# There are 4 values.
# For an even number of values:
#
# Median = (middle value 1 + middle value 2) / 2
#
# Median = (20 + 30) / 2
#        = 25

arr = np.array([10, 20, 30, 40])

print(np.median(arr))
# Output: 25.0


# ============================================================
# 4. What does np.argmin() return?
# ============================================================

# np.argmin() returns the INDEX/POSITION
# of the smallest value.

arr = np.array([50, 20, 80, 10])

print(np.argmin(arr))
# Output: 3
#
# Explanation:
# 10 is the smallest value.
# Its index is 3.


# ============================================================
# 5. What does np.argmax() return?
# ============================================================

# np.argmax() returns the INDEX/POSITION
# of the largest value.

arr = np.array([50, 20, 80, 10])

print(np.argmax(arr))
# Output: 2
#
# Explanation:
# 80 is the largest value.
# Its index is 2.


# ============================================================
# 6. What is the relationship between variance
#    and standard deviation?
# ============================================================

# Standard Deviation = Square Root of Variance
#
# Variance = Standard Deviation ** 2

variance = 25

standard_deviation = np.sqrt(variance)

print(standard_deviation)
# Output: 5.0


# Example:
#
# Variance = 25
# Standard Deviation = sqrt(25)
#                    = 5


# ============================================================
# 7. What does the 50th percentile represent?
# ============================================================

# The 50th percentile represents the MEDIAN.
#
# It means approximately:
# 50% of the values are below it.
# 50% of the values are above it.

arr = np.array([10, 20, 30, 40, 50])

print(np.percentile(arr, 50))
# Output: 30.0


# ============================================================
# 8. What does axis=0 do?
# ============================================================

# In a 2D array:
#
# axis=0 works DOWN the rows.
# It produces a result for EACH COLUMN.
#
# Easy memory:
#
# axis=0 -> Column-wise result

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.mean(arr, axis=0))

# Output:
# [25. 35. 45.]
#
# Calculation:
#
# Column 1 -> (10 + 40) / 2 = 25
# Column 2 -> (20 + 50) / 2 = 35
# Column 3 -> (30 + 60) / 2 = 45


# ============================================================
# 9. What does axis=1 do?
# ============================================================

# In a 2D array:
#
# axis=1 works ACROSS the columns.
# It produces a result for EACH ROW.
#
# Easy memory:
#
# axis=1 -> Row-wise result

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.mean(arr, axis=1))

# Output:
# [20. 50.]
#
# Calculation:
#
# Row 1 -> (10 + 20 + 30) / 3 = 20
# Row 2 -> (40 + 50 + 60) / 3 = 50


# ============================================================
# 10. If rows represent students and columns represent
#     subjects, which axis calculates the average
#     of each subject?
# ============================================================

# Answer:
#
# axis=0
#
# Because axis=0 calculates DOWN each column.
#
# Example:
#
#             Math   English   Science
# Student 1    80      70        90
# Student 2    60      80        70
# Student 3    90      90        80
#
# axis=0 gives:
#
# Math     -> (80 + 60 + 90) / 3
# English  -> (70 + 80 + 90) / 3
# Science  -> (90 + 70 + 80) / 3


# ============================================================
# IMPORTANT AXIS MEMORY TRICK
# ============================================================

# axis=0
# ↓ DOWN
# COLUMN-WISE
#
# axis=1
# → ACROSS
# ROW-WISE


# ============================================================
# QUICK SUMMARY
# ============================================================

# np.sum()       -> Sum of values
# np.mean()      -> Average
# np.median()    -> Middle value
# np.argmin()    -> Index of minimum value
# np.argmax()    -> Index of maximum value
# Variance       -> Squared spread
# Standard Dev.  -> Square root of variance
# 50th percentile-> Median
# axis=0         -> Column-wise
# axis=1         -> Row-wise
