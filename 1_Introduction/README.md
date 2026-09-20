# 🧮 NumPy Complete Course
## Chapter 1 — Introduction to NumPy

> 🎯 **Chapter Goal:** Understand the **foundation of NumPy** before learning array creation and advanced concepts.

---

# 1. ⭐ What is NumPy?

## 📌 Definition

**NumPy** stands for **Numerical Python**.

NumPy is a Python library mainly used for:

- 🔢 **Numerical calculations**
- 📦 **Arrays**
- 🧮 **Mathematical operations**
- 📊 **Statistical calculations**
- 🤖 **Machine Learning**
- 🔬 **Scientific computing**

The most important idea is:

> 🔥 **NumPy provides powerful array-based tools for numerical computing in Python.**

### 🧠 Simple idea

```text
🐍 Python
   ↓
🔢 NumPy
   ↓
📦 Arrays
   ↓
🧮 Numerical calculations
   ↓
📊 Data Science
```

---

# 2. ⭐ Why Do We Use NumPy?

Suppose we have student marks:

```python
marks = [70, 80, 90, 60, 85]
```

We want to **add 5 marks** to every student.

## 🐍 Using a Python List

```python
marks = [70, 80, 90, 60, 85]

new_marks = []

for mark in marks:
    new_marks.append(mark + 5)

print(new_marks)
```

### 📤 Output

```text
[75, 85, 95, 65, 90]
```

We need a **loop** to process every value.

---

## 🔢 Using NumPy

```python
import numpy as np

marks = np.array([70, 80, 90, 60, 85])

new_marks = marks + 5

print(new_marks)
```

### 📤 Output

```text
[75 85 95 65 90]
```

### 🧮 Mathematical Dry Run

```text
70 + 5 = 75
80 + 5 = 85
90 + 5 = 95
60 + 5 = 65
85 + 5 = 90
```

Visual:

```text
Original
┌────┬────┬────┬────┬────┐
│ 70 │ 80 │ 90 │ 60 │ 85 │
└────┴────┴────┴────┴────┘
   ↓    ↓    ↓    ↓    ↓
  +5   +5   +5   +5   +5
   ↓    ↓    ↓    ↓    ↓
┌────┬────┬────┬────┬────┐
│ 75 │ 85 │ 95 │ 65 │ 90 │
└────┴────┴────┴────┴────┘
```

🔥 **Important:** This is an example of an **element-wise operation**.

We will study the broader idea of **vectorization** later.

---

# 3. ⭐ NumPy vs Python List

This is a **fundamental NumPy concept**.

## 🐍 Python List

### Syntax

```python
list_name = [value1, value2, value3]
```

Example:

```python
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
```

### 📤 Output

```text
[1, 2, 3, 4, 5, 6]
```

Why?

For Python lists:

> `+` means **concatenation**.

---

## 🔢 NumPy Array

### Syntax

```python
array_name = np.array([value1, value2, value3])
```

Example:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
```

### 📤 Output

```text
[5 7 9]
```

### 🧮 Dry Run

```text
1 + 4 = 5
2 + 5 = 7
3 + 6 = 9
```

Visual:

```text
[1  2  3]
 +  +  +
[4  5  6]
 ↓  ↓  ↓
[5  7  9]
```

### 🧠 Memory Trick

> 🐍 **List `+` → Join**  
> 🔢 **Array `+` → Calculate**

---

# 4. 🔥 Another Important Difference — Multiplication

## Python List

```python
numbers = [1, 2, 3]

print(numbers * 2)
```

### Output

```text
[1, 2, 3, 1, 2, 3]
```

Python repeats the list.

---

## NumPy Array

```python
import numpy as np

numbers = np.array([1, 2, 3])

print(numbers * 2)
```

### Output

```text
[2 4 6]
```

### 🧮 Dry Run

```text
1 × 2 = 2
2 × 2 = 4
3 × 2 = 6
```

Visual:

```text
[ 1   2   3 ]
  ×   ×   ×
[ 2   2   2 ]
  ↓   ↓   ↓
