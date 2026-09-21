# 🎯 Chapter 15 — NumPy Boolean Masking

Welcome to **Chapter 15** 🚀

Boolean Masking is one of the **most important NumPy techniques** for Data Science.

You already learned conditions such as:

```python
arr > 50
arr == 30
arr < 100
```

Now we will learn how to use those conditions to **filter actual data**.

---

# 📚 Chapter 15 Roadmap

We will learn:

1. 🔘 What is Boolean Masking?
2. Boolean arrays
3. Basic filtering
4. Multiple conditions
5. `&` — AND
6. `|` — OR
7. `~` — NOT
8. Filtering 2D arrays
9. Combining masking with indexing
10. 🌍 Real-world examples
11. ⚠️ Common mistakes
12. 💼 Interview Questions
13. 📝 Practice
14. 🎯 Mini Exercise
15. 📋 Summary
16. 🧪 Quiz

---

# 1️⃣ What is Boolean Masking?

### 📖 Definition

**Boolean masking** means using an array of `True` and `False` values to **select/filter elements** from a NumPy array.

Think of it like a filter:

```text
Original Data
     ↓
Condition
     ↓
True / False
     ↓
Keep True values
     ↓
Filtered Data
```

---

# 2️⃣ First Understand Boolean Arrays

Consider:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
```

Now:

```python
print(arr > 30)
```

Output:

```text
[False False False  True  True]
```

Why?

```text
10 > 30 → False
20 > 30 → False
30 > 30 → False
40 > 30 → True
50 > 30 → True
```

Visual:

```text
Value:    10     20     30     40     50
           ↓      ↓      ↓      ↓      ↓
> 30:    False  False  False  True   True
```

This is called a **Boolean array**.

---

# 3️⃣ Boolean Masking

Now use that Boolean array to filter:

```python
result = arr[arr > 30]

print(result)
```

Output:

```text
[40 50]
```

### 🧠 What happened?

First:

```python
arr > 30
```

produced:

```text
[False False False True True]
```

Then:

```python
arr[condition]
```

kept only the `True` positions.

```text
10 → False → ❌
20 → False → ❌
30 → False → ❌
40 → True  → ✅
50 → True  → ✅
```

Result:

```text
[40 50]
```

---

# ⭐ Golden Pattern

Remember this syntax:

```python
array[condition]
```

Examples:

```python
arr[arr > 50]
```

```python
arr[arr < 50]
```

```python
arr[arr == 50]
```

```python
arr[arr != 50]
```

---

# 4️⃣ Filtering with `>`

```python
marks = np.array([45, 78, 92, 33, 85])

result = marks[marks > 70]

print(result)
```

Output:

```text
[78 92 85]
```

Dry run:

```text
45 > 70 → ❌
78 > 70 → ✅
92 > 70 → ✅
33 > 70 → ❌
85 > 70 → ✅
```

---

# 5️⃣ Filtering with `<`

```python
marks = np.array([45, 78, 92, 33, 85])

result = marks[marks < 50]

print(result)
```

Output:

```text
[45 33]
```

---

# 6️⃣ Filtering with `>=`

Suppose we want students who scored **at least 80**.

```python
marks = np.array([45, 78, 92, 33, 85])

result = marks[marks >= 80]

print(result)
```

Output:

```text
[92 85]
```

---

# 7️⃣ Filtering with `==`

Find values equal to `50`:

```python
arr = np.array([20, 50, 30, 50, 70])

result = arr[arr == 50]

print(result)
```

Output:

```text
[50 50]
```

---

# 8️⃣ Filtering with `!=`

Find values that are **not equal to 50**:

```python
arr = np.array([20, 50, 30, 50, 70])

result = arr[arr != 50]

print(result)
```

Output:

```text
[20 30 70]
```

---

# 🔥 9️⃣ Multiple Conditions

This is where Boolean Masking becomes extremely powerful.

Suppose:

```python
marks = np.array([45, 55, 65, 75, 85, 95])
```

We want:

```text
marks > 50
AND
marks < 90
```

Use:

```python
result = marks[(marks > 50) & (marks < 90)]

print(result)
```

Output:

```text
[55 65 75 85]
```

---

# ⭐ `&` Means AND

The condition:

```python
(marks > 50) & (marks < 90)
```

means:

> Keep values satisfying **both conditions**.

Visual:

```text
55 → >50 ✅ → <90 ✅ → KEEP
65 → >50 ✅ → <90 ✅ → KEEP
75 → >50 ✅ → <90 ✅ → KEEP
85 → >50 ✅ → <90 ✅ → KEEP
95 → >50 ✅ → <90 ❌ → REMOVE
45 → >50 ❌ → REMOVE
```

---

# ⚠️ Important: Use Parentheses

Correct:

```python
marks[(marks > 50) & (marks < 90)]
```

❌ Avoid:

```python
marks[marks > 50 & marks < 90]
```

For NumPy conditions, put **each condition inside parentheses**.

---

# 🔟 `|` Means OR

Suppose we want:

```text
marks < 50
OR
marks > 90
```

Use:

```python
marks = np.array([30, 45, 60, 75, 92, 98])

