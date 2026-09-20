# ============================================================
# 3. 1D ARRAY
# ============================================================
import numpy as np

arr = np.array([10, 20, 30, 40])

print("\n1D Array:")
print(arr)
print("\n Number of dimensions:", arr.ndim)

# ============================================================
# 4. 2D ARRAY
# ============================================================
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape", arr.shape)

# ============================================================
# 5. 3D ARRAY
# ============================================================
arr = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])

print("\n3D Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape", arr.shape)

# ============================================================
# 7. dtype
# ============================================================
arr = np.array([10, 20, 30])
print("\ndtype Example:")
print(arr)
print("Data type:", arr.dtype)

# ============================================================
# 8. SPECIFYING dtype
# ============================================================

arr = np.array([10, 20, 30], dtype="float64")
print("\nSpecified dtype:")
print(arr)
print(arr.dtype)

# ============================================================
# 9. dtype - INTEGER vs FLOAT
# ============================================================

# Integer array:
int_arr = np.array([10, 20, 30], dtype="int32")

# Float array:
float_arr = np.array([10, 20, 30], dtype="float64")

print("\nInteger Array:")
print(int_arr)
print(int_arr.dtype)

print("\nFloat Array:")
print(float_arr)
print(float_arr.dtype)

# ============================================================
# 10. WHY dtype IS IMPORTANT
# ============================================================

marks = np.array([70, 80, 90], dtype="int32")

salary = np.array([25000.50, 30000.75], dtype="float64")

print("\nMarks:")
print(marks)

print("\nSalary:")
print(salary)

# ============================================================
# 11. ndmin
# ============================================================

arr1 = np.array([1, 2, 3])

print("\nNormal Array:")
print(arr1)
print("Dimensions:", arr1.ndim)

# ndmin=2:

arr2 = np.array([1, 2, 3], ndmin=2)
print(arr2)
print("Dimensions:", arr2.ndim)

# ============================================================
# 12. IMPORTANT POINT ABOUT ndmin
# ============================================================

arr = np.array([
    [1, 2],
    [3, 4]
], ndmin=2)

print("\nndmin with an existing 2D array:")
print(arr)
print("Dimensions:", arr.ndim)

# ============================================================
# 13. np.zeros()
# ============================================================

# np.zeros() creates an array filled with zeros.
#
# Syntax:
#
# np.zeros(shape)


# 1D zeros:

arr = np.zeros(5)
print("\n1D zeros:")
print(arr)

# ============================================================
# 14. 2D np.zeros()
# ============================================================

# (2, 3) means:
#
# 2 rows
# 3 columns

arr = np.zeros((2,3))
print("\n2D zeros:")
print(arr)

# ============================================================
# 15. np.zeros() WITH INTEGER dtype
# ============================================================

# By default zeros() normally creates float values.
#
# We can specify integer dtype.
arr = np.zeros((2,3), dtype=int)

print("\nInteger zeros:")
print(arr)

# ============================================================
# 16. np.ones()
# ============================================================

# np.ones() creates an array filled with ones.
#
# Syntax:
#
# np.ones(shape)

arr = np.ones(5)
print("\n1D ones:")
print(arr)

arr = np.ones((2,3))
print("\n2D ones:")
print(arr)

arr = np.ones((2,2,3))
print("\n3D ones:")
print(arr)

# ============================================================
# 17. np.ones() WITH INTEGER dtype
# ============================================================

arr = np.ones((2,3), dtype=int)
print("\nInteger ones:")
print(arr)

# ============================================================
# 18. np.full()
# ============================================================

# np.full() creates an array where every element
# contains the value we specify.
#
# Syntax:
#
# np.full(shape, value)
print("\n1D full 7:")
arr = np.full(5,7)
print(arr)

print("\n2D full 7:")
arr = np.full((2,3), 7)
print(arr)

print("\n3D full 7:")
arr = np.full((2,2,3), 7)
print(arr)

# ============================================================
# 20. np.empty()
# ============================================================

arr = np.empty((2,3))

print("\nnp.empty() Example:")

