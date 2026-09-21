# 🚀 NumPy — Chapter 9: Reshaping Arrays

Welcome to **Chapter 9 — Reshaping Arrays**! 🎯

So far we learned:

```text
Chapter 2 → Creating Arrays
Chapter 3 → Attributes
Chapter 4 → Indexing
Chapter 5 → Slicing
Chapter 6 → Array Operations
Chapter 7 → Mathematical Functions
Chapter 8 → Statistical Functions
```

Now we will learn how to **change the structure/dimensions of an array**.

---

# 📘 1. What is Reshaping?

### Definition

**Reshaping** means changing the **shape of an array without changing its data**.

For example:

```text
Original:

[1 2 3 4 5 6]
```

We can reshape it into:

```text
2 × 3

[1 2 3]
[4 5 6]
```

The values are still:

```text
1 2 3 4 5 6
```

Only their **arrangement** changed.

---

# 🧠 Important Rule

When reshaping:

> **The total number of elements must remain the same.**

For example:

```text
6 elements
```

can become:

```text
2 × 3 = 6
3 × 2 = 6
1 × 6 = 6
6 × 1 = 6
```

But cannot become:

```text
2 × 4 = 8 ❌
```

because the original array has only 6 elements.

---

# 1️⃣ `reshape()`

## 📌 Definition

`reshape()` changes the shape of an array while keeping the same elements.

### Syntax

```python
array.reshape(rows, columns)
```

or:

```python
array.reshape((rows, columns))
```

---

# 🔹 Basic Example

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print(new_arr)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

# 🧮 Dry Run

Original:

```text
[1 2 3 4 5 6]
```

Number of elements:

```text
6
```

Requested shape:

```text
2 × 3
```

Calculate:

```text
2 × 3 = 6
```

Because both are `6`, reshaping is possible.

Result:

```text
1  2  3
4  5  6
```

---

# 2️⃣ Reshape 1D → 3D

We can also create more dimensions.

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2, 2, 2)

print(new_arr)
```

Output:

```text
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

Shape:

```python
print(new_arr.shape)
```

Output:

```text
(2, 2, 2)
```

Meaning:

```text
2 layers
2 rows per layer
2 columns per row
```

---

# 📊 Reshape Visual

Original:

```text
[1 2 3 4 5 6 7 8]
```

After:

```text
reshape(2, 2, 2)
```

we get:

```text
Layer 0:

1  2
3  4


Layer 1:

5  6
7  8
```

---

# 3️⃣ Reshape Without Changing Data

Look carefully:

```python
arr = np.array([10, 20, 30, 40, 50, 60])

print(arr.reshape(3, 2))
```

Output:

```text
[[10 20]
 [30 40]
 [50 60]]
```

The data itself did not change.

Before:

```text
10 20 30 40 50 60
```

After:

```text
10 20
30 40
50 60
```

### ⭐ Key Point

> `reshape()` changes the **structure**, not the actual values.

---

# 4️⃣ Checking Shape Before and After

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("Original shape:", arr.shape)

new_arr = arr.reshape(2, 3)

print("New shape:", new_arr.shape)
```

Output:

```text
Original shape: (6,)
New shape: (2, 3)
```

---

# 5️⃣ Reshape Error

Suppose:

```python
arr = np.array([1, 2, 3, 4, 5, 6])
```

This has:

```text
6 elements
```

Now:

```python
arr.reshape(2, 4)
```

would require:

```text
2 × 4 = 8 elements
```

But we only have:

```text
6 elements
```

So NumPy raises a **ValueError**.

### ⭐ Rule

```text
Original size = New shape product
```

Must be true.

---

# 6️⃣ `-1` in `reshape()`

This is a very useful NumPy feature. 🔥

NumPy can automatically calculate one dimension if we use:

```text
-1
```

Example:

```python
arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.reshape(2, -1))
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

Why?

We have:

```text
6 elements
```

We specify:

```text
2 rows
```

NumPy calculates:

```text
6 ÷ 2 = 3
```

Therefore:

```text
(2, 3)
```

---

# 🔥 Another Example

```python
arr = np.arange(12)

print(arr.reshape(3, -1))
```

Output:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

Because:

```text
12 ÷ 3 = 4
```

So:

```text
reshape(3, -1)
```

becomes:

```text
reshape(3, 4)
```

---

# 🧠 `-1` Memory Trick

> **`-1` means: NumPy, you calculate this dimension for me.**

---

# 7️⃣ `flatten()`

## 📌 Definition

`flatten()` converts a multi-dimensional array into a **1D array**.

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = arr.flatten()

print(result)
```

Output:

```text
[1 2 3 4 5 6]
```

Visual:

```text
Before:

1  2  3
4  5  6

       ↓ flatten()

[1 2 3 4 5 6]
```

---

# 8️⃣ `flatten()` with 3D Array

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

print(arr.flatten())
```

Output:

```text
[1 2 3 4 5 6 7 8]
```

So:

```text
3D
 ↓
2D
 ↓
1D
```

---

# 9️⃣ `ravel()`

## 📌 Definition

`ravel()` also converts an array into a **1D array**.

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = arr.ravel()

print(result)
```

Output:

```text
[1 2 3 4 5 6]
```

So both:

```python
arr.flatten()
```

and:

```python
arr.ravel()
```

produce a 1D representation.

---

# 🔥 `flatten()` vs `ravel()`

This is important.

| Feature | `flatten()` | `ravel()` |
|---|---|---|
| Converts to 1D | ✅ | ✅ |
| Returns 1D array | ✅ | ✅ |
| Generally creates a copy | ✅ | Usually tries to return a view when possible |
| Memory efficient | Less | More |
| Simpler beginner choice | ✅ | — |

### ⭐ Beginner Memory Trick

```text
flatten → flat + independent copy
ravel   → flatten-like + may share memory
```

We will study **Copy vs View** in detail in **Chapter 13**.

For now, remember:

> **`flatten()` generally creates a copy, while `ravel()` may return a view.**

---

# 🔟 `transpose()`

Now we learn an important operation for 2D arrays.

## 📌 Definition

**Transpose** changes rows into columns and columns into rows.

Suppose:

```text
1  2  3
4  5  6
```

Transpose:

```text
1  4
2  5
3  6
```

---

# Syntax

```python
np.transpose(arr)
```

or:

```python
arr.transpose()
```

---

# Example

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.transpose(arr))
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

# 🧠 Transpose Visual

Original:

```text
      Columns
       ↓ ↓ ↓
      1 2 3
      4 5 6
```

Shape:

```text
(2, 3)
```

After transpose:

```text
      1 4
      2 5
      3 6
```

Shape:

```text
(3, 2)
```

Therefore:

```text
(2, 3) → (3, 2)
```

---

# 1️⃣1️⃣ `.T`

NumPy provides a shortcut:

```python
arr.T
```

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

Therefore:

```python
arr.T
```

is a convenient way to transpose a 2D array.

---

# 📊 `transpose()` vs `.T`

| Method | Example |
|---|---|
| Function | `np.transpose(arr)` |
| Method | `arr.transpose()` |
| Shortcut | `arr.T` |

For a 2D array, they produce the same transpose.

---

# 1️⃣2️⃣ Shape Changes

Suppose:

```python
arr = np.arange(12)
```

Shape:

```text
(12,)
```

We can reshape it into:

```text
(3, 4)
```

```python
arr.reshape(3, 4)
```

Or:

```text
(2, 6)
```

```python
arr.reshape(2, 6)
```

Or:

```text
(4, 3)
```

```python
arr.reshape(4, 3)
```

Or:

```text
(2, 2, 3)
```

```python
arr.reshape(2, 2, 3)
```

All are possible because:

```text
12 elements
```

and:

```text
3 × 4 = 12
2 × 6 = 12
4 × 3 = 12
2 × 2 × 3 = 12
```

---

# 1️⃣3️⃣ `resize()`

## 📌 Definition

`resize()` changes the shape of an array and **can change the total number of elements**.

This is an important difference from `reshape()`.

---

## Example

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr.resize(2, 3)

print(arr)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

Here the array itself was modified.

---

# 🔥 `reshape()` vs `resize()`

| Feature | `reshape()` | `resize()` |
|---|---|---|
| Changes shape | ✅ | ✅ |
| Usually returns a new array/view | ✅ | — |
| Changes original array directly | No | ✅ |
| Must preserve total number of elements | ✅ | ❌ |
| Can change size | ❌ | ✅ |

### ⭐ Important

With:

```python
arr.reshape(...)
```

the original `arr` remains unchanged unless you assign the result.

Example:

```python
new_arr = arr.reshape(2, 3)
```

But:

```python
arr.resize(2, 3)
```

modifies `arr` itself.

---

# 1️⃣4️⃣ `resize()` Can Change Size

Example:

```python
arr = np.array([1, 2, 3, 4])

