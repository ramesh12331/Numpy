# 🧮 NumPy Complete Course
# Chapter 2 — Creating Arrays

> 🎯 **Chapter Goal:** Learn how to create NumPy arrays from the ground up: **`np.array()` → 1D → 2D → 3D → `dtype` → `ndmin` → zeros → ones → full → empty → arange → linspace → eye → random arrays**.

---

# 1. ⭐ What is a NumPy Array?

## 📌 Definition

A **NumPy array** is a collection of values arranged in one or more dimensions.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
```

Visual:

```text
arr
 ↓
┌────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │
└────┴────┴────┴────┘
```

🔥 **Important:** NumPy arrays are the fundamental data structure we will use throughout this course.

---

# 2. ⭐ `np.array()`

## 📌 Definition

`np.array()` converts a Python sequence, such as a list, into a NumPy array.

## Syntax

```python
np.array(object)
```

Common form:

```python
np.array([value1, value2, value3])
```

---

## 💻 Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

### Output

```text
[10 20 30 40]
```

### 🔎 Line-by-line

```python
import numpy as np
```

➡️ Imports NumPy.

```python
arr = np.array([10, 20, 30, 40])
```

➡️ Converts the Python list into a NumPy array.

```python
print(arr)
```

➡️ Displays the array.

---

# 3. 🟢 1D Array

## 📌 Definition

A **1D array** is a one-dimensional sequence of values.

Think of it as a **single row**.

```python
arr = np.array([10, 20, 30, 40])
```

Visual:

```text
Index →   0    1    2    3
          ↓    ↓    ↓    ↓
        ┌────┬────┬────┬────┐
        │ 10 │ 20 │ 30 │ 40 │
        └────┴────┴────┴────┘
```

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.ndim)
```

Output:

```text
[10 20 30 40]
1
```

🔥 `ndim` tells us the number of dimensions.

We will study `ndim` deeply in **Chapter 3**.

---

# 4. 🟡 2D Array

## 📌 Definition

A **2D array** contains rows and columns.

Think of it like a **table**.

### Example

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)
```

### Output

```text
[[10 20 30]
 [40 50 60]]
```

Visual:

```text
        Column
         ↓↓↓
       0   1   2
       ↓   ↓   ↓
    ┌────┬────┬────┐
 0  │ 10 │ 20 │ 30 │
    ├────┼────┼────┤
 1  │ 40 │ 50 │ 60 │
    └────┴────┴────┘
      ↑
     Row
```

This array has:

```text
2 rows
3 columns
```

So its shape is:

```text
(2, 3)
```

We will study `shape` in detail in Chapter 3.

---

# 5. 🔵 3D Array

## 📌 Definition

A **3D array** is an array containing multiple 2D arrays.

Think of it like multiple tables stacked together.

Example:

```python
import numpy as np

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

print(arr)
```

### Output

```text
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

Visual:

```text
3D Array
│
├── Matrix 1
│   ┌───────────┐
│   │ 1  2  3   │
│   │ 4  5  6   │
│   └───────────┘
│
└── Matrix 2
    ┌───────────┐
    │ 7  8  9   │
    │10 11 12   │
    └───────────┘
```

### Mathematical structure

```text
2 matrices
× 2 rows
× 3 columns
```

So the shape is:

```text
(2, 2, 3)
```

---

# 6. 🧠 1D vs 2D vs 3D

| Dimension | Example | Meaning |
|---|---|---|
| **1D** | `[1,2,3]` | One sequence |
| **2D** | `[[1,2],[3,4]]` | Rows + columns |
| **3D** | `[[[1,2],[3,4]]]` | Collection of 2D arrays |

### 🧠 Memory Trick

```text
1D → Line
2D → Table
3D → Stack of Tables
```

---

# 7. ⭐ `dtype`

## 📌 Definition

`dtype` means **data type**.

It tells NumPy what type of values the array contains.

Common types include:

```text
int
float
bool
complex
```

---

## Example

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr.dtype)
```

Possible output:

```text
int64
```

The exact integer dtype can depend on your platform/environment.

---

# 8. Specifying `dtype`

You can explicitly choose a dtype.

### Syntax

```python
np.array(data, dtype=data_type)
```

### Example

```python
import numpy as np

arr = np.array([10, 20, 30], dtype="float64")

