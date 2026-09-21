# ============================================================
# NUMPY COMPLETE COURSE
# CHAPTER 7 - MATHEMATICAL FUNCTIONS
# VS CODE NOTES WITH COMMENTED EXPLANATION
# ============================================================
#
# In Chapter 6, we learned operators:
#
#     +   -   *   /   %   **
#
# In this chapter:
# We learn NumPy's BUILT-IN MATHEMATICAL FUNCTIONS.
#
# Functions covered:
#
#     np.add()
#     np.subtract()
#     np.multiply()
#     np.divide()
#     np.sqrt()
#     np.square()
#     np.power()
#     np.abs()
#     np.exp()
#     np.log()
#
# IMPORTANT:
# These functions are generally vectorized.
# That means they can operate on every element of an array.
#
# Source: NumPy Chapter 7 - Mathematical Functions
# ============================================================


import numpy as np


# ============================================================
# 1. WHAT ARE NUMPY MATHEMATICAL FUNCTIONS?
# ============================================================
#
# NumPy provides ready-made functions for mathematical
# calculations on arrays.
#
# Examples:
#
#     np.sqrt()    -> Square root
#     np.square()  -> Square
#     np.abs()     -> Absolute value
#
#
# Basic idea:
#
#     Python value
#          ↓
#     NumPy function
#          ↓
#     Mathematical result
#
#
# For arrays:
#
#     Array
#       ↓
#     NumPy function
#       ↓
#     Function applied to every element
# ============================================================


# ============================================================
# 2. FUNCTIONS WE LEARN IN CHAPTER 7
# ============================================================
#
# np.add()       -> Addition
# np.subtract()  -> Subtraction
# np.multiply()  -> Multiplication
# np.divide()    -> Division
# np.sqrt()      -> Square root
# np.square()    -> Square
# np.power()     -> Power
# np.abs()       -> Absolute value
# np.exp()       -> Exponential
# np.log()       -> Natural logarithm
# ============================================================


# ============================================================
# 3. np.add()
# ============================================================
#
# Definition:
#
# np.add() performs ELEMENT-WISE ADDITION.
#
# Syntax:
#
#     np.add(array1, array2)
#
# Example:
#
#     a = [10, 20, 30]
#     b = [ 1,  2,  3]
#
#     10 + 1 = 11
#     20 + 2 = 22
#     30 + 3 = 33
# ============================================================

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

result = np.add(a, b)

print("np.add():")
print(result)

# Output:
# [11 22 33]


# ============================================================
# DRY RUN - np.add()
# ============================================================
#
#     10 + 1 = 11
#     20 + 2 = 22
#     30 + 3 = 33
#
# Result:
#
#     [11 22 33]
# ============================================================


# ============================================================
# np.add() VS + OPERATOR
# ============================================================
#
# Both produce the same element-wise result:
#
#     a + b
#
# and:
#
#     np.add(a, b)
#
# ============================================================

print("\nUsing + operator:")
print(a + b)

print("\nUsing np.add():")
print(np.add(a, b))

# Output:
# [11 22 33]
# [11 22 33]


# ============================================================
# 4. np.subtract()
# ============================================================
#
# Definition:
#
# np.subtract() performs ELEMENT-WISE SUBTRACTION.
#
# Syntax:
#
#     np.subtract(array1, array2)
#
# Example:
#
#     10 - 1 = 9
#     20 - 2 = 18
#     30 - 3 = 27
# ============================================================

result = np.subtract(a, b)

print("\nnp.subtract():")
print(result)

# Output:
# [ 9 18 27]


# ============================================================
# DRY RUN - np.subtract()
# ============================================================
#
#     10 - 1 = 9
#     20 - 2 = 18
#     30 - 3 = 27
#
# Result:
#
#     [9 18 27]
# ============================================================


# ============================================================
# EQUIVALENT OPERATOR
# ============================================================
#
#     a - b
#
# and:
#
#     np.subtract(a, b)
#
# perform the same element-wise subtraction.
# ============================================================

print("\nUsing - operator:")
print(a - b)

print("\nUsing np.subtract():")
print(np.subtract(a, b))


# ============================================================
# 5. np.multiply()
# ============================================================
#
# Definition:
#
# np.multiply() performs ELEMENT-WISE MULTIPLICATION.
#
# Syntax:
#
#     np.multiply(array1, array2)
#
# Example:
#
#     a = [2, 3, 4]
#     b = [5, 6, 7]
#
#     2 × 5 = 10
#     3 × 6 = 18
#     4 × 7 = 28
# ============================================================

