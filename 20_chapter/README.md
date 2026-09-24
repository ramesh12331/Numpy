# 🚀 Chapter 20 — Advanced NumPy

Welcome to **Chapter 20**! 🎯

You already learned the core NumPy concepts from Chapters 1–19. Now we start the **advanced NumPy concepts used in Data Science and Machine Learning**.

Don't worry—we'll still learn from the beginner level and build step by step.

---

# 📚 What We Will Learn

1. ⚡ Vectorization
2. 🔥 Why vectorization is fast
3. 🧩 Universal Functions — ufuncs
4. 📐 Axis in depth
5. 🚀 Performance comparison
6. 💾 Memory efficiency
7. 🏗️ Structured arrays
8. 🎯 Advanced indexing
9. 🔢 Integer/fancy indexing
10. 🎭 Boolean + advanced indexing
11. 🌍 Real-world examples
12. ⚠️ Common mistakes
13. 🎤 Interview questions
14. 💻 Practice
15. 🧪 Mini project
16. 📝 Quiz

---

# 1️⃣ What is Vectorization?

### 📌 Definition

**Vectorization** means performing an operation on an entire NumPy array at once instead of manually processing each element with a Python loop.

For example:

### ❌ Python loop

```python
numbers = [10, 20, 30, 40]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

Output:

```text
[20, 40, 60, 80]
```

---

### ✅ NumPy vectorization

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

result = numbers * 2

print(result)
```

Output:

```text
[20 40 60 80]
```

### ⭐ Important

Instead of:

```text
element → loop → element → loop
```

NumPy lets you think:

```text
whole array
     ↓
operation
     ↓
whole result
```

---

# 2️⃣ Why Is Vectorization Important?

Suppose we have:

```text
1,000,000 numbers
```

With a Python loop:

```text
number 1 → process
number 2 → process
number 3 → process
...
number 1,000,000 → process
```

With NumPy:

```text
1,000,000 numbers
        ↓
   NumPy operation
        ↓
      result
```

NumPy operations are implemented using optimized compiled numerical routines, so they can be substantially faster than equivalent Python-level loops for many numerical workloads.

---

# 3️⃣ Simple Vectorization Example

```python
import numpy as np

prices = np.array([
    100,
    200,
    300,
    400
])

discount = prices * 0.10

print(discount)
```

Output:

```text
[10. 20. 30. 40.]
```

Final prices:

```python
final_prices = prices - discount

print(final_prices)
```

Output:

```text
[ 90. 180. 270. 360.]
```

### 🌍 Real-world use

This is common in:

* 💰 Sales analysis
* 📊 Data preprocessing
* 🤖 Machine Learning
* 📈 Financial calculations
* 🧪 Scientific computing

---

# 4️⃣ Vectorization vs Loop

Let's compare.

### Loop

```python
numbers = [10, 20, 30, 40]

result = []

for x in numbers:
    result.append(x * 5)

print(result)
```

### NumPy

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

result = numbers * 5

print(result)
```

### 🧠 Memory Trick

> **Loop → one element at a time**

> **Vectorization → whole array operation**

---

# 5️⃣ Vectorized Mathematical Operations

NumPy supports many vectorized operations.

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

print(arr + 10)
print(arr * 2)
print(arr ** 2)
print(np.sqrt(arr))
```

Output:

```text
[11 14 19 26 35]

[ 2  8 18 32 50]

[  1  16  81 256 625]

[1. 2. 3. 4. 5.]
```

No explicit Python loop is required.

---

# 6️⃣ What Are Universal Functions — ufuncs?

### 📌 Definition

A **ufunc**, or **Universal Function**, is a NumPy function designed to operate element-by-element on NumPy arrays.

Examples:

```python
np.add()
np.subtract()
np.multiply()
np.divide()
np.sqrt()
np.exp()
np.log()
np.sin()
np.cos()
```

---

# 7️⃣ Example of a ufunc

```python
import numpy as np

arr = np.array([1, 4, 9, 16])

result = np.sqrt(arr)

print(result)
```

Output:

```text
[1. 2. 3. 4.]
```

Conceptually:

```text
arr
 ↓
[1, 4, 9, 16]

sqrt()
 ↓
[1, 2, 3, 4]
```

---

# 8️⃣ Why Are ufuncs Useful?

Without NumPy:

```python
numbers = [1, 4, 9, 16]

result = []

for x in numbers:
    result.append(x ** 0.5)
```

With NumPy:

```python
arr = np.array([1, 4, 9, 16])

result = np.sqrt(arr)
```

Much cleaner.

---

# 9️⃣ Common NumPy ufuncs

| Ufunc           | Purpose           |
| --------------- | ----------------- |
| `np.add()`      | Addition          |
| `np.subtract()` | Subtraction       |
| `np.multiply()` | Multiplication    |
| `np.divide()`   | Division          |
| `np.sqrt()`     | Square root       |
| `np.square()`   | Square            |
| `np.power()`    | Power             |
| `np.abs()`      | Absolute value    |
| `np.exp()`      | Exponential       |
| `np.log()`      | Natural logarithm |
| `np.sin()`      | Sine              |
| `np.cos()`      | Cosine            |

---

# 🔟 Example — Multiple ufuncs

```python
import numpy as np

arr = np.array([
    -4,
    9,
    16,
    25
])

print("Absolute:")
print(np.abs(arr))

print("\nSquare Root:")
print(np.sqrt(np.abs(arr)))

print("\nSquare:")
print(np.square(arr))

print("\nPower:")
print(np.power(arr, 2))
```

---

# 1️⃣1️⃣ Axis in Depth ⭐⭐⭐

You learned `axis` in Chapter 8.

Now let's understand it more deeply.

Consider:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Visual:

```text
             Columns
          0     1     2

Row 0    10    20    30
Row 1    40    50    60
Row 2    70    80    90
```

---

# 1️⃣2️⃣ `axis=0`

Think:

> **Operate down the rows → calculate for each column**

```python
print(np.sum(arr, axis=0))
```

Output:

```text
[120 150 180]
```

Dry run:

```text
Column 0:

10
40
70

10 + 40 + 70 = 120
```

Column 1:

```text
20 + 50 + 80 = 150
```

Column 2:

```text
30 + 60 + 90 = 180
```

Therefore:

```text
[120, 150, 180]
```

---

# 1️⃣3️⃣ `axis=1`

Think:

> **Operate across columns → calculate for each row**

```python
print(np.sum(arr, axis=1))
```

Output:

```text
[60 150 240]
```

Dry run:

```text
Row 0:

10 + 20 + 30 = 60
```

```text
Row 1:

40 + 50 + 60 = 150
```

```text
Row 2:

70 + 80 + 90 = 240
```

---

# 🧠 Axis Memory Trick

For a 2D array:

```text
axis=0
   ↓
DOWN
   ↓
columns remain
```

```text
axis=1
   →
ACROSS
   →
rows remain
```

### ⭐ Remember

```text
axis=0 → column-wise result
axis=1 → row-wise result
```

---

# 1️⃣4️⃣ Axis With Mean

```python
import numpy as np

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print("Subject averages:")
print(np.mean(marks, axis=0))

print("\nStudent averages:")
print(np.mean(marks, axis=1))
```

Output:

```text
Subject averages:
[78.33333333 81.66666667 84.33333333]

Student averages:
[80.         73.33333333 91.        ]
```

Interpretation:

```text
axis=0
↓
average of each subject

axis=1
↓
average of each student
```

---

# 1️⃣5️⃣ Axis in 3D Arrays

Now things become more advanced.

Consider:

```python
arr = np.arange(24).reshape(2, 3, 4)
```

Shape:

```text
(2, 3, 4)
```

Meaning:

```text
2 layers
3 rows per layer
4 columns per row
```

Visual:

```text
Layer 0
---------
0   1   2   3
4   5   6   7
8   9  10  11


Layer 1
---------
12  13  14  15
16  17  18  19
20  21  22  23
```

Here there are **three axes**:

```text
axis=0 → layers
axis=1 → rows
axis=2 → columns
```

### 🧠 General idea

For shape:

```text
(2, 3, 4)
```

the axes correspond to:

```text
axis 0 → size 2
axis 1 → size 3
axis 2 → size 4
```

---

# 1️⃣6️⃣ Performance Comparison

We can compare a Python loop with NumPy vectorization.