print(arr)
print(arr.dtype)
```

### Output

```text
[10. 20. 30.]
float64
```

### 🧮 Dry Run

Original values:

```text
10
20
30
```

Converted to floating-point values:

```text
10.0
20.0
30.0
```

---

# 9. 🔥 Why is `dtype` Important?

Suppose you are storing:

```text
Student marks
Employee salaries
Temperature
Age
Prices
```

The data type affects how NumPy stores and processes those values.

Example:

```python
arr = np.array([10, 20, 30], dtype="int32")
```

versus:

```python
arr = np.array([10, 20, 30], dtype="float64")
```

The first stores integers, while the second stores floating-point numbers.

---

# 10. ⭐ `ndmin`

## 📌 Definition

`ndmin` specifies the **minimum number of dimensions** for the resulting array.

### Syntax

```python
np.array(data, ndmin=n)
```

---

## Example

Normally:

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
print(arr.ndim)
```

Output:

```text
[1 2 3]
1
```

Now use:

```python
arr = np.array([1, 2, 3], ndmin=2)

print(arr)
print(arr.ndim)
```

Output:

```text
[[1 2 3]]
2
```

Visual:

```text
Before:
[1 2 3]

After ndmin=2:
[[1 2 3]]
```

🔥 **Important:**

`ndmin=2` does not mean "make exactly 2 dimensions" in every situation.

It means:

> **Make sure the array has at least 2 dimensions.**

---

# 11. 🟢 `np.zeros()`

## 📌 Definition

`np.zeros()` creates an array filled with **zeros**.

## Syntax

```python
np.zeros(shape)
```

---

## Example — 1D

```python
import numpy as np

arr = np.zeros(5)

print(arr)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

By default, the values are floating-point zeros.

---

## Example — 2D

```python
arr = np.zeros((2, 3))

print(arr)
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

Visual:

```text
┌─────┬─────┬─────┐
│ 0.  │ 0.  │ 0.  │
├─────┼─────┼─────┤
│ 0.  │ 0.  │ 0.  │
└─────┴─────┴─────┘
```

### Mathematical concept

`(2, 3)` means:

```text
2 rows × 3 columns
```

Total elements:

```text
2 × 3 = 6
```

---

# 12. 🟢 `np.ones()`

## 📌 Definition

`np.ones()` creates an array filled with **ones**.

### Syntax

```python
np.ones(shape)
```

### Example

```python
import numpy as np

arr = np.ones((2, 3))

print(arr)
```

### Output

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

---

# 13. 🟡 `np.full()`

## 📌 Definition

`np.full()` creates an array where **every element has the specified value**.

### Syntax

```python
np.full(shape, value)
```

### Example

```python
import numpy as np

arr = np.full((2, 3), 7)

print(arr)
```

### Output

```text
[[7 7 7]
 [7 7 7]]
```

### 🧠 Memory Trick

```text
zeros → fill with 0
ones  → fill with 1
full  → fill with your value
```

---

# 14. 🟠 `np.empty()`

## 📌 Definition

`np.empty()` creates an array **without initializing its elements to a particular value**.

### Syntax

```python
np.empty(shape)
```

### Example

```python
import numpy as np

arr = np.empty((2, 3))

print(arr)
```

The output values are **not predictable** and depend on the existing memory contents.

For example, you might see values similar to:

```text
[[6.9e-310 0.0e+000 4.9e-324]
 [0.0e+000 1.2e-322 0.0e+000]]
```

⚠️ Do **not** expect zeros.

### 🧠 Difference

```text
zeros() → initialized to 0
empty() → values are uninitialized
```

---

# 15. 🔢 `np.arange()`

## 📌 Definition

`np.arange()` creates a sequence of values using a **step size**.

### Syntax

```python
np.arange(start, stop, step)
```

`stop` is normally **excluded**.

---

## Example

```python
import numpy as np

arr = np.arange(1, 10)

print(arr)
```

Output:

```text
[1 2 3 4 5 6 7 8 9]
```

### Dry Run

Start:

```text
1
```

Continue with default step:

```text
+1
```

Stop before:

```text
10
```

Therefore:

```text
1 2 3 4 5 6 7 8 9
```

---

## Example with step

```python
arr = np.arange(0, 11, 2)

print(arr)
```

Output:

```text
[ 0  2  4  6  8 10]
```

### Mathematical dry run

```text
0
↓ +2
2
↓ +2
4
↓ +2
6
↓ +2
8
↓ +2
10
```

---

# 16. 🔥 `arange()` Parameters

```python
np.arange(start, stop, step)
```

Example:

```python
np.arange(2, 12, 3)
```

Dry run:

```text
2
5
8
11
```

