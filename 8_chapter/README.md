# 🚀 NumPy — Chapter 8: Statistical Functions

Welcome to **Chapter 8 — NumPy Statistical Functions**! 🎯

In Chapter 7, we learned mathematical functions such as:

```text
np.sqrt()
np.square()
np.power()
np.abs()
np.exp()
np.log()
```

Now we move to **Statistics**.

Statistics is extremely important for:

- 📊 Data Science
- 🤖 Machine Learning
- 📈 Data Analysis
- 🧠 AI
- 📋 Student/Sales/Employee datasets

---

# 📘 1. What is Statistics?

**Statistics** means collecting, analyzing, and understanding data.

Suppose we have student marks:

```python
import numpy as np

marks = np.array([60, 70, 80, 90, 100])
```

We may want to know:

```text
Total marks?
Average marks?
Middle value?
Smallest mark?
Largest mark?
How spread out are the marks?
```

NumPy provides functions for these calculations.

---

# 📚 Chapter 8 Functions

| Function | Purpose |
|---|---|
| `np.sum()` | Total |
| `np.mean()` | Average |
| `np.median()` | Middle value |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.min()` | Minimum |
| `np.max()` | Maximum |
| `np.argmin()` | Index of minimum |
| `np.argmax()` | Index of maximum |
| `np.percentile()` | Percentile |
| `axis` | Direction of calculation |

---

# 1️⃣ `np.sum()`

## 📌 Definition

`np.sum()` calculates the **total/sum** of all elements.

### Syntax

```python
np.sum(array)
```

### Example

```python
import numpy as np

marks = np.array([60, 70, 80, 90, 100])

total = np.sum(marks)

print(total)
```

### Output

```text
400
```

### 🧮 Dry Run

```text
60 + 70 + 80 + 90 + 100
= 400
```

---

# 2️⃣ `np.mean()`

## 📌 Definition

`mean` means **average**.

### Formula

```text
Mean = Sum of all values / Number of values
```

For:

```text
60, 70, 80, 90, 100
```

we have:

```text
Sum = 400
Number of values = 5
```

Therefore:

```text
Mean = 400 / 5
     = 80
```

### Syntax

```python
np.mean(array)
```

### Example

```python
marks = np.array([60, 70, 80, 90, 100])

print(np.mean(marks))
```

Output:

```text
80.0
```

### ⭐ Remember

```text
np.sum()  → total
np.mean() → average
```

---

# 3️⃣ `np.median()`

## 📌 Definition

**Median** is the middle value after the data is arranged in sorted order.

Example:

```text
10, 20, 30, 40, 50
```

The middle value is:

```text
30
```

Therefore:

```text
Median = 30
```

### Syntax

```python
np.median(array)
```

### Example

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.median(arr))
```

Output:

```text
30.0
```

---

# 🧠 Odd Number of Values

Suppose:

```text
5, 10, 15, 20, 25
```

There are 5 values.

The middle value is:

```text
15
```

So:

```text
Median = 15
```

---

# 🧠 Even Number of Values

Now:

```text
10, 20, 30, 40
```

There are 4 values.

There are two middle values:

```text
20 and 30
```

Median is:

```text
(20 + 30) / 2
= 25
```

Example:

```python
arr = np.array([10, 20, 30, 40])

print(np.median(arr))
```

Output:

```text
25.0
```

---

# 4️⃣ `np.min()`

## 📌 Definition

`np.min()` returns the **smallest value**.

### Syntax

```python
np.min(array)
```

Example:

```python
marks = np.array([60, 70, 80, 90, 100])

print(np.min(marks))
```

Output:

```text
60
```

---

# 5️⃣ `np.max()`

## 📌 Definition

`np.max()` returns the **largest value**.

```python
print(np.max(marks))
```

Output:

```text
100
```

### Memory Trick

```text
min → smallest
max → largest
```

---

# 6️⃣ `np.argmin()`

This is slightly different from `np.min()`.

## 📌 Definition

`np.argmin()` returns the **index of the smallest value**.

Example:

```python
arr = np.array([50, 20, 80, 10, 60])

print(np.argmin(arr))
```

Output:

```text
3
```

Why?

```text
Index:  0   1   2   3   4
Value: 50  20  80  10  60
                    ↑
                  minimum
```

The minimum value is:

```text
10
```

Its index is:

```text
3
```

Therefore:

```text
np.min(arr)    → 10
np.argmin(arr) → 3
```

---

# 7️⃣ `np.argmax()`

## 📌 Definition

`np.argmax()` returns the **index of the largest value**.

Example:

```python
arr = np.array([50, 20, 80, 10, 60])

print(np.argmax(arr))
```

Output:

```text
2
```

Because:

```text
Index:  0   1   2   3   4
Value: 50  20  80  10  60
                ↑
              maximum
```

So:

```text
np.max(arr)     → 80
np.argmax(arr)  → 2
```

---

# 🧠 Very Important Difference

| Function | Returns |
|---|---|
| `np.min()` | Minimum **value** |
| `np.argmin()` | Index of minimum |
| `np.max()` | Maximum **value** |
| `np.argmax()` | Index of maximum |

### ⭐ Memory Trick

> **`arg` → argument/index position**

So:

```text
min    → value
argmin → position

max    → value
argmax → position
```

---

# 8️⃣ `np.var()` — Variance

Now we enter an important statistics concept. 📊

## 📌 Definition

**Variance** measures how much data values are spread out from the mean.

### Basic idea

If values are close to the mean:

```text
Low variance
```

If values are far from the mean:

```text
High variance
```

---

# 🧮 Variance Formula

For a population:

```text
Variance = Σ(x - mean)² / N
```

Where:

```text
x    → each value
mean → average
N    → number of values
```

Don't worry — let's calculate it step by step.

---

# 🔍 Variance Dry Run

Consider:

```text
[10, 20, 30]
```

### Step 1 — Calculate mean

```text
Mean = (10 + 20 + 30) / 3
     = 60 / 3
     = 20
```

### Step 2 — Difference from mean

```text
10 - 20 = -10
20 - 20 = 0
30 - 20 = 10
```

### Step 3 — Square the differences

```text
(-10)² = 100
0²     = 0
10²    = 100
```

### Step 4 — Calculate average

```text
Variance = (100 + 0 + 100) / 3

         = 200 / 3

         ≈ 66.67
```

NumPy:

```python
arr = np.array([10, 20, 30])

print(np.var(arr))
```

Output:

```text
66.66666666666667
```

---

# 9️⃣ `np.std()` — Standard Deviation

## 📌 Definition

**Standard deviation** tells us how spread out values are from the mean.

It is related to variance.

### Formula

```text
Standard Deviation = √Variance
```

For our previous example:

```text
Variance ≈ 66.67
```

Therefore:

```text
Standard deviation
= √66.67
≈ 8.165
```

NumPy:

```python
arr = np.array([10, 20, 30])

print(np.std(arr))
```

Output approximately:

```text
8.16496581
```

---

# 🔥 Variance vs Standard Deviation

```text
Variance
   ↓
Square of spread

Standard deviation
   ↓
Square root of variance
```

Mathematically:

```text
std = √variance
```

Therefore:

```text
np.std(arr) ≈ np.sqrt(np.var(arr))
```

---

# 🧠 Simple Understanding

Suppose:

```text
Dataset A:
50, 50, 50, 50
```

All values are identical.

```text
Mean = 50
Variance = 0
Standard deviation = 0
```

There is **no spread**.

Now:

```text
Dataset B:
10, 30, 50, 70, 90
```

Values are more spread out.

Therefore:

```text
Variance → larger
Standard deviation → larger
```

---

# 🔟 `np.percentile()`

## 📌 Definition

A **percentile** tells us the value below which a certain percentage of observations fall.

### Syntax

```python
np.percentile(array, percentile)
```

For example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.percentile(arr, 50))
```

Output:

```text
30.0
```

### Why?

The 50th percentile corresponds to the **median**.

So:

```text
50th percentile = median
```

---

# 📊 Common Percentiles

```text
25th percentile → Q1
50th percentile → Median / Q2
75th percentile → Q3
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print("25th:", np.percentile(arr, 25))
print("50th:", np.percentile(arr, 50))
print("75th:", np.percentile(arr, 75))
```

Output:

```text
25th: 20.0
50th: 30.0
75th: 40.0
```

---

# 🌍 Real-World Example — Exam Marks

Suppose:

```python
marks = np.array([
    35, 45, 50, 55, 60,
    65, 70, 75, 80, 90
])
```

We can calculate:

```python
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard deviation:", np.std(marks))
```

This gives us a quick statistical summary of the marks.

---

# 🚨 Important Concept: `axis`

Now we reach one of the **most important concepts in NumPy**.

You will use `axis` repeatedly in:

- NumPy
- Pandas
- Data Science
- Machine Learning

So let's understand it carefully.

---

# 📘 What is Axis?

For a 2D array:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Visual:

```text
             Columns
          0    1    2
        ┌────┬────┬────┐
Row 0   │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
Row 1   │ 40 │ 50 │ 60 │
        ├────┼────┼────┤
Row 2   │ 70 │ 80 │ 90 │
        └────┴────┴────┘
