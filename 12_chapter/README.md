# 🔎 Chapter 12 — NumPy Searching and Sorting

Welcome to **Chapter 12** 🎯

In Chapter 11, we learned how to **split arrays**.

Now we will learn how to:

- 🔎 **Search** for values
- 📍 Find positions of values
- 🎯 Filter values using conditions
- 📊 Sort arrays
- 🏆 Find the sorting order using `argsort()`

---

# 📚 Chapter 12 Roadmap

We will learn:

1. 🔎 `np.where()`
2. 🎯 Searching with conditions
3. `np.searchsorted()`
4. 📊 `np.sort()`
5. `np.argsort()`
6. 🔍 Filtering arrays
7. 🎯 Finding specific values
8. 🌍 Real-world examples
9. ⚠️ Common mistakes
10. 💼 Interview Questions
11. 📝 Practice
12. 🎯 Mini Exercise
13. 📋 Summary
14. 🧪 Quiz

---

# 1️⃣ What is Searching?

### 📖 Definition

**Searching** means finding values or their **positions** inside an array.

For example:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Suppose we want to find:

```text
Where is 30?
```

Answer:

```text
index = 2
```

Visual:

```text
Index:   0   1   2   3   4
         ↓   ↓   ↓   ↓   ↓
Array:  10  20  30  40  50
                 ↑
              value=30
```

---

# 2️⃣ `np.where()`

`np.where()` is one of the **most important searching functions** in NumPy.

### 📖 Definition

`np.where()` returns the **indices/positions where a condition is True**.

### Syntax

```python
np.where(condition)
```

---

# 🟢 Example 1 — Find a Specific Value

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 30])

result = np.where(arr == 30)

print(result)
```

### Output

```text
(array([2, 4]),)
```

Why?

```text
Index:   0   1   2   3   4
Array:  10  20  30  40  30
                 ↑       ↑
                30      30
```

So:

```text
30 occurs at indexes → 2, 4
```

---

# ⭐ Important

`np.where()` returns an **array of indices**.

Example:

```python
result = np.where(arr == 30)

print(result[0])
```

Output:

```text
[2 4]
```

---

# 3️⃣ `np.where()` with Greater Than

```python
import numpy as np

marks = np.array([45, 78, 92, 33, 85])

result = np.where(marks > 80)

print(result)
```

Output:

```text
(array([2, 4]),)
```

Because:

```text
45 → ❌
78 → ❌
92 → ✅
33 → ❌
85 → ✅
```

Therefore:

```text
indexes → 2, 4
```

---

# 4️⃣ `np.where()` with Less Than

```python
marks = np.array([45, 78, 92, 33, 85])

result = np.where(marks < 50)

print(result)
```

Output:

```text
(array([0, 3]),)
```

Because:

```text
45 → index 0
33 → index 3
```

---

# 5️⃣ `np.where()` with Multiple Conditions

We can combine conditions.

```python
marks = np.array([45, 78, 92, 33, 85])

result = np.where((marks >= 50) & (marks <= 90))

print(result)
```

Output:

```text
(array([1, 4]),)
```

Values:

```text
78
85
```

### ⚠️ Important

With NumPy arrays, use:

```python
&
|
~
```

instead of:

```python
and
or
not
```

So:

```python
(marks >= 50) & (marks <= 90)
```

✅ Correct.

---

# 6️⃣ `np.where()` Can Replace Values

`np.where()` has another very useful form:

```python
np.where(condition, value_if_true, value_if_false)
```

### Example

Suppose:

```python
marks = np.array([35, 55, 80, 25, 90])
```

We want:

```text
marks >= 40 → "Pass"
marks < 40  → "Fail"
```

We can write:

```python
result = np.where(marks >= 40, "Pass", "Fail")

print(result)
```

Output:

```text
['Fail' 'Pass' 'Pass' 'Fail' 'Pass']
```

### 🧠 Visual

```text
35 → <40 → Fail
55 → >=40 → Pass
80 → >=40 → Pass
25 → <40 → Fail
90 → >=40 → Pass
```

This is extremely useful for **data preprocessing**.

---

# 🌍 Real-World Example — Employee Salary

```python
salary = np.array([
    25000,
    45000,
    60000,
    30000,
    80000
])
```

Suppose:

```text
salary >= 50000 → "High"
salary < 50000  → "Normal"
```

Code:

```python
result = np.where(
    salary >= 50000,
    "High",
    "Normal"
)

print(result)
```

Output:

```text
['Normal' 'Normal' 'High' 'Normal' 'High']
```

---

# 7️⃣ `np.searchsorted()`

Now let's learn another searching function.

### 📖 Definition

`np.searchsorted()` finds the **position where a value should be inserted** in a sorted array while maintaining the sorted order.

### Syntax

```python
np.searchsorted(array, value)
```

---

# 🟢 Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.searchsorted(arr, 35)

print(result)
```

