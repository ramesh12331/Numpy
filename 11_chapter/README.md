# ✂️ Chapter 11 — NumPy Splitting Arrays

Welcome to **Chapter 11** 🎯

In Chapter 10, we learned how to **join** arrays.

Now we will learn the opposite operation:

> 🔪 **Splitting = dividing one NumPy array into multiple smaller arrays.**

---

# 📚 Chapter 11 Roadmap

We will learn:

1. 🔪 What is splitting?
2. `np.split()`
3. `np.array_split()`
4. `np.vsplit()`
5. `np.hsplit()`
6. 🔍 Difference between `split()` and `array_split()`
7. 🧠 Visual dry runs
8. 🌍 Real-world examples
9. ⚠️ Common mistakes
10. 💼 Interview questions
11. 📝 Practice
12. 🎯 Mini exercise
13. 📋 Summary
14. 🧪 Quiz

---

# 1️⃣ What is Array Splitting?

### 📖 Definition

**Splitting** means dividing one NumPy array into **multiple smaller arrays**.

For example:

```text
Original Array

[10 20 30 40 50 60]

          ↓ SPLIT

[10 20]   [30 40]   [50 60]
```

So remember:

```text
Joining     → 🔗 combine arrays
Splitting   → ✂️ divide arrays
```

---

# 2️⃣ `np.split()`

`np.split()` divides an array into a **specified number of equal parts**.

### Syntax

```python
np.split(array, number_of_parts)
```

---

## 🟢 Example 1 — 1D Array

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 3)

print(result)
```

### Output

```text
[array([10, 20]), array([30, 40]), array([50, 60])]
```

### 🧠 Visual Dry Run

Original:

```text
[10 20 30 40 50 60]
```

Split into **3 parts**:

```text
Part 1       Part 2       Part 3

[10 20]      [30 40]      [50 60]
```

Each part contains:

```text
6 elements ÷ 3 parts = 2 elements
```

---

# ⭐ Important Rule

`np.split()` requires the array to be **evenly divisible** by the number of sections.

Example:

```text
6 elements ÷ 3 = 2
```

✅ Works.

But:

```text
6 elements ÷ 4 = 1.5
```

❌ Cannot create 4 equal parts.

---

# ❌ Example

```python
arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 4)
```

You will get an error similar to:

```text
ValueError:
array split does not result in an equal division
```

### 🧠 Remember

```text
np.split()
     ↓
Equal parts required
```

---

# 3️⃣ Getting Individual Split Arrays

The result of `np.split()` is a **list of NumPy arrays**.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(arr, 3)

print(parts)
```

Now:

```python
print(parts[0])
print(parts[1])
print(parts[2])
```

Output:

```text
[10 20]
[30 40]
[50 60]
```

### Visual

```text
parts
  │
  ├── parts[0] → [10 20]
  ├── parts[1] → [30 40]
  └── parts[2] → [50 60]
```

---

# 4️⃣ `np.split()` with `axis`

For 2D arrays, we can specify the axis.

Consider:

```python
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
```

Shape:

```text
(2, 4)
```

Visual:

```text
      C0 C1 C2 C3

R0 →  1  2  3  4
R1 →  5  6  7  8
```

---

## 🔵 Split rows — `axis=0`

```python
result = np.split(arr, 2, axis=0)

print(result)
```

Output:

```text
[array([[1, 2, 3, 4]]),
 array([[5, 6, 7, 8]])]
```

Visual:

```text
Original

1 2 3 4
5 6 7 8

      ↓ axis=0

Part 1

1 2 3 4

Part 2

5 6 7 8
```

### 🧠 Memory Trick

```text
axis=0
   ↓
rows
```

---

# 5️⃣ Split Columns — `axis=1`

Same array:

```python
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
```

Now:

```python
result = np.split(arr, 2, axis=1)

print(result)
```

Output:

```text
[array([[1, 2],
        [5, 6]]),

 array([[3, 4],
        [7, 8]])]
```

Visual:

```text
Original

1 2 | 3 4
5 6 | 7 8

  ↓       ↓

Part 1    Part 2

1 2       3 4
5 6       7 8
```

### 🧠 Remember

```text
axis=0 → split rows
axis=1 → split columns
```

---

# 6️⃣ `np.array_split()`

Now we have a very useful function:

```python
np.array_split()
```

### 📖 Definition

`np.array_split()` can split an array into multiple parts **even when equal splitting is not possible**.

---

## Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.array_split(arr, 4)

print(result)
```

Output:

```text
[array([10, 20]),
 array([30, 40]),
 array([50]),
 array([60])]