Output:

```text
[ 2  5  8 11]
```

The next value would be:

```text
14
```

which is outside the stop boundary.

---

# 17. 🔵 `np.linspace()`

## 📌 Definition

`np.linspace()` creates a specified number of **evenly spaced values** between a start and stop value.

### Syntax

```python
np.linspace(start, stop, num)
```

By default, both the start and stop values are included.

---

## Example

```python
import numpy as np

arr = np.linspace(0, 10, 5)

print(arr)
```

### Output

```text
[ 0.   2.5  5.   7.5 10. ]
```

---

# 18. 🧮 `linspace()` Mathematical Dry Run

We want:

```text
Start = 0
Stop = 10
Number of values = 5
```

Distance:

```text
10 - 0 = 10
```

There are:

```text
5 - 1 = 4
```

intervals.

Step:

```text
10 / 4 = 2.5
```

Therefore:

```text
0
↓ +2.5
2.5
↓ +2.5
5
↓ +2.5
7.5
↓ +2.5
10
```

Final:

```text
[0.  2.5  5.  7.5 10.]
```

🔥 **Important Difference**

```text
arange()  → choose the step
linspace() → choose the number of values
```

---

# 19. 🟣 `np.eye()`

## 📌 Definition

`np.eye()` creates a **2D identity-style matrix** with ones on the main diagonal and zeros elsewhere.

### Syntax

```python
np.eye(n)
```

### Example

```python
import numpy as np

arr = np.eye(3)

print(arr)
```

### Output

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

Visual:

```text
┌─────┬─────┬─────┐
│  1  │  0  │  0  │
├─────┼─────┼─────┤
│  0  │  1  │  0  │
├─────┼─────┼─────┤
│  0  │  0  │  1  │
└─────┴─────┴─────┘
```

The main diagonal contains `1`.

---

# 20. 🎲 Random Arrays

NumPy can generate random values.

There are several random functions.

---

## 20.1 `np.random.rand()`

### 📌 Definition

Generates random floating-point values in the interval **[0, 1)**.

### Syntax

```python
np.random.rand(size)
```

### Example

```python
import numpy as np

arr = np.random.rand(5)

print(arr)
```

Possible output:

```text
[0.42 0.17 0.83 0.61 0.09]
```

⚠️ Your output will normally be different because the values are random.

---

# 21. 🎲 `np.random.random()`

`np.random.random()` also generates random floating-point values in **[0, 1)**.

### Example

```python
import numpy as np

arr = np.random.random(5)

print(arr)
```

Possible output:

```text
[0.73 0.21 0.58 0.14 0.92]
```

---

# 22. 🎲 `np.random.randint()`

## 📌 Definition

Generates random integers.

### Syntax

```python
np.random.randint(low, high, size)
```

The `high` value is excluded.

### Example

```python
import numpy as np

arr = np.random.randint(1, 10, 5)

print(arr)
```

Possible output:

```text
[3 8 1 6 4]
```

All values are:

```text
>= 1
and
< 10
```

So possible values are:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9
```

---

# 23. 🎲 Random 2D Array

```python
import numpy as np

arr = np.random.randint(1, 100, size=(3, 4))

print(arr)
```

Possible output:

```text
[[25 71 43 89]
 [12 64 31 56]
 [92 18 77 40]]
```

Meaning:

```text
3 rows × 4 columns
```

---

# 24. 🧠 Complete Array Creation Comparison

| Function | Purpose | Example |
|---|---|---|
| `np.array()` | Create from existing data | `np.array([1,2,3])` |
| `np.zeros()` | Fill with `0` | `np.zeros((2,3))` |
| `np.ones()` | Fill with `1` | `np.ones((2,3))` |
| `np.full()` | Fill with chosen value | `np.full((2,3),7)` |
| `np.empty()` | Uninitialized values | `np.empty((2,3))` |
| `np.arange()` | Sequence using step | `np.arange(0,10,2)` |
| `np.linspace()` | Evenly spaced values | `np.linspace(0,10,5)` |
| `np.eye()` | Identity-style matrix | `np.eye(3)` |
| `np.random.rand()` | Random floats [0,1) | `np.random.rand(5)` |
| `np.random.random()` | Random floats [0,1) | `np.random.random(5)` |
| `np.random.randint()` | Random integers | `np.random.randint(1,10,5)` |

---

# 25. 🧠 `arange()` vs `linspace()`

This is a **very important interview concept**.

### `arange()`

```python
np.arange(0, 10, 2)
```

You specify:

> **Step size**

Result:

```text
[0 2 4 6 8]
```

### `linspace()`

```python
np.linspace(0, 10, 5)
```

You specify:

> **Number of values**

Result:

```text
[0.  2.5 5.  7.5 10.]
```

### 🔥 Memory Trick

> **`arange` → How much should I jump?**  
> **`linspace` → How many values do I need?**

---

# 26. 🧠 `zeros()` vs `ones()` vs `full()`

```text
np.zeros()
     ↓
