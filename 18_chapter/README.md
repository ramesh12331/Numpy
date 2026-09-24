# 🚀 Chapter 18 — NumPy Handling Missing Values

Welcome to **Chapter 18**! 🎯

In real-world datasets, some values are often missing.

For example:

```text
Employee    Age    Salary
-------------------------
Ramesh      25     50000
Suresh      NaN    60000
Kiran       28     NaN
```

Here, `NaN` means **Not a Number / missing numerical value**.

Today we will learn how to **detect and work with missing and invalid numerical values** using NumPy.

---

# 📚 What We Will Learn

1. 🔹 What is `NaN`?
2. 🔹 Creating `np.nan`
3. 🔹 `np.isnan()`
4. 🔹 `np.isfinite()`
5. 🔹 `np.isinf()`
6. 🔹 Combining these functions
7. 🔹 Filtering missing values
8. 🔹 Replacing missing values
9. 🔹 `NaN` with mathematical functions
10. 🔹 Real-world dataset example
11. 🔹 Common mistakes
12. 🔹 Interview questions
13. 🔹 Practice
14. 🔹 Mini exercise
15. 🔹 Summary
16. 🔹 Quiz

---

# 1️⃣ What is `NaN`?

### 📌 Definition

`NaN` means:

> **Not a Number**

NumPy represents it using:

```python
np.nan
```

Example:

```python
import numpy as np

x = np.nan

print(x)
```

Output:

```text
nan
```

---

# 🧠 Important Concept

`NaN` is commonly used to represent a **missing numerical value**.

For example:

```python
salary = np.array([
    50000,
    60000,
    np.nan,
    70000
])

print(salary)
```

Output:

```text
[50000. 60000.    nan 70000.]
```

Notice that the array may become a floating-point array because `NaN` is a floating-point value.

---

# 2️⃣ Why Do We Need Missing-Value Handling?

Imagine this dataset:

```python
marks = np.array([
    80,
    90,
    np.nan,
    70,
    85
])
```

Suppose we calculate:

```python
print(np.mean(marks))
```

Output:

```text
nan
```

Why?

Because:

```text
80 + 90 + NaN + 70 + 85
                  ↓
                 NaN
```

Once `NaN` enters the calculation, many ordinary NumPy calculations produce `NaN`.

---

# 3️⃣ Detecting `NaN` with `np.isnan()` ⭐⭐⭐

NumPy provides:

```python
np.isnan()
```

It checks whether a value is `NaN`.

Example:

```python
import numpy as np

arr = np.array([
    10,
    np.nan,
    30,
    np.nan,
    50
])

result = np.isnan(arr)

print(result)
```

Output:

```text
[False  True False  True False]
```

### 🧠 Meaning

```text
10      → False
NaN     → True
30      → False
NaN     → True
50      → False
```

So:

> `True` means the value is `NaN`.

---

# 4️⃣ Visual Understanding

Consider:

```text
Array:

10     NaN     30     NaN     50
 ↓       ↓      ↓       ↓      ↓
False  True   False   True   False
```

Therefore:

```python
np.isnan(arr)
```

creates a **Boolean mask**.

This connects directly with **Chapter 15 — Boolean Masking**.

---

# 5️⃣ Finding Only Missing Values

We can use the Boolean mask:

```python
print(arr[np.isnan(arr)])
```

Output:

```text
[nan nan]
```

This means:

```text
arr
 ↓
[10, NaN, 30, NaN, 50]

np.isnan(arr)
 ↓
[False, True, False, True, False]

arr[mask]
 ↓
[NaN, NaN]
```

---

# 6️⃣ Finding Non-Missing Values

We can use `~`:

```python
mask = ~np.isnan(arr)

print(arr[mask])
```

Output:

```text
[10. 30. 50.]
```

### 🧠 Remember

```text
np.isnan(arr)
      ↓
Find NaN

~np.isnan(arr)
      ↓
Find NOT NaN
```

---

# 7️⃣ Counting Missing Values ⭐

A very common data-analysis task is:

> How many missing values are present?

Example:

```python
arr = np.array([
    10,
    np.nan,
    30,
    np.nan,
    50
])

missing_count = np.sum(np.isnan(arr))

print(missing_count)
```

Output:

```text
2
```

### Why does this work?

`np.isnan(arr)` gives:

```text
[False, True, False, True, False]
```

Boolean values behave numerically in this context:

```text
False → 0
True  → 1
```

So:

```text
0 + 1 + 0 + 1 + 0 = 2
```

Therefore:

```python
np.sum(np.isnan(arr))
```

counts the number of `NaN` values.

---

# 8️⃣ `np.isfinite()` ⭐⭐⭐

Now let's understand:

```python
np.isfinite()
```

### 📌 Definition

`np.isfinite()` checks whether a value is a **finite number**.

Finite means:

```text
Not NaN
AND
Not +∞
AND
Not -∞
```

Example:

```python
arr = np.array([
    10,
    np.nan,
    np.inf,
    -np.inf,
    50
])

print(np.isfinite(arr))
```

Output:

```text
[ True False False False  True]
```

Visual:

```text
10       → True
NaN      → False
+inf     → False
-inf     → False
50       → True
```

---

# 9️⃣ What is Infinity?

NumPy provides:

```python
np.inf
```

which represents positive infinity.

Example:

```python
print(np.inf)
```

Output:

```text
inf
```

Negative infinity:

```python
print(-np.inf)
```

Output:

```text
-inf
```

---

# 🔟 `np.isinf()`

To detect infinity:

```python
np.isinf()
```

Example:

```python
arr = np.array([
    10,
    np.inf,
    30,
    -np.inf,
    50
])

print(np.isinf(arr))
```

Output:

```text
[False  True False  True False]
```

So:

```text
np.isinf()
      ↓
Detect +∞ and -∞
```

---

# 1️⃣1️⃣ `np.isnan()` vs `np.isinf()` vs `np.isfinite()`

This comparison is **very important**.

| Function        | Detects               |
| --------------- | --------------------- |
| `np.isnan()`    | `NaN`                 |
| `np.isinf()`    | `+∞` and `-∞`         |
| `np.isfinite()` | Normal finite numbers |

Example:

```python
arr = np.array([
    10,
    np.nan,
    np.inf,
    -np.inf
])
```

Results:

```text
np.isnan()
[False, True, False, False]

np.isinf()
[False, False, True, True]

np.isfinite()
[True, False, False, False]
```

---

# 1️⃣2️⃣ Relationship Between Them

Think of it like this:

```text
                 NUMERICAL VALUES
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
       FINITE                    NON-FINITE
          │                         │
          ↓                    ┌────┴────┐
     normal numbers             NaN     Infinity
```

So:

```text
finite → normal usable numbers
non-finite → NaN or infinity
```

---

# 1️⃣3️⃣ Removing `NaN` Values

Suppose:

```python
arr = np.array([
    10,
    np.nan,
    30,
    np.nan,
    50
])
```

We can keep only non-NaN values:

```python
clean = arr[~np.isnan(arr)]

print(clean)
```

Output:

```text
[10. 30. 50.]
```

### Step-by-step

```text
arr
↓
[10, NaN, 30, NaN, 50]

np.isnan(arr)
↓
[F, T, F, T, F]

~np.isnan(arr)
↓
[T, F, T, F, T]

arr[mask]
↓
[10, 30, 50]
```

---

# 1️⃣4️⃣ Replacing `NaN` Values

Sometimes we don't want to remove missing values.

Instead, we may want to **replace** them.

Example:

```python
arr = np.array([
    10,
    np.nan,
    30,
    np.nan,
    50
])

arr[np.isnan(arr)] = 0

print(arr)
```

Output:

```text
[10.  0. 30.  0. 50.]
```

So:

```text
NaN → 0
```

---

# ⚠️ Is Replacing With 0 Always Correct?

**No.**

It depends on the meaning of the missing value.

For example:

```text
Salary = missing
```

Replacing it with:

```text
0
```

may incorrectly mean:

> The employee earns zero salary.

Instead, you might use an appropriate statistical value such as the mean or median, depending on the data and analysis goal.

---

# 1️⃣5️⃣ Replacing `NaN` With Mean

Suppose:

```python
arr = np.array([
    10,
    20,
    np.nan,
    40,
    50
])
```

First calculate the mean of the known values.

A normal:

```python
np.mean(arr)
```

returns:

```text
nan
```

Instead, use:

```python
np.nanmean(arr)
```

Example:

```python
mean_value = np.nanmean(arr)

print(mean_value)
```

Output:

```text
30.0
```

Because:

```text
10 + 20 + 40 + 50
------------------
        4

= 30
```

Then replace:

```python
arr[np.isnan(arr)] = mean_value

print(arr)
```

Output:

```text
[10. 20. 30. 40. 50.]
```

---

# 1️⃣6️⃣ Useful `nan*` Functions

NumPy provides special functions that ignore `NaN` values.

### `np.nanmean()`

```python
np.nanmean(arr)
```

Calculates mean while ignoring `NaN`.

### `np.nansum()`

```python
np.nansum(arr)
```

Calculates sum while ignoring `NaN`.

### `np.nanmin()`

```python
np.nanmin(arr)
```

Minimum ignoring `NaN`.

### `np.nanmax()`

```python
np.nanmax(arr)
```

Maximum ignoring `NaN`.

### `np.nanmedian()`

```python
np.nanmedian(arr)
```

Median ignoring `NaN`.

---

# 📊 Normal vs NaN-Aware Functions

| Normal        | Ignores NaN      |
| ------------- | ---------------- |
| `np.sum()`    | `np.nansum()`    |
| `np.mean()`   | `np.nanmean()`   |
| `np.min()`    | `np.nanmin()`    |
| `np.max()`    | `np.nanmax()`    |
| `np.median()` | `np.nanmedian()` |

### 🧠 Memory Trick

> Add **`nan`** after `np.` to remember that the function handles `NaN`.

```text
mean     → nanmean
sum      → nansum
min      → nanmin
max      → nanmax
median   → nanmedian
```

---

# 1️⃣7️⃣ Important Example

```python
import numpy as np

arr = np.array([
    10,
    20,
    np.nan,
    40,
    50
])

print("Normal mean:")
print(np.mean(arr))

print("\nNaN-aware mean:")
print(np.nanmean(arr))

print("\nNormal sum:")
print(np.sum(arr))

print("\nNaN-aware sum:")
print(np.nansum(arr))
```

Output:

```text
Normal mean:
nan

NaN-aware mean:
30.0

Normal sum:
nan

NaN-aware sum:
120.0
```

---

# 1️⃣8️⃣ 2D Arrays With Missing Values

Missing data is also common in 2D arrays.

```python
data = np.array([
    [10, 20, 30],
    [40, np.nan, 60],
    [70, 80, np.nan]
])

print(data)
```

Output:

```text
[[10. 20. 30.]
 [40. nan 60.]
 [70. 80. nan]]
```

---

# 1️⃣9️⃣ Count Missing Values in Entire Array

```python
missing = np.sum(np.isnan(data))

print(missing)
```

Output:

```text
2
```

There are two missing values.

---

# 2️⃣0️⃣ Count Missing Values Per Column

This is very useful in data analysis.

```python
missing_per_column = np.sum(np.isnan(data), axis=0)

print(missing_per_column)
```

Output:

```text
[0 1 1]
```

Visual:

```text
Column 1    Column 2    Column 3
   0           1           1
```

---

# 2️⃣1️⃣ Count Missing Values Per Row

```python
missing_per_row = np.sum(np.isnan(data), axis=1)

print(missing_per_row)
```

Output:

```text
[0 1 1]
```

Meaning:

```text
Row 1 → 0 missing values
Row 2 → 1 missing value
Row 3 → 1 missing value
```

---

# 2️⃣2️⃣ `np.isfinite()` for Data Cleaning ⭐

Suppose:

```python
data = np.array([
    10,
    20,
    np.nan,
    np.inf,
    50,
    -np.inf
])
```

We want only valid finite numbers.

Use:

```python
clean = data[np.isfinite(data)]

print(clean)
```

Output:

```text
[10. 20. 50.]
```

This removes:

```text
NaN
+inf
-inf
```

---

# 2️⃣3️⃣ Real-World Example — Employee Salaries

Imagine:

```python
import numpy as np

salary = np.array([
    45000,
    52000,
    np.nan,
    60000,
    58000,
    np.nan,
    70000
])

print("Salary:")
print(salary)

print("\nMissing values:")
print(np.isnan(salary))

print("\nNumber of missing salaries:")
print(np.sum(np.isnan(salary)))

print("\nAverage salary ignoring missing values:")
print(np.nanmean(salary))
```

