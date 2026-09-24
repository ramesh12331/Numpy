# 🚀 Chapter 19 — NumPy Data Types (`dtype`)

Welcome to **Chapter 19**! 🎯

In this chapter we will understand an important NumPy concept:

> ⭐ **`dtype` tells us what type of data an array stores.**

This is especially important in **Data Science, Machine Learning, memory optimization, and performance**.

---

# 📚 What We Will Learn

1. 🔹 What is a data type?
2. 🔹 `dtype`
3. 🔹 Integer types
4. 🔹 `int32` vs `int64`
5. 🔹 Float types
6. 🔹 Boolean type
7. 🔹 Complex numbers
8. 🔹 String data
9. 🔹 `astype()`
10. 🔹 Type conversion
11. 🔹 Memory usage
12. 🔹 Common mistakes
13. 🔹 Real-world examples
14. 🔹 Interview questions
15. 🔹 Practice
16. 🔹 Quiz

---

# 1️⃣ What is a Data Type?

A **data type** tells Python/NumPy what kind of value we are storing.

Examples:

```text
10       → integer
10.5     → float
True     → boolean
"Hello"  → string
2 + 3j   → complex
```

Think of it like different containers:

```text
📦 Integer Box   → 10
📦 Float Box     → 10.5
📦 Boolean Box   → True
📦 String Box    → "Hello"
```

---

# 2️⃣ What is `dtype`?

In NumPy:

```python
arr.dtype
```

tells us the **data type of the elements inside the array**.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.dtype)
```

Typical output:

```text
[10 20 30 40]
int64
```

Depending on your platform and NumPy configuration, the default integer dtype may differ.

---

# 3️⃣ Integer Data Type

Integers are whole numbers:

```text
10
20
-5
100
```

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.dtype)
```

Typical output:

```text
[10 20 30 40]
int64
```

---

# 4️⃣ Explicitly Specify `dtype`

We can tell NumPy which data type to use.

```python
arr = np.array(
    [10, 20, 30, 40],
    dtype="int32"
)

print(arr)
print(arr.dtype)
```

Output:

```text
[10 20 30 40]
int32
```

### 🧠 Important

```python
dtype="int32"
```

means:

> Store the integers using a 32-bit integer data type.

---

# 5️⃣ `int32` vs `int64` ⭐⭐⭐

This is very important.

| Type    |    Size | Signed integer range                                    |
| ------- | ------: | ------------------------------------------------------- |
| `int32` | 4 bytes | -2,147,483,648 to 2,147,483,647                         |
| `int64` | 8 bytes | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |

### 🧠 Memory

```text
int32 → 32 bits → 4 bytes
int64 → 64 bits → 8 bytes
```

So `int64` can store a much larger range of integer values, while `int32` uses less memory.

---

# 6️⃣ Important Example — `int32`

```python
import numpy as np

arr = np.array(
    [45, 67, 899874564675, 23],
    dtype="int32"
)

print(arr)
```

Here:

```text
899874564675
```

is much larger than the maximum signed `int32` value:

```text
2,147,483,647
```

Therefore, depending on the NumPy/Python version and conversion path, this can result in an **integer overflow/error** rather than successfully storing the value.

### ❌ Don't do this

```python
dtype="int32"
```

when your data contains integers outside the supported range.

---

# 7️⃣ Use `int64`

For the same large value:

```python
import numpy as np

arr = np.array(
    [45, 67, 899874564675, 23],
    dtype="int64"
)

print(arr)
print(arr.dtype)
```

Output:

```text
[           45            67 899874564675            23]
int64
```

### 🧠 Remember

```text
int32
   ↓
smaller range
smaller memory

int64
   ↓
larger range
larger memory
```

---

# 8️⃣ Float Data Type

A float contains decimal values.

Examples:

```text
10.5
20.75
3.14
-5.6
```

Example:

```python
arr = np.array([10.5, 20.5, 30.5])

print(arr)
print(arr.dtype)
```

Typical output:

```text
[10.5 20.5 30.5]
float64
```

---

# 9️⃣ Explicit Float Type

```python
arr = np.array(
    [10, 20, 30],
    dtype="float32"
)

print(arr)
print(arr.dtype)
```

Output:

```text
[10. 20. 30.]
float32
```

Notice:

```text
10
```

became:

```text
10.
```

because the array is now storing floating-point values.

---

# 🔟 `float32` vs `float64`