a_mul = np.array([2, 3, 4])
b_mul = np.array([5, 6, 7])

result = np.multiply(a_mul, b_mul)

print("\nnp.multiply():")
print(result)

# Output:
# [10 18 28]


# ============================================================
# DRY RUN
# ============================================================
#
#     2 × 5 = 10
#     3 × 6 = 18
#     4 × 7 = 28
#
# Result:
#
#     [10 18 28]
# ============================================================


# ============================================================
# 6. np.divide()
# ============================================================
#
# Definition:
#
# np.divide() performs ELEMENT-WISE DIVISION.
#
# Syntax:
#
#     np.divide(array1, array2)
#
# Example:
#
#     10 ÷ 2 = 5
#     20 ÷ 4 = 5
#     30 ÷ 5 = 6
# ============================================================

a_div = np.array([10, 20, 30])
b_div = np.array([2, 4, 5])

result = np.divide(a_div, b_div)

print("\nnp.divide():")
print(result)

# Output:
# [5. 5. 6.]


# ============================================================
# DRY RUN
# ============================================================
#
#     10 ÷ 2 = 5
#     20 ÷ 4 = 5
#     30 ÷ 5 = 6
#
# Result:
#
#     [5. 5. 6.]
# ============================================================


# ============================================================
# 7. OPERATOR VS NUMPY FUNCTION
# ============================================================
#
# Addition:
#
#     a + b
#     np.add(a, b)
#
# Subtraction:
#
#     a - b
#     np.subtract(a, b)
#
# Multiplication:
#
#     a * b
#     np.multiply(a, b)
#
# Division:
#
#     a / b
#     np.divide(a, b)
#
#
# Quick memory:
#
#     Operator       NumPy Function
#
#     +              np.add()
#     -              np.subtract()
#     *              np.multiply()
#     /              np.divide()
# ============================================================


# ============================================================
# 8. np.sqrt()
# ============================================================
#
# sqrt means SQUARE ROOT.
#
# Mathematical concept:
#
# If:
#
#     x² = n
#
# then:
#
#     √n = x
#
#
# Examples:
#
#     √4  = 2
#     √9  = 3
#     √16 = 4
#     √25 = 5
#
#
# Syntax:
#
#     np.sqrt(array)
# ============================================================

arr = np.array([4, 9, 16, 25])

result = np.sqrt(arr)

print("\nnp.sqrt():")
print(result)

# Output:
# [2. 3. 4. 5.]


# ============================================================
# DRY RUN - np.sqrt()
# ============================================================
#
#     √4  = 2
#     √9  = 3
#     √16 = 4
#     √25 = 5
#
# Result:
#
#     [2. 3. 4. 5.]
# ============================================================


# ============================================================
# 9. REAL-WORLD EXAMPLE - DISTANCE
# ============================================================
#
# Distance formula:
#
#     distance = √(x² + y²)
#
# Suppose:
#
#     x = 3
#     y = 4
#
# Then:
#
#     distance = √(3² + 4²)
#              = √(9 + 16)
#              = √25
#              = 5
# ============================================================

x = 3
y = 4

distance = np.sqrt(x ** 2 + y ** 2)

print("\nDistance:")
print(distance)

# Output:
# 5.0


# ============================================================
# 10. np.square()
# ============================================================
#
# np.square() calculates the SQUARE of every element.
#
# Mathematical formula:
#
#     square(x) = x²
#
# Syntax:
#
#     np.square(array)
# ============================================================

arr = np.array([2, 3, 4, 5])

result = np.square(arr)

print("\nnp.square():")
print(result)

# Output:
# [ 4  9 16 25]


# ============================================================
# DRY RUN
# ============================================================
#
#     2² = 4
#     3² = 9
#     4² = 16
#     5² = 25
#
# Result:
#
#     [4 9 16 25]
# ============================================================


# ============================================================
# 11. np.square() VS ** 2
# ============================================================
#
# These are equivalent for calculating squares:
#
#     np.square(arr)
#
# and:
#
#     arr ** 2
# ============================================================

arr = np.array([2, 3, 4])

print("\nUsing np.square():")
print(np.square(arr))