```

Notice:

```text
6 elements
4 parts
```

The parts are not all equal:

```text
Part 1 → 2 elements
Part 2 → 2 elements
Part 3 → 1 element
Part 4 → 1 element
```

But NumPy can still perform the split.

---

# ⭐ `split()` vs `array_split()`

This is a **very important difference**.

| Function | Equal division required? |
|---|---|
| `np.split()` | ✅ Yes |
| `np.array_split()` | ❌ No |

### Easy memory trick:

```text
split()
   ↓
STRICT ⚠️
Equal parts required

array_split()
   ↓
FLEXIBLE ✅
Unequal parts allowed
```

---

# 7️⃣ `np.vsplit()`

`vsplit()` means:

> **Vertical Split**

It splits a 2D array **row-wise**.

### Syntax

```python
np.vsplit(array, number_of_parts)
```

---

## Example

```python
import numpy as np

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

result = np.vsplit(arr, 2)

print(result)
```

Output:

```text
[array([[1, 2],
        [3, 4]]),

 array([[5, 6],
        [7, 8]])]
```

Visual:

```text
Original

1 2
3 4
5 6
7 8

       ↓ vsplit

Part 1       Part 2

1 2          5 6
3 4          7 8
```

### 🧠 Remember

```text
vsplit
   ↓
vertical
   ↓
split rows
```

---

# 8️⃣ `np.hsplit()`

`hsplit()` means:

> **Horizontal Split**

It splits a 2D array **column-wise**.

### Syntax

```python
np.hsplit(array, number_of_parts)
```

---

## Example

```python
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.hsplit(arr, 2)

print(result)
```

Output:

```text
[array([[1, 2],
        [5, 6]]),

 array([[3, 4],
        [7, 8]])]
```

Visual:

```text
Original

1 2 | 3 4
5 6 | 7 8

 ↓       ↓

Part 1  Part 2

1 2     3 4
5 6     7 8
```

### 🧠 Remember

```text
hsplit
   ↓
horizontal
   ↓
split columns
```

---

# 🔥 `vsplit()` vs `hsplit()`

| Function | Splits |
|---|---|
| `np.vsplit()` | Rows |
| `np.hsplit()` | Columns |

Memory:

```text
V → Vertical → Rows ⬇️

H → Horizontal → Columns ➡️
```

---

# 9️⃣ Same Result in Different Ways

Consider:

```python
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
```

### Method 1

```python
np.split(arr, 2, axis=0)
```

### Method 2

```python
np.vsplit(arr, 2)
```

Both split **rows**.

---

Similarly:

```python
np.split(arr, 2, axis=1)
```

and:

```python
np.hsplit(arr, 2)
```

both split **columns**.

---

# 🧠 Big Picture

```text
                 SPLITTING
                     ✂️
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ↓              ↓              ↓
    split()      array_split()     vsplit()
       │              │              │
    equal          flexible         rows
       │
       │
       └──────────────┐
                      ↓
                   hsplit()
                      │
                    columns
```

---

# 🔟 Splitting at Specific Positions

`np.split()` can also accept **indices** instead of just the number of sections.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, [2, 4])

print(result)
```

Output:

```text
[array([10, 20]),
 array([30, 40]),
 array([50, 60])]
```

### 🧠 Dry Run

The split positions are:

```text
[10 20 | 30 40 | 50 60]
      2      4
```

So:

```text
index 0,1 → first part
index 2,3 → second part
index 4,5 → third part
```

This is useful when you want to control **exactly where splitting happens**.

---

# 🌍 Real-World Example — Student Data

Suppose we have:

```python
students = np.array([
    [101, 80, 85],
    [102, 75, 90],
    [103, 88, 92],
    [104, 70, 78]
])
```

Visual:

```text
ID   Math   English

101   80      85
102   75      90
103   88      92
104   70      78
```

Suppose we want to divide students into two groups.

```python
groups = np.vsplit(students, 2)

print(groups[0])
print(groups[1])
```

Output:

```text
[[101  80  85]
 [102  75  90]]

[[103  88  92]
 [104  70  78]]
```

Now:

```text
Group 1 → Students 101, 102

Group 2 → Students 103, 104
```

---

# 🌍 Real-World Example — Features and Target

Suppose:

```python
data = np.array([
    [20, 50000, 1],
    [25, 60000, 0],
    [30, 75000, 1]
])
```

Columns:

```text
Age | Salary | Purchased
```

We could split columns:

```python
features = data[:, :2]
target = data[:, 2:]
```

Result:

```text
features

20 50000
25 60000
30 75000
```

and:

```text
target

1
0
1
```

This kind of separation is common in **Machine Learning**.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Using `split()` with unequal parts

```python
arr = np.array([1, 2, 3, 4, 5])

np.split(arr, 2)
```

❌ This fails because:

```text
5 ÷ 2
```

is not an equal division.

Use:

```python
np.array_split(arr, 2)
```

instead.

---