arr.resize(2, 3)

print(arr)
```

Output:

```text
[[1 2 3]
 [4 0 0]]
```

The requested size is:

```text
2 × 3 = 6
```

Original size:

```text
4
```

The additional positions are filled with zeros for this numeric array.

---

# ⚠️ Don't Confuse `reshape()` and `resize()`

### `reshape()`

```text
6 elements
   ↓
2 × 3
```

Must remain:

```text
6 elements
```

### `resize()`

```text
4 elements
   ↓
2 × 3
```

Can become:

```text
6 elements
```

---

# 🧠 Important Note

There is also a NumPy function:

```python
np.resize()
```

which has different behavior from the **in-place array method**:

```python
arr.resize()
```

For beginner learning, first remember the method:

```python
arr.resize(...)
```

and understand that it can modify the original array and change its size.

---

# 1️⃣5️⃣ Complete Example

Let's use all the important concepts.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original:")
print(arr)

print("\nReshape:")
print(arr.reshape(2, 3))

print("\nReshape with -1:")
print(arr.reshape(3, -1))

print("\n2D array:")
matrix = arr.reshape(2, 3)
print(matrix)

print("\nFlatten:")
print(matrix.flatten())

print("\nRavel:")
print(matrix.ravel())

print("\nTranspose:")
print(matrix.T)
```

Output:

```text
Original:
[1 2 3 4 5 6]

Reshape:
[[1 2 3]
 [4 5 6]]

Reshape with -1:
[[1 2]
 [3 4]
 [5 6]]

2D array:
[[1 2 3]
 [4 5 6]]

Flatten:
[1 2 3 4 5 6]

Ravel:
[1 2 3 4 5 6]

Transpose:
[[1 4]
 [2 5]
 [3 6]]
```

---

# 🌍 Real-World Example — Image Data

Images are commonly represented as arrays.

For a grayscale image, you might have:

```text
Height × Width
```

For example:

```text
28 × 28
```

That means:

```text
28 × 28 = 784 pixels
```

You could represent the pixels as:

```python
image = np.arange(784)
```

Then:

```python
image_2d = image.reshape(28, 28)
```

Now:

```text
1D pixel data
     ↓
reshape
     ↓
28 × 28 image matrix
```

This type of operation is important in **image processing and machine learning**.

---

# 🌍 Real-World Example — Student Dataset

Suppose we have:

```python
marks = np.array([
    80, 75, 90,
    65, 88, 70,
    92, 85, 95
])
```

There are:

```text
9 values
```

Suppose:

```text
3 students
3 subjects
```

We can reshape:

```python
marks = marks.reshape(3, 3)
```

Result:

```text
[[80 75 90]
 [65 88 70]
 [92 85 95]]
```

Now:

```text
Rows    → Students
Columns → Subjects
```

This is very common in data science.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Wrong number of elements

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 4)
```

Wrong because:

```text
2 × 4 = 8
```

but:

```text
size = 6
```

---

## ❌ Mistake 2 — Forgetting to store reshape result

```python
arr.reshape(2, 3)