print("\nUsing ** 2:")
print(arr ** 2)

# Output:
# [4 9 16]
# [4 9 16]


# ============================================================
# 12. np.power()
# ============================================================
#
# np.power() calculates values raised to a specified power.
#
# Mathematical concept:
#
#     x^n
#
# means multiplying x by itself n times.
#
# Example:
#
#     2³ = 2 × 2 × 2 = 8
#
#
# Syntax:
#
#     np.power(array, exponent)
# ============================================================

arr = np.array([2, 3, 4])

result = np.power(arr, 3)

print("\nnp.power(arr, 3):")
print(result)

# Output:
# [ 8 27 64]


# ============================================================
# DRY RUN
# ============================================================
#
#     2³ = 8
#     3³ = 27
#     4³ = 64
#
# Result:
#
#     [8 27 64]
# ============================================================


# ============================================================
# 13. DIFFERENT POWERS
# ============================================================
#
# Same array can be raised to different powers.
# ============================================================

arr = np.array([2, 3, 4])

print("\nPower 2:")
print(np.power(arr, 2))

# Output:
# [ 4  9 16]

print("\nPower 3:")
print(np.power(arr, 3))

# Output:
# [ 8 27 64]

print("\nPower 4:")
print(np.power(arr, 4))

# Output:
# [ 16  81 256]


# ============================================================
# 14. np.abs()
# ============================================================
#
# np.abs() returns the ABSOLUTE VALUE.
#
# Absolute value means:
#
#     Distance from zero, ignoring the sign.
#
#
# Examples:
#
#     |-10| = 10
#     |-5|  = 5
#     |0|   = 0
#     |5|   = 5
#     |10|  = 10
#
#
# Syntax:
#
#     np.abs(array)
# ============================================================

arr = np.array([-10, -5, 0, 5, 10])

result = np.abs(arr)

print("\nnp.abs():")
print(result)

# Output:
# [10  5  0  5 10]


# ============================================================
# DRY RUN - np.abs()
# ============================================================
#
#     -10 -> 10
#      -5 -> 5
#       0 -> 0
#       5 -> 5
#      10 -> 10
#
# Result:
#
#     [10 5 0 5 10]
# ============================================================


# ============================================================
# 15. REAL-WORLD EXAMPLE - TEMPERATURE DIFFERENCE
# ============================================================
#
# Expected temperature:
#
#     30°C
#
# Actual temperatures:
#
#     28, 32, 25, 35
#
# We want to know how FAR each temperature is from 30.
#
# Formula:
#
#     difference = abs(actual - expected)
# ============================================================

actual = np.array([28, 32, 25, 35])

difference = np.abs(actual - 30)

print("\nTemperature differences:")
print(difference)

# Output:
# [2 2 5 5]


# ============================================================
# DRY RUN
# ============================================================
#
#     28 - 30 = -2
#     abs(-2) = 2
#
#     32 - 30 = 2
#     abs(2) = 2
#
#     25 - 30 = -5
#     abs(-5) = 5
#
#     35 - 30 = 5
#     abs(5) = 5
#
# Result:
#
#     [2 2 5 5]
#
# Useful when we care about how far a value is from a target,
# regardless of whether it is above or below.
# ============================================================


# ============================================================
# 16. np.exp()
# ============================================================
#
# np.exp(x) calculates:
#
#     e^x
#
# where:
#
#     e ≈ 2.71828
#
# This is called the EXPONENTIAL FUNCTION.
#
#
# Syntax:
#
#     np.exp(array)
# ============================================================

arr = np.array([0, 1, 2])

result = np.exp(arr)

print("\nnp.exp():")
print(result)

# Output approximately:
# [1.         2.71828183 7.3890561]


# ============================================================
# DRY RUN - np.exp()
# ============================================================
#
#     e⁰ = 1
#     e¹ ≈ 2.718
#     e² ≈ 7.389
# ============================================================


# ============================================================
# 17. WHERE IS np.exp() USED?
# ============================================================
#
# np.exp() is important in:
#
#     Statistics
#     Machine Learning
#     Neural Networks
#     Probability
#     Exponential growth
#     Exponential decay
#
#
# Example:
#
# Sigmoid function:
#
#     sigmoid(x) = 1 / (1 + e^(-x))
#
# You don't need to memorize the complete formula now.
#
# Remember:
#
#     np.exp() calculates exponential values.
#
# It is heavily used in Data Science and Machine Learning.
# ============================================================