## ❌ Mistake 2 — Confusing `axis`

For 2D arrays:

```text
axis=0 → rows
axis=1 → columns
```

---

## ❌ Mistake 3 — Confusing split and join

```text
JOIN
🔗
many arrays → one array
```

```text
SPLIT
✂️
one array → many arrays
```

---

# 💼 Interview Questions

### Q1. What is array splitting?

**Answer:**

Array splitting divides one NumPy array into multiple smaller arrays.

---

### Q2. What is `np.split()`?

**Answer:**

`np.split()` divides an array into a specified number of equal sections.

---

### Q3. What happens if equal splitting is impossible?

**Answer:**

`np.split()` raises a `ValueError`.

---

### Q4. Which function allows unequal splits?

**Answer:**

```python
np.array_split()
```

---

### Q5. What is `vsplit()`?

**Answer:**

`vsplit()` vertically splits a 2D array, meaning it splits rows.

---

### Q6. What is `hsplit()`?

**Answer:**

`hsplit()` horizontally splits a 2D array, meaning it splits columns.

---

### Q7. Difference between `split()` and `array_split()`?

**Answer:**

```text
split()
→ equal division required

array_split()
→ unequal division allowed
```

---

### Q8. What does `axis=0` mean when splitting a 2D array?

**Answer:**

It splits along the rows.

---

### Q9. What does `axis=1` mean?

**Answer:**

It splits along the columns.

---

# 📝 Practice

## Practice 1

Create:

```python
arr = np.array([10, 20, 30, 40, 50, 60])
```

Split it into **3 equal parts** using:

```python
np.split()
```

Expected:

```text
[10 20]
[30 40]
[50 60]
```

---

## Practice 2

Split this array into 4 parts:

```python
arr = np.array([1, 2, 3, 4, 5, 6])
```

Use:

```python
np.array_split()
```

---

## Practice 3

Given:

```python
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
```

Split the rows into 2 groups using:

```python
np.vsplit()
```

---

## Practice 4

Given:

```python
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
```

Split the columns into 2 groups using:

```python
np.hsplit()
```

---

# 🎯 Mini Coding Exercise

Try this yourself first:

```python
import numpy as np

sales = np.array([
    [100, 200, 300, 400],
    [150, 250, 350, 450],
    [120, 220, 320, 420],
    [180, 280, 380, 480]
])

# 1. Split rows into 2 groups
# 2. Split columns into 2 groups
# 3. Print every resulting array
```

Expected concept:

```text
Original

100 200 | 300 400
150 250 | 350 450
--------+--------
120 220 | 320 420
180 280 | 380 480
```

---

# 📋 Chapter 11 Summary

| Function | Purpose | Equal Parts Required? |
|---|---|---|
| `np.split()` | Split array | ✅ Yes |
| `np.array_split()` | Flexible splitting | ❌ No |
| `np.vsplit()` | Split rows | Usually yes |
| `np.hsplit()` | Split columns | Usually yes |

---

# 🧠 Final Memory Map

```text
              ✂️ SPLIT ARRAY
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    split()    array_split()   vsplit()
       │            │            │
     Equal       Flexible       Rows
       │
       │
       ↓
    hsplit()
       │
    Columns
```

### ⭐ Most Important

```text
np.split()
→ equal division

np.array_split()
→ unequal division allowed

np.vsplit()
→ rows

np.hsplit()
→ columns
```

---

# 🧪 Chapter 11 Quiz

**1.** Which function requires equal division?

A. `array_split()`  
B. `split()`  
C. `vsplit()`  
D. `reshape()`

**2.** Which function allows unequal divisions?

A. `split()`  
B. `array_split()`  
C. `hstack()`  
D. `stack()`

**3.** `vsplit()` splits:

A. Columns  
B. Rows  
C. Values  
D. Dimensions

**4.** `hsplit()` splits:

A. Rows  
B. Columns  
C. Depth  
D. Elements

**5.** What does this do?

```python
np.split(arr, 3)
```

A. Joins 3 arrays  
B. Creates 3 equal sections  
C. Creates 3 new dimensions  
D. Sorts the array

**6.** For a 2D array, which axis represents rows when splitting?

A. `axis=0`  
B. `axis=1`

**7.** For a 2D array, which axis represents columns?

A. `axis=0`  
B. `axis=1`

**8.** What is the opposite operation of joining?

A. Reshaping  
B. Broadcasting  
C. Splitting  
D. Indexing

---

# ✅ Chapter 11 COMPLETE

You now know:

**`np.split()` → `np.array_split()` → `np.vsplit()` → `np.hsplit()` → axis-based splitting → equal vs unequal splitting.**

👉 Type **`NEXT`** when you're ready for **Chapter 12 — Searching and Sorting Arrays** 🔎📊