| Type      |    Size | Precision |
| --------- | ------: | --------- |
| `float32` | 4 bytes | Lower     |
| `float64` | 8 bytes | Higher    |

Example:

```python
arr1 = np.array([10.5, 20.5], dtype="float32")
arr2 = np.array([10.5, 20.5], dtype="float64")

print(arr1.dtype)
print(arr2.dtype)
```

Output:

```text
float32
float64
```

### 🧠 Practical idea

For very large numerical datasets, choosing an appropriate dtype can reduce memory usage.

But don't choose a smaller dtype blindly—make sure its range and precision are sufficient for your calculations.

---

# 1️⃣1️⃣ Boolean Data Type

Boolean values have only two possibilities:

```text
True
False
```

NumPy uses:

```text
bool
```

Example:

```python
arr = np.array([
    True,
    False,
    True
])

print(arr)
print(arr.dtype)
```

Output:

```text
[ True False  True]
bool
```

---

# 1️⃣2️⃣ Boolean Example

Boolean arrays are very useful for filtering.

```python
marks = np.array([
    80,
    45,
    90,
    35
])

result = marks >= 50

print(result)
```

Output:

```text
[ True False  True False]
```

This is a Boolean array.

Remember Chapter 15:

```text
Boolean Masking
       ↓
True / False
       ↓
Filter data
```

---

# 1️⃣3️⃣ Complex Data Type

A complex number contains:

```text
real part + imaginary part
```

Example:

```text
2 + 3j
```

Python uses:

```text
j
```

for the imaginary component.

Example:

```python
arr = np.array([
    2 + 3j,
    4 + 5j
])

print(arr)
print(arr.dtype)
```

Output will typically look like:

```text
[2.+3.j 4.+5.j]
complex128
```

---

# 1️⃣4️⃣ Access Real and Imaginary Parts

```python
arr = np.array([
    2 + 3j,
    4 + 5j
])

print(arr.real)
print(arr.imag)
```

Output:

```text
[2. 4.]
[3. 5.]
```

So:

```text
2 + 3j
↑   ↑
real imaginary
```

---

# 1️⃣5️⃣ String Data

NumPy can also store strings.

Example:

```python
arr = np.array([
    "Ramesh",
    "Suresh",
    "Kiran"
])

print(arr)
print(arr.dtype)
```

The dtype will typically be a Unicode string dtype such as:

```text
<U6
```

The exact string dtype depends on the strings stored.

---

# 🧠 What Does `<U6` Mean?

A dtype such as:

```text
<U6
```

can be understood as:

```text
< → byte order/type metadata
U → Unicode string
6 → maximum character length represented by that dtype
```

For example:

```text
"Ramesh"
```

has 6 characters.

---

# 1️⃣6️⃣ `dtype` with `np.array()`

General syntax:

```python
np.array(data, dtype=data_type)
```

Examples:

```python
np.array([1, 2, 3], dtype="int32")
```

```python
np.array([1.5, 2.5, 3.5], dtype="float32")
```

```python
np.array([True, False], dtype="bool")
```

---

# 1️⃣7️⃣ Type Conversion with `astype()` ⭐⭐⭐

Sometimes we already have an array and want to convert it to another dtype.

Use:

```python
astype()
```

### Syntax

```python
new_array = old_array.astype(new_dtype)
```

---

# 1️⃣8️⃣ Integer → Float

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr.dtype)

new_arr = arr.astype(float)

print(new_arr)
print(new_arr.dtype)
```

Output:

```text
int64
[10. 20. 30.]
float64
```

---

# 1️⃣9️⃣ Float → Integer

```python
arr = np.array([10.5, 20.8, 30.9])

new_arr = arr.astype(int)

print(new_arr)
```

Output:

```text
[10 20 30]
```

### ⚠️ Important

Converting floating-point values to integer removes the fractional part:

```text
10.5 → 10
20.8 → 20
30.9 → 30
```

This is **truncation**, not normal rounding.

---

# 2️⃣0️⃣ Float → Integer Dry Run

```text
10.9
 ↓
remove decimal part
 ↓
10
```

Not:

```text
11
```

If you specifically want rounding, use a rounding function before conversion.

Example:

```python
arr = np.array([10.9, 20.2, 30.7])

rounded = np.round(arr)

print(rounded)
```

Typical output:

```text
[11. 20. 31.]
```

Then you could convert:

```python
result = np.round(arr).astype(int)

print(result)
```

Output:

```text
[11 20 31]
```

---

# 2️⃣1️⃣ Integer → Boolean

```python
arr = np.array([0, 1, 2, 0, 5])