```python
import numpy as np
import time


# ------------------------------------------------------------
# Python loop
# ------------------------------------------------------------

numbers = list(range(1_000_000))

start = time.perf_counter()

result = []

for x in numbers:
    result.append(x * 2)

loop_time = time.perf_counter() - start


# ------------------------------------------------------------
# NumPy vectorization
# ------------------------------------------------------------

arr = np.arange(1_000_000)

start = time.perf_counter()

result = arr * 2

numpy_time = time.perf_counter() - start


print("Python loop time:", loop_time)
print("NumPy time:", numpy_time)
```

You may see NumPy finish faster, although the exact timings depend on your machine, NumPy version, Python version, and workload.

### ⚠️ Important

Don't memorize:

> "NumPy is always X times faster."

The actual speedup depends on the operation and environment.

---

# 1️⃣7️⃣ Why NumPy Can Be Faster

A simplified picture:

```text
Python loop

Python
  ↓
loop
  ↓
Python operation
  ↓
Python operation
  ↓
Python operation
  ↓
...
```

NumPy:

```text
Python
  ↓
NumPy operation
  ↓
optimized compiled implementation
  ↓
result
```

This is one reason NumPy is widely used for numerical computing.

---

# 1️⃣8️⃣ Memory Efficiency ⭐

NumPy arrays store elements in a compact, typed representation.

Example:

```python
import numpy as np

arr32 = np.zeros(
    1_000_000,
    dtype=np.int32
)

arr64 = np.zeros(
    1_000_000,
    dtype=np.int64
)

print(arr32.nbytes)
print(arr64.nbytes)
```

Output:

```text
4000000
8000000
```

So:

```text
int32 → 4 MB approximately
int64 → 8 MB approximately
```

---

# 1️⃣9️⃣ Choosing a dtype

Suppose you know your data contains:

```text
Age:
0–120
```

Using an unnecessarily large integer type may consume more memory than required.

However:

> ⭐ **Choose a dtype that safely supports the required range and precision.**

Don't simply choose the smallest dtype.

---

# 2️⃣0️⃣ Structured Arrays

Now let's learn a more advanced feature.

A normal NumPy array generally has one dtype for its elements.

But sometimes we want records with multiple fields.

For example:

```text
Employee

ID     Age     Salary
101    25      50000
102    30      60000
103    28      55000
```

A **structured array** lets us define fields with different data types.

---

# 2️⃣1️⃣ Creating a Structured Array

```python
import numpy as np

employee_dtype = np.dtype([
    ("id", "i4"),
    ("age", "i4"),
    ("salary", "f8")
])

employees = np.array([
    (101, 25, 50000.0),
    (102, 30, 60000.0),
    (103, 28, 55000.0)
], dtype=employee_dtype)

print(employees)
```

Output will look similar to:

```text
[(101, 25, 50000.) (102, 30, 60000.) (103, 28, 55000.)]
```

---

# 2️⃣2️⃣ Access a Field

We can access:

```python
print(employees["id"])
```

Output:

```text
[101 102 103]
```

Age:

```python
print(employees["age"])
```

Output:

```text
[25 30 28]
```

Salary:

```python
print(employees["salary"])
```

Output:

```text
[50000. 60000. 55000.]
```

---

# 2️⃣3️⃣ Structured Array Visual

Think:

```text
employees
│
├── id
│    └── [101, 102, 103]
│
├── age
│    └── [25, 30, 28]
│
└── salary
     └── [50000, 60000, 55000]
```

This is useful for understanding structured numerical records.

For general tabular data analysis, however, **Pandas DataFrames are usually more convenient**.

---

# 2️⃣4️⃣ Advanced Indexing

You already learned normal indexing:

```python
arr[2]
```

Advanced indexing allows us to select multiple specific positions using arrays/lists of indices.

This is sometimes called:

> **Fancy indexing**

---

# 2️⃣5️⃣ Integer/Fancy Indexing

Example:

```python
import numpy as np

arr = np.array([
    10,
    20,
    30,
    40,
    50
])

result = arr[[0, 2, 4]]

print(result)
```

Output:

```text
[10 30 50]
```

We selected:

```text
index 0 → 10
index 2 → 30
index 4 → 50
```

---

# 2️⃣6️⃣ Visual

```text
Index:
  0    1    2    3    4
  ↓    ↓    ↓    ↓    ↓
[10] [20] [30] [40] [50]
 ↑         ↑         ↑
 0         2         4
```

Result:

```text
[10 30 50]
```

---