[ 2   4   6 ]
```

> ⚠️ **Important Difference**
>
> ```python
> [1, 2, 3] * 2
> ```
> → repeats the list.
>
> ```python
> np.array([1, 2, 3]) * 2
> ```
> → multiplies every element.

---

# 5. 📊 Python List vs NumPy Array

| Feature | 🐍 Python List | 🔢 NumPy Array |
|---|---|---|
| Main purpose | General-purpose collection | Numerical computing |
| Numerical operations | Less convenient | ⭐ Very convenient |
| Element-wise operations | Usually require loops | ⭐ Direct |
| Multidimensional data | Less convenient | ⭐ Excellent |
| Mathematical functions | Limited | ⭐ Many |
| Data Science | Useful | ⭐ Very important |

### 🧠 Golden Rule

> **Python List → General-purpose data**  
> **NumPy Array → Numerical data**

---

# 6. 🚀 Advantages of NumPy

## ⚡ 1. Efficient Numerical Operations

NumPy makes numerical calculations convenient.

```python
arr + 10
```

```python
arr * 2
```

```python
arr / 5
```

---

## 📦 2. Multidimensional Arrays

NumPy supports arrays with multiple dimensions:

```text
1D
↓
[1, 2, 3]

2D
↓
[[1, 2],
 [3, 4]]

3D
↓
Multiple 2D arrays
```

We will study this properly in **Chapter 2**.

---

## 🧮 3. Mathematical Functions

NumPy provides many mathematical functions:

```python
np.sqrt()
np.sum()
np.mean()
np.min()
np.max()
```

These will be covered in later chapters.

---

## 📊 4. Data Science

NumPy is an important numerical computing tool in the Python data-science ecosystem.

Conceptually:

```text
                 📊 Data Science
                       │
              ┌────────┴────────┐
              ↓                 ↓
           🔢 NumPy          🐼 Pandas
              ↓
       Numerical processing
              ↓
        Statistics / ML
```

---

## 💾 5. Efficient Numerical Data

NumPy arrays are designed for numerical data and can be more memory-efficient than general Python lists for suitable numerical workloads.

---

# 7. 🛠️ NumPy Installation

## 📌 Definition

Installation means adding the NumPy package to your Python environment.

### 💻 VS Code Terminal

Run:

```bash
pip install numpy
```

Alternative:

```bash
python -m pip install numpy
```

### 🔍 Check Installation

```bash
pip show numpy
```

If installed, you will see information about the package.

---

# 8. 📥 Importing NumPy

## 📌 Definition

**Importing** means making a Python library available inside your program.

### Syntax

```python
import numpy as np
```

### Breakdown

```text
import
  ↓
Load a library

numpy
  ↓
Library name

as
  ↓
Create an alias

np
  ↓
Short name
```

Therefore:

```python
import numpy as np
```

means:

> ⭐ **Import NumPy and use `np` as its alias.**

---

# 9. ⭐ Why Do We Use `np`?

Instead of:

```python
numpy.array()
numpy.sqrt()
numpy.mean()
```

we normally write:

```python
np.array()
np.sqrt()
np.mean()
```

### 🧠 Remember

```text
numpy → Library
np    → Alias
```

`np` is the standard convention used in NumPy code.

---

# 10. 🔍 Checking NumPy Version

## 📌 Definition

`np.__version__` returns the **installed NumPy version**.

### Syntax

```python
np.__version__
```

### Example

```python
import numpy as np

print(np.__version__)
```

### Output

Your exact version depends on your environment.

For example:

```text
2.x.x
```

---

# 11. 🎯 First NumPy Program

Create this file in VS Code:

```text
numpy_chapter1.py
```

### 💻 Code

```python
# ============================================================
# NumPy Chapter 1 - First Program
# ============================================================

import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Print the array
print("Array:")
print(arr)

# Add 10 to every element
result = arr + 10

print("After adding 10:")
print(result)

# Print NumPy version
print("NumPy Version:")
print(np.__version__)
```

### 📤 Expected Output

```text
Array:
[10 20 30 40 50]