result = arr.astype(bool)

print(result)
```

Output:

```text
[False  True  True False  True]
```

### 🧠 Rule

For numeric values:

```text
0     → False
non-0 → True
```

---

# 2️⃣2️⃣ Boolean → Integer

```python
arr = np.array([
    True,
    False,
    True
])

result = arr.astype(int)

print(result)
```

Output:

```text
[1 0 1]
```

So:

```text
True  → 1
False → 0
```

---

# 2️⃣3️⃣ String → Integer

If the strings contain valid integers:

```python
arr = np.array([
    "10",
    "20",
    "30"
])

result = arr.astype(int)

print(result)
print(result.dtype)
```

Output:

```text
[10 20 30]
int64
```

---

# 2️⃣4️⃣ String → Float

```python
arr = np.array([
    "10.5",
    "20.5",
    "30.5"
])

result = arr.astype(float)

print(result)
```

Output:

```text
[10.5 20.5 30.5]
```

---

# ⚠️ Invalid Conversion

This will fail:

```python
arr = np.array([
    "10",
    "hello",
    "30"
])

result = arr.astype(int)
```

Why?

Because:

```text
"hello"
```

cannot be converted into an integer.

---

# 2️⃣5️⃣ `itemsize` and Data Types ⭐

Remember Chapter 3?

We learned:

```python
arr.itemsize
```

It tells us how many bytes each element uses.

Example:

```python
arr32 = np.array([10, 20, 30], dtype="int32")
arr64 = np.array([10, 20, 30], dtype="int64")

print(arr32.itemsize)
print(arr64.itemsize)
```

Output:

```text
4
8
```

Therefore:

```text
int32 → 4 bytes per element
int64 → 8 bytes per element
```

---

# 2️⃣6️⃣ Memory Calculation

Suppose:

```python
arr = np.array(
    [10, 20, 30, 40, 50],
    dtype="int32"
)
```

There are:

```text
5 elements
```

Each element:

```text
4 bytes
```

Therefore:

```text
5 × 4 = 20 bytes
```

Check:

```python
print(arr.nbytes)
```

Output:

```text
20
```

---

# 2️⃣7️⃣ `int32` vs `int64` Memory Example

```python
arr32 = np.zeros(1_000_000, dtype="int32")
arr64 = np.zeros(1_000_000, dtype="int64")

print(arr32.nbytes)
print(arr64.nbytes)
```

Output:

```text
4000000
8000000
```

Approximately:

```text
int32 → 4 MB
int64 → 8 MB
```

So choosing the dtype can matter when working with **millions of values**.

---

# 2️⃣8️⃣ Data Type Summary

NumPy commonly works with types such as:

```text
Integer
Float
Boolean
Complex
String
```

Visual:

```text
                 NumPy dtype
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      Numeric       Boolean       String
        │             │             │
   ┌────┼────┐        │             │
   ↓    ↓    ↓        ↓             ↓
 int  float complex   bool        Unicode
```

---

# 2️⃣9️⃣ Complete VS Code Practice Program

```python
# ============================================================
# NUMPY - DATA TYPES
# ============================================================

import numpy as np


# ============================================================
# 1. INTEGER ARRAY
# ============================================================

arr_int = np.array([10, 20, 30, 40])

print("Integer Array:")
print(arr_int)

print("Data Type:")
print(arr_int.dtype)


# ============================================================
# 2. INT32 ARRAY
# ============================================================

arr_int32 = np.array(
    [10, 20, 30, 40],
    dtype="int32"
)

print("\nINT32 Array:")
print(arr_int32)

print("Data Type:")
print(arr_int32.dtype)

print("Item Size:")
print(arr_int32.itemsize)


# ============================================================
# 3. INT64 ARRAY
# ============================================================

arr_int64 = np.array(
    [10, 20, 30, 40],
    dtype="int64"
)

print("\nINT64 Array:")
print(arr_int64)

print("Data Type:")
print(arr_int64.dtype)

print("Item Size:")
print(arr_int64.itemsize)


# ============================================================
# 4. FLOAT ARRAY
# ============================================================

arr_float = np.array([
    10.5,
    20.5,
    30.5
])

print("\nFloat Array:")
print(arr_float)

print("Data Type:")
print(arr_float.dtype)


# ============================================================
# 5. BOOLEAN ARRAY
# ============================================================

arr_bool = np.array([
    True,
    False,
    True
])

