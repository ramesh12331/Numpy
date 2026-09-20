# 🚀 NumPy — Chapter 4: Indexing

Welcome to **Chapter 4 — NumPy Indexing**! 🎯

In Chapter 3, we learned how to understand an array using:

```text
ndim → shape → size → dtype → itemsize → nbytes
```

Now we will learn how to **access specific values** from an array.

---

# 📘 1. What is Indexing?

### Definition

**Indexing** means accessing a specific element from an array using its **position/index**.

For example:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Visual:

```text
Value:    10   20   30   40   50
Index:     0    1    2    3    4
```

If we want `30`:

```python
print(arr[2])
```

Output:

```text
30
```

### ⭐ Important

NumPy indexing starts from **0**, not 1.

```text
First element  → index 0
Second element → index 1
Third element  → index 2
```

---

# 1️⃣ 1D Array Indexing

A **1D array** is like a single row.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
```

Output:

```text
10
20
30
40
50
```

Visual:

```text
        0    1    2    3    4
       ↓    ↓    ↓    ↓    ↓
      10   20   30   40   50
```

---

# 🧠 Easy Trick

Think:

> **Index = position starting from ZERO**

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Array:   10   20   30   40   50
```

So:

```python
arr[3]
```

means:

> Give me the value at **index 3**.

Answer:

```text
40
```

---

# 2️⃣ Positive Indexing

Positive indexing starts from the **left side**.

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Array:   10   20   30   40   50
```

Examples:

```python
print(arr[0])   # 10
print(arr[2])   # 30
print(arr[4])   # 50
```

Output:

```text
10
30
50
```

---

# 3️⃣ Negative Indexing

Negative indexing starts from the **right side**.

```text
Index:   -5   -4   -3   -2   -1
          ↓    ↓    ↓    ↓    ↓
Array:   10   20   30   40   50
```

So:

```python
print(arr[-1])
```

Output:

```text
50
```

Because `-1` means **last element**.

### Examples

```python
print(arr[-1])
print(arr[-2])
print(arr[-3])
```

Output:

```text
50
40
30
```

### ⭐ Memory Trick

> **Positive → left to right**  
> **Negative → right to left**

---

# 4️⃣ Positive vs Negative Indexing

```text
Positive:

  0    1    2    3    4
  ↓    ↓    ↓    ↓    ↓
 10   20   30   40   50
                       ↑
                     last


Negative:

 -5   -4   -3   -2   -1
  ↓    ↓    ↓    ↓    ↓
 10   20   30   40   50
```

Therefore:

```python
arr[0]  → 10
arr[-1] → 50

arr[1]  → 20
arr[-2] → 40
```

---

# 5️⃣ 2D Array Indexing

Now things become slightly more interesting. 🔥

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
             Column
          0    1    2
        ┌────┬────┬────┐
Row 0   │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
Row 1   │ 40 │ 50 │ 60 │
        ├────┼────┼────┤
Row 2   │ 70 │ 80 │ 90 │
        └────┴────┴────┘
```

For a 2D array, we use:

```python
arr[row, column]
```

### ⭐ Syntax

```python
array[row_index, column_index]
```

---

# 6️⃣ Access a Specific Element

Suppose we want `50`.

It is:

```text
Row = 1
Column = 1
```

Therefore:

```python
print(arr[1, 1])
```

Output:

```text
50
```

Visual:

```text
             0    1    2
                  ↓
        ┌────┬────┬────┐
    0   │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
    1   │ 40 │ 50 │ 60 │ ← Row 1
        ├────┼────┼────┤
    2   │ 70 │ 80 │ 90 │
        └────┴────┴────┘
                  ↑
              arr[1,1]
```

---

# 7️⃣ More 2D Examples

```python
print(arr[0, 0])
```

Output:

```text
10
```

```python
print(arr[0, 2])
```

Output:

```text
30
```

```python
print(arr[2, 0])
```

Output:

```text
70
```

```python
print(arr[2, 2])
```

Output:

```text
90
```

---

# 🧠 Dry Run

Question:

```python
arr[2, 1]
```

Step 1:

```text
2 → Row 2
```

Step 2:

```text
1 → Column 1
```

Go to:

```text
             0    1    2
        ┌────┬────┬────┐
    0   │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
    1   │ 40 │ 50 │ 60 │
        ├────┼────┼────┤
    2   │ 70 │ 80 │ 90 │
        └────┴────┴────┘
                  ↑
```

Answer:

```text
80
```

---

# 8️⃣ Alternative 2D Syntax

You can also write:

```python
arr[1][2]
```

This gives:

```text
60
```

But the standard NumPy style is:

```python
arr[1, 2]
```

### ⭐ Prefer

```python
arr[row, column]
```

---

# 9️⃣ Selecting a Complete Row

Suppose:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

To select **Row 1**:

```python
print(arr[1])
```

Output:

```text
[40 50 60]
```

Visual:

```text
        ┌────┬────┬────┐
    0   │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
    1   │ 40 │ 50 │ 60 │  ← SELECTED
        ├────┼────┼────┤
    2   │ 70 │ 80 │ 90 │
        └────┴────┴────┘
```

### ⭐ Syntax

```python
arr[row_index]
```

---

# 🔟 Selecting a Complete Column

To select a complete column, use:

```python
arr[:, column_index]
```

### What does `:` mean?

`:` means:

> **Take everything**

So:

```python
arr[:, 1]
```

means:

```text
all rows
column 1
```

Output:

```text
[20 50 80]
```

Visual:

```text
             0    1    2
                  ↓
        ┌────┬────┬────┐
    0   │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
    1   │ 40 │ 50 │ 60 │
        ├────┼────┼────┤
    2   │ 70 │ 80 │ 90 │
        └────┴────┴────┘
                  ↓
             [20 50 80]
```

---

# 🔥 Row vs Column

This is **very important**.

### Complete Row

```python
arr[1, :]
```

Output:

```text
[40 50 60]
```

Meaning:

```text
Row 1
All columns
```

### Complete Column

```python
arr[:, 1]
```

Output:

```text
[20 50 80]
```

Meaning:

```text
All rows
Column 1
```

---

# 🧠 Easy Memory Trick

Remember:

```text
arr[row, column]
```

For **row**:

```text
arr[1, :]
    ↑  ↑
  row all columns
```

For **column**:

```text
arr[:, 1]
    ↑  ↑
   all  column
   rows
```

### ⭐ Key Rule

> `:` means **ALL**

---

# 1️⃣1️⃣ Negative Indexing in 2D Arrays

Consider:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Negative row indexes:

```text
        -3
         ↓
        10 20 30

        -2
         ↓
        40 50 60

        -1
         ↓
        70 80 90
```

So:

```python
print(arr[-1])
```

Output:

```text
[70 80 90]
```

---

# 1️⃣2️⃣ Negative Column Index

```python
print(arr[:, -1])
```

Output:

```text
[30 60 90]
```

Because `-1` means **last column**.

Visual:

```text
             0    1   -1
        ┌────┬────┬────┐
        │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
        │ 40 │ 50 │ 60 │
        ├────┼────┼────┤
        │ 70 │ 80 │ 90 │
        └────┴────┴────┘
                       ↑
                   last column
```

---

# 1️⃣3️⃣ 3D Array Indexing

Now let's understand 3D arrays.

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

Think of this as **two 2D arrays/layers**.

```text
Layer 0:

1  2
3  4


Layer 1:

5  6
7  8
```

A 3D array uses:

```python
arr[layer, row, column]
```

---

# 🔥 3D Example

Get `6`.

Where is `6`?

```text
Layer 1
Row 0
Column 1
```

Therefore:

```python
print(arr[1, 0, 1])
```

Output:

```text
6
```

### ⭐ 3D Syntax

```python
arr[layer, row, column]
```

---

# 📊 Dimensions and Indexing

| Array | Index format |
|---|---|
| 1D | `arr[index]` |
| 2D | `arr[row, column]` |
| 3D | `arr[layer, row, column]` |

### Memory Trick

```text
1D → index

2D → row, column

3D → layer, row, column
```

---

# 🌍 Real-World Example

Imagine student marks:

```text
Rows    → Students
Columns → Subjects
```

```python
marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])
```

Suppose:

```text
Column 0 → Maths
Column 1 → Science
Column 2 → English
```

