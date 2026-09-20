# 🚀 NumPy — Chapter 3 Array Attributes

Welcome to Chapter 3! 🎯

In Chapter 2, we learned how to create NumPy arrays.

Now we will learn how to inspect an array — its dimensions, shape, number of elements, data type, and memory usage.

---

# 📘 1. What are Array Attributes

Array attributes are properties that tell us important information about a NumPy array.

For example

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

We can ask NumPy

- ❓ How many dimensions
- ❓ How many rows and columns
- ❓ How many total elements
- ❓ What data type
- ❓ How much memory does each element use
- ❓ How much total memory does the array use

NumPy provides attributes for this.

---

# 🧠 Chapter 3 Topics

 Attribute  Meaning 
------
 `ndim`  Number of dimensions 
 `shape`  Size of each dimension 
 `size`  Total number of elements 
 `dtype`  Data type 
 `itemsize`  Memory used by one element 
 `nbytes`  Total memory used 

### ⭐ Easy Memory Trick

 ndim → shape → size → dtype → itemsize → nbytes

---

# 1️⃣ `ndim` — Number of Dimensions

### 📌 Definition

`ndim` tells us how many dimensions an array has.

### Syntax

```python
array.ndim
```

### Example

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.ndim)
```

### Output

```text
2
```

### Why

Our array looks like

```text
        Columns
       ↓   ↓   ↓
      10  20  30   ← Row 1
      40  50  60   ← Row 2
```

It has

```text
Rows + Columns
```

So it is a 2-dimensional array.

### Examples

```python
np.array([1, 2, 3]).ndim
```

Output

```text
1
```

```python
np.array([
    [1, 2],
    [3, 4]
]).ndim
```

Output

```text
2
```

A 3D example

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

print(arr.ndim)
```

Output

```text
3
```

---

# 2️⃣ `shape` — Size of Each Dimension

### 📌 Definition

`shape` tells us the size of the array in each dimension.

For a 2D array

```text
(number of rows, number of columns)
```

### Syntax

```python
array.shape
```

### Example

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.shape)
```

### Output

```text
(2, 3)
```

This means

```text
2 rows
3 columns
```

Visual

```text
        3 columns
     ┌─────────────┐
     │ 10  20  30 │  ← Row 1
     │ 40  50  60 │  ← Row 2
     └─────────────┘
          2 rows
```

So

```text
shape = (2, 3)
```

### ⭐ Remember

```text
shape = (rows, columns)
```

for a 2D array.

---

# 3️⃣ `size` — Total Number of Elements

### 📌 Definition

`size` tells us the total number of elements in the array.

### Syntax

```python
array.size
```

Example

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.size)
```

Output

```text
6
```

Why

```text
2 rows × 3 columns
```

Therefore

```text
2 × 3 = 6
```

So

```text
size = 6
```

### 🧮 Formula

For a 2D array

```text
size = rows × columns
```

Example

```text
shape = (4, 5)

size = 4 × 5
     = 20
```

---

# 4️⃣ `dtype` — Data Type

### 📌 Definition

`dtype` tells us the data type of the elements stored inside the NumPy array.

### Syntax

```python
array.dtype
```

Example

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr.dtype)
```

Possible output

```text
int64
```

The exact integer dtype can depend on your platformNumPy build.

---

## Example with Float

```python
arr = np.array([10.5, 20.5, 30.5])

print(arr.dtype)
```

Output commonly

```text
float64
```

---

## Example with Boolean

```python
arr = np.array([True, False, True])

print(arr.dtype)
```

Output

```text
bool
```

---

# 5️⃣ `itemsize` — Memory Used by One Element

### 📌 Definition

`itemsize` tells us

 How many bytes are used by one array element.

### Syntax

```python
array.itemsize
```

Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr.dtype)
print(arr.itemsize)
```

Possible output

```text
int64
8
```

That means

```text
One element = 8 bytes
```

For example

```text
10 → 8 bytes
20 → 8 bytes
30 → 8 bytes
40 → 8 bytes
```

---

# 6️⃣ `nbytes` — Total Memory Used

### 📌 Definition

`nbytes` tells us the total number of bytes used by the array's elements.

### Syntax

```python
array.nbytes
```

Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr.nbytes)
```

If the array uses `int64`

```text
4 elements × 8 bytes
```

Therefore

```text
32 bytes
```

Output

```text
32
```

---

# 🧮 Important Formula

This is very important for interviews.

```text
nbytes = size × itemsize
```

Example

```text
size = 4
itemsize = 8 bytes
```

Therefore

```text
nbytes = 4 × 8
       = 32 bytes
```

---

# 🔥 Complete Example

Let's combine everything.

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(Array)
print(arr)

print(Number of dimensions, arr.ndim)
print(Shape, arr.shape)
print(Total elements, arr.size)
print(Data type, arr.dtype)
print(Memory per element, arr.itemsize, bytes)
print(Total memory, arr.nbytes, bytes)
```

### Output

Depending on your platform

```text
Array
[[10 20 30]
 [40 50 60]]

Number of dimensions 2
Shape (2, 3)
Total elements 6
Data type int64
Memory per element 8 bytes
Total memory 48 bytes
```

---

# 🧠 Dry Run

Array

```text
[[10, 20, 30],
 [40, 50, 60]]
```

### Step 1 — `ndim`

```text
2
```

Because

```text
Rows + Columns
```

---

### Step 2 — `shape`

```text
(2, 3)
```

Because

```text
2 rows
3 columns
```

---

### Step 3 — `size`

```text
2 × 3 = 6
```

So

```text
size = 6
```

---

### Step 4 — `dtype`

The values are integers.

For example

```text
int64
```

