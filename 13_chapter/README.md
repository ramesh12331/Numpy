# 📋 Chapter 13 — NumPy Copy vs View

Welcome to **Chapter 13** 🎯

This is a **very important NumPy concept**, especially when working with large datasets.

In this chapter we will understand:

```text
copy() → independent data 📋
view() → shares underlying data 👀
```

The biggest question we will answer is:

> ❓ **If I change one array, will another array also change?**

---

# 📚 Chapter 13 Roadmap

We will learn:

1. 📋 What is a Copy?
2. 👀 What is a View?
3. `copy()`
4. `view()`
5. 🧠 Memory behavior
6. 🔍 How to check whether arrays share data
7. Copy vs View comparison
8. 🌍 Real-world examples
9. ⚠️ Common mistakes
10. 💼 Interview Questions
11. 📝 Practice
12. 🎯 Mini Exercise
13. 📋 Summary
14. 🧪 Quiz

---

# 1️⃣ First Understand the Problem

Consider:

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40])
```

Now we write:

```python
arr2 = arr1
```

What happens?

Many beginners think:

```text
arr1 → [10 20 30 40]

arr2 → [10 20 30 40]
```

and assume they are two independent arrays.

❌ **That's not what happens.**

Both variable names refer to the **same array object**.

---

# 2️⃣ Assignment Is NOT Copy

Let's see:

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40])

arr2 = arr1

arr2[0] = 999

print("arr1:", arr1)
print("arr2:", arr2)
```

### Output

```text
arr1: [999  20  30  40]
arr2: [999  20  30  40]
```

😲 Why did `arr1` change?

Because:

```python
arr2 = arr1
```

does **not create a new independent array**.

---

# 🧠 Visual Understanding

Think of the array as a box in memory:

```text
             MEMORY
        ┌───────────────┐
        │ 10 20 30 40   │
        └───────────────┘
             ↑       ↑
             │       │
           arr1     arr2
```

Both names point to the **same data**.

So:

```python
arr2[0] = 999
```

changes the same memory:

```text
        ┌───────────────┐
        │ 999 20 30 40  │
        └───────────────┘
             ↑       ↑
             │       │
           arr1     arr2
```

Therefore:

```text
arr1 → changed
arr2 → changed
```

---

# ⭐ Important

Remember these three concepts:

```text
arr2 = arr1
       ↓
same array/object reference

arr2 = arr1.copy()
       ↓
independent copy

arr2 = arr1.view()
       ↓
new view sharing underlying data
```

This distinction is **extremely important**.

---

# 3️⃣ What is a Copy?

### 📖 Definition

A **copy** creates a **new array with its own data**.

Syntax:

```python
new_array = old_array.copy()
```

---

# 🟢 Example — `copy()`

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40])

arr2 = arr1.copy()

arr2[0] = 999

print("arr1:", arr1)
print("arr2:", arr2)
```

### Output

```text
arr1: [10 20 30 40]
arr2: [999  20  30  40]
```

🎉 This time `arr1` did **not** change.

---

# 🧠 Why?

Because:

```python
arr2 = arr1.copy()
```

creates separate data.

Visual:

```text
             MEMORY

        ┌───────────────┐
arr1 →  │ 10 20 30 40   │
        └───────────────┘


        ┌───────────────┐
arr2 →  │ 10 20 30 40   │
        └───────────────┘
```

Two separate arrays.

After:

```python
arr2[0] = 999
```

we get:

```text
        ┌───────────────┐
arr1 →  │ 10 20 30 40   │
        └───────────────┘


        ┌───────────────┐
arr2 →  │ 999 20 30 40  │
        └───────────────┘
```

---

# 🔥 Key Point

```text
copy()
  ↓
Independent data
  ↓
Changing one does NOT change the other
```

---

# 4️⃣ What is a View?

Now let's understand `view()`.

### 📖 Definition

A **view** creates another array object that **shares the same underlying data** with the original array.

Syntax:

```python
new_array = old_array.view()
```

---

# 🟢 Example — `view()`

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40])

arr2 = arr1.view()

arr2[0] = 999

print("arr1:", arr1)
print("arr2:", arr2)
```

### Output

```text
arr1: [999  20  30  40]
arr2: [999  20  30  40]
```

Again:

```text
arr1 changed
arr2 changed
```

Why?

Because the view **shares the underlying data**.

---

# 🧠 Visual

