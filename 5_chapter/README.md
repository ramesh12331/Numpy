# 🚀 NumPy — Chapter 5: Slicing

Welcome to **Chapter 5 — NumPy Slicing**! 🎯

In Chapter 4, we learned **Indexing**, which is used to access individual elements, rows, or columns.

Now we will learn **Slicing**, which is used to access **a range of elements**.

---

# 📘 1. What is Slicing?

### Definition

**Slicing** means extracting a **part/range of an array**.

For example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
```

If we want:

```text
20, 30, 40
```

we can use slicing:

```python
print(arr[1:4])
```

Output:

```text
[20 30 40]
```

---

# 🧠 Indexing vs Slicing

| Concept | Purpose | Example |
|---|---|---|
| Indexing | Get one position | `arr[2]` |
| Slicing | Get a range | `arr[1:4]` |

### Easy Memory Trick

> **Indexing → ONE**  
> **Slicing → RANGE**

---

# 1️⃣ Basic Slicing Syntax

The basic syntax is:

```python
array[start:stop]
```

There is also:

```python
array[start:stop:step]
```

### Meaning

```text
start → where to start
stop  → where to stop
step  → how many positions to move
```

### ⭐ Very Important

The **stop index is excluded**.

For:

```python
arr[1:4]
```

NumPy takes:

```text
1
2
3
```

but **not 4**.

---

# 2️⃣ 1D Slicing

Consider:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
```

Visual:

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Array:   10   20   30   40   50
```

---

## Example 1 — `1:4`

```python
print(arr[1:4])
```

Output:

```text
[20 30 40]
```

### Dry Run

```text
arr[1:4]

Start = 1
Stop  = 4
```

Take:

```text
index 1 → 20
index 2 → 30
index 3 → 40
```

Stop before index `4`.

Therefore:

```text
[20 30 40]
```

---

# 3️⃣ Start Omitted

You can omit `start`.

```python
print(arr[:3])
```

Output:

```text
[10 20 30]
```

This means:

```text
start → beginning
stop  → 3
```

So:

```text
arr[:3]
```

means:

> Start from the beginning and stop before index 3.

---

# 4️⃣ Stop Omitted

You can omit `stop`.

```python
print(arr[2:])
```

Output:

```text
[30 40 50]
```

This means:

```text
start → 2
stop  → end
```

---

# 5️⃣ Both Start and Stop Omitted

```python
print(arr[:])
```

Output:

```text
[10 20 30 40 50]
```

It selects the **entire array**.

---

# 📊 Basic Slicing Patterns

| Syntax | Meaning |
|---|---|
| `arr[1:4]` | Index 1 to 3 |
| `arr[:4]` | Beginning to index 3 |
| `arr[2:]` | Index 2 to end |
| `arr[:]` | Entire array |

---

# 6️⃣ Slicing with Step

Syntax:

```python
arr[start:stop:step]
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50, 60])
```

Use:

```python
print(arr[0:6:2])
```

Output:

```text
[10 30 50]
```

### Dry Run

Indexes:

```text
0    1    2    3    4    5
↓    ↓    ↓    ↓    ↓    ↓
10   20   30   40   50   60
```

Start at `0`.

Step = `2`.

Therefore:

```text
0 → 10
2 → 30
4 → 50
```

Result:

```text
[10 30 50]
```

---

# 7️⃣ Every Second Element

A very common pattern:

```python
print(arr[::2])
```

Output:

```text
[10 30 50]
```

Meaning:

```text
start = beginning
stop  = end
step  = 2
```

---

# 8️⃣ Every Third Element

```python
print(arr[::3])
```

Output:

```text
[10 40]
```

Because:

```text
Index 0 → 10
Index 3 → 40
```

---

# 9️⃣ Negative Slicing

Negative indexes work with slicing too.

```python
arr = np.array([10, 20, 30, 40, 50])
```

To get the last three elements:

```python
print(arr[-3:])
```

Output:

```text
[30 40 50]
```

Visual:

```text
Index:   -5   -4   -3   -2   -1
          ↓    ↓    ↓    ↓    ↓
Array:   10   20   30   40   50
                    ↑    ↑    ↑