Output:

```text
3
```

Why?

Current array:

```text
[10 20 30 40 50]
```

If we insert `35`:

```text
[10 20 30 35 40 50]
         ↑
       index 3
```

Therefore:

```text
35 should be inserted at index 3.
```

---

# ⭐ Important Rule

`searchsorted()` assumes the input array is **sorted**.

For example:

```python
arr = np.array([10, 20, 30, 40, 50])
```

✅ Sorted.

But:

```python
arr = np.array([30, 10, 50, 20, 40])
```

❌ Not sorted.

---

# 8️⃣ Search Multiple Values

You can search for multiple values.

```python
arr = np.array([10, 20, 30, 40, 50])

result = np.searchsorted(
    arr,
    [15, 25, 45]
)

print(result)
```

Output:

```text
[1 2 4]
```

Explanation:

```text
15 → between 10 and 20 → index 1

25 → between 20 and 30 → index 2

45 → between 40 and 50 → index 4
```

---

# 9️⃣ `side` Parameter

`searchsorted()` also has a `side` parameter.

Syntax:

```python
np.searchsorted(
    array,
    value,
    side="left"
)
```

or:

```python
np.searchsorted(
    array,
    value,
    side="right"
)
```

Consider:

```python
arr = np.array([10, 20, 20, 30, 40])
```

Search for:

```text
20
```

### `side="left"`

Returns the position of the **first suitable location**.

```python
np.searchsorted(arr, 20, side="left")
```

Output:

```text
1
```

### `side="right"`

Returns the position **after existing equal values**.

```python
np.searchsorted(arr, 20, side="right")
```

Output:

```text
3
```

Visual:

```text
Index:  0   1   2   3   4
        ↓   ↓   ↓   ↓   ↓
Array: 10  20  20  30  40
            ↑   ↑
           same values
```

So:

```text
left  → before the first 20
right → after the last 20
```

---

# 🔟 `np.sort()`

Now let's learn **sorting**.

### 📖 Definition

`np.sort()` returns a **sorted copy** of an array.

### Syntax

```python
np.sort(array)
```

---

# 🟢 Example

```python
import numpy as np

arr = np.array([50, 10, 40, 20, 30])

result = np.sort(arr)

print(result)
```

Output:

```text
[10 20 30 40 50]
```

Original array:

```text
[50 10 40 20 30]
```

Sorted:

```text
[10 20 30 40 50]
```

---

# ⭐ Important — Original Array

`np.sort()` does **not normally modify the original array**.

Example:

```python
arr = np.array([50, 10, 40, 20, 30])

result = np.sort(arr)

print("Original:", arr)
print("Sorted:", result)
```

Output:

```text
Original: [50 10 40 20 30]
Sorted:   [10 20 30 40 50]
```

---

# 1️⃣1️⃣ Sorting 2D Arrays

Consider:

```python
arr = np.array([
    [30, 10, 20],
    [60, 40, 50]
])
```

### Default sorting

```python
result = np.sort(arr)

print(result)
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

Each row is sorted.

---

# 1️⃣2️⃣ Sorting by Axis

### `axis=1`

Sort each row:

```python
result = np.sort(arr, axis=1)
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

### `axis=0`

Sort each column:

```python
result = np.sort(arr, axis=0)
```

Output:

```text
[[30 10 20]
 [60 40 50]]
```

Let's understand why.

Original:

```text
30  10  20
60  40  50
```

Column 0:

```text
30
60
```

Already sorted.

Column 1:

```text
10
40
```

Already sorted.

Column 2:

```text
20
50
```

Already sorted.

So the result doesn't change.

---

# 1️⃣3️⃣ `np.argsort()`

This is a **very important Data Science function**.

### 📖 Definition

`np.argsort()` returns the **indices that would sort an array**.

Let's understand carefully.

---

## Example

```python
import numpy as np

arr = np.array([50, 10, 40, 20, 30])

result = np.argsort(arr)

print(result)
```

Output:

```text
[1 3 4 2 0]
```

At first this may look confusing. 😵

Let's understand.

Original:

```text
Index:  0   1   2   3   4
Value: 50  10  40  20  30
```

Sorted values:

```text
10  20  30  40  50
```

Where did these values come from?

```text
10 → index 1
20 → index 3
30 → index 4
40 → index 2
50 → index 0
```

Therefore:

```text
[1, 3, 4, 2, 0]
```

That's `argsort()`.

---

# 🧠 `sort()` vs `argsort()`

This is one of the most important concepts in this chapter.

| Function | Returns |
|---|---|
| `np.sort()` | Sorted values |
| `np.argsort()` | Indices that produce sorted order |