# ============================================================
# 18. np.log()
# ============================================================
#
# np.log() calculates the NATURAL LOGARITHM.
#
# Natural logarithm has base:
#
#     e
#
#
# Mathematical relationship:
#
# If:
#
#     e^x = y
#
# then:
#
#     ln(y) = x
#
#
# Therefore:
#
#     ln(e) = 1
#     ln(1) = 0
#
#
# Syntax:
#
#     np.log(array)
# ============================================================

arr = np.array([1, np.e, np.e ** 2])

result = np.log(arr)

print("\nnp.log():")
print(result)

# Output approximately:
# [0. 1. 2.]


# ============================================================
# 19. np.log() DRY RUN
# ============================================================
#
#     ln(1)   = 0
#     ln(e)   = 1
#     ln(e²)  = 2
#
# Result:
#
#     [0. 1. 2.]
# ============================================================


# ============================================================
# 20. exp() AND log() RELATIONSHIP
# ============================================================
#
# These functions are mathematical opposites.
#
#     exp(x) -> e^x
#
#     log(x) -> ln(x)
#
#
# Example:
#
#     exp(2)   -> e²
#
#     log(e²)  -> 2
#
#
# Therefore:
#
#     np.log(np.exp(x)) = x
#
# for appropriate finite real values.
# ============================================================

x = 2

print("\nexp(2):")
print(np.exp(x))

print("\nlog(exp(2)):")
print(np.log(np.exp(x)))

# Output approximately:
# 7.389056...
# 2.0


# ============================================================
# 21. COMPLETE MATHEMATICAL FUNCTIONS EXAMPLE
# ============================================================

arr = np.array([-4, -1, 0, 1, 4])

print("\n" + "=" * 60)
print("COMPLETE MATHEMATICAL FUNCTIONS")
print("=" * 60)

print("\nAbsolute:")
print(np.abs(arr))

# Output:
# [4 1 0 1 4]

print("\nSquare:")
print(np.square(arr))

# Output:
# [16  1  0  1 16]

print("\nPower 3:")
print(np.power(arr, 3))

# Output:
# [-64  -1   0   1  64]


# ============================================================
# 22. ALL CHAPTER 7 FUNCTIONS
# ============================================================
#
# np.add()
#     -> a + b
#
# np.subtract()
#     -> a - b
#
# np.multiply()
#     -> a × b
#
# np.divide()
#     -> a ÷ b
#
# np.sqrt()
#     -> √x
#
# np.square()
#     -> x²
#
# np.power()
#     -> xⁿ
#
# np.abs()
#     -> |x|
#
# np.exp()
#     -> eˣ
#
# np.log()
#     -> ln(x)
# ============================================================


# ============================================================
# 23. UNIVERSAL FUNCTIONS / VECTORIZED OPERATIONS
# ============================================================
#
# NumPy mathematical functions generally operate
# element by element on arrays.
#
# Example:
#
#     arr = [1, 4, 9, 16]
#
#     np.sqrt(arr)
#
# NumPy effectively performs:
#
#     √1
#     √4
#     √9
#     √16
#
# Result:
#
#     [1. 2. 3. 4.]
#
# This is one reason NumPy is useful for numerical computing.
# ============================================================

arr = np.array([1, 4, 9, 16])

print("\nVectorized square root:")
print(np.sqrt(arr))

# Output:
# [1. 2. 3. 4.]


# ============================================================
# 24. PYTHON math VS NUMPY
# ============================================================
#
# Python has the math module.
#
# Example:
#
#     import math
#     math.sqrt(16)
#
# This works with an individual scalar value.
#
#
# NumPy is designed to work directly with arrays.
#
#     arr = np.array([1, 4, 9, 16])
#
#     np.sqrt(arr)
#
# Result:
#
#     [1. 2. 3. 4.]
#
#
# Easy memory:
#
#     math -> individual scalar values
#
#     NumPy -> arrays + numerical computing
# ============================================================


import math

print("\nPython math.sqrt():")
print(math.sqrt(16))

print("\nNumPy np.sqrt() with array:")
print(np.sqrt(np.array([1, 4, 9, 16])))


# ============================================================
# 25. REAL-WORLD EXAMPLE - STUDENT DATA
# ============================================================
#
# Suppose we have marks:
#
#     [25, 36, 49, 64, 81, 100]
# ============================================================