```text
                 SAME DATA
             ┌───────────────┐
             │ 10 20 30 40   │
             └───────────────┘
                  ↑       ↑
                  │       │
                arr1     arr2
```

`arr2` is a **view** of the same underlying data.

---

# 5️⃣ Copy vs View

Let's compare.

### 📋 Copy

```python
arr2 = arr1.copy()
```

```text
arr1 → [10 20 30 40]

arr2 → [10 20 30 40]

Different data
```

Change:

```python
arr2[0] = 999
```

Result:

```text
arr1 → [10 20 30 40]

arr2 → [999 20 30 40]
```

---

### 👀 View

```python
arr2 = arr1.view()
```

```text
arr1 ──┐
       ↓
    SAME DATA
       ↑
arr2 ──┘
```

Change:

```python
arr2[0] = 999
```

Result:

```text
arr1 → [999 20 30 40]

arr2 → [999 20 30 40]
```

---

# ⭐ Most Important Table

| Feature | `copy()` | `view()` |
|---|---|---|
| New array object | ✅ | ✅ |
| New underlying data | ✅ | ❌ |
| Shares data with original | ❌ | ✅ |
| Change copy affects original | ❌ | ✅ |
| Independent data | ✅ | ❌ |
| Memory efficient | Less | More |
| Main purpose | Independent data | Shared data |

---

# 6️⃣ Object vs Data

This is a slightly deeper concept, but very important.

With:

```python
arr2 = arr1.view()
```

`arr2` is a **different array object**, but it shares the same underlying data.

So:

```text
Array object → different
Underlying data → shared
```

Visual:

```text
arr1 object ──────┐
                  ↓
              DATA MEMORY
                  ↑
arr2 object ──────┘
```

This is why changing elements through one can affect the other.

---

# 7️⃣ Checking `base`

NumPy provides `.base` to help determine whether an array is based on another array.

Example:

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40])

arr2 = arr1.view()

print(arr2.base)
```

Possible output:

```text
[10 20 30 40]
```

This indicates that the view is based on another array.

For a copy:

```python
arr3 = arr1.copy()

print(arr3.base)
```

Output:

```text
None
```

### 🧠 Meaning

```text
view
 ↓
has a base / shares underlying data

copy
 ↓
base is None
```

---

# 8️⃣ Checking with `np.shares_memory()`

NumPy also provides:

```python
np.shares_memory()
```

### Example

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40])

arr2 = arr1.copy()
arr3 = arr1.view()

print(np.shares_memory(arr1, arr2))
print(np.shares_memory(arr1, arr3))
```

Output:

```text
False
True
```

Meaning:

```text
arr1 & arr2 → ❌ Don't share memory

arr1 & arr3 → ✅ Share memory
```

---

# 9️⃣ `np.may_share_memory()`

There is also:

```python
np.may_share_memory()
```

Example:

```python
np.may_share_memory(arr1, arr3)
```

It gives a conservative indication that arrays **may share memory**.

For learning the basic copy/view distinction, remember:

```text
shares_memory()
→ checks actual memory sharing

may_share_memory()
→ may share memory
```

You don't need to focus heavily on `may_share_memory()` yet.

---

# 🔟 Copy vs View with Slicing

This is **very important**.

Suppose:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
```

Now:

```python
part = arr[1:4]
```

Many NumPy slices are **views** of the original array.

Let's test:

```python
part[0] = 999

print("arr:", arr)
print("part:", part)
```

Output:

```text
arr:  [ 10 999  30  40  50]
part: [999  30  40]
```

😲 The original changed.

---

# 🧠 Why?

Because:

```python
part = arr[1:4]
```

generally creates a **view** rather than an independent copy.

Visual:

```text
Original:

[10 20 30 40 50]
    └────────┘
       view
```

The slice refers to part of the same underlying data.

---

# ⭐ If You Want an Independent Slice

Use:

```python
part = arr[1:4].copy()
```

Then:

```python
part[0] = 999
```

The original stays unchanged.

```text
Original:
[10 20 30 40 50]