```

NumPy has:

```text
axis=0
axis=1
```

---

# 🧠 Easy Axis Trick

For a 2D array:

```text
axis=0 → DOWN the rows
axis=1 → ACROSS the columns
```

Visual:

```text
axis=0
  ↓
  ↓
  ↓

10  20  30
40  50  60
70  80  90

       → axis=1 →
```

### ⭐ Memory Trick

> **axis=0 → vertical/down**  
> **axis=1 → horizontal/across**

---

# 1️⃣1️⃣ `sum()` with Axis

Consider:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

---

## `axis=0`

```python
print(np.sum(arr, axis=0))
```

Output:

```text
[120 150 180]
```

### Dry Run

Column 0:

```text
10 + 40 + 70 = 120
```

Column 1:

```text
20 + 50 + 80 = 150
```

Column 2:

```text
30 + 60 + 90 = 180
```

Therefore:

```text
[120 150 180]
```

### Visual

```text
             ↓    ↓    ↓
             axis=0
        ┌────┬────┬────┐
        │ 10 │ 20 │ 30 │
        ├────┼────┼────┤
        │ 40 │ 50 │ 60 │
        ├────┼────┼────┤
        │ 70 │ 80 │ 90 │
        └────┴────┴────┘
          120  150  180
```

---

# 1️⃣2️⃣ `sum()` with `axis=1`

```python
print(np.sum(arr, axis=1))
```

Output:

```text
[ 60 150 240]
```

### Dry Run

Row 0:

```text
10 + 20 + 30 = 60
```

Row 1:

```text
40 + 50 + 60 = 150
```

Row 2:

```text
70 + 80 + 90 = 240
```

Therefore:

```text
[60, 150, 240]
```

---

# 🔥 Axis Comparison

```text
Original:

10  20  30
40  50  60
70  80  90
```

### `axis=0`

```text
10+40+70 = 120
20+50+80 = 150
30+60+90 = 180

Result:
[120 150 180]
```

### `axis=1`

```text
10+20+30 = 60
40+50+60 = 150
70+80+90 = 240

Result:
[60 150 240]
```

---

# 🧠 Why Does Axis Work This Way?

This is a common beginner confusion.

Think:

```text
axis=0
```

means:

> Collapse the **rows** and calculate down each column.

And:

```text
axis=1
```

means:

> Collapse the **columns** and calculate across each row.

### ⭐ Another Memory Trick

```text
axis=0 → column-wise result
axis=1 → row-wise result
```

Both descriptions are useful:

```text
axis=0 → down → result for each column
axis=1 → across → result for each row
```

---

# 1️⃣3️⃣ Mean with Axis

```python
print(np.mean(arr, axis=0))
```

Output:

```text
[40. 50. 60.]
```

Because:

```text
Column 0:
(10 + 40 + 70) / 3 = 40

Column 1:
(20 + 50 + 80) / 3 = 50

Column 2:
(30 + 60 + 90) / 3 = 60
```

---

### `axis=1`

```python
print(np.mean(arr, axis=1))
```

Output:

```text
[20. 50. 80.]
```

Because:

```text
Row 0 → 20
Row 1 → 50
Row 2 → 80
```

---

# 1️⃣4️⃣ Min and Max with Axis

### Minimum by column

```python
print(np.min(arr, axis=0))
```

Output:

```text
[10 20 30]
```

### Minimum by row

```python
print(np.min(arr, axis=1))
```

Output:

```text
[10 40 70]
```

---

### Maximum by column

```python
print(np.max(arr, axis=0))
```

Output:

```text
[70 80 90]
```

### Maximum by row

```python
print(np.max(arr, axis=1))
```

Output:

```text
[30 60 90]
```

---

# 📊 Statistical Functions with Axis

Many NumPy statistical functions support `axis`.

| Function | Purpose |
|---|---|
| `np.sum()` | Total |
| `np.mean()` | Average |
| `np.median()` | Middle value |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.min()` | Minimum |
| `np.max()` | Maximum |

Example:

```python
np.mean(arr, axis=0)
```

---

# 🌍 Real-World Example — Student Marks

Suppose:

```text
Rows    → Students
Columns → Subjects
```

```python
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])
```

Imagine:

```text
Column 0 → Maths
Column 1 → Science
Column 2 → English
```

### Average mark for each subject

```python
print(np.mean(marks, axis=0))
```

Output:

```text
[78.33333333 81.66666667 84.33333333]
```

This gives:

```text
Maths average
Science average
English average
```

---

### Average mark for each student

```python
print(np.mean(marks, axis=1))
```

Output:

```text
[80.         73.33333333 91.        ]
```

This gives:

```text
Student 1 average
Student 2 average
Student 3 average
```