0 0 0 0

np.ones()
     ↓
1 1 1 1

np.full()
     ↓
7 7 7 7
```

### Example

```python
np.zeros(4)
```

```text
[0. 0. 0. 0.]
```

```python
np.ones(4)
```

```text
[1. 1. 1. 1.]
```

```python
np.full(4, 7)
```

```text
[7 7 7 7]
```

---

# 27. 🌍 Real-World Example — Student Data

Suppose a school has **30 students** and initially wants an array to store marks.

```python
import numpy as np

marks = np.zeros(30)

print(marks)
```

This creates:

```text
30 values
```

all initially set to zero.

Later, actual marks can be assigned.

---

# 28. 🌍 Real-World Example — Temperature

Suppose you want **7 equally spaced temperature points** from `20°C` to `40°C`.

```python
import numpy as np

temperature = np.linspace(20, 40, 7)

print(temperature)
```

Output:

```text
[20.         23.33333333 26.66666667 30.
 33.33333333 36.66666667 40.        ]
```

This demonstrates why `linspace()` is useful when you need a fixed number of evenly spaced values.

---

# 29. ⚠️ Common Mistakes

## Mistake 1 — Forgetting parentheses

❌

```python
np.array
```

This refers to the function itself.

✅

```python
np.array([1, 2, 3])
```

This calls the function.

---

## Mistake 2 — Confusing shape with values

```python
np.zeros((2, 3))
```

means:

```text
2 rows
3 columns
```

not:

```text
2 and 3 as array values
```

---

## Mistake 3 — Forgetting `arange()` excludes stop

```python
np.arange(1, 5)
```

Output:

```text
[1 2 3 4]
```

Not:

```text
[1 2 3 4 5]
```

---

## Mistake 4 — Confusing `arange()` and `linspace()`

```text
arange  → step
linspace → number of values
```

---

## Mistake 5 — Expecting `empty()` to return zeros

❌

```python
np.empty(5)
```

does **not** mean:

```text
[0 0 0 0 0]
```

The values are uninitialized.

---

# 30. 🎤 Interview Questions

### Q1. How do you create a NumPy array?

```python
np.array([1, 2, 3])
```

---

### Q2. What is a 1D array?

A one-dimensional sequence of values.

Example:

```python
[1, 2, 3]
```

---

### Q3. What is a 2D array?

An array organized into rows and columns.

Example:

```python
[
    [1, 2],
    [3, 4]
]
```

---

### Q4. What is a 3D array?

An array containing multiple 2D arrays.

---

### Q5. What does `dtype` mean?

**Data type** of the array elements.

---

### Q6. What does `ndmin` do?

It specifies the **minimum number of dimensions** for the resulting array.

---

### Q7. What does `np.zeros()` do?

Creates an array filled with zeros.

---

### Q8. What does `np.ones()` do?

Creates an array filled with ones.

---

### Q9. What does `np.full()` do?

Creates an array filled with a specified value.

---

### Q10. What does `np.empty()` do?

Creates an array with **uninitialized elements**.

---

### Q11. Difference between `arange()` and `linspace()`?

> **`arange()` uses a step size; `linspace()` uses the number of values.**

---

### Q12. What does `np.eye(3)` create?

A `3 × 3` identity-style matrix.

---

### Q13. What does `np.random.randint(1, 10, 5)` mean?

Generate **5 random integers** from `1` up to but not including `10`.

---

# 31. 💻 Practice Questions

### 🟢 Beginner

**1.** Create this array:

```text
[10 20 30 40 50]
```

using `np.array()`.

**2.** Create a 1D array containing numbers from `1` to `10`.

**3.** Create a `3 × 3` array of zeros.

**4.** Create a `2 × 4` array of ones.

**5.** Create a `3 × 3` array filled with `7`.

---

### 🟡 Intermediate

**6.** Create:

```text
0, 2, 4, 6, 8, 10
```

using `np.arange()`.

**7.** Create exactly 6 evenly spaced values between `0` and `100`.

**8.** Create a `4 × 4` identity matrix.

**9.** Create five random integers between `1` and `50`.

**10.** Create a `3 × 4` random integer array between `10` and `100`.

---

# 32. 🧪 Mini Coding Exercise

Create a program that generates a simple **student marks dataset**.

Requirements:

```text
1. Create 10 random marks
2. Marks should be between 0 and 100
3. Store them in a NumPy array
4. Print the marks
```

Hint:

```python
np.random.randint(...)
```

Example output will be different each time:

```text
[78 45 92 61 83 55 71 99 64 38]
```

---

# 33. 📋 Chapter 2 Summary

| ⭐ Concept | 📌 Purpose |
|---|---|
| **`np.array()`** | Create array from existing data |
| **1D** | Single sequence |
| **2D** | Rows + columns |
| **3D** | Collection of 2D arrays |
| **`dtype`** | Control/check data type |
| **`ndmin`** | Set minimum dimensions |
| **`zeros()`** | Fill with zeros |
| **`ones()`** | Fill with ones |
| **`full()`** | Fill with chosen value |
| **`empty()`** | Create uninitialized array |
| **`arange()`** | Sequence using step |
| **`linspace()`** | Evenly spaced values |
| **`eye()`** | Identity-style matrix |
| **`random.rand()`** | Random floats |
| **`random.random()`** | Random floats |
| **`random.randint()`** | Random integers |

---

# 🧠 34. Revision Points

### ⭐ Array Creation

```python
np.array([1, 2, 3])
```

### ⭐ 1D

```text
[1 2 3]
```

### ⭐ 2D

```text
[[1 2]
 [3 4]]