Part:
[999 30 40]
```

---

# 🔥 Very Important Rule

When you want an **independent subset**, use:

```python
subset = arr[start:stop].copy()
```

instead of simply:

```python
subset = arr[start:stop]
```

---

# 1️⃣1️⃣ Real-World Example — Student Marks

Suppose:

```python
marks = np.array([
    80,
    75,
    90,
    65,
    88
])
```

You want the first three marks:

```python
top_students = marks[:3]
```

Now:

```python
top_students[0] = 100
```

Because slicing can create a view, the original may become:

```text
[100 75 90 65 88]
```

If you don't want that:

```python
top_students = marks[:3].copy()
```

Now:

```python
top_students[0] = 100
```

Original remains:

```text
[80 75 90 65 88]
```

---

# 1️⃣2️⃣ Real-World Example — Image Processing

Suppose an image is represented as a NumPy array:

```text
Image
 ↓
Large NumPy array
 ↓
Millions of values
```

Creating unnecessary copies can consume significant memory.

A view can sometimes allow you to work with a portion of the data without copying all the underlying data.

```text
Original Image
      │
      ├── View → selected region
      │
      └── Original data remains shared
```

But if you need to modify the extracted region **without affecting the original**, use:

```python
region = image[100:200, 100:200].copy()
```

---

# 1️⃣3️⃣ Memory Efficiency

Suppose we have a very large array:

```python
arr = np.arange(1_000_000)
```

A copy can require another block of memory for the data.

A view can often reuse the same underlying data.

Conceptually:

```text
COPY

Original → 💾 Data
Copy     → 💾 Another Data

Memory → more
```

versus:

```text
VIEW

Original ──┐
           ├── 💾 Same Data
View ──────┘

Memory → less
```

### ⭐ Important

A view can be **memory efficient**, but it requires care because modifications can affect the original data.

---

# 1️⃣4️⃣ Assignment vs View vs Copy

This is a very useful comparison.

```python
arr2 = arr1
```

### Assignment

```text
Same array object/reference
```

---

```python
arr2 = arr1.view()
```

### View

```text
Different array object
Same underlying data
```

---

```python
arr2 = arr1.copy()
```

### Copy

```text
Different array object
Different underlying data
```

---

# 🧠 Complete Visual

```text
                arr1
                  │
                  ↓
             ┌─────────┐
             │  DATA   │
             └─────────┘
              ↑       ↑
              │       │
           arr2      view
        assignment   object


COPY:

arr1 ─────→ ┌─────────┐
            │ DATA A  │
            └─────────┘

arr2 ─────→ ┌─────────┐
            │ DATA B  │
            └─────────┘
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1

Thinking this creates a copy:

```python
arr2 = arr1
```

It doesn't.

---

## ❌ Mistake 2

Thinking `view()` creates independent data.

It doesn't.

```python
arr2 = arr1.view()
```

The underlying data is shared.

---

## ❌ Mistake 3

Forgetting that slices can share data.

```python
part = arr[1:4]
```

If you need independence:

```python
part = arr[1:4].copy()
```

---

## ❌ Mistake 4

Using `copy()` everywhere.

Copies can consume additional memory.

If you intentionally want shared data and understand the consequences, a view may be appropriate.

---

# 💼 Interview Questions

### Q1. What is the difference between a copy and a view?

**Answer:**

A copy creates independent data, while a view creates another array object that shares the underlying data.

---

### Q2. Does `arr2 = arr1` create a copy?

**Answer:**

No. It creates another reference to the same array object.

---

### Q3. How do you create an independent NumPy array?

```python
arr2 = arr1.copy()
```

---

### Q4. How do you create a view?

```python
arr2 = arr1.view()
```

---

### Q5. If you modify a view, can the original change?

**Answer:**

Yes. Because the view shares the underlying data.

---

### Q6. Which is generally more memory efficient?

**Answer:**

A view can be more memory efficient because it can share the underlying data instead of creating another data copy.

---

### Q7. What does `.base` help you determine?

**Answer:**

It can show whether an array is based on another array, which is useful for understanding views and shared data.

---

### Q8. How can you check whether two arrays share memory?

```python
np.shares_memory(arr1, arr2)
```

---

### Q9. What happens with this?

```python
arr2 = arr1[1:4]
```

**Answer:**

A slice often creates a view, so changes to the slice can affect the original array.

---

# 📝 Practice

## Practice 1 — Assignment

Predict the output:

```python
import numpy as np

arr1 = np.array([10, 20, 30])

arr2 = arr1

arr2[0] = 100

print(arr1)
print(arr2)
```

---

## Practice 2 — Copy

Predict:

```python
arr1 = np.array([10, 20, 30])

arr2 = arr1.copy()

arr2[0] = 100

print(arr1)
print(arr2)
```

