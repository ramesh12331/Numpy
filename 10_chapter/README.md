# 🚀 Chapter 10 — NumPy Joining Arrays

Welcome to **Chapter 10** 🎯

In this chapter, we will learn how to **combine multiple NumPy arrays into one array**.

---

# 📚 Chapter 10 Roadmap

We will learn:

1. 🔗 What is Joining?
2. `np.concatenate()`
3. `np.vstack()`
4. `np.hstack()`
5. `np.stack()`
6. `np.dstack()`
7. 🔍 Difference between joining methods
8. 🧠 Visual dry runs
9. 🌍 Real-world examples
10. ⚠️ Common mistakes
11. 💼 Interview Questions
12. 📝 Practice
13. 🎯 Mini Project
14. 📋 Summary
15. 🧪 Quiz

---

# 1️⃣ What is Joining?

### 📖 Definition

**Joining** means:

> Combining two or more NumPy arrays into a single array.

Think of it like this:

```text
Array A        Array B
[1 2 3]   +   [4 5 6]

        ↓ JOIN

[1 2 3 4 5 6]
```

So:

```text
Array 1 + Array 2
       ↓
   One Array
```

---

# 2️⃣ `np.concatenate()`

`np.concatenate()` is one of the most important joining functions.

### 🔑 Definition

`np.concatenate()` joins arrays along an **existing axis**.

### Syntax

```python
np.concatenate((array1, array2), axis=0)
```

---

## 🟢 Example 1 — 1D Arrays

```python
import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

result = np.concatenate((arr1, arr2))

print(result)
```

### Output

```text
[10 20 30 40 50 60]
```

### 🧠 Dry Run

```text
arr1 → [10 20 30]

arr2 → [40 50 60]

             ↓

result → [10 20 30 40 50 60]
```

---

# 3️⃣ Concatenate 2D Arrays

Consider:

```python
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])
```

Visual:

```text
arr1             arr2

1  2              5  6
3  4              7  8
```

---

## 🔵 `axis=0`

```python
result = np.concatenate((arr1, arr2), axis=0)

print(result)
```

Output:

```text
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

### Visual

```text
arr1
┌───────┐
│ 1  2  │
│ 3  4  │
└───────┘

arr2
┌───────┐
│ 5  6  │
│ 7  8  │
└───────┘

      ↓ axis=0

┌───────┐
│ 1  2  │
│ 3  4  │
│ 5  6  │
│ 7  8  │
└───────┘
```

### 🧠 Remember

**`axis=0` → add rows**

---

# 4️⃣ `axis=1`

Now:

```python
result = np.concatenate((arr1, arr2), axis=1)

print(result)
```

Output:

```text
[[1 2 5 6]
 [3 4 7 8]]
```

Visual:

```text
arr1        arr2

1  2    +   5  6
3  4        7  8

       ↓

1  2  5  6
3  4  7  8
```

### 🧠 Remember

**`axis=1` → add columns**

---

# ⭐ Important Rule

For:

```python
np.concatenate((arr1, arr2), axis=0)
```

the number of **columns must match**.

Example:

```text
arr1 → 2 × 3
arr2 → 2 × 3
```

✅ Valid.

But:

```text
arr1 → 2 × 3
arr2 → 2 × 4
```

❌ Cannot concatenate along `axis=0`.

---

# 5️⃣ `np.vstack()`

`vstack` means:

> **Vertical Stack**

Think:

```text
⬇️
⬇️
⬇️
```

It places arrays **one below another**.

### Syntax

```python
np.vstack((array1, array2))
```

---

## Example

```python
import numpy as np

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.vstack((arr1, arr2))

print(result)
```

Output:

```text
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

Visual:

```text
1 2
3 4
---
5 6
7 8
```

### 🧠 Easy Memory Trick

**V = Vertical**

```text
V
⬇️
⬇️
```

---

# 6️⃣ `np.hstack()`

`hstack` means:

> **Horizontal Stack**

It places arrays **side by side**.

### Syntax

```python
np.hstack((array1, array2))
```

---

## Example

```python
import numpy as np

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.hstack((arr1, arr2))

print(result)
```

Output:

```text
[[1 2 5 6]
 [3 4 7 8]]
```

Visual:

```text
1 2 | 5 6
3 4 | 7 8
```

### 🧠 Memory Trick

**H = Horizontal**

```text
→ → →
```

---

# 7️⃣ `np.stack()`

This is an **important difference**.

`np.stack()` joins arrays by creating a **new axis**.

### Syntax

```python
np.stack((array1, array2), axis=0)
```