# 2️⃣7️⃣ Selecting Rows Using Advanced Indexing

Consider:

```python
students = np.array([
    [101, 80],
    [102, 90],
    [103, 70],
    [104, 95]
])
```

Select rows 0 and 2:

```python
result = students[[0, 2]]

print(result)
```

Output:

```text
[[101  80]
 [103  70]]
```

---

# 2️⃣8️⃣ Selecting Specific Rows and Columns

We can combine arrays of row and column indices.

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

rows = [0, 1, 2]
columns = [2, 0, 1]

result = arr[rows, columns]

print(result)
```

Output:

```text
[30 40 80]
```

Why?

```text
arr[0, 2] → 30
arr[1, 0] → 40
arr[2, 1] → 80
```

---

# 2️⃣9️⃣ Boolean + Advanced Indexing

You can combine concepts you've already learned.

```python
marks = np.array([
    [101, 80],
    [102, 45],
    [103, 90],
    [104, 35]
])

result = marks[marks[:, 1] >= 50]

print(result)
```

Output:

```text
[[101  80]
 [103  90]]
```

This combines:

```text
Chapter 4 → indexing
Chapter 15 → Boolean masking
Chapter 20 → advanced indexing
```

---

# 3️⃣0️⃣ Advanced Indexing vs Slicing

This is important.

### Slicing

```python
arr[1:4]
```

Selects a continuous range.

### Advanced indexing

```python
arr[[1, 3, 4]]
```

Selects specific positions.

Visual:

```text
Slicing:
[10, 20, 30, 40, 50]
      └──────────┘
        20,30,40


Advanced indexing:
[10, 20, 30, 40, 50]
      ↑       ↑   ↑
     20      40  50
```

---

# 3️⃣1️⃣ Copy Behavior — Important Advanced Point

Advanced indexing generally produces a **copy**, rather than a view.

Example:

```python
arr = np.array([
    10,
    20,
    30,
    40
])

selected = arr[[0, 2]]

selected[0] = 999

print("Selected:")
print(selected)

print("Original:")
print(arr)
```

Output:

```text
Selected:
[999  30]

Original:
[10 20 30 40]
```

The original array was not changed.

This is different from many slicing operations, which commonly return views.

---

# 3️⃣2️⃣ Vectorization + Boolean Masking

These concepts become extremely powerful together.

Example:

```python
salary = np.array([
    30000,
    45000,
    60000,
    75000,
    90000
])

salary[salary > 50000] = salary[salary > 50000] * 1.10

print(salary)
```

Output:

```text
[30000 45000 66000 82500 99000]
```

We performed a calculation on selected values **without writing a Python loop**.

---

# 3️⃣3️⃣ Real-World Example — Employee Salary Adjustment

Suppose:

```python
salary = np.array([
    30000,
    45000,
    60000,
    75000,
    90000
])
```

Company rule:

> Employees earning more than ₹50,000 receive a 10% increase.

NumPy:

```python
salary[salary > 50000] *= 1.10

print(salary)
```

Output:

```text
[30000 45000 66000 82500 99000]
```

### Flow

```text
Salary
   ↓
salary > 50000
   ↓
True / False mask
   ↓
Select matching salaries
   ↓
Multiply by 1.10
```

This is a very common Data Science pattern.

---

# 3️⃣4️⃣ Complete Advanced NumPy Program

```python
# ============================================================
# NUMPY - ADVANCED CONCEPTS
# ============================================================

import numpy as np


# ============================================================
# 1. VECTORIZATION
# ============================================================

numbers = np.array([10, 20, 30, 40])

result = numbers * 2

print("Vectorized Multiplication:")
print(result)


# ============================================================
# 2. UNIVERSAL FUNCTION - SQRT
# ============================================================

arr = np.array([1, 4, 9, 16])

result = np.sqrt(arr)

print("\nSquare Root:")
print(result)


# ============================================================
# 3. AXIS
# ============================================================

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print("\nSubject Total:")
print(np.sum(marks, axis=0))

print("\nStudent Total:")
print(np.sum(marks, axis=1))


# ============================================================
# 4. ADVANCED INDEXING
# ============================================================

numbers = np.array([
    10,
    20,
    30,
    40,
    50
])

selected = numbers[[0, 2, 4]]

print("\nAdvanced Indexing:")
print(selected)


# ============================================================
# 5. BOOLEAN MASKING
# ============================================================