print("\nBoolean Array:")
print(arr_bool)

print("Data Type:")
print(arr_bool.dtype)


# ============================================================
# 6. COMPLEX ARRAY
# ============================================================

arr_complex = np.array([
    2 + 3j,
    4 + 5j
])

print("\nComplex Array:")
print(arr_complex)

print("Data Type:")
print(arr_complex.dtype)


# ============================================================
# 7. STRING ARRAY
# ============================================================

arr_string = np.array([
    "Ramesh",
    "Suresh",
    "Kiran"
])

print("\nString Array:")
print(arr_string)

print("Data Type:")
print(arr_string.dtype)


# ============================================================
# 8. ASTYPE - INTEGER TO FLOAT
# ============================================================

arr = np.array([10, 20, 30])

float_arr = arr.astype(float)

print("\nInteger Array:")
print(arr)

print("Converted Float Array:")
print(float_arr)

print("New Data Type:")
print(float_arr.dtype)


# ============================================================
# 9. ASTYPE - FLOAT TO INTEGER
# ============================================================

arr = np.array([
    10.5,
    20.8,
    30.9
])

int_arr = arr.astype(int)

print("\nOriginal Float Array:")
print(arr)

print("Converted Integer Array:")
print(int_arr)


# ============================================================
# 10. BOOLEAN TO INTEGER
# ============================================================

arr = np.array([
    True,
    False,
    True
])

int_arr = arr.astype(int)

print("\nBoolean Array:")
print(arr)

print("Integer Array:")
print(int_arr)


# ============================================================
# 11. MEMORY USAGE
# ============================================================

arr32 = np.zeros(
    1_000_000,
    dtype="int32"
)

arr64 = np.zeros(
    1_000_000,
    dtype="int64"
)

print("\nINT32 Memory:")
print(arr32.nbytes)

print("\nINT64 Memory:")
print(arr64.nbytes)
```

---

# 🌍 Real-World Example — Employee Data

Suppose we have:

```python
employee_age = np.array([
    25,
    30,
    28,
    35
], dtype="int32")

employee_salary = np.array([
    45000.5,
    52000.75,
    48000.25,
    65000.00
], dtype="float64")
```

We can inspect:

```python
print(employee_age.dtype)
print(employee_salary.dtype)
```

Output:

```text
int32
float64
```

This is useful when building numerical datasets because you can understand:

```text
Age
 ↓
Integer

Salary
 ↓
Float
```

---

# ⭐ Why Does `dtype` Matter?

There are three major reasons.

### 1️⃣ Memory

Smaller suitable dtypes can reduce memory usage.

### 2️⃣ Range

Different integer types can represent different ranges.

```text
int32 → smaller range
int64 → larger range
```

### 3️⃣ Precision

Different floating-point types have different precision characteristics.

---

# ⚠️ Common Mistakes

### ❌ Mistake 1

Thinking:

```python
dtype="int32"
```

and:

```python
dtype="int64"
```

are the same.

They differ in:

* memory
* range

---

### ❌ Mistake 2

Expecting:

```python
np.array([10.5]).astype(int)
```

to round automatically.

It produces:

```text
[10]
```

because the fractional part is discarded.

---

### ❌ Mistake 3

Using an integer dtype for values that need decimals.

For example:

```text
Salary = 45000.75
```

should not be stored as an integer if the decimal portion matters.

---

### ❌ Mistake 4

Using `int32` for extremely large integers.

Always consider the required range.

---

### ❌ Mistake 5

Thinking `dtype` changes the original array when using `astype()`.

Example:

```python
new_arr = arr.astype(float)
```

creates a converted array.

It does not simply change the original array in place.

---

# 🎯 Interview Questions

### Q1. What is `dtype`?

**Answer:**
`dtype` specifies the data type of elements stored in a NumPy array.

---

### Q2. How do you check an array's dtype?

```python
arr.dtype
```

---

### Q3. What is `int32`?

**Answer:**
A signed 32-bit integer data type that normally uses **4 bytes per element**.

---

### Q4. What is `int64`?

**Answer:**
A signed 64-bit integer data type that normally uses **8 bytes per element**.

---

### Q5. What is `astype()`?

**Answer:**
`astype()` creates an array converted to the requested data type.

Example:

```python
arr.astype(float)
```

---

### Q6. What happens when float is converted to int?

The fractional portion is discarded.

```text
10.9 → 10
```

---

### Q7. What is the difference between `int32` and `int64`?

|        | `int32` | `int64` |
| ------ | ------: | ------: |
| Bits   |      32 |      64 |
| Bytes  |       4 |       8 |
| Range  | Smaller |  Larger |
| Memory |   Lower |  Higher |

---

### Q8. What does `itemsize` tell us?

It tells us how many **bytes one element** occupies.

---

### Q9. What does `nbytes` tell us?

It tells us the total number of bytes used by the array's elements.

---

### Q10. Why is dtype important in Data Science?

Because it affects:

* Memory usage
* Numerical range
* Precision
* Computational behavior

---

# 💻 Practice Questions

### Practice 1

Create an `int32` array:

```python
[10, 20, 30, 40]
```

Print:

```text
array
dtype
itemsize
nbytes
```

---

### Practice 2

Create:

```python
[10.5, 20.5, 30.5]
```

using `float32`.

Check:

```python
dtype
itemsize
```

---

### Practice 3

Convert:

```python
[10, 20, 30]
```

from integer to float using:

```python
astype()
```

---

### Practice 4

Convert:

```python
[10.5, 20.8, 30.9]
```

to integer.

Predict the output **before running the code**.

---

# 🧩 Mini Exercise

Create these four arrays:

```text
Integer
Float
Boolean
Complex
```

Then print:

```text
Array
dtype
itemsize
nbytes
```

Use this structure:

```python
import numpy as np