```

So:

```python
arr[-3:]
```

means:

> Start at the third-last element and continue to the end.

---

# 🔟 Negative Start and Stop

```python
print(arr[-4:-1])
```

Output:

```text
[20 30 40]
```

Dry run:

```text
-4 → 20
-3 → 30
-2 → 40
-1 → stop
```

Remember:

> **Stop is excluded.**

---

# 🔥 11. Reverse an Array

One of the most important slicing tricks:

```python
arr[::-1]
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[::-1])
```

Output:

```text
[50 40 30 20 10]
```

### Why?

The step is:

```text
-1
```

So NumPy moves:

```text
right → left
```

Visual:

```text
50 → 40 → 30 → 20 → 10
```

### ⭐ Remember

```python
arr[::-1]
```

means:

> **Reverse the array**

---

# 12️⃣ 2D Array Slicing

Now let's work with a 2D array.

```python
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
```

Visual:

```text
          Columns
       0    1    2     3
    ┌────┬────┬─────┬─────┐
 0  │ 10 │ 20 │ 30  │ 40  │
    ├────┼────┼─────┼─────┤
 1  │ 50 │ 60 │ 70  │ 80  │
    ├────┼────┼─────┼─────┤
 2  │ 90 │100 │ 110 │ 120 │
    └────┴────┴─────┴─────┘
```

For 2D slicing, the general form is:

```python
arr[row_slice, column_slice]
```

### ⭐ Important

```text
arr[ROWS, COLUMNS]
```

---

# 13️⃣ Select Multiple Rows

Suppose we want the first two rows:

```python
print(arr[0:2, :])
```

Output:

```text
[[ 10  20  30  40]
 [ 50  60  70  80]]
```

Explanation:

```text
0:2 → rows 0 and 1
:   → all columns
```

---

# 14️⃣ Select Multiple Columns

Suppose we want columns 1 and 2:

```python
print(arr[:, 1:3])
```

Output:

```text
[[ 20  30]
 [ 60  70]
 [100 110]]
```

Explanation:

```text
:   → all rows
1:3 → columns 1 and 2
```

---

# 🧠 Very Important Pattern

```python
arr[rows, columns]
```

For example:

```python
arr[0:2, 1:3]
```

means:

```text
Rows:
0, 1

Columns:
1, 2
```

Output:

```text
[[20 30]
 [60 70]]
```

---

# 🔥 15. 2D Slicing Visual

For:

```python
arr[0:2, 1:3]
```

Original:

```text
       0    1    2     3
    ┌────┬────┬─────┬─────┐
 0  │ 10 │ 20 │ 30  │ 40  │
    ├────┼────┼─────┼─────┤
 1  │ 50 │ 60 │ 70  │ 80  │
    ├────┼────┼─────┼─────┤
 2  │ 90 │100 │ 110 │ 120 │
    └────┴────┴─────┴─────┘

             ↓ select

       1    2
    ┌────┬─────┐
    │ 20 │ 30  │
    ├────┼─────┤
    │ 60 │ 70  │
    └────┴─────┘
```

Result:

```text
[[20 30]
 [60 70]]
```

---

# 16️⃣ Select a Complete Row Using Slicing

```python
print(arr[1, :])
```

Output:

```text
[50 60 70 80]
```

Meaning:

```text
Row 1
All columns
```

---

# 17️⃣ Select a Complete Column Using Slicing

```python
print(arr[:, 2])
```

Output:

```text
[ 30  70 110]
```

Meaning:

```text
All rows
Column 2
```

---

# 18️⃣ Select a Range of Rows and All Columns

```python
print(arr[1:3, :])
```

Output:

```text
[[ 50  60  70  80]
 [ 90 100 110 120]]
```

Meaning:

```text
Rows 1 and 2
All columns
```

---

# 19️⃣ Select All Rows and a Range of Columns

```python
print(arr[:, 1:4])
```

Output:

```text
[[ 20  30  40]
 [ 60  70  80]
 [100 110 120]]