Let's use:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
```

---

## 🔵 `axis=0`

```python
result = np.stack((arr1, arr2), axis=0)

print(result)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

Notice:

```text
arr1 → [1 2 3]
arr2 → [4 5 6]

          ↓ stack

[[1 2 3]
 [4 5 6]]
```

Shape:

```python
print(result.shape)
```

Output:

```text
(2, 3)
```

Originally:

```text
arr1.shape → (3,)
arr2.shape → (3,)
```

After stack:

```text
(2, 3)
```

So **a new dimension was created**.

---

# 8️⃣ `np.stack(axis=1)`

```python
result = np.stack((arr1, arr2), axis=1)

print(result)
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

Visual:

```text
arr1   arr2

 1      4
 2      5
 3      6
```

Result:

```text
1 4
2 5
3 6
```

---

# ⭐ concatenate vs stack

This is a very important interview topic.

### `concatenate()`

Works along an **existing axis**.

### `stack()`

Creates a **new axis**.

Think:

```text
concatenate
    ↓
existing dimension
```

```text
stack
    ↓
NEW dimension
```

---

# 9️⃣ `np.dstack()`

`dstack` means:

> **Depth Stack**

It stacks arrays along the **third axis/depth direction** for suitable 1D/2D inputs.

Example:

```python
import numpy as np

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.dstack((arr1, arr2))

print(result)
```

Output:

```text
[[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]]
```

Shape:

```python
print(result.shape)
```

Output:

```text
(2, 2, 2)
```

---

# 🧠 Understand `dstack()` Visually

Before:

```text
arr1

1 2
3 4
```

and:

```text
arr2

5 6
7 8
```

After depth stacking:

```text
Depth 1       Depth 2

1 2           5 6
3 4           7 8
```

Think of it as **layers**:

```text
Layer 1
┌───────┐
│ 1  2  │
│ 3  4  │
└───────┘

Layer 2
┌───────┐
│ 5  6  │
│ 7  8  │
└───────┘
```

This creates a 3D array.

---

# 🔥 All Joining Functions Together

| Function | Meaning | Main Direction |
|---|---|---|
| `concatenate()` | Join along existing axis | Existing axis |
| `vstack()` | Vertical stack | Rows ⬇️ |
| `hstack()` | Horizontal stack | Columns ➡️ |
| `stack()` | Create new axis | New dimension |
| `dstack()` | Depth stack | Depth |

---

# 🧠 Easy Memory Trick

Remember:

```text
V → Vertical → ⬇️

H → Horizontal → ➡️

D → Depth → 📚

STACK → NEW AXIS 🆕

CONCATENATE → EXISTING AXIS 🔗
```

---

# 🔟 Real-World Example — Student Marks

Suppose we have marks from two exams.

### Exam 1

```python
exam1 = np.array([
    [80, 75, 90],
    [65, 88, 72]
])
```

### Exam 2

```python
exam2 = np.array([
    [85, 78, 95],
    [70, 90, 75]
])
```

---

## Combine students vertically

```python
result = np.vstack((exam1, exam2))

print(result)
```

Output:

```text
[[80 75 90]
 [65 88 72]
 [85 78 95]
 [70 90 75]]
```

---

# 🌍 Real-World Example — Sales Data

Suppose January sales:

```python
january = np.array([100, 200, 300])
```

February sales:

```python
february = np.array([150, 250, 350])
```

Join:

```python
sales = np.concatenate((january, february))

print(sales)
```

Output:

```text
[100 200 300 150 250 350]
```

Now we have one sales array.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Forgetting parentheses

Wrong:

```python
np.concatenate(arr1, arr2)
```

Correct:

```python
np.concatenate((arr1, arr2))
```

---

## ❌ Mistake 2 — Wrong dimensions

Example:

```python
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6, 7]
])
```

Trying:

```python
np.concatenate((arr1, arr2), axis=0)
```

will fail because the column counts don't match.

```text
arr1 → 2 × 2

arr2 → 1 × 3