Output:

```text
Salary:
[45000. 52000.    nan 60000. 58000.    nan 70000.]

Missing values:
[False False  True False False  True False]

Number of missing salaries:
2

Average salary ignoring missing values:
57000.0
```

---

# 2️⃣4️⃣ Complete VS Code Practice Program

```python
# ============================================================
# NUMPY - HANDLING MISSING VALUES
# ============================================================

import numpy as np


# ============================================================
# 1. CREATE ARRAY WITH MISSING VALUES
# ============================================================

data = np.array([
    10,
    20,
    np.nan,
    40,
    np.nan,
    60
])

print("Original Data:")
print(data)


# ============================================================
# 2. CHECK FOR NaN
# ============================================================

nan_mask = np.isnan(data)

print("\nNaN Mask:")
print(nan_mask)


# ============================================================
# 3. COUNT NaN VALUES
# ============================================================

missing_count = np.sum(np.isnan(data))

print("\nNumber of Missing Values:")
print(missing_count)


# ============================================================
# 4. GET ONLY NaN VALUES
# ============================================================

missing_values = data[np.isnan(data)]

print("\nMissing Values:")
print(missing_values)


# ============================================================
# 5. GET ONLY NON-NaN VALUES
# ============================================================

valid_values = data[~np.isnan(data)]

print("\nValid Values:")
print(valid_values)


# ============================================================
# 6. CALCULATE MEAN IGNORING NaN
# ============================================================

mean_value = np.nanmean(data)

print("\nMean Ignoring NaN:")
print(mean_value)


# ============================================================
# 7. REPLACE NaN WITH MEAN
# ============================================================

clean_data = data.copy()

clean_data[np.isnan(clean_data)] = mean_value

print("\nData After Replacing NaN:")
print(clean_data)


# ============================================================
# 8. CHECK INFINITY
# ============================================================

data_with_inf = np.array([
    10,
    np.inf,
    20,
    -np.inf,
    30
])

print("\nData With Infinity:")
print(data_with_inf)

print("\nInfinity Mask:")
print(np.isinf(data_with_inf))


# ============================================================
# 9. CHECK FINITE VALUES
# ============================================================

print("\nFinite Mask:")
print(np.isfinite(data_with_inf))


# ============================================================
# 10. GET ONLY FINITE VALUES
# ============================================================

finite_values = data_with_inf[np.isfinite(data_with_inf)]

print("\nFinite Values:")
print(finite_values)
```

---

# ⚠️ Common Mistakes

### ❌ Mistake 1 — Using `== np.nan`

Don't do:

```python
arr == np.nan
```

to detect missing values.

Use:

```python
np.isnan(arr)
```

---

### ❌ Mistake 2 — Expecting `np.mean()` to ignore NaN

```python
np.mean(arr)
```

may return:

```text
nan
```

Use:

```python
np.nanmean(arr)
```

when you want the mean while ignoring `NaN`.

---

### ❌ Mistake 3 — Confusing `NaN` and `None`

These are not the same concept.

```text
NaN  → numerical floating-point special value
None → Python's absence-of-value object
```

For NumPy numerical arrays, `np.nan` is commonly used for missing numerical data.

---

### ❌ Mistake 4 — Removing every invalid value without thinking

Before cleaning data, understand what the value means.

For example:

```text
Salary = NaN
```

doesn't automatically mean:

```text
Salary = 0
```

The correct treatment depends on the dataset and analysis.

---

# 🎯 Interview Questions

### Q1. What is `np.nan`?

**Answer:**
`np.nan` represents a `NaN` floating-point value and is commonly used to represent missing numerical data.

---

### Q2. How do you detect NaN values?

```python
np.isnan(arr)
```

---

### Q3. How do you count missing values?

```python
np.sum(np.isnan(arr))
```

---

### Q4. What does `np.isinf()` do?

It detects positive and negative infinity.

---

### Q5. What does `np.isfinite()` do?

It returns `True` for finite numerical values and `False` for `NaN` and infinite values.

---

### Q6. What is the difference between `np.mean()` and `np.nanmean()`?

```text
np.mean()
    ↓
normal mean calculation

np.nanmean()
    ↓
mean while ignoring NaN
```

---

### Q7. How can you remove NaN values?