```

Meaning:

```text
All rows
Columns 1, 2, 3
```

---

# 2️⃣0️⃣ 2D Slicing with Step

We can also use:

```text
start:stop:step
```

Example:

```python
print(arr[::2, :])
```

Output:

```text
[[ 10  20  30  40]
 [ 90 100 110 120]]
```

It selects:

```text
Row 0
Row 2
```

because step = `2`.

---

# 21️⃣ Reverse Rows

```python
print(arr[::-1, :])
```

Output:

```text
[[ 90 100 110 120]
 [ 50  60  70  80]
 [ 10  20  30  40]]
```

The rows are reversed.

---

# 22️⃣ Reverse Columns

```python
print(arr[:, ::-1])
```

Output:

```text
[[ 40  30  20  10]
 [ 80  70  60  50]
 [120 110 100  90]]
```

The columns are reversed.

---

# 🔥 23. Reverse Entire 2D Array

```python
print(arr[::-1, ::-1])
```

Output:

```text
[[120 110 100  90]
 [ 80  70  60  50]
 [ 40  30  20  10]]
```

### Understand it:

```text
arr[::-1, ::-1]
     ↓       ↓
  reverse  reverse
   rows    columns
```

---

# 24️⃣ 3D Slicing

Now let's look at a 3D array.

```python
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
```

Shape:

```python
print(arr.shape)
```

Output:

```text
(2, 2, 3)
```

Meaning:

```text
2 layers
2 rows per layer
3 columns per row
```

---

# 25️⃣ Select One Layer

```python
print(arr[0])
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

# 26️⃣ Slice Rows from a 3D Array

```python
print(arr[:, 0, :])
```

Meaning:

```text
: → all layers
0 → row 0
: → all columns
```

Output:

```text
[[1 2 3]
 [7 8 9]]
```

---

# 27️⃣ Slice Columns from a 3D Array

```python
print(arr[:, :, 1])
```

Meaning:

```text
: → all layers
: → all rows
1 → column 1
```

Output:

```text
[[ 2  5]
 [ 8 11]]
```

---

# 🧠 Slicing Cheat Sheet

```text
1D:
arr[start:stop:step]

2D:
arr[row_start:row_stop:row_step,
    col_start:col_stop:col_step]

3D:
arr[layer_slice,
    row_slice,
    column_slice]
```

---

# 🌍 Real-World Example

Imagine sales data:

```python
sales = np.array([
    [100, 200, 300, 400],
    [150, 250, 350, 450],
    [200, 300, 400, 500]
])
```

Suppose columns represent:

```text
Jan | Feb | Mar | Apr
```

### Get January sales:

```python
sales[:, 0]
```

Output:

```text
[100 150 200]
```

### Get January + February:

```python
sales[:, 0:2]
```

Output:

```text
[[100 200]
 [150 250]
 [200 300]]
```

### Get March + April:

```python
sales[:, 2:4]
```

Output:

```text
[[300 400]
 [350 450]
 [400 500]]
```

This type of slicing is extremely useful when working with **datasets**.

---

# ⚠️ Common Mistakes

### ❌ Mistake 1 — Forgetting that stop is excluded

```python
arr[1:4]
```

does **not** include index `4`.

It includes:

```text
1, 2, 3
```

---

### ❌ Mistake 2 — Confusing indexing and slicing

```python
arr[2]
```

→ one element/row depending on dimensions.

```python
arr[1:4]
```

→ a range.

---

### ❌ Mistake 3 — Confusing row and column

Remember:

```python
arr[row, column]
```

not:

```python
arr[column, row]
```

---

### ❌ Mistake 4 — Forgetting the second dimension

For a 2D array:

```python
arr[0:2, 1:3]
```

is correct.

The comma separates:

```text
rows , columns
```

---

# 💼 Interview Questions

### Q1. What is slicing?

**Answer:**  
Slicing is used to extract a **range or portion** of an array.

---

### Q2. What is the syntax for slicing?

```python
arr[start:stop:step]
```

---

### Q3. Is the stop index included?

**Answer:**  
No. The **stop index is excluded**.

---

### Q4. How do you reverse a NumPy array?

```python
arr[::-1]
```

---

### Q5. How do you select all rows from column 1?

```python
arr[:, 1]
```

---

### Q6. How do you select rows 1 and 2?