marks = np.array([25, 36, 49, 64, 81, 100])

print("\nStudent Marks:")
print(marks)


# ============================================================
# SQUARE ROOT OF MARKS
# ============================================================

print("\nSquare root:")
print(np.sqrt(marks))

# Output:
# [ 5.  6.  7.  8.  9. 10.]


# ============================================================
# SQUARE OF MARKS
# ============================================================

print("\nSquare:")
print(np.square(marks))


# ============================================================
# ABSOLUTE DIFFERENCE FROM 50
# ============================================================
#
# We calculate:
#
#     |marks - 50|
# ============================================================

print("\nAbsolute difference from 50:")
print(np.abs(marks - 50))


# ============================================================
# 26. COMMON MISTAKE - FORGETTING np.
# ============================================================
#
# Wrong:
#
#     sqrt(arr)
#
# unless sqrt was separately imported.
#
# Preferred beginner style:
#
#     np.sqrt(arr)
#
# Same idea applies to:
#
#     np.square()
#     np.power()
#     np.abs()
#     np.exp()
#     np.log()
# ============================================================


# ============================================================
# 27. COMMON MISTAKE - square() VS sqrt()
# ============================================================
#
# square:
#
#     x²
#
# sqrt:
#
#     √x
#
#
# Example:
#
#     square(4) -> 16
#
#     sqrt(4)   -> 2
# ============================================================

print("\nSquare of 4:")
print(np.square(4))

print("\nSquare root of 4:")
print(np.sqrt(4))


# ============================================================
# 28. COMMON MISTAKE - power() VS sqrt()
# ============================================================
#
#     np.power(arr, 2)
#
# means:
#
#     arr²
#
#
# while:
#
#     np.sqrt(arr)
#
# means:
#
#     √arr
# ============================================================


# ============================================================
# 29. COMMON MISTAKE - np.log()
# ============================================================
#
# IMPORTANT:
#
#     np.log(x)
#
# means NATURAL LOGARITHM.
#
# Base:
#
#     e
#
#
# For base-10 logarithm:
#
#     np.log10(x)
#
# This chapter focuses on:
#
#     np.log()
# ============================================================


# ============================================================
# 30. PRACTICE PROGRAM
# ============================================================
#
# Run this in VS Code.
# ============================================================

arr = np.array([1, 4, 9, 16, 25])

print("\n" + "=" * 60)
print("PRACTICE PROGRAM")
print("=" * 60)

print("\nOriginal:")
print(arr)

print("\nSquare root:")
print(np.sqrt(arr))

print("\nSquare:")
print(np.square(arr))

print("\nPower 2:")
print(np.power(arr, 2))

print("\nAbsolute:")
print(np.abs(arr))

# Expected output:
#
# Original:
# [ 1  4  9 16 25]
#
# Square root:
# [1. 2. 3. 4. 5.]
#
# Square:
# [  1  16  81 256 625]
#
# Power 2:
# [  1  16  81 256 625]
#
# Absolute:
# [ 1  4  9 16 25]


# ============================================================
# 31. MINI CODING EXERCISE
# ============================================================
#
# Create:
#
#     numbers = [-16, -9, -4, 0, 4, 9, 16]
#
# Find:
#
#     1. Absolute values
#     2. Squares
#     3. Cubes
#     4. Square roots
#     5. Positive array and its square roots
# ============================================================

numbers = np.array([-16, -9, -4, 0, 4, 9, 16])


# ============================================================
# 1. ABSOLUTE VALUES
# ============================================================

print("\n1. Absolute values:")
print(np.abs(numbers))

# Output:
# [16  9  4  0  4  9 16]


# ============================================================
# 2. SQUARES
# ============================================================

print("\n2. Squares:")
print(np.square(numbers))

# Output:
# [256  81  16   0  16  81 256]


# ============================================================
# 3. CUBES
# ============================================================
#
# Cube means:
#
#     x³
#
# Use:
#
#     np.power(numbers, 3)
# ============================================================

print("\n3. Cubes:")
print(np.power(numbers, 3))

# Output:
# [-4096  -729   -64     0    64   729  4096]