Example:

```python
arr = np.array([50, 10, 40, 20, 30])
```

### `sort()`

```python
np.sort(arr)
```

Result:

```text
[10 20 30 40 50]
```

### `argsort()`

```python
np.argsort(arr)
```

Result:

```text
[1 3 4 2 0]
```

### Memory Trick 🧠

```text
sort
 ↓
VALUES

argsort
 ↓
INDEXES
```

---

# 1️⃣4️⃣ Using `argsort()` to Sort Related Data

This is where `argsort()` becomes extremely useful.

Suppose:

```python
names = np.array([
    "Ravi",
    "John",
    "Anil"
])

marks = np.array([
    75,
    90,
    60
])
```

We want to sort students by marks.

First:

```python
order = np.argsort(marks)

print(order)
```

Output:

```text
[2 0 1]
```

Why?

```text
60 → index 2
75 → index 0
90 → index 1
```

Now:

```python
print(names[order])
print(marks[order])
```

Output:

```text
['Anil' 'Ravi' 'John']
[60 75 90]
```

### 🔥 This is very important for Data Science.

We used the same index order to rearrange **multiple related arrays**.

---

# 1️⃣5️⃣ Filtering Arrays

Searching and filtering often work together.

Suppose:

```python
marks = np.array([
    45,
    80,
    92,
    35,
    67
])
```

We want marks greater than 70.

### Method 1 — Boolean Mask

```python
result = marks[marks > 70]

print(result)
```

Output:

```text
[80 92]
```

---

# Method 2 — `np.where()`

```python
indexes = np.where(marks > 70)

print(indexes)
```

Output:

```text
(array([1, 2]),)
```

Then:

```python
print(marks[indexes])
```

Output:

```text
[80 92]
```

---

# 🧠 Difference

```text
marks > 70
     ↓
Boolean mask
     ↓
[False True True False False]
```

Then:

```text
marks[mask]
     ↓
[80 92]
```

While:

```text
np.where(marks > 70)
     ↓
indexes
     ↓
[1 2]
```

---

# 🌍 Real-World Example — Product Prices

```python
prices = np.array([
    500,
    1200,
    750,
    2000,
    900
])
```

Find products costing more than ₹1000:

```python
expensive = prices[prices > 1000]

print(expensive)
```

Output:

```text
[1200 2000]
```

Find their positions:

```python
indexes = np.where(prices > 1000)

print(indexes)
```

Output:

```text
(array([1, 3]),)
```

---

# 🌍 Real-World Example — Employee Salaries

```python
salary = np.array([
    25000,
    50000,
    35000,
    80000,
    45000
])
```

Find employees earning at least 45,000:

```python
result = salary[salary >= 45000]

print(result)
```

Output:

```text
[50000 80000 45000]
```

Sort salaries:

```python
sorted_salary = np.sort(salary)

print(sorted_salary)
```

Output:

```text
[25000 35000 45000 50000 80000]
```

Get sorting indexes:

```python
order = np.argsort(salary)

print(order)
```

Output:

```text
[0 2 4 1 3]
```

---

# 🔥 Complete Search + Sort Flow

```text
                 NumPy Search & Sort
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      np.where()    searchsorted()   np.sort()
          │              │              │
       Find           Insert          Values
       indexes        position        sorted
          │
          ↓
      np.argsort()
          │
          ↓
    Sorting indexes
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Thinking `np.where()` returns values

```python
arr = np.array([10, 20, 30])

np.where(arr == 20)
```

Returns:

```text
(array([1]),)
```

It returns the **index**, not directly the value.

---

## ❌ Mistake 2 — Using `searchsorted()` on an unsorted array

```python
arr = np.array([30, 10, 20])
```

Don't assume:

```python
np.searchsorted(arr, 15)
```

will give a meaningful insertion position.

Sort first if needed:

```python
arr = np.sort(arr)
```

---

## ❌ Mistake 3 — Confusing `sort()` and `argsort()`

Remember:

```text
sort()
   ↓
values

argsort()
   ↓