```

### ⭐ 3D

```text
[
  [[1 2],
   [3 4]],

  [[5 6],
   [7 8]]
]
```

### ⭐ Fill Arrays

```python
np.zeros((2, 3))
np.ones((2, 3))
np.full((2, 3), 7)
```

### ⭐ Generate Sequences

```python
np.arange(0, 10, 2)
np.linspace(0, 10, 5)
```

### ⭐ Identity Matrix

```python
np.eye(3)
```

### ⭐ Random

```python
np.random.rand(5)
np.random.random(5)
np.random.randint(1, 10, 5)
```

---

# 🧠 🔥 Most Important Memory Map

```text
                 📦 CREATE ARRAY
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   np.array()       Fill Arrays    Generate
                     │              │
               ┌─────┼─────┐    ┌───┴────┐
               ↓     ↓     ↓    ↓        ↓
             zeros ones full arange  linspace
                                  │
                                  ↓
                               Random
```

---

# 📝 Chapter 2 Quiz

Try these without looking at the notes.

### 1️⃣ What does `np.array()` do?

### 2️⃣ What is the difference between a **1D**, **2D**, and **3D** array?

### 3️⃣ What does `dtype` mean?

### 4️⃣ What does `ndmin=2` do?

### 5️⃣ What is the output?

```python
import numpy as np

arr = np.zeros((2, 3))

print(arr)
```

### 6️⃣ What is the difference between:

```python
np.zeros(5)
```

and:

```python
np.ones(5)
```

### 7️⃣ What does this create?

```python
np.full((2, 3), 7)
```

### 8️⃣ What is special about `np.empty()`?

### 9️⃣ What is the output?

```python
np.arange(1, 10, 2)
```

### 🔟 What is the difference between `arange()` and `linspace()`?

### 1️⃣1️⃣ What does this create?

```python
np.eye(3)
```

### 1️⃣2️⃣ What does this mean?

```python
np.random.randint(1, 10, 5)
```

---

# ✅ Chapter 2 Completion Checklist

```text
☑ np.array()
☑ 1D arrays
☑ 2D arrays
☑ 3D arrays
☑ dtype
☑ ndmin
☑ zeros()
☑ ones()
☑ full()
☑ empty()
☑ arange()
☑ linspace()
☑ eye()
☑ Random arrays
☑ Mathematical dry runs
☑ Visual explanations
☑ Real-world examples
☑ Common mistakes
☑ Interview questions
☑ Practice questions
☑ Mini exercise
☑ Summary
☑ Revision points
☑ Quiz
```

# 🏆 Chapter 2 — COMPLETE

When you are ready, type **`NEXT`**.

➡️ **Chapter 3 — Array Attributes** will cover:

**`ndim` → `shape` → `size` → `dtype` → `itemsize` → `nbytes`**, with memory calculations and detailed visual dry runs.