---

## Practice 3 — View

Predict:

```python
arr1 = np.array([10, 20, 30])

arr2 = arr1.view()

arr2[0] = 100

print(arr1)
print(arr2)
```

---

## Practice 4 — Memory

What will this return?

```python
print(np.shares_memory(arr1, arr2))
```

Test it for:

```python
arr2 = arr1.copy()
```

and:

```python
arr2 = arr1.view()
```

---

# 🎯 Mini Coding Exercise

Run this complete program:

```python
import numpy as np

# Original array
arr = np.array([10, 20, 30, 40, 50])

# Create a copy
copy_arr = arr.copy()

# Create a view
view_arr = arr.view()

# Modify the copy
copy_arr[0] = 100

# Modify the view
view_arr[1] = 200

print("Original:", arr)
print("Copy:", copy_arr)
print("View:", view_arr)

print()
print("Original & Copy share memory:",
      np.shares_memory(arr, copy_arr))

print("Original & View share memory:",
      np.shares_memory(arr, view_arr))
```

### Expected Output

```text
Original: [ 10 200  30  40  50]
Copy:     [100  20  30  40  50]
View:     [ 10 200  30  40  50]

Original & Copy share memory: False
Original & View share memory: True
```

### 🧠 Dry Run

Initially:

```text
arr
[10 20 30 40 50]
```

After copy modification:

```text
copy_arr
[100 20 30 40 50]

arr
[10 20 30 40 50]
```

No effect on original.

Then view modification:

```text
view_arr[1] = 200
```

Because the view shares data:

```text
arr
[10 200 30 40 50]
```

---

# 📋 Chapter 13 Summary

| Concept | Meaning |
|---|---|
| `arr2 = arr1` | Same array reference |
| `copy()` | Independent data |
| `view()` | Shares underlying data |
| `.base` | Helps inspect array ownership/base |
| `np.shares_memory()` | Checks actual memory sharing |
| Slicing | Often creates a view |
| `.copy()` after slicing | Creates independent data |

---

# 🧠 One-Minute Revision

```text
                 NumPy Arrays
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   Assignment       View          Copy
        │             │             │
   arr2 = arr1   arr2 = arr1.view()  arr2 = arr1.copy()
        │             │             │
   Same object    Shared data     Separate data
        │             │             │
        ↓             ↓             ↓
    Changes       Changes can     Changes do NOT
    affect both   affect original affect original
```

### ⭐ Golden Rule

```text
Need independent data?
        ↓
      copy()
```

```text
Need shared underlying data?
        ↓
      view()
```

```text
Need to simply reference the same array?
        ↓
    arr2 = arr1
```

---

# 🧪 Chapter 13 Quiz

### 1. Does this create an independent copy?

```python
arr2 = arr1
```

A. Yes  
B. No

---

### 2. Which creates independent data?

A. `view()`  
B. `copy()`

---

### 3. Which shares underlying data?

A. `copy()`  
B. `view()`

---

### 4. What happens here?

```python
arr2 = arr1.view()
arr2[0] = 999
```

Can `arr1[0]` also change?

A. Yes  
B. No

---

### 5. What does this do?

```python
arr2 = arr1.copy()
```

A. Creates independent data  
B. Creates a view  
C. Deletes the array  
D. Sorts the array

---

### 6. What does this check?

```python
np.shares_memory(arr1, arr2)
```

A. Shape  
B. Data type  
C. Memory sharing  
D. Number of dimensions

---

### 7. Which statement is correct?

A. `copy()` shares underlying data  
B. `view()` always creates independent data  
C. `copy()` creates independent data  
D. Assignment always creates a new array

---

### 8. What should you use if you want an independent sliced array?

```python
part = arr[1:4] ______
```

Fill in the blank.

---

# ✅ Chapter 13 COMPLETE

You now understand one of the most important NumPy memory concepts:

**Assignment → View → Copy → Memory Sharing → Slicing behavior**.

👉 Type **`NEXT`** when you're ready for:

# 🚀 Chapter 14 — NumPy Broadcasting

We will learn how NumPy performs operations between arrays with **different shapes**, including:

```text
Scalar + Array
1D + 2D
Compatible Shapes
Broadcasting Rules
Broadcasting Errors
Real-world examples
```

This is a **very important concept for NumPy and Data Science**.