To get the **Science mark of Student 2**:

```python
print(marks[1, 1])
```

Output:

```text
88
```

To get all Science marks:

```python
print(marks[:, 1])
```

Output:

```text
[75 88 85]
```

---

# ⚠️ Common Mistakes

### ❌ Mistake 1 — Forgetting zero indexing

```python
arr = np.array([10, 20, 30])
print(arr[1])
```

The answer is:

```text
20
```

not `10`.

---

### ❌ Mistake 2 — Reversing row and column

For:

```python
arr[row, column]
```

Don't confuse:

```python
arr[column, row]
```

---

### ❌ Mistake 3 — Trying an invalid index

```python
arr = np.array([10, 20, 30])

print(arr[3])
```

This causes an **IndexError**, because valid indexes are:

```text
0, 1, 2
```

---

# 💼 Interview Questions

### Q1. What is indexing?

**Answer:**  
Indexing is the process of accessing a specific element using its position.

---

### Q2. Does NumPy indexing start from 0?

**Answer:**  
Yes. NumPy uses **zero-based indexing**.

---

### Q3. How do you access an element in a 2D array?

**Answer:**

```python
arr[row, column]
```

---

### Q4. How do you select the second row?

```python
arr[1]
```

or:

```python
arr[1, :]
```

---

### Q5. How do you select the second column?

```python
arr[:, 1]
```

---

### Q6. What does `:` mean in NumPy indexing?

**Answer:**

`:` means **select all elements along that axis**.

---

### Q7. What does `-1` mean?

**Answer:**

`-1` represents the **last element/index** along the selected axis.

---

### Q8. How do you access a 3D array?

**Answer:**

```python
arr[layer, row, column]
```

---

# 🧪 Practice

Run this code:

```python
import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Array:")
print(arr)

print("First element:", arr[0, 0])
print("Last element:", arr[-1, -1])

print("Second row:", arr[1])
print("Third row:", arr[2])

print("First column:", arr[:, 0])
print("Second column:", arr[:, 1])
print("Last column:", arr[:, -1])
```

### Predict the output before running it. 🧠

---

# 🎯 Mini Coding Exercise

Create this array:

```python
students = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 88, 92]
])
```

Answer these using indexing:

### 1. Get `80`

```python
?
```

### 2. Get `75`

```python
?
```

### 3. Get the complete second row

```python
?
```

### 4. Get the complete third row

```python
?
```

### 5. Get the first column

```python
?
```

### 6. Get the last column

```python
?
```

### 7. Get the last element

```python
?
```

---

# 📌 Chapter 4 Summary

| Concept | Syntax | Meaning |
|---|---|---|
| 1D indexing | `arr[i]` | Access one element |
| 2D indexing | `arr[row, col]` | Access one element |
| 3D indexing | `arr[layer, row, col]` | Access one element |
| Positive index | `0, 1, 2...` | Left/top → right/bottom |
| Negative index | `-1, -2...` | Right/bottom → left/top |
| Complete row | `arr[row, :]` | All columns |
| Complete column | `arr[:, col]` | All rows |
| All | `:` | Everything along that axis |

---

# 🧠 Final Revision Map

```text
                    NUMPY INDEXING
                          │
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
       1D                2D                3D
        │                 │                 │
    arr[i]          arr[row,col]    arr[layer,row,col]
        │                 │                 │
        ↓                 ↓                 ↓
   One position      Row + Column     Layer + Row + Column


Positive Index
0 → first
1 → second
2 → third

Negative Index
-1 → last
-2 → second last


2D:
arr[1, :] → complete row
arr[:, 1] → complete column

⭐ : → ALL
```

## 📝 Chapter 4 Quiz

1. What is the index of the first element?
2. What does `arr[-1]` return?
3. What does `arr[2, 1]` mean?
4. How do you select all rows from column `2`?
5. How do you select row `1` and all columns?
6. What does `:` mean?
7. What is the indexing format for a 3D array?

**Chapter 4 — COMPLETE ✅**

Type **`NEXT`** when you're ready for **Chapter 5 — NumPy Slicing**, where we'll learn `start:stop:step`, row slicing, column slicing, reverse arrays, and 2D/3D slicing.