After adding 10:
[20 30 40 50 60]

NumPy Version:
2.x.x
```

Your version number may be different.

---

# 12. 🔎 Line-by-Line Explanation

### ① Import NumPy

```python
import numpy as np
```

➡️ Makes NumPy available.

---

### ② Create the array

```python
arr = np.array([10, 20, 30, 40, 50])
```

➡️ Creates a **NumPy array**.

Visual:

```text
arr
 ↓
┌────┬────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└────┴────┴────┴────┴────┘
```

---

### ③ Print the array

```python
print(arr)
```

Output:

```text
[10 20 30 40 50]
```

---

### ④ Add 10

```python
result = arr + 10
```

NumPy performs:

```text
10 + 10 = 20
20 + 10 = 30
30 + 10 = 40
40 + 10 = 50
50 + 10 = 60
```

Result:

```text
[20 30 40 50 60]
```

---

### ⑤ Print the version

```python
print(np.__version__)
```

➡️ Displays the installed NumPy version.

---

# 13. 💰 Real-World Example — Sales

Suppose a shop has sales for five days:

```python
import numpy as np

sales = np.array([1000, 1500, 1200, 1800, 2000])

discounted_sales = sales * 0.90

print("Original Sales:")
print(sales)

print("After 10% Discount:")
print(discounted_sales)
```

### 📤 Output

```text
Original Sales:
[1000 1500 1200 1800 2000]

After 10% Discount:
[ 900. 1350. 1080. 1620. 1800.]
```

### 🧮 Mathematical Dry Run

A **10% discount** means:

```text
100% - 10%
    ↓
  90%
    ↓
 0.90
```

Therefore:

```text
1000 × 0.90 = 900
1500 × 0.90 = 1350
1200 × 0.90 = 1080
1800 × 0.90 = 1620
2000 × 0.90 = 1800
```

🔥 **Real-world connection:** The same type of operation is useful for sales, salaries, discounts, numerical datasets, and feature transformations.

---

# 14. ⚠️ Common Mistakes

## ❌ Mistake 1 — Forgetting the import

```python
arr = np.array([1, 2, 3])
```

without importing NumPy can cause:

```text
NameError: name 'np' is not defined
```

### ✅ Correct

```python
import numpy as np

arr = np.array([1, 2, 3])
```

---

## ❌ Mistake 2 — NumPy is not installed

Possible error:

```text
ModuleNotFoundError: No module named 'numpy'
```

### ✅ Fix

```bash
pip install numpy
```

---

## ❌ Mistake 3 — Confusing List and Array Operations

```python
[1, 2, 3] * 2
```

➡️ **Repeats**

```python
np.array([1, 2, 3]) * 2
```

➡️ **Mathematical multiplication**

---

# 15. 🎤 Interview Questions

### Q1. What is NumPy?

**Answer:**  
NumPy is a Python library used for **numerical computing and efficient array-based operations**.

### Q2. What does NumPy stand for?

**Answer:**  
**Numerical Python.**

### Q3. Why is NumPy used in Data Science?

**Answer:**  
It provides efficient numerical operations, arrays, mathematical functions, and tools for processing numerical data.

### Q4. How do you install NumPy?

```bash
pip install numpy
```

### Q5. How do you import NumPy?

```python
import numpy as np
```

### Q6. What is `np`?

**Answer:**  
`np` is the conventional **alias** for NumPy.

### Q7. How do you check the NumPy version?

```python
print(np.__version__)
```

### Q8. What is the difference between a Python list and a NumPy array?

**Answer:**  
A Python list is a general-purpose collection, while a NumPy array is designed for efficient **numerical and multidimensional operations**.

### Q9. What is the output?

```python
import numpy as np

a = np.array([1, 2, 3])