```python
arr[~np.isnan(arr)]
```

---

### Q8. How can you replace NaN values with zero?

```python
arr[np.isnan(arr)] = 0
```

---

### Q9. How can you replace NaN with the mean?

```python
mean_value = np.nanmean(arr)

arr[np.isnan(arr)] = mean_value
```

---

### Q10. What are `np.inf` and `-np.inf`?

They represent positive and negative infinity.

---

# 💻 Practice

Try this yourself:

```python
import numpy as np

salary = np.array([
    45000,
    np.nan,
    55000,
    60000,
    np.nan,
    75000
])
```

Find:

### 1️⃣ Number of missing values

```python
# Write your code
```

### 2️⃣ Average salary ignoring missing values

```python
# Write your code
```

### 3️⃣ Get only valid salaries

```python
# Write your code
```

### 4️⃣ Replace missing salaries with average salary

```python
# Write your code
```

---

# 🧩 Mini Exercise

Create this array:

```python
data = np.array([
    10,
    np.nan,
    30,
    np.inf,
    50,
    -np.inf,
    70
])
```

Your program should print:

```text
Original data
Number of NaN values
Number of infinite values
Number of finite values
Only finite values
Mean ignoring NaN
```

---

# ⭐ Chapter 18 Summary

| Concept         | Syntax           | Purpose                   |
| --------------- | ---------------- | ------------------------- |
| NaN             | `np.nan`         | Missing numerical value   |
| Detect NaN      | `np.isnan()`     | Find missing values       |
| Infinity        | `np.inf`         | Positive infinity         |
| Detect infinity | `np.isinf()`     | Find infinite values      |
| Finite check    | `np.isfinite()`  | Find valid finite numbers |
| NaN mean        | `np.nanmean()`   | Mean ignoring NaN         |
| NaN sum         | `np.nansum()`    | Sum ignoring NaN          |
| NaN min         | `np.nanmin()`    | Minimum ignoring NaN      |
| NaN max         | `np.nanmax()`    | Maximum ignoring NaN      |
| NaN median      | `np.nanmedian()` | Median ignoring NaN       |

---

# 🧠 Quick Memory Map

```text
                 MISSING / INVALID DATA
                          │
             ┌────────────┼────────────┐
             ↓            ↓            ↓
            NaN        + / - inf    Normal number
             │            │            │
             ↓            ↓            ↓
       np.isnan()    np.isinf()   np.isfinite()
             │            │            │
             └────────────┴────────────┘
                          ↓
                    DATA CLEANING
```

### 🔥 Remember These 5

```text
np.nan
np.isnan()
np.isinf()
np.isfinite()
np.nanmean()
```

---

# 🧪 Chapter 18 Quiz

**Q1.** What does `np.nan` represent?

A. Zero
B. Missing numerical value
C. Negative number
D. String

**Q2.** Which function detects NaN?

A. `np.isinf()`
B. `np.isnan()`
C. `np.isfinite()`
D. `np.nanmean()`

**Q3.** Which function detects infinity?

A. `np.isinf()`
B. `np.isnan()`
C. `np.mean()`
D. `np.sum()`

**Q4.** Which function returns `True` for finite numbers?

A. `np.isnan()`
B. `np.isinf()`
C. `np.isfinite()`
D. `np.nan()`

**Q5.** Which function calculates mean while ignoring NaN?

A. `np.mean()`
B. `np.nanmean()`
C. `np.isfinite()`
D. `np.nansum()`

**Q6.** How do you remove NaN values?

A.

```python
arr[np.isnan(arr)]
```

B.

```python
arr[~np.isnan(arr)]
```

C.

```python
np.isinf(arr)
```

D.

```python
arr == np.nan
```

**Q7.** What does this return?

```python
np.sum(np.isnan(arr))
```

A. Sum of values
B. Number of NaN values
C. Number of infinite values
D. Mean

---

## 🏁 Chapter 18 — COMPLETE

You now know how NumPy handles:

**`NaN → missing values → infinity → finite values → detection → filtering → replacement → NaN-aware statistics`**

### Next → Chapter 19: NumPy Data Types

We will learn:

`int → float → bool → complex → string → dtype → astype() → type conversion → int32 vs int64 → memory considerations → practical examples → interview questions → quiz`

Type **NEXT** when you're ready.