# Integer
integer_array = ...

# Float
float_array = ...

# Boolean
boolean_array = ...

# Complex
complex_array = ...
```

---

# 🧠 Chapter 19 Memory Map

```text
                    NumPy Data Types
                          │
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
     Numeric           Boolean            String
        │                 │                 │
   ┌────┼────┐            ↓                 ↓
   ↓    ↓    ↓           bool            Unicode
  int  float complex
   │
 ┌─┴───────┐
 ↓         ↓
int32     int64
4 bytes   8 bytes
```

---

# ⭐ Final Summary

| Concept    | Meaning                     |
| ---------- | --------------------------- |
| `dtype`    | Data type of array elements |
| `int`      | Whole numbers               |
| `float`    | Decimal numbers             |
| `bool`     | `True` / `False`            |
| `complex`  | Complex numbers             |
| `string`   | Text                        |
| `int32`    | 32-bit integer              |
| `int64`    | 64-bit integer              |
| `float32`  | 32-bit floating point       |
| `float64`  | 64-bit floating point       |
| `astype()` | Convert dtype               |
| `itemsize` | Bytes per element           |
| `nbytes`   | Total bytes                 |

---

# 🔥 Most Important Points

```text
dtype
 ↓
What type of data?

astype()
 ↓
Convert data type

itemsize
 ↓
Bytes per element

nbytes
 ↓
Total memory used
```

And remember:

```text
int32 → 4 bytes
int64 → 8 bytes

float32 → 4 bytes
float64 → 8 bytes
```

**But always choose a dtype based on the required range and precision, not simply because it uses less memory.**

---

# 🧪 Chapter 19 Quiz

**Q1.** Which attribute tells you the array's data type?

A. `shape`
B. `size`
C. `dtype`
D. `ndim`

**Q2.** How many bytes does a typical `int32` element use?

A. 2
B. 4
C. 8
D. 16

**Q3.** How many bytes does a typical `int64` element use?

A. 2
B. 4
C. 8
D. 16

**Q4.** Which method converts an array to another dtype?

A. `convert()`
B. `change()`
C. `astype()`
D. `dtype()`

**Q5.** What happens to `10.8` when converted using `.astype(int)`?

A. `11`
B. `10.8`
C. `10`
D. Error

**Q6.** What does `itemsize` represent?

A. Number of rows
B. Number of elements
C. Bytes per element
D. Total dimensions

**Q7.** What does `nbytes` represent?

A. Bytes per element
B. Total bytes used by array elements
C. Number of elements
D. Data type

**Q8.** Which type stores `True` and `False`?

A. `int`
B. `float`
C. `bool`
D. `complex`

---

## 🏁 Chapter 19 — COMPLETE

You now understand:

**`dtype → int → float → bool → complex → string → int32/int64 → astype() → type conversion → itemsize → nbytes → memory optimization`**

### 🚀 Next → Chapter 20 — Advanced NumPy

We will learn:

**Vectorization → Universal Functions (ufuncs) → Axis in depth → Performance → Memory efficiency → Structured arrays → Advanced indexing**

Type **NEXT** when ready.