indexes
```

---

## ❌ Mistake 4 — Using Python `and`

Wrong:

```python
(arr > 20) and (arr < 50)
```

Correct:

```python
(arr > 20) & (arr < 50)
```

---

# 💼 Interview Questions

### Q1. What does `np.where()` do?

**Answer:**

It returns the indices where a specified condition is True.

---

### Q2. Can `np.where()` replace values?

**Answer:**

Yes.

```python
np.where(condition, true_value, false_value)
```

---

### Q3. What is `np.searchsorted()`?

**Answer:**

It finds the position where a value can be inserted into a sorted array while maintaining sorted order.

---

### Q4. What does `np.sort()` return?

**Answer:**

It returns a sorted array.

---

### Q5. What does `np.argsort()` return?

**Answer:**

It returns the indices that would sort the array.

---

### Q6. Difference between `sort()` and `argsort()`?

**Answer:**

```text
sort()    → sorted values
argsort() → sorted indexes
```

---

### Q7. Why is `argsort()` useful in Data Science?

**Answer:**

It allows us to sort one array and use the resulting index order to rearrange related arrays.

---

### Q8. What assumption does `searchsorted()` make?

**Answer:**

The input array should be sorted.

---

# 📝 Practice Questions

### Practice 1

Find the positions of values greater than 50:

```python
arr = np.array([20, 60, 40, 80, 30, 90])
```

Expected indexes:

```text
[1 3 5]
```

---

### Practice 2

Find all values less than 40.

```python
arr = np.array([20, 60, 40, 80, 30, 90])
```

Expected:

```text
[20 30]
```

---

### Practice 3

Sort:

```python
arr = np.array([70, 20, 90, 40, 10])
```

Expected:

```text
[10 20 40 70 90]
```

---

### Practice 4

Find `argsort()`:

```python
arr = np.array([70, 20, 90, 40, 10])
```

Expected:

```text
[4 1 3 0 2]
```

---

### Practice 5

Find where `25` should be inserted:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Expected:

```text
2
```

---

# 🎯 Mini Coding Exercise

Create this dataset:

```python
import numpy as np

students = np.array([
    "Ravi",
    "Anil",
    "John",
    "Priya",
    "Kiran"
])

marks = np.array([
    75,
    92,
    65,
    88,
    70
])
```

### Your tasks:

**1.** Find students who scored above 75.

**2.** Find their indexes.

**3.** Sort the marks.

**4.** Get the `argsort()` indexes.

**5.** Sort the student names according to their marks.

Expected sorted result:

```text
Anil
Priya
Ravi
Kiran
John
```

with marks:

```text
92
88
75
70
65
```

💡 Hint for descending order:

```python
order = np.argsort(marks)[::-1]
```

Then:

```python
students[order]
marks[order]
```

---

# 📋 Chapter 12 Summary

| Function | Purpose |
|---|---|
| `np.where()` | Find positions based on a condition |
| `np.where(condition, x, y)` | Choose values based on condition |
| `np.searchsorted()` | Find insertion position in sorted array |
| `np.sort()` | Sort values |
| `np.argsort()` | Get indexes for sorting |
| Boolean masking | Filter values |
| `&` | AND condition |
| `\|` | OR condition |
| `~` | NOT condition |

---

# 🧠 One-Minute Revision

```text
🔎 SEARCH
   │
   ├── np.where()
   │      ↓
   │   Find indexes
   │
   └── np.searchsorted()
          ↓
      Find insertion position


📊 SORT
   │
   ├── np.sort()
   │      ↓
   │   Sorted VALUES
   │
   └── np.argsort()
          ↓
      Sorted INDEXES
```

### ⭐ Most Important Memory Trick

```text
where()      → WHERE is it? 📍

searchsorted → WHERE should it go? 📌

sort()       → WHAT are the sorted values? 📊

argsort()    → WHICH indexes create the sorted order? 🔢
```

---

# 🧪 Chapter 12 Quiz

### 1. Which function finds indexes based on a condition?

A. `np.sort()`  
B. `np.where()`  
C. `np.stack()`  
D. `np.reshape()`

### 2. What does `np.sort()` return?

A. Indexes  
B. Boolean values  
C. Sorted values  
D. Shape

### 3. What does `np.argsort()` return?

A. Sorted values  
B. Sorted indexes  
C. Array size  
D. Data type

### 4. What does `searchsorted()` find?

A. Maximum value  
B. Minimum value  
C. Insertion position  
D. Array shape

### 5. Which operation is best for filtering?

A. Boolean masking  
B. `reshape()`  
C. `transpose()`  
D. `stack()`

### 6. What does this return?

```python
np.where(arr > 50)
```

A. Values greater than 50  
B. Indexes where values are greater than 50  
C. Sorted values  
D. Array shape

### 7. What is the difference?

```text
np.sort(arr)
np.argsort(arr)
```

### 8. Why should an array generally be sorted before using `searchsorted()`?

---

# ✅ Chapter 12 COMPLETE

You now know:

**`np.where()` → `np.searchsorted()` → `np.sort()` → `np.argsort()` → filtering → searching → sorting indexes.**

👉 Type **`NEXT`** when you're ready for:

# **Chapter 13 — Copy vs View** 📋👀

We will learn an **extremely important NumPy concept**:

```text
copy() → independent data 📋

view() → shares underlying data 👀
```

with memory diagrams and practical examples.