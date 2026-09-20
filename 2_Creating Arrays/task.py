import numpy as np


# ============================================================
# 48. PRACTICE QUESTIONS - BEGINNER
# ============================================================

# ------------------------------------------------------------
# Practice 1:
# Create:
# [10 20 30 40 50]
# using np.array()
# ------------------------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("Practice 1:")
print(arr)


# ------------------------------------------------------------
# Practice 2:
# Create a 1D array containing numbers from 1 to 10.
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr = np.array(numbers)

print("\nPractice 2:")
print(arr)


# ------------------------------------------------------------
# Practice 3:
# Create a 3 × 3 array of zeros.
# ------------------------------------------------------------

arr = np.zeros((3, 3), dtype=int)

print("\nPractice 3:")
print(arr)


# ------------------------------------------------------------
# Practice 4:
# Create a 2 × 4 array of ones.
# ------------------------------------------------------------

arr = np.ones((2, 4), dtype=int)

print("\nPractice 4:")
print(arr)


# ------------------------------------------------------------
# Practice 5:
# Create a 3 × 3 array filled with 7.
# ------------------------------------------------------------

arr = np.full((3, 3), 7)

print("\nPractice 5:")
print(arr)


# ============================================================
# 49. PRACTICE QUESTIONS - INTERMEDIATE
# ============================================================

# ------------------------------------------------------------
# Practice 6:
# Create:
# [0 2 4 6 8 10]
# using np.arange()
# ------------------------------------------------------------

arr = np.arange(0, 11, 2)

print("\nPractice 6:")
print(arr)


# ------------------------------------------------------------
# Practice 7:
# Create exactly 6 evenly spaced values
# between 0 and 100.
# ------------------------------------------------------------

arr = np.linspace(0, 100, 6)

print("\nPractice 7:")
print(arr)


# ------------------------------------------------------------
# Practice 8:
# Create a 4 × 4 identity matrix.
#
# Identity Matrix:
#
# [1 0 0 0]
# [0 1 0 0]
# [0 0 1 0]
# [0 0 0 1]
# ------------------------------------------------------------

arr = np.eye(4, dtype=int)

print("\nPractice 8:")
print(arr)


# ------------------------------------------------------------
# Practice 9:
# Create 5 random integers between 1 and 50.
#
# randint(low, high, size)
#
# Important:
# low  -> included
# high -> excluded
#
# randint(1, 51, 5)
# means numbers can be from 1 to 50.
# ------------------------------------------------------------

arr = np.random.randint(1, 51, 5)

print("\nPractice 9:")
print(arr)


# ------------------------------------------------------------
# Practice 10:
# Create a 3 × 4 random integer array
# between 10 and 100.
#
# 3 rows
# 4 columns
# ------------------------------------------------------------

arr = np.random.randint(10, 101, size=(3, 4))

print("\nPractice 10:")
print(arr)


# ============================================================
# 50. MINI CODING EXERCISE
# ============================================================

# Create marks for 10 students.
#
# Marks should be between:
# 0 and 100
#
# randint(0, 101, 10)
#
# 0   -> included
# 101 -> excluded
# Therefore possible values are 0 to 100.
# ------------------------------------------------------------

student_marks = np.random.randint(0, 101, 10)

print("\nMini Exercise - Student Marks:")
print(student_marks)


# ============================================================
# EXTRA PRACTICE WITH STUDENT MARKS
# ============================================================

# Find the highest mark
print("\nHighest Mark:")
print(np.max(student_marks))


# Find the lowest mark
print("\nLowest Mark:")
print(np.min(student_marks))


# Find the average mark
print("\nAverage Mark:")
print(np.mean(student_marks))


# Find total marks
print("\nTotal Marks:")
print(np.sum(student_marks))


# Find how many students are there
print("\nNumber of Students:")
print(student_marks.size)


# Find students who scored 50 or more
passed_students = student_marks[student_marks >= 50]

print("\nStudents Scored 50 or More:")
print(passed_students)


# Count students who scored 50 or more
pass_count = np.sum(student_marks >= 50)

print("\nNumber of Students Scored 50 or More:")
print(pass_count)