result = marks[(marks < 50) | (marks > 90)]

print(result)
```

Output:

```text
[30 45 92 98]
```

### 🧠 Meaning

```text
< 50 OR > 90
```

If **either condition** is True → keep the value.

---

# 1️⃣1️⃣ `~` Means NOT

The `~` operator reverses a Boolean condition.

Suppose:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Condition:

```python
arr > 30
```

gives:

```text
[False False False True True]
```

Now:

```python
~(arr > 30)
```

gives:

```text
[True True True False False]
```

Therefore:

```python
result = arr[~(arr > 30)]

print(result)
```

Output:

```text
[10 20 30]
```

### 🧠 Remember

```text
& → AND
| → OR
~ → NOT
```

---

# 📊 Boolean Operators

| Operator | Meaning |
|---|---|
| `&` | AND |
| `|` | OR |
| `~` | NOT |

Memory trick:

```text
& → Both ✅
| → Either ✅
~ → Reverse 🔄
```

---

# 1️⃣2️⃣ Multiple Conditions Example

Suppose:

```python
marks = np.array([35, 45, 55, 65, 75, 85, 95])
```

### Condition 1

```python
marks > 50
```

### Condition 2

```python
marks < 90
```

Together:

```python
result = marks[(marks > 50) & (marks < 90)]

print(result)
```

Output:

```text
[55 65 75 85]
```

---

# 1️⃣3️⃣ Three Conditions

You can use more than two conditions.

Example:

```python
marks = np.array([40, 55, 65, 75, 85, 95])

result = marks[
    (marks >= 50) &
    (marks <= 90) &
    (marks != 75)
]

print(result)
```

Output:

```text
[55 65 85]
```

Let's check:

```text
40 → <50 → ❌
55 → ✅
65 → ✅
75 → excluded because !=75 is False
85 → ✅
95 → >90 → ❌
```

---

# 1️⃣4️⃣ Boolean Masking with 2D Arrays

Now let's work with a matrix.

```python
marks = np.array([
    [80, 45, 90],
    [65, 75, 55],
    [95, 35, 85]
])
```

We want all marks greater than `80`.

```python
result = marks[marks > 80]

print(result)
```

Output:

```text
[90 95 85]
```

Notice that the result is **1D**.

It extracts all elements satisfying the condition.

---

# 🧠 Visual

Original:

```text
80   45   90
65   75   55
95   35   85
```

Condition `> 80`:

```text
❌   ❌   ✅
❌   ❌   ❌
✅   ❌   ✅
```

Result:

```text
[90 95 85]
```

---

# 1️⃣5️⃣ Filtering Rows in a 2D Array

Sometimes we don't want individual values.

We want **complete rows**.

Suppose:

```python
students = np.array([
    [101, 80],
    [102, 65],
    [103, 90],
    [104, 45]
])
```

Columns:

```text
Student_ID   Marks
```

We want students whose marks are greater than `70`.

Marks are column `1`.

```python
result = students[students[:, 1] > 70]

print(result)
```

Output:

```text
[[101  80]
 [103  90]]
```

### 🧠 Understand Carefully

First:

```python
students[:, 1]
```

gets the marks column:

```text
[80 65 90 45]
```

Then:

```python
students[:, 1] > 70
```

gives:

```text
[True False True False]
```

Then:

```python
students[condition]
```

selects complete rows:

```text
[101 80]
[103 90]
```

---

# ⭐ This Pattern Is Very Important

For a 2D dataset:

```python
data[data[:, column_index] > value]
```

Example:

```python
students[students[:, 1] > 70]
```

This pattern is extremely useful in Data Science.

---

# 1️⃣6️⃣ Filtering Rows with Multiple Conditions

Suppose:

```python
students = np.array([
    [101, 80],
    [102, 65],
    [103, 90],
    [104, 45],
    [105, 75]
])
```

We want marks between `70` and `90`.

```python
result = students[
    (students[:, 1] >= 70) &
    (students[:, 1] <= 90)
]

print(result)
```

Output:

```text
[[101  80]
 [103  90]
 [105  75]]
```

---

# 1️⃣7️⃣ Boolean Mask + Assignment

Boolean masking isn't only for reading data.

We can also **modify values**.

Suppose:

```python
marks = np.array([35, 45, 55, 65, 75])
```

We want to replace all marks below `50` with `0`.

```python
marks[marks < 50] = 0

