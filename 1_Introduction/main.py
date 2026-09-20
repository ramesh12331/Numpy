# ============================================================
# 2. WHY DO WE USE NUMPY?
# ============================================================
marks = [70, 80, 90, 60, 85]

new_marks = []

for mark in marks:
    new_marks.append(mark+5)
print(new_marks)

# ============================================================
# USING NUMPY
# ============================================================
print("numpy")
import numpy as np
marks = np.array([70, 80, 90, 60, 85])

new_marks = marks + 5
print(new_marks)

# ============================================================
# 3. NUMPY VS PYTHON LIST
# ============================================================
# ---------------------------
# Python List
# ---------------------------

a = [1, 2, 3]
b = [4, 5, 6]

print("\nPython List Addition:")
print(a+b)

# ---------------------------
# NumPy Array
# ---------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nNumPy Array Addition:")
print(a+b)

# ============================================================
# 4. MULTIPLICATION DIFFERENCE
# ============================================================

# ---------------------------
# Python List
# ---------------------------
numbers = [1, 2, 3]

print("\nPython List Multiplication:")
print(numbers*2)

# ---------------------------
# NumPy Array
# ---------------------------
numbers = np.array([1, 2, 3])

print("\nNumPy Array Multiplication:")
print(numbers*2)

# ============================================================
# 6. ADVANTAGES OF NUMPY
# ============================================================
# ---------------------------
# 1. Efficient numerical operations
# ---------------------------

arr = np.array([10, 20, 30])

print("\nAdd 10:")
print(arr + 10)

print("\nMultiply by 2:")
print(arr * 2)

print("\nDivide by 5:")
print(arr / 5)

# ============================================================
# 10. CHECK NUMPY VERSION
# ============================================================

print("\nNumPy Version:")
print(np.__version__)

# ============================================================
# 11. FIRST NUMPY PROGRAM
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print("\nArray:")
print(arr)

# Add 10 to every element.

result = arr + 10

print("\nAfter adding 10:")
print(result)

# ============================================================
# 13. REAL-WORLD EXAMPLE - SALES
# ============================================================
# Sales for five days.
sales  = np.array([
    1000,
    1500,
    1200,
    1800,
    2000
])

# 10% discount means customer pays 90%.
#
# 100% - 10% = 90%
# 90% = 0.90
discounted_sales = sales *0.90

print("\nOriginal Sales:")
print(sales)

print("\nAfter 10% Discount:")
print(discounted_sales)

# ============================================================
# 16. BEGINNER PRACTICE
# ============================================================
arr = np.array([10, 20, 30, 40, 50])

print("\n Print the array")
print(arr)

print("\n Add 10 to every element.")
print(arr + 10)

print("\n Multiply every element by 2")
print(arr * 2)

print("\n numpy version")
print(np.__version__)

# ============================================================
# 17. MINI CODING EXERCISE
# ============================================================
numbers = np.array([100, 200, 300, 400, 500])

# Add 50.
numbers = numbers + 50

# Multiply the result by 2.
numbers = numbers * 2

print("\nFinal Result:")
print(numbers)

print("\nNumPy Version:")
print(np.__version__)