print(a * 2)
```

**Answer:**

```text
[2 4 6]
```

---

# 16. 💻 Practice Questions

### 🟢 Beginner

**1.** Create a NumPy array containing:

```text
10, 20, 30, 40, 50
```

**2.** Print the array.

**3.** Add `10` to every element.

**4.** Multiply every element by `2`.

**5.** Print the NumPy version.

---

### 🟡 Understanding

**6.** What is the difference between:

```python
[1, 2, 3] * 2
```

and:

```python
np.array([1, 2, 3]) * 2
```

**7.** Why does:

```python
[1, 2, 3] + [4, 5, 6]
```

produce a different result from:

```python
np.array([1, 2, 3]) + np.array([4, 5, 6])
```

---

# 17. 🧪 Mini Coding Exercise

Write one complete program that:

1. Imports NumPy
2. Creates an array:

```text
[100, 200, 300, 400, 500]
```

3. Adds `50`
4. Multiplies the result by `2`
5. Prints the final array
6. Prints the NumPy version

### Expected final result

```text
[300 500 700 900 1100]
```

### 🧮 Dry Run

```text
Original:
[100 200 300 400 500]

Add 50:
[150 250 350 450 550]

Multiply by 2:
[300 500 700 900 1100]
```

---

# 18. 📋 Chapter 1 Summary

| ⭐ Concept | 📌 Meaning | 💻 Syntax |
|---|---|---|
| **NumPy** | Numerical Python | — |
| **Library** | Reusable Python functionality | — |
| **Array** | Numerical data structure | `np.array()` |
| **Installation** | Install NumPy | `pip install numpy` |
| **Import** | Load NumPy | `import numpy as np` |
| **Alias** | Short name | `np` |
| **Version** | Installed version | `np.__version__` |
| **Element-wise operation** | Operation on each element | `arr + 10` |

---

# 🧠 Chapter 1 Revision Points

### ⭐ Remember these 6 things

```python
# 1. Import
import numpy as np

# 2. Create an array
arr = np.array([10, 20, 30])

# 3. Add
arr + 10

# 4. Multiply
arr * 2

# 5. Check version
np.__version__

# 6. Install
# pip install numpy
```

### 🔥 Golden Rule

> 🐍 **Python List → General-purpose collection**  
> 🔢 **NumPy Array → Numerical computing**

---

# 🎯 Chapter 1 Final Mental Model

```text
                 🔢 NumPy
                    │
                    ↓
          ⭐ Numerical Python
                    │
                    ↓
              📦 NumPy Array
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
        🔢 Data   🧮 Math   📊 Statistics
          │         │         │
          └─────────┼─────────┘
                    ↓
             🚀 Data Science
```

---

# 📝 Chapter 1 Quiz

Answer these without looking at the notes:

### 1️⃣ What does **NumPy** stand for?

### 2️⃣ What is NumPy mainly used for?

### 3️⃣ How do you install NumPy?

### 4️⃣ What does this mean?

```python
import numpy as np
```

### 5️⃣ What is the purpose of `np`?

### 6️⃣ How do you create a NumPy array?

### 7️⃣ How do you check the NumPy version?

### 8️⃣ What is the output?

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr + 5)
```

### 9️⃣ What is the difference between:

```python
[1, 2, 3] * 2
```

and:

```python
np.array([1, 2, 3]) * 2
```

### 🔟 Why is NumPy important for Data Science?

---

# ✅ Chapter 1 Completion Checklist

```text
☑ What is NumPy?
☑ Why NumPy?
☑ NumPy vs Python Lists
☑ Advantages of NumPy
☑ Installation
☑ Importing NumPy
☑ np.__version__
☑ First NumPy program
☑ Mathematical dry run
☑ Real-world example
☑ Common mistakes
☑ Interview questions
☑ Practice questions
☑ Mini exercise
☑ Summary
☑ Revision points
☑ Quiz
```

# 🏆 Chapter 1 — COMPLETE

When you're ready, type **`NEXT`**.

➡️ **Chapter 2 — Creating Arrays** will start with the fundamental concept **`np.array()`**, then move through **1D → 2D → 3D → `dtype` → `ndmin` → `zeros()` → `ones()` → `full()` → `empty()` → `arange()` → `linspace()` → `eye()` → Random Arrays**.