# ============================================================
# 4. SQUARE ROOTS OF numbers
# ============================================================
#
# IMPORTANT:
#
# numbers contains negative values.
#
# The real-number square root of a negative number is not
# a real number.
#
# Therefore NumPy will produce nan values for negative
# inputs in the real-valued calculation and may display
# a RuntimeWarning.
#
# The non-negative values can still produce square roots.
# ============================================================

print("\n4. Square roots:")
print(np.sqrt(numbers))

# Expected concept:
#
# Negative values -> nan
# 0              -> 0
# 4              -> 2
# 9              -> 3
# 16             -> 4


# ============================================================
# 5. POSITIVE ARRAY AND SQUARE ROOTS
# ============================================================
#
# Create a positive array first.
# ============================================================

positive_numbers = np.array([0, 4, 9, 16, 25])

print("\n5. Positive array:")
print(positive_numbers)

print("\nSquare roots of positive array:")
print(np.sqrt(positive_numbers))

# Output:
# [0. 2. 3. 4. 5.]


# ============================================================
# 32. INTERVIEW QUESTIONS
# ============================================================
#
# Q1. What does np.sqrt() do?
#
# Answer:
# It calculates the square root of each element.
#
#
# Q2. What is the difference between np.square()
#     and np.sqrt()?
#
#     np.square(x) -> x²
#     np.sqrt(x)   -> √x
#
#
# Q3. What does np.power() do?
#
# Answer:
# It raises each element to a specified power.
#
# Example:
#
#     np.power([2, 3], 3)
#
# Output:
#
#     [8 27]
#
#
# Q4. What does np.abs() do?
#
# Answer:
# It returns the absolute value of each element.
#
#
# Q5. What does np.exp(x) calculate?
#
# Answer:
#
#     eˣ
#
#
# Q6. What does np.log(x) calculate?
#
# Answer:
# The natural logarithm:
#
#     ln(x)
#
#
# Q7. What is the relationship between exp() and log()?
#
# They are inverse mathematical operations:
#
#     log(exp(x)) = x
#
# for appropriate finite real values.
#
#
# Q8. What is the difference between a + b
#     and np.add(a, b)?
#
# Both perform element-wise addition for compatible arrays.
#
#     a + b
#
# uses the operator.
#
#     np.add(a, b)
#
# explicitly calls NumPy's addition function.
# ============================================================


# ============================================================
# 33. FINAL REVISION MAP
# ============================================================
#
#              NUMPY MATHEMATICAL FUNCTIONS
#                          |
#          ┌───────────────┼────────────────┐
#          ↓               ↓                ↓
#      Arithmetic      Power / Root        Other
#          |               |                |
#        add             square             abs
#        subtract        sqrt               exp
#        multiply        power              log
#        divide
#
#
# ============================================================
# MUST REMEMBER
# ============================================================
#
# np.add()       -> addition
#
# np.subtract()  -> subtraction
#
# np.multiply()  -> multiplication
#
# np.divide()    -> division
#
# np.sqrt()      -> √x
#
# np.square()    -> x²
#
# np.power()     -> xⁿ
#
# np.abs()       -> |x|
#
# np.exp()       -> eˣ
#
# np.log()       -> ln(x)
# ============================================================


# ============================================================
# 34. CHAPTER 7 QUIZ
# ============================================================
#
# Try answering WITHOUT looking at the previous sections.
#
# 1. What is np.sqrt(25)?
#
# 2. What is np.square(5)?
#
# 3. What is np.power(2, 4)?
#
# 4. What does np.abs(-20) return?
#
# 5. What does np.exp(0) return?
#
# 6. What does np.log(1) return?
#
# 7. What is the difference between np.square()
#    and np.power()?
#
# 8. What is the difference between np.sqrt()
#    and np.square()?
#
# 9. What does np.add() do?
#
# 10. What does np.log() represent mathematically?
# ============================================================


# ============================================================
# CHAPTER 7 COMPLETE ✅
# ============================================================
#
# NEXT:
#
# CHAPTER 8 - NUMPY STATISTICAL FUNCTIONS
#
# Topics:
#
#     np.sum()
#     np.mean()
#     np.median()
#     np.std()
#     np.var()
#     np.min()
#     np.max()
#     np.argmin()
#     np.argmax()
#     Percentiles
#     Axis concept
#
# ⭐ IMPORTANT:
#
# The AXIS concept is especially important because it will
# appear throughout:
#
#     NumPy
#     Pandas
#     Data Science
#
# ============================================================