salary = np.array([
    30000,
    45000,
    60000,
    75000,
    90000
])

high_salary = salary[salary > 50000]

print("\nHigh Salaries:")
print(high_salary)


# ============================================================
# 6. VECTORIZED SALARY UPDATE
# ============================================================

salary[salary > 50000] *= 1.10

print("\nUpdated Salaries:")
print(salary)


# ============================================================
# 7. STRUCTURED ARRAY
# ============================================================

employee_dtype = np.dtype([
    ("id", "i4"),
    ("age", "i4"),
    ("salary", "f8")
])

employees = np.array([
    (101, 25, 50000),
    (102, 30, 60000),
    (103, 28, 55000)
], dtype=employee_dtype)

print("\nEmployees:")
print(employees)

print("\nEmployee IDs:")
print(employees["id"])

print("\nEmployee Salaries:")
print(employees["salary"])
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Thinking vectorization means no loops exist anywhere

Vectorization means **you don't need to write the Python-level loop for many array operations**.

Internally, NumPy still performs the necessary computation.

---

## ❌ Mistake 2 — Confusing `axis=0` and `axis=1`

For a 2D array:

```text
axis=0 → down → column-wise result
axis=1 → across → row-wise result
```

---

## ❌ Mistake 3 — Confusing `*` and `@`

```python
A * B
```

→ element-wise multiplication

```python
A @ B
```

→ matrix multiplication

---

## ❌ Mistake 4 — Thinking advanced indexing always returns a view

Integer/fancy indexing generally produces a **copy**.

---

## ❌ Mistake 5 — Choosing dtype only based on memory

Don't automatically use the smallest dtype.

Consider:

```text
Range
Precision
Memory
Performance
```

---

# 🎤 Interview Questions

### Q1. What is vectorization?

**Answer:**
Vectorization is performing operations on entire NumPy arrays without explicitly writing a Python loop for each element.

---

### Q2. Why is NumPy vectorization usually faster than Python loops?

**Answer:**
NumPy operations use optimized compiled numerical implementations, reducing Python-level loop overhead.

---

### Q3. What is a ufunc?

**Answer:**
A ufunc, or Universal Function, is a NumPy function that performs element-wise operations efficiently on arrays.

Examples:

```python
np.sqrt()
np.add()
np.exp()
```

---

### Q4. What does `axis=0` mean for a 2D array?

**Answer:**
It performs the reduction down rows, producing one result for each column.

---

### Q5. What does `axis=1` mean?

**Answer:**
It performs the reduction across columns, producing one result for each row.

---

### Q6. What is fancy indexing?

**Answer:**
Fancy indexing, also called integer-array indexing, uses arrays or lists of indices to select specific elements.

Example:

```python
arr[[0, 2, 4]]
```

---

### Q7. What is a structured array?

**Answer:**
A structured array is a NumPy array whose records can contain named fields with different data types.

---

### Q8. What is vectorized salary processing?

Example:

```python
salary[salary > 50000] *= 1.10
```

It applies the calculation to all selected values without an explicit Python loop.

---

# 💻 Practice

## Practice 1 — Vectorization

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
```

Calculate:

```text
arr × 5
arr + 100
arr²
sqrt(arr)
```

---

## Practice 2 — Axis

Given:

```python
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])
```

Find:

1. Total for each student
2. Total for each subject
3. Average for each student
4. Average for each subject

---

## Practice 3 — Advanced Indexing

Given:

```python
arr = np.array([
    10,
    20,
    30,
    40,
    50,
    60
])
```

Select:

```text
10
30
60
```

using advanced indexing.

---

# 🧩 Mini Project — Employee Salary Analysis

Create:

```python
employees = np.array([
    [101, 25, 30000],
    [102, 30, 55000],
    [103, 28, 45000],
    [104, 35, 75000],
    [105, 40, 90000]
])
```

Columns:

```text
Employee ID
Age
Salary
```

### Task 1

Extract salaries:

```python
salary = employees[:, 2]
```

### Task 2

Find salaries above `50000`.

### Task 3

Give those employees a 10% salary increase.

### Task 4

Find:

```text
Average salary
Maximum salary
Minimum salary
```

### Task 5

Find employees older than 30.

This mini project combines:

```text
Indexing
Boolean Masking
Vectorization
Statistics
Advanced NumPy
```

---

# 🧠 Chapter 20 Memory Map

```text
                    ADVANCED NUMPY
                         │
       ┌─────────────────┼─────────────────┐
       ↓                 ↓                 ↓
 Vectorization         ufuncs             Axis
       │                 │                 │
       ↓                 ↓                 ↓
 Fast array          sqrt/add/etc.     axis 0 / 1 / 2
 operations
       │
       ├───────────────┐
       ↓               ↓
 Performance        Memory
       │               │
       ↓               ↓
 optimized          dtype
 operations         itemsize
                    nbytes
       │
       └───────────────┐
                       ↓
                Advanced Indexing
                       │
                 ┌─────┴─────┐
                 ↓           ↓
              Integer     Boolean
              indexing     masking