print(marks)
```

Output:

```text
[ 0  0 55 65 75]
```

🔥 This is very useful.

---

# 1️⃣8️⃣ Replace Values Using Boolean Masking

Suppose we want to cap marks at `90`.

```python
marks = np.array([75, 95, 85, 100, 65])

marks[marks > 90] = 90

print(marks)
```

Output:

```text
[75 90 85 90 65]
```

This is a simple example of **data cleaning**.

---

# 🌍 1️⃣9️⃣ Real-World Example — Employee Salary

```python
salary = np.array([
    25000,
    45000,
    60000,
    35000,
    80000
])
```

Find salaries greater than `50000`:

```python
high_salary = salary[salary > 50000]

print(high_salary)
```

Output:

```text
[60000 80000]
```

---

# 🌍 2️⃣0️⃣ Real-World Example — Product Prices

```python
prices = np.array([
    500,
    1200,
    750,
    2000,
    900
])
```

Find products between ₹700 and ₹1500:

```python
result = prices[
    (prices >= 700) &
    (prices <= 1500)
]

print(result)
```

Output:

```text
[1200 750 900]
```

---

# 🌍 2️⃣1️⃣ Real-World Example — Temperature

```python
temperature = np.array([
    18,
    25,
    32,
    40,
    22,
    35
])
```

Find temperatures above `30`:

```python
hot = temperature[temperature > 30]

print(hot)
```

Output:

```text
[32 40 35]
```

---

# 🌍 2️⃣2️⃣ Real-World Example — Data Cleaning

Suppose:

```python
ages = np.array([
    20,
    25,
    -5,
    30,
    200,
    35
])
```

Clearly:

```text
-5  → invalid
200 → invalid
```

We can find valid ages:

```python
valid_ages = ages[
    (ages >= 0) &
    (ages <= 120)
]

print(valid_ages)
```

Output:

```text
[20 25 30 35]
```

This is a simple example of **data preprocessing**.

---

# 🔥 2️⃣3️⃣ Boolean Masking vs `np.where()`

You learned both.

### Boolean Masking

```python
arr[arr > 50]
```

Returns:

```text
actual values
```

Example:

```text
[60 70 80]
```

---

### `np.where()`

```python
np.where(arr > 50)
```

Returns:

```text
indexes
```

Example:

```text
[2 3 4]
```

### Comparison

| Operation | Result |
|---|---|
| `arr[arr > 50]` | Matching values |
| `np.where(arr > 50)` | Matching indexes |

---

# 🧠 2️⃣4️⃣ Boolean Masking Mental Model

Remember this flow:

```text
             ARRAY
               │
               ↓
           CONDITION
               │
               ↓
        TRUE / FALSE MASK
               │
               ↓
       Keep TRUE elements
               │
               ↓
          FILTERED DATA
```

Example:

```text
[10 20 30 40 50]
       │
       ↓
     > 30
       │
       ↓
[ F  F  F  T  T ]
       │
       ↓
[40 50]
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Using `and`

Wrong:

```python
arr[(arr > 20) and (arr < 50)]
```

Correct:

```python
arr[(arr > 20) & (arr < 50)]
```

---

## ❌ Mistake 2 — Using `or`

Wrong:

```python
arr[(arr < 20) or (arr > 50)]
```

Correct:

```python
arr[(arr < 20) | (arr > 50)]
```

---

## ❌ Mistake 3 — Missing parentheses

Wrong:

```python
arr[arr > 20 & arr < 50]
```

Correct:

```python
arr[(arr > 20) & (arr < 50)]
```

---

## ❌ Mistake 4 — Using `&&`

Python/NumPy does not use:

```python
&&
```

Use:

```python
&
```

---

## ❌ Mistake 5 — Confusing `~`

`~` means **NOT**, not approximately.

```python
~(arr > 50)
```

means:

> Keep values that are **not greater than 50**.

---

# 💼 Interview Questions

### Q1. What is Boolean masking?

**Answer:**

Boolean masking is a technique for filtering NumPy arrays using a Boolean condition.

---

### Q2. What does this return?

```python
arr[arr > 50]
```

**Answer:**

It returns the elements of `arr` that are greater than 50.

---

### Q3. What does `&` mean?

**Answer:**

`&` performs element-wise logical AND between Boolean arrays.

---

### Q4. What does `|` mean?

**Answer:**

`|` performs element-wise logical OR.

---

### Q5. What does `~` mean?

**Answer:**

`~` reverses a Boolean mask.

---

### Q6. Why do we use parentheses?

Example:

```python
arr[(arr > 20) & (arr < 50)]
```

**Answer:**

Parentheses make each Boolean condition explicit and ensure the conditions are combined correctly with NumPy's element-wise operators.