---

### Step 5 — `itemsize`

For `int64`

```text
8 bytes
```

---

### Step 6 — `nbytes`

```text
size × itemsize

6 × 8

= 48 bytes
```

---

# 📊 All Attributes Together

 Attribute  Meaning  Example 
---------
 `ndim`  Number of dimensions  `2` 
 `shape`  Rows and columns  `(2, 3)` 
 `size`  Total elements  `6` 
 `dtype`  Data type  `int64` 
 `itemsize`  Bytes per element  `8` 
 `nbytes`  Total bytes  `48` 

---

# 🌍 Real-World Example

Suppose we have student marks

```python
marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])
```

We can inspect it

```python
print(Dimensions, marks.ndim)
print(Shape, marks.shape)
print(Total marks, marks.size)
print(Data type, marks.dtype)
print(Memory per value, marks.itemsize)
print(Total memory, marks.nbytes)
```

Output might be

```text
Dimensions 2
Shape (3, 3)
Total marks 9
Data type int64
Memory per value 8
Total memory 72
```

This tells us

```text
3 students
3 subjects
9 marks
```

---

# ⚠️ Common Mistakes

### ❌ Mistake 1 Using parentheses

Wrong

```python
arr.shape()
```

Correct

```python
arr.shape
```

`shape` is an attribute, not a function.

---

### ❌ Mistake 2

Wrong

```python
arr.ndim()
```

Correct

```python
arr.ndim
```

---

### ❌ Mistake 3

Wrong

```python
arr.size()
```

Correct

```python
arr.size
```

---

### 🧠 Important Difference

```python
arr.reshape()
```

is a method.

But

```python
arr.shape
arr.size
arr.ndim
arr.dtype
```

are attributes.

---

# 🎯 Attribute vs Method

 Type  Example  Parentheses 
---------
 Attribute  `arr.shape`  ❌ No 
 Attribute  `arr.size`  ❌ No 
 Attribute  `arr.ndim`  ❌ No 
 Attribute  `arr.dtype`  ❌ No 
 Method  `arr.reshape()`  ✅ Yes 
 Method  `arr.flatten()`  ✅ Yes 

### Memory Trick

 Property → no `()`  
 Action → usually `()`

---

# 💼 Interview Questions

### Q1. What does `ndim` return

Answer  
`ndim` returns the number of dimensions of a NumPy array.

---

### Q2. What does `shape` return

Answer  
`shape` returns the size of each dimension.

For example

```python
(3, 4)
```

means

```text
3 rows
4 columns
```

---

### Q3. What is the difference between `size` and `shape`

Answer

```text
shape → structuredimensions
size  → total number of elements
```

Example

```text
shape = (2, 3)
size  = 6
```

---

### Q4. What does `dtype` tell us

Answer  
It tells us the data type of the elements in the NumPy array.

---

### Q5. What is `itemsize`

Answer  
`itemsize` tells us the number of bytes used by one element.

---

### Q6. What is `nbytes`

Answer  
`nbytes` tells us the total memory used by the array's elements.

---

### Q7. How do you calculate `nbytes`

Answer

```text
nbytes = size × itemsize
```

---

# 📝 Practice

Try this in VS Code

```python
import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print(Dimensions, arr.ndim)
print(Shape, arr.shape)
print(Size, arr.size)
print(Data type, arr.dtype)
print(Item size, arr.itemsize)
print(Total bytes, arr.nbytes)
```

Before running it, predict

```text
ndim   = 
shape  = 
size   = 
```

### 💡 Hint

The array contains

```text
3 rows
4 columns
```

Therefore

```text
shape = (3, 4)
size = 3 × 4
```

---

# 🧪 Mini Exercise

Create this array

```python
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
```

Find

1. `ndim`
2. `shape`
3. `size`
4. `dtype`
5. `itemsize`
6. `nbytes`

Then verify using Python.

---

# 📌 Chapter 3 Summary

```text
                 NumPy Array
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
      ndim          shape           size
  dimensions     structure      total values
       │              │              │
       ↓              ↓              ↓
       2            (2, 3)           6
       
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
     dtype         itemsize        nbytes
   data type     bytesvalue     total bytes
       │              │              │
       ↓              ↓              ↓
    int64          8 bytes        48 bytes
```

### ⭐ Must Remember

 Attribute  Remember as 
------
 `ndim`  How many dimensions 
 `shape`  What is the structure 
 `size`  How many values 
 `dtype`  What type 
 `itemsize`  Bytes per value 
 `nbytes`  Total bytes 

---

# 🎯 Chapter 3 Quiz

Don't look at the answers yet.

### 1. What does `ndim` represent

A. Number of elements  
B. Number of dimensions  
C. Data type  
D. Memory size  

### 2. If

```python
arr.shape
```

returns

```text
(5, 4)
```

How many elements are there

### 3. Which attribute gives the data type

A. `type`  
B. `dtype`  
C. `datatype()`  
D. `data`

### 4. What does `itemsize` represent

### 5. If

```text
size = 20
itemsize = 8
```

What is `nbytes`

### 6. Which is correct

```python
A. arr.shape()
B. arr.shape
```

### 7. What is the difference between an attribute and a method

---

## 🔑 Quick Revision

```text
ndim    → Dimensions
shape   → Structure
size    → Total elements
dtype   → Data type
itemsize → Bytes per element
nbytes  → Total bytes
```

Chapter 3 — COMPLETE ✅

When you're ready, type `NEXT` for

# 🚀 Chapter 4 — NumPy Indexing

We will learn 1D, 2D, and 3D indexing, positivenegative indexes, row selection, column selection, and complete rowscolumns with visual dry runs.