print("\nnp.empty() Example:")
print(arr)

# ============================================================
# 22. np.arange()
# ============================================================

arr = np.arange(10)
print(arr)

arr = np.arange(1,10)
print(arr)

arr = np.arange(0,10,2)
print(arr)

# ============================================================
# 24. arange() WITH STEP
# ============================================================

arr = np.arange(0, 11, 2)

print("\nnp.arange(0, 11, 2):")
print(arr)

# ============================================================
# 25. arange() ANOTHER EXAMPLE
# ============================================================

arr = np.arange(2, 12, 3)
print(arr)

# ============================================================
# 26. np.linspace()
# ============================================================

arr = np.linspace(0, 10 ,5)

print("\nnp.linspace(0, 10, 5):")
print(arr)

# ============================================================
# 29. np.eye()
# ============================================================
arr = np.eye(3)
print("\nnp.eye(3):")
print(arr)

# ============================================================
# 31. RANDOM ARRAYS
# ============================================================

# NumPy provides random functions to generate
# random numbers.
#
# Common functions:
#
# np.random.rand()
# np.random.random()
# np.random.randint()

# ============================================================
# 32. np.random.rand()
# ============================================================

arr = np.random.rand(5)
print("\nnp.random.rand(5):")
print(arr)

# ============================================================
# 33. np.random.random()
# ============================================================

arr = np.random.random(5)
print(arr)

# ============================================================
# 35. np.random.randint()
# ============================================================

arr = np.random.randint(1, 10, 5)
print(arr)

# ============================================================
# 37. RANDOM 2D ARRAY
# ============================================================

arr = np.random.randint(1,100 ,size=(3,4))
print(arr)

# ============================================================
# 38. RANDOM STUDENT MARKS
# ============================================================

arr = np.random.randint(0, 101, 10)
print(arr)

# ============================================================
# 39. REAL-WORLD EXAMPLE - STUDENT DATA
# ============================================================

marks = np.zeros(30, dtype=int)
print("\nInitial Student Marks:")
print(marks)

# ============================================================
# 40. REAL-WORLD EXAMPLE - TEMPERATURE
# ============================================================
temperature = np.linspace(20, 40, 7)

print("\nTemperature Points:")

print(temperature)

# ============================================================
# 48. PRACTICE QUESTIONS - BEGINNER
# ============================================================
# Practice 1:
# Create:
#
# [10 20 30 40 50]
#
# using np.array()

arr = np.array([10, 20, 30, 40, 50])
print(arr)

# Practice 2:
# Create a 1D array containing numbers from 1 to 10.
numbers = [1,2,3,4,5,6,7,8,9]
arr = np.array(numbers)
print(arr)

# Practice 3:
# Create a 3 × 3 array of zeros.

arr = np.zeros((3,3), dtype=int)
print(arr)

# Practice 4:
# Create a 2 × 4 array of ones.

arr = np.ones((2,4))
print(arr)

# Practice 4:
# Create a 2 × 4 array of ones.

arr = np.full((3,3),7)
print(arr)

# ============================================================
# 49. PRACTICE QUESTIONS - INTERMEDIATE
# ============================================================

# Practice 6:
# Create:
#
# [0 2 4 6 8 10]
#
# using np.arange()

arr = np.arange(0, 11, 2)
print(arr)

# Practice 7:
# Create exactly 6 evenly spaced values
# between 0 and 100.

arr = np.linspace(0, 100, 6)
print(arr)

# Practice 8:
# Create a 4 × 4 identity matrix.

# arr = np.eye((4,4),1)
# print(arr)

# Practice 9:
# Create 5 random integers between 1 and 50

arr = np.random.randint(1,50,5)
print(arr)

# Practice 10:
# Create a 3 × 4 random integer array
# between 10 and 100.

arr = np.random.randint(10, 100, size=(3,4))
[print(arr)]

# ============================================================
# 50. MINI CODING EXERCISE
# ============================================================
student_marks = np.random.randint(0, 101, 10)

print("\nMini Exercise - Student Marks:")
print(student_marks)