---

### Q7. Difference between Boolean masking and `np.where()`?

**Answer:**

```text
Boolean masking
→ returns matching values

np.where()
→ returns matching indexes
```

---

### Q8. Can Boolean masking modify an array?

**Answer:**

Yes.

Example:

```python
arr[arr < 0] = 0
```

This replaces negative values with zero.

---

# 📝 Practice Questions

## Practice 1

Given:

```python
arr = np.array([10, 25, 30, 45, 50, 65])
```

Find values greater than `40`.

Expected:

```text
[45 50 65]
```

---

## Practice 2

Find values between `20` and `50`.

Expected:

```text
[25 30 45 50]
```

---

## Practice 3

Find values below `20` **OR** above `50`.

Expected:

```text
[10 65]
```

---

## Practice 4

Find values that are **NOT greater than 40**.

Expected:

```text
[10 25 30]
```

---

## Practice 5

Replace all values below `30` with `0`.

Input:

```python
arr = np.array([10, 25, 30, 45, 50])
```

Expected:

```text
[ 0  0 30 45 50]
```

---

# 🎯 Mini Coding Exercise

Create this student dataset:

```python
import numpy as np

students = np.array([
    [101, 85],
    [102, 45],
    [103, 92],
    [104, 68],
    [105, 76],
    [106, 35]
])
```

Columns:

```text
Student ID | Marks
```

### Your Tasks

### 1️⃣ Find students who scored above 70.

```python
?
```

Expected:

```text
[[101  85]
 [103  92]
 [105  76]]
```

### 2️⃣ Find students who scored between 50 and 80.

Expected:

```text
[[104  68]
 [105  76]]
```

### 3️⃣ Find students who scored below 50.

Expected:

```text
[[102  45]
 [106  35]]
```

### 4️⃣ Replace marks below 50 with `0`.

Expected dataset:

```text
[[101  85]
 [102   0]
 [103  92]
 [104  68]
 [105  76]
 [106   0]]
```

💡 Hint:

```python
students[students[:, 1] < 50, 1] = 0
```

---

# 📋 Chapter 15 Summary

| Concept | Meaning |
|---|---|
| Boolean array | Array containing `True` / `False` |
| Boolean masking | Filtering using conditions |
| `arr[condition]` | Select matching values |
| `&` | AND |
| `|` | OR |
| `~` | NOT |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater/equal |
| `<=` | Less/equal |
| `==` | Equal |
| `!=` | Not equal |

---

# 🧠 One-Minute Revision

```text
              BOOLEAN MASKING
                    │
                    ↓
                CONDITION
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
        True                False
          ↓                   ↓
        KEEP                REMOVE
          │
          ↓
     FILTERED DATA
```

### ⭐ Golden Pattern

```python
array[condition]
```

Examples:

```python
arr[arr > 50]
```

```python
arr[(arr > 20) & (arr < 80)]
```

```python
arr[(arr < 20) | (arr > 80)]
```

```python
arr[~(arr > 50)]
```

### 🔥 Remember

```text
& → AND
| → OR
~ → NOT
```

---

# 🧪 Chapter 15 Quiz

### 1. What does Boolean masking do?

A. Sorts an array  
B. Filters an array using conditions  
C. Reshapes an array  
D. Joins arrays

### 2. What does this return?

```python
arr[arr > 50]
```

A. Indexes  
B. Matching values  
C. Shape  
D. Data type

### 3. Which operator means AND?

A. `and`  
B. `&`  
C. `&&`  
D. `+`

### 4. Which operator means OR?

A. `or`  
B. `||`  
C. `|`  
D. `+`

### 5. Which operator means NOT?

A. `!`  
B. `not`  
C. `~`  
D. `!=`

### 6. Which is correct?

A.
```python
arr[arr > 20 and arr < 50]
```

B.
```python
arr[(arr > 20) & (arr < 50)]
```

### 7. What does this do?

```python
arr[arr < 0] = 0
```

A. Removes negative values  
B. Replaces negative values with 0  
C. Finds negative indexes  
D. Sorts the array

### 8. Complete:

```text
Boolean Masking → ______ data using conditions.
```

---

# ✅ Chapter 15 COMPLETE

You now know:

**Boolean arrays → Boolean masking → filtering → multiple conditions → AND → OR → NOT → 2D filtering → modifying data → real-world data cleaning.**

👉 Type **`NEXT`** when you're ready for:

# 🎲 Chapter 16 — NumPy Random Module

We will learn:

```text
np.random.rand()
np.random.randn()
np.random.randint()
np.random.random()
np.random.choice()
np.random.seed()
Random distributions
```

with **real-world examples, dry runs, and Data Science use cases**.