### ⭐ This is why `axis` is so important in Data Science.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Confusing `min` and `argmin`

```text
np.min(arr)
```

returns:

```text
value
```

while:

```text
np.argmin(arr)
```

returns:

```text
index
```

---

## ❌ Mistake 2 — Confusing variance and standard deviation

Remember:

```text
std = √variance
```

---

## ❌ Mistake 3 — Confusing axis 0 and axis 1

Remember:

```text
axis=0 → DOWN → result for each column

axis=1 → ACROSS → result for each row
```

---

## ❌ Mistake 4 — Forgetting that median requires ordered position

For understanding median, think of the values in **sorted order**.

---

# 💼 Interview Questions

### Q1. What does `np.sum()` do?

Returns the sum/total of array elements.

### Q2. What does `np.mean()` calculate?

The arithmetic average.

```text
mean = sum / number of values
```

### Q3. What is the difference between `min()` and `argmin()`?

```text
min    → minimum value
argmin → index of minimum
```

### Q4. What is the difference between `max()` and `argmax()`?

```text
max    → maximum value
argmax → index of maximum
```

### Q5. What is variance?

A measure of how much values are spread around the mean.

### Q6. What is standard deviation?

The square root of variance.

### Q7. What is the 50th percentile?

It corresponds to the **median**.

### Q8. What does `axis=0` mean for a 2D array?

It calculates down the rows, producing a result for each column.

### Q9. What does `axis=1` mean?

It calculates across the columns, producing a result for each row.

### Q10. Why is axis important in Data Science?

Because datasets commonly contain rows and columns, and we often need calculations **per row** or **per column**.

---

# 🧪 Practice Program

Run this in VS Code:

```python
import numpy as np

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print("Marks:")
print(marks)

print("\nTotal:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))

print("\nColumn totals:")
print(np.sum(marks, axis=0))

print("\nRow totals:")
print(np.sum(marks, axis=1))

print("\nColumn averages:")
print(np.mean(marks, axis=0))

print("\nRow averages:")
print(np.mean(marks, axis=1))
```

---

# 🎯 Mini Coding Exercise

Create:

```python
sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450]
])
```

Find:

### 1. Total sales

```python
?
```

### 2. Average sales

```python
?
```

### 3. Minimum sales

```python
?
```

### 4. Maximum sales

```python
?
```

### 5. Total for each column

```python
?
```

### 6. Total for each row

```python
?
```

### 7. Average for each column

```python
?
```

### 8. Average for each row

```python
?
```

### 9. Index of minimum value

```python
?
```

### 10. Index of maximum value

```python
?
```

---

# 📌 Chapter 8 Summary

| Function / Concept | Meaning |
|---|---|
| `np.sum()` | Total |
| `np.mean()` | Average |
| `np.median()` | Middle value |
| `np.var()` | Variance |
| `np.std()` | Standard deviation |
| `np.min()` | Minimum value |
| `np.max()` | Maximum value |
| `np.argmin()` | Index of minimum |
| `np.argmax()` | Index of maximum |
| `np.percentile()` | Percentile |
| `axis=0` | Down → result for each column |
| `axis=1` | Across → result for each row |

---

# 🧠 Final Revision Map

```text
                 NUMPY STATISTICS
                        │
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
    Central          Spread           Position
   Tendency
       │                │                │
   mean             variance          min
   median           std               max
                                      argmin
                                      argmax
       │
       ↓
   Percentile
```

### ⭐ Most Important Formulas

```text
Mean
= Sum / Number of values

Variance
= Average of squared differences from mean

Standard Deviation
= √Variance
```

### ⭐ Most Important Axis Rule

```text
2D Array

axis=0
↓
down the rows
→ result for each column

axis=1
→
across the columns
→ result for each row
```

---

# 📝 Chapter 8 Quiz

Try these without looking back:

1. What is the difference between `np.sum()` and `np.mean()`?
2. What is the median of `[10, 20, 30, 40, 50]`?
3. What is the median of `[10, 20, 30, 40]`?
4. What does `np.argmin()` return?
5. What does `np.argmax()` return?
6. What is the relationship between variance and standard deviation?
7. What does the 50th percentile represent?
8. What does `axis=0` do?
9. What does `axis=1` do?
10. For a student-marks array where rows are students and columns are subjects, which axis would you use to calculate the **average of each subject**?

---

# ✅ Chapter 8 COMPLETE

### Next → 🚀 **Chapter 9 — Reshaping Arrays**

We will learn:

```text
reshape()
resize()
flatten()
ravel()
transpose()
.T
Changing dimensions
```

with **visual transformations**, shape calculations, and step-by-step dry runs.

Type **`NEXT`** when ready.