```

---

# ⭐ Final Summary

| Concept           | Key idea                                                      |
| ----------------- | ------------------------------------------------------------- |
| Vectorization     | Operate on arrays without explicit Python loops               |
| ufunc             | NumPy element-wise universal function                         |
| `axis=0`          | Reduction down rows → one result per column                   |
| `axis=1`          | Reduction across columns → one result per row                 |
| `axis=2`          | Third dimension in suitable higher-dimensional arrays         |
| Performance       | Vectorized NumPy operations often reduce Python-loop overhead |
| Memory efficiency | Choose appropriate dtype                                      |
| Structured array  | Named fields with potentially different dtypes                |
| Fancy indexing    | Select specific positions using index arrays                  |
| Boolean indexing  | Select data using True/False conditions                       |

---

# 🔥 10 Things to Remember

```text
1️⃣ Vectorization → whole array operation

2️⃣ ufunc → NumPy universal function

3️⃣ np.sqrt(arr) → vectorized square root

4️⃣ axis=0 → column-wise result

5️⃣ axis=1 → row-wise result

6️⃣ dtype affects memory and numerical representation

7️⃣ arr[[0, 2, 4]] → advanced indexing

8️⃣ arr[arr > 50] → Boolean filtering

9️⃣ Advanced integer indexing generally creates a copy

🔟 Vectorization + Boolean masking = powerful Data Science pattern
```

---

# 🧪 Chapter 20 Quiz

### Q1. What is vectorization?

A. Converting arrays to lists
B. Performing array operations without explicit Python-level loops
C. Sorting an array
D. Reshaping an array

### Q2. What is a ufunc?

A. A Pandas function
B. A Python loop
C. A NumPy Universal Function
D. A database function

### Q3. What does this do?

```python
np.sqrt(arr)
```

A. Adds values
B. Finds square roots
C. Squares values
D. Finds maximum

### Q4. For:

```python
arr.shape == (3, 4)
```

what does `axis=0` reduce over?

A. Columns
B. Rows
C. Entire array only
D. Nothing

### Q5. For a 2D array, what does `axis=1` produce?

A. One result per row
B. One result per column
C. One result per dimension
D. No result

### Q6. What is:

```python
arr[[0, 2, 4]]
```

?

A. Slicing
B. Fancy/integer indexing
C. Reshaping
D. Broadcasting

### Q7. What does this do?

```python
salary[salary > 50000]
```

A. Finds salaries below 50,000
B. Finds salaries above 50,000
C. Sorts salaries
D. Deletes salaries

### Q8. What does a structured array provide?

A. Only strings
B. Named fields that can have different dtypes
C. Only 3D arrays
D. Only Boolean values

### Q9. Which operation is matrix multiplication?

A. `A * B`
B. `A + B`
C. `A @ B`
D. `A / B`

### Q10. Why can vectorized NumPy code be faster than a Python loop?

A. NumPy never performs calculations
B. NumPy uses optimized compiled numerical operations
C. NumPy deletes data
D. NumPy converts everything to strings

---

## 🏁 Chapter 20 — COMPLETE

You have now completed the **Advanced NumPy fundamentals**:

**Vectorization → ufuncs → axis → performance → memory efficiency → structured arrays → advanced indexing → Boolean + integer indexing**.

### 🚀 Next → Chapter 21 — NumPy for Data Science

We will connect everything you've learned to real Data Science work:

**Data preprocessing → numerical calculations → statistics → Machine Learning → feature engineering → image processing → scientific computing → real-world datasets → mini project → quiz.**

Type **NEXT** when ready.