```python
arr[1:3, :]
```

---

### Q7. How do you select columns 1 and 2?

```python
arr[:, 1:3]
```

---

### Q8. What does `::2` mean?

**Answer:**  
Start from the beginning, go to the end, and move with a **step of 2**.

Example:

```python
arr[::2]
```

---

# 🧪 Practice Program

Run this in VS Code:

```python
import numpy as np

arr = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

print("Original Array:")
print(arr)

print("\n1. First two rows:")
print(arr[:2, :])

print("\n2. Last two rows:")
print(arr[-2:, :])

print("\n3. First three columns:")
print(arr[:, :3])

print("\n4. Last two columns:")
print(arr[:, -2:])

print("\n5. Rows 1 and 2, columns 2 and 3:")
print(arr[1:3, 2:4])

print("\n6. Reverse rows:")
print(arr[::-1, :])

print("\n7. Reverse columns:")
print(arr[:, ::-1])

print("\n8. Reverse everything:")
print(arr[::-1, ::-1])
```

---

# 🎯 Mini Coding Exercise

Use:

```python
import numpy as np

students = np.array([
    [80, 70, 90, 85],
    [60, 88, 75, 92],
    [95, 82, 89, 90],
    [72, 78, 85, 80]
])
```

Find using **slicing only**:

### 1. First two rows

```python
?
```

### 2. Last two rows

```python
?
```

### 3. First two columns

```python
?
```

### 4. Last two columns

```python
?
```

### 5. Rows 1 and 2, columns 1 and 2

```python
?
```

### 6. Reverse the rows

```python
?
```

### 7. Reverse the columns

```python
?
```

### 8. Reverse the entire array

```python
?
```

---

# 📌 Chapter 5 Summary

| Concept | Syntax | Meaning |
|---|---|---|
| Basic slice | `arr[1:4]` | Range |
| Start omitted | `arr[:4]` | Beginning → 3 |
| Stop omitted | `arr[2:]` | 2 → end |
| Everything | `arr[:]` | Entire array |
| Step | `arr[::2]` | Every 2nd element |
| Reverse | `arr[::-1]` | Reverse |
| 2D slicing | `arr[rows, cols]` | Rows + columns |
| Rows | `arr[1:3, :]` | Selected rows |
| Columns | `arr[:, 1:3]` | Selected columns |
| Reverse rows | `arr[::-1, :]` | Reverse row order |
| Reverse columns | `arr[:, ::-1]` | Reverse column order |
| Reverse all | `arr[::-1, ::-1]` | Reverse rows + columns |

---

# 🧠 Final Revision

Remember this one formula:

```text
START : STOP : STEP
```

And for 2D arrays:

```text
ROWS , COLUMNS
```

Therefore:

```python
arr[1:3, 2:4]
```

means:

```text
Rows    → 1, 2
Columns → 2, 3
```

And:

```python
arr[::-1, ::-1]
```

means:

```text
Reverse rows
     +
Reverse columns
```

### ⭐ Most Important Slicing Patterns

```python
arr[1:4]          # range
arr[:4]           # beginning
arr[2:]           # end
arr[::2]          # every 2nd
arr[::-1]         # reverse

arr[1:3, :]       # rows
arr[:, 1:3]       # columns
arr[::-1, :]      # reverse rows
arr[:, ::-1]      # reverse columns
arr[::-1, ::-1]   # reverse everything
```

## 📝 Chapter 5 Quiz

1. What is the difference between indexing and slicing?
2. In `arr[1:5]`, is index `5` included?
3. What does `arr[:3]` return?
4. What does `arr[2:]` return?
5. What does `arr[::2]` mean?
6. How do you reverse a 1D array?
7. How do you select all rows from column `2`?
8. How do you select rows `1` and `2` from a 2D array?
9. What does `arr[::-1, :]` do?
10. What does `arr[:, ::-1]` do?

**Chapter 5 — COMPLETE ✅**

Type **`NEXT`** for **Chapter 6 — NumPy Array Operations**, where we'll learn **addition, subtraction, multiplication, division, modulus, power, comparisons, and logical operations** with step-by-step mathematical dry runs.