print(arr)
```

The original array is not automatically replaced.

Use:

```python
arr = arr.reshape(2, 3)
```

if you want to reassign it.

---

## ❌ Mistake 3 — Using more than one `-1`

Don't do:

```python
arr.reshape(-1, -1)
```

NumPy cannot determine both dimensions automatically.

Use only **one `-1`**.

Example:

```python
arr.reshape(2, -1)
```

---

## ❌ Mistake 4 — Confusing `flatten()` and `reshape(-1)`

Both can produce a 1D array:

```python
arr.flatten()
```

and:

```python
arr.reshape(-1)
```

But they have different memory/view behavior.

We'll study memory behavior in **Chapter 13**.

---

# 💼 Interview Questions

### Q1. What is reshaping?

Changing the shape/structure of an array without changing its data.

---

### Q2. What is the main rule of `reshape()`?

The total number of elements must remain the same.

```text
old size = new shape product
```

---

### Q3. What does `-1` mean in reshape?

It tells NumPy to **automatically calculate that dimension**.

---

### Q4. What does `flatten()` do?

Converts an array into a 1D array and generally creates a copy.

---

### Q5. What does `ravel()` do?

Converts an array into a 1D array and generally tries to return a view when possible.

---

### Q6. What does transpose do?

It swaps the axes; for a 2D array, **rows become columns and columns become rows**.

---

### Q7. What is `.T`?

`.T` is a convenient transpose attribute.

```python
arr.T
```

---

### Q8. Difference between `reshape()` and `resize()`?

```text
reshape() → shape changes, size must stay the same

resize()  → can change both shape and size
```

---

# 🧪 Practice Program

Run this:

```python
import numpy as np

arr = np.arange(12)

print("Original:")
print(arr)

print("\nOriginal shape:")
print(arr.shape)

matrix = arr.reshape(3, 4)

print("\n3 × 4:")
print(matrix)

print("\nShape:")
print(matrix.shape)

print("\nTranspose:")
print(matrix.T)

print("\nFlatten:")
print(matrix.flatten())

print("\nRavel:")
print(matrix.ravel())
```

---

# 🎯 Mini Coding Exercise

Create:

```python
numbers = np.arange(1, 13)
```

### 1. Reshape into `3 × 4`

```python
?
```

### 2. Reshape into `4 × 3`

```python
?
```

### 3. Reshape into `2 × 2 × 3`

```python
?
```

### 4. Use `-1` to create `3 × 4`

```python
?
```

### 5. Convert the `3 × 4` array into 1D using `flatten()`

```python
?
```

### 6. Convert it into 1D using `ravel()`

```python
?
```

### 7. Transpose the `3 × 4` array

```python
?
```

### 8. Check the shape after transpose

```python
?
```

---

# 📌 Chapter 9 Summary

| Concept | Purpose |
|---|---|
| `reshape()` | Change shape while preserving number of elements |
| `-1` | Automatically calculate one dimension |
| `flatten()` | Convert to 1D, generally creates a copy |
| `ravel()` | Convert to 1D, may return a view |
| `transpose()` | Swap axes |
| `.T` | Shortcut for transpose |
| `resize()` | Change shape and potentially size |

---

# 🧠 Final Revision Map

```text
                    ARRAY RESHAPING
                          │
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
    reshape()          flatten()          ravel()
        │                 │                 │
   change shape        → 1D              → 1D
   same size          copy generally     view possible
        │
        ↓
      -1
        │
        ↓
 NumPy calculates
 dimension
```

And:

```text
             2D ARRAY
                │
                ↓
        transpose / .T
                │
                ↓
       rows ↔ columns
```

### ⭐ Must Remember

```text
reshape() → change structure
flatten() → make 1D copy
ravel()   → make 1D, view possible
.T        → transpose
resize()  → can change size
-1        → NumPy calculates dimension
```

---

# 📝 Chapter 9 Quiz

1. What is reshaping?
2. What is the main rule of `reshape()`?
3. Can an array of 12 elements be reshaped to `(3, 4)`?
4. Can an array of 12 elements be reshaped to `(5, 3)`?
5. What does `-1` mean in `reshape()`?
6. What does `flatten()` do?
7. What is the main difference between `flatten()` and `ravel()`?
8. What does `.T` do?
9. What happens to a `(2, 3)` array after transpose?
10. What is the difference between `reshape()` and `resize()`?

---

# ✅ Chapter 9 COMPLETE

### Next → 🚀 **Chapter 10 — Joining Arrays**

We will learn:

```text
np.concatenate()
np.vstack()
np.hstack()
np.stack()
np.dstack()
```

with **visual diagrams**, row/column joining, shape changes, and clear differences between each method.

Type **`NEXT`** when ready.