columns:
2 ≠ 3
```

---

## ❌ Mistake 3 — Confusing `stack()` and `concatenate()`

Remember:

```text
concatenate → existing axis
stack       → new axis
```

---

# 💼 Interview Questions

### Q1. What is array joining?

**Answer:**

Array joining means combining two or more NumPy arrays into a single array.

---

### Q2. What is `np.concatenate()`?

**Answer:**

`np.concatenate()` joins arrays along an existing axis.

---

### Q3. What does `axis=0` usually mean for a 2D array?

**Answer:**

It operates down the rows and, when concatenating, adds rows.

---

### Q4. What does `axis=1` mean?

**Answer:**

It operates across columns and, when concatenating, adds columns.

---

### Q5. What is `vstack()`?

**Answer:**

`vstack()` vertically stacks arrays, usually adding rows.

---

### Q6. What is `hstack()`?

**Answer:**

`hstack()` horizontally stacks arrays, usually adding columns.

---

### Q7. Difference between `stack()` and `concatenate()`?

**Answer:**

```text
concatenate → joins along an existing axis

stack → joins along a new axis
```

---

### Q8. What does `dstack()` do?

**Answer:**

`dstack()` stacks arrays along the depth direction, producing a third dimension for suitable inputs.

---

# 📝 Practice Questions

### Practice 1

Create:

```python
arr1 = [10, 20, 30]
arr2 = [40, 50, 60]
```

Join them using:

```python
np.concatenate()
```

Expected:

```text
[10 20 30 40 50 60]
```

---

### Practice 2

Create:

```text
1 2
3 4
```

and:

```text
5 6
7 8
```

Use:

```python
np.vstack()
```

Expected:

```text
1 2
3 4
5 6
7 8
```

---

### Practice 3

Use the same arrays with:

```python
np.hstack()
```

Expected:

```text
1 2 5 6
3 4 7 8
```

---

### Practice 4

Use:

```python
np.stack()
```

with:

```python
[1, 2, 3]
[4, 5, 6]
```

Try both:

```python
axis=0
```

and:

```python
axis=1
```

Check their shapes.

---

# 🎯 Mini Coding Exercise

Try this without looking at the answer first.

```python
import numpy as np

# January sales
january = np.array([
    [100, 200, 300],
    [150, 250, 350]
])

# February sales
february = np.array([
    [120, 220, 320],
    [170, 270, 370]
])

# 1. Join vertically
# 2. Join horizontally
# 3. Print the shapes
```

### Your task:

Complete:

```python
vertical = ?

horizontal = ?

print(vertical)
print(horizontal)

print(vertical.shape)
print(horizontal.shape)
```

---

# 📋 Chapter 10 Summary

| Concept | Meaning |
|---|---|
| `concatenate()` | Join along existing axis |
| `axis=0` | Add rows |
| `axis=1` | Add columns |
| `vstack()` | Vertical joining |
| `hstack()` | Horizontal joining |
| `stack()` | Join using a new axis |
| `dstack()` | Depth joining |
| `V` | Vertical ⬇️ |
| `H` | Horizontal ➡️ |
| `D` | Depth 📚 |

---

# 🧠 One-Minute Revision

```text
                    JOINING
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
 concatenate         stack         dstack
        │              │              │
 existing axis      NEW axis        depth
        │
   ┌────┴────┐
   ↓         ↓
axis=0     axis=1
   ↓         ↓
 rows     columns
```

And:

```text
vstack → rows ⬇️

hstack → columns ➡️
```

---

# 🧪 Chapter 10 Quiz

### 1. Which function joins arrays along an existing axis?

A. `np.stack()`  
B. `np.concatenate()`  
C. `np.reshape()`  
D. `np.flatten()`

---

### 2. `vstack()` means:

A. Vertical stack  
B. Value stack  
C. Variable stack  
D. Vector stack

---

### 3. `hstack()` is mainly used for:

A. Adding rows  
B. Adding columns  
C. Sorting  
D. Reshaping

---

### 4. Which function creates a new axis?

A. `concatenate()`  
B. `stack()`  
C. `vstack()`  
D. `sort()`

---

### 5. What does `axis=0` mean when concatenating 2D arrays?

A. Add columns  
B. Add rows  
C. Add depth  
D. Delete rows

---

### 6. What does `axis=1` mean?

A. Add columns  
B. Add rows  
C. Add depth  
D. Reverse array

---

### 7. Which function is associated with depth stacking?

A. `hstack()`  
B. `vstack()`  
C. `dstack()`  
D. `ravel()`

---

### 8. What is the main difference?

```text
concatenate → ?
stack       → ?
```

---

# ✅ Chapter 10 COMPLETE

You have now learned:

**`concatenate()` → `vstack()` → `hstack()` → `stack()` → `dstack()` → axis → joining rules**.

When you're ready:

# 👉 Type `NEXT`

Then we will start **Chapter 11 — Splitting Arrays** ✂️

We will learn:

```text
np.split()
np.array_split()
np.vsplit()
np.hsplit()
```

with visual diagrams and dry runs.