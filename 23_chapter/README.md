# 🚀 NUMPY — CHAPTER 23

# 🏆 NumPy Projects: Beginner → Advanced → Job-Ready

🎯 **This is the final chapter of your NumPy syllabus.**

In this chapter, we will stop learning individual functions and start using NumPy like a **Data Scientist / Python Developer**.

### 🗺️ Project Roadmap

| Level           | Project                             |
| --------------- | ----------------------------------- |
| 🟢 Beginner     | Student Marks Analysis              |
| 🟡 Intermediate | Sales Analysis                      |
| 🟡 Intermediate | Employee Salary Analysis            |
| 🟡 Intermediate | Temperature Analysis                |
| 🔵 Advanced     | Statistical Data Analysis           |
| 🔵 Advanced     | Simple Image Processing             |
| 🔴 Job-Ready    | Complete Data Science NumPy Project |

---

# 🟢 PROJECT 1 — Student Marks Analysis

## 🎯 Problem Statement

We have marks of 10 students.

We want to find:

* Total marks
* Average marks
* Highest marks
* Lowest marks
* Student with highest marks
* Pass students
* Fail students
* Grade
* Percentage

---

## 📦 Step 1 — Create Dataset

```python
import numpy as np


# ============================================================
# STUDENT MARKS DATA
# ============================================================

marks = np.array([
    78,
    65,
    92,
    45,
    88,
    56,
    72,
    39,
    95,
    61
])


print("Student Marks:")
print(marks)
```

### Output

```text
Student Marks:
[78 65 92 45 88 56 72 39 95 61]
```

---

# 📊 Step 2 — Basic Statistics

```python
# Total marks
total = np.sum(marks)

# Average marks
average = np.mean(marks)

# Highest marks
highest = np.max(marks)

# Lowest marks
lowest = np.min(marks)


print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```

### Output

```text
Total: 691
Average: 69.1
Highest: 95
Lowest: 39
```

---

# 🔎 Step 3 — Find Top Student Position

```python
# Find index of highest marks
top_student_index = np.argmax(marks)

print("Top Student Index:", top_student_index)
print("Top Student Marks:", marks[top_student_index])
```

### Output

```text
Top Student Index: 8
Top Student Marks: 95
```

Remember:

```text
Index     0   1   2   3   4   5   6   7   8   9
Marks    78  65  92  45  88  56  72  39  95  61
                                             ↑
                                           index 8
```

---

# ✅ Step 4 — Pass / Fail

Suppose:

```text
Pass >= 40
Fail < 40
```

We can use Boolean masking.

```python
pass_students = marks[marks >= 40]
fail_students = marks[marks < 40]

print("Pass Students Marks:")
print(pass_students)

print("Fail Students Marks:")
print(fail_students)
```

### Output

```text
Pass Students Marks:
[78 65 92 45 88 56 72 95 61]

Fail Students Marks:
[39]
```

---

# 🏅 Step 5 — Create Grades

We can use `np.where()`.

```python
grades = np.where(
    marks >= 90, "A",
    np.where(
        marks >= 75, "B",
        np.where(
            marks >= 60, "C",
            np.where(
                marks >= 40, "D", "F"
            )
        )
    )
)


print("Marks:")
print(marks)

print("Grades:")
print(grades)
```

### Output

```text
Marks:
[78 65 92 45 88 56 72 39 95 61]

Grades:
['B' 'C' 'A' 'D' 'B' 'D' 'C' 'F' 'A' 'C']
```

---

# 🧠 Concepts Used

This one project used:

```text
np.array()
     ↓
np.sum()
     ↓
np.mean()
     ↓
np.max()
     ↓
np.min()
     ↓
np.argmax()
     ↓
Boolean Masking
     ↓
np.where()
```

🔥 This is exactly how separate NumPy concepts start becoming a real program.

---

# 🟡 PROJECT 2 — Sales Analysis

Now let's work with business data.

## 🎯 Problem

A company records sales for 12 months.

We want to calculate:

* Total sales
* Average sales
* Maximum sales
* Minimum sales
* Best month
* Months above average
* Sales growth

---

## 💻 Code

```python
import numpy as np


# ============================================================
# MONTHLY SALES DATA
# ============================================================

sales = np.array([
    12000,
    15000,
    18000,
    14000,
    21000,
    25000,
    22000,
    28000,
    30000,
    27000,
    32000,
    35000
])


# ============================================================
# BASIC SALES ANALYSIS
# ============================================================

total_sales = np.sum(sales)

average_sales = np.mean(sales)

maximum_sales = np.max(sales)

minimum_sales = np.min(sales)

best_month_index = np.argmax(sales)


print("Total Sales:", total_sales)

print("Average Sales:", average_sales)

print("Maximum Sales:", maximum_sales)

print("Minimum Sales:", minimum_sales)

print("Best Month Index:", best_month_index)

print("Best Month Sales:", sales[best_month_index])
```

### Output

```text
Total Sales: 267000
Average Sales: 22250.0
Maximum Sales: 35000
Minimum Sales: 12000
Best Month Index: 11
Best Month Sales: 35000
```

---

# 📈 Sales Above Average

```python
above_average = sales[sales > average_sales]

print("Sales Above Average:")
print(above_average)
```

Output:

```text
[25000 28000 30000 27000 32000 35000]
```

---

# 📊 Calculate Month-to-Month Difference

One useful technique is:

```python
difference = np.diff(sales)

print("Month-to-Month Change:")
print(difference)
```

Conceptually:

```text
Month 1 → Month 2
15000 - 12000 = 3000

Month 2 → Month 3
18000 - 15000 = 3000
```

So:

```python
np.diff()
```

helps us calculate **consecutive differences**.

---

# 🟡 PROJECT 3 — Employee Salary Analysis

Now let's combine:

* NumPy
* Boolean masking
* Statistics
* Vectorization
* `np.where()`

---

## 📦 Dataset

```python
import numpy as np


# ============================================================
# EMPLOYEE DATA
# ============================================================

employee_ids = np.array([
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108
])


salary = np.array([
    35000,
    45000,
    55000,
    70000,
    90000,
    48000,
    65000,
    100000
])
```

---

# 💰 Salary Statistics

```python
print("Average Salary:", np.mean(salary))

print("Minimum Salary:", np.min(salary))

print("Maximum Salary:", np.max(salary))
```

Output:

```text
Average Salary: 64625.0
Minimum Salary: 35000
Maximum Salary: 100000
```

---

# 🔍 High Salary Employees

Suppose:

```text
High Salary >= 70000
```

```python
high_salary = salary[salary >= 70000]

print("High Salary Employees:")
print(high_salary)
```

Output:

```text
[ 70000  90000 100000]
```

---

# 📈 Give Everyone a 10% Salary Increase

This is where **vectorization** becomes very useful.

```python
new_salary = salary * 1.10

print("Old Salary:")
print(salary)

print("New Salary:")
print(new_salary)
```

Example:

```text
35000 × 1.10 = 38500
```

No loop is required.

🔥 **NumPy performs the operation on the entire array.**

---

# 🏷️ Salary Category

```python
category = np.where(
    salary >= 70000,
    "High",
    "Normal"
)

print(category)
```

Output:

```text
['Normal' 'Normal' 'Normal' 'High' 'High' 'Normal' 'Normal' 'High']
```

---

# 🟡 PROJECT 4 — Temperature Analysis

Suppose we have temperatures for 7 days.

```python
import numpy as np


temperature = np.array([
    32,
    35,
    31,
    38,
    40,
    36,
    33
])


print("Temperature:")
print(temperature)

print("Average:", np.mean(temperature))

print("Highest:", np.max(temperature))

print("Lowest:", np.min(temperature))
```

---

## 🌡️ Find Hot Days

Suppose:

```text
Hot day >= 37°C
```

```python
hot_days = temperature[temperature >= 37]

print("Hot Days:")
print(hot_days)
```

Output:

```text
[38 40]
```

---

# 🌡️ Celsius → Fahrenheit

Formula:

```text
°F = (°C × 9/5) + 32
```

NumPy version:

```python
fahrenheit = (temperature * 9 / 5) + 32

print("Celsius:")
print(temperature)

print("Fahrenheit:")
print(fahrenheit)
```

🔥 Notice:

We didn't use a loop.

This is **vectorization**.

---

# 🔵 PROJECT 5 — Statistical Data Analysis

Now let's build a more advanced numerical analysis project.

## Dataset

```python
import numpy as np


data = np.array([
    12, 15, 18, 20, 22,
    24, 25, 27, 30, 32,
    35, 38, 40, 42, 100
])
```

Notice:

```text
100
```

looks unusually high.

This could be an **outlier**.

---

# 📊 Basic Statistics

```python
print("Mean:", np.mean(data))

print("Median:", np.median(data))

print("Standard Deviation:", np.std(data))

print("Variance:", np.var(data))

print("Minimum:", np.min(data))

print("Maximum:", np.max(data))
```

---

# 📌 Percentiles

```python
q25 = np.percentile(data, 25)

q50 = np.percentile(data, 50)

q75 = np.percentile(data, 75)


print("25th Percentile:", q25)

print("50th Percentile:", q50)

print("75th Percentile:", q75)
```

Remember:

```text
25th percentile → Q1
50th percentile → Median
75th percentile → Q3
```

---

# 🔎 Simple Z-Score Analysis

Formula:

```text
z = (x - mean) / standard_deviation
```

NumPy:

```python
mean = np.mean(data)

std = np.std(data)

z_scores = (data - mean) / std

print("Z-Scores:")
print(z_scores)
```

We can then inspect unusually distant values.

⚠️ **Important:** Z-score is only one possible outlier method. The correct method depends on the dataset and statistical assumptions.

---

# 🔵 PROJECT 6 — Simple Image Processing

One of the most interesting uses of NumPy is **image processing**.

An image can be represented as numbers.

For a grayscale image:

```text
0   → Black
255 → White
```

Example:

```python
import numpy as np


image = np.array([
    [0,   50, 100],
    [150, 200, 250],
    [100, 150, 200]
])


print(image)
```

Visual:

```text
┌───────────────┐
│  0   50  100  │
│ 150  200  250 │
│ 100  150  200 │
└───────────────┘
```

---

# ☀️ Increase Brightness

Suppose we want to increase brightness by 30.

```python
brighter = image + 30

print(brighter)
```

But there is a problem.

Pixel values should normally stay between:

```text
0 → 255
```

So use:

```python
brighter = np.clip(image + 30, 0, 255)

print(brighter)
```

🔥 `np.clip()` keeps values inside a specified range.

---

# ⚫⚪ Image Thresholding

Suppose:

```text
pixel >= 128 → White
pixel < 128  → Black
```

```python
binary_image = np.where(
    image >= 128,
    255,
    0
)

print(binary_image)
```

Output:

```text
[[  0   0   0]
 [255 255 255]
 [  0 255 255]]
```

This is a simple example of **image segmentation/thresholding**.

---

# 🔴 PROJECT 7 — Complete Data Science-Style NumPy Project

Now let's combine many concepts.

## 🎯 Problem

We have employee information:

```text
Employee ID
Age
Salary
Experience
```

We want to:

1. Create data
2. Calculate statistics
3. Find high salaries
4. Calculate salary in lakhs
5. Normalize salary
6. Create experience categories
7. Find experienced employees
8. Give salary increment
9. Detect missing/invalid values
10. Produce a final report

---

## 💻 Complete VS Code Code

```python
import numpy as np


# ============================================================
# 1. CREATE EMPLOYEE DATA
# ============================================================

employee_id = np.array([
    101, 102, 103, 104, 105,
    106, 107, 108, 109, 110
])


age = np.array([
    24, 27, 30, 35, 29,
    40, 26, 32, 38, 28
])


salary = np.array([
    35000, 45000, 55000, 75000, 50000,
    90000, 40000, 65000, 85000, 48000
])


experience = np.array([
    1, 2, 4, 8, 3,
    12, 2, 6, 10, 3
])


# ============================================================
# 2. BASIC STATISTICS
# ============================================================

print("=" * 60)
print("EMPLOYEE STATISTICS")
print("=" * 60)

print("Average Salary:", np.mean(salary))

print("Minimum Salary:", np.min(salary))

print("Maximum Salary:", np.max(salary))

print("Average Age:", np.mean(age))

print("Average Experience:", np.mean(experience))


# ============================================================
# 3. HIGH SALARY EMPLOYEES
# ============================================================

high_salary = salary[salary >= 70000]

print("\nHigh Salary Employees:")
print(high_salary)


# ============================================================
# 4. SALARY IN LAKHS
# ============================================================

salary_lakhs = salary / 100000

print("\nSalary in Lakhs:")
print(salary_lakhs)


# ============================================================
# 5. SALARY NORMALIZATION
# ============================================================

salary_min = np.min(salary)

salary_max = np.max(salary)

salary_normalized = (
    (salary - salary_min)
    / (salary_max - salary_min)
)


print("\nNormalized Salary:")
print(salary_normalized)


# ============================================================
# 6. EXPERIENCE CATEGORY
# ============================================================

experience_category = np.where(
    experience >= 5,
    "Experienced",
    "Beginner"
)


print("\nExperience Category:")
print(experience_category)


# ============================================================
# 7. EXPERIENCED EMPLOYEES
# ============================================================

experienced_salary = salary[experience >= 5]

print("\nExperienced Employee Salaries:")
print(experienced_salary)


# ============================================================
# 8. 10% SALARY INCREMENT
# ============================================================

new_salary = salary * 1.10

print("\nNew Salary After 10% Increment:")
print(new_salary)


# ============================================================
# 9. FIND EMPLOYEE WITH HIGHEST SALARY
# ============================================================

highest_index = np.argmax(salary)

print("\nHighest Paid Employee ID:")
print(employee_id[highest_index])

print("Highest Salary:")
print(salary[highest_index])


# ============================================================
# 10. CHECK INVALID DATA
# ============================================================

print("\nCheck for Invalid Salary Values:")

print(np.isfinite(salary))


# ============================================================
# FINAL REPORT
# ============================================================

print("\n" + "=" * 60)
print("FINAL REPORT")
print("=" * 60)

print("Number of Employees:", salary.size)

print("Average Salary:", np.mean(salary))

print("Highest Salary:", np.max(salary))

print("Lowest Salary:", np.min(salary))

print("Average Experience:", np.mean(experience))

print("Experienced Employees:", np.sum(experience >= 5))
```

---

# 🧠 What Did We Use?

This final project connects almost your **entire NumPy course**:

```text
                     NUMPY
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      Arrays       Statistics      Filtering
        │              │              │
        ↓              ↓              ↓
    np.array()     np.mean()       Boolean Mask
                   np.max()        np.where()
                   np.min()
                       │
                       ↓
                 Vectorization
                       │
                       ↓
              Feature Engineering
                       │
                       ↓
              Data Science / ML
```

---

# 🧩 NumPy Project Skills Map

| Project                 | Main NumPy Concepts                     |
| ----------------------- | --------------------------------------- |
| 🎓 Student Marks        | Array, statistics, masking, `where`     |
| 💰 Sales                | Statistics, `diff`, filtering           |
| 👨‍💼 Employee Salary   | Vectorization, masking, normalization   |
| 🌡️ Temperature         | Arithmetic, statistics, conversion      |
| 📊 Statistical Analysis | Mean, median, std, variance, percentile |
| 🖼️ Image Processing    | 2D arrays, `clip`, `where`              |
| 🚀 Data Science Project | Multiple NumPy concepts together        |

---

# ⚠️ Common Project Mistakes

### ❌ Mistake 1 — Using Python `and`

Don't write:

```python
arr[(arr > 10) and (arr < 50)]
```

Use:

```python
arr[(arr > 10) & (arr < 50)]
```

---

### ❌ Mistake 2 — Forgetting parentheses

Wrong:

```python
arr > 10 & arr < 50
```

Correct:

```python
(arr > 10) & (arr < 50)
```

---

### ❌ Mistake 3 — Confusing `*` and `@`

```python
A * B
```

➡️ Element-wise multiplication.

```python
A @ B
```

➡️ Matrix multiplication.

---

### ❌ Mistake 4 — Forgetting that `randint()` excludes `high`

```python
np.random.randint(1, 10, 5)
```

Possible values:

```text
1 2 3 4 5 6 7 8 9
```

Not 10.

---

### ❌ Mistake 5 — Ignoring shapes

Before an operation:

```python
print(arr.shape)
```

is one of your best debugging tools.

---

# 🏆 NUMPY COMPLETE COURSE — FINAL CHEAT SHEET

| Chapter | Main Topic      | Important Functions                   |        |
| ------- | --------------- | ------------------------------------- | ------ |
| 1       | Introduction    | `np.array()`                          |        |
| 2       | Creating Arrays | `zeros`, `ones`, `arange`, `linspace` |        |
| 3       | Attributes      | `ndim`, `shape`, `size`, `dtype`      |        |
| 4       | Indexing        | `arr[row,col]`                        |        |
| 5       | Slicing         | `start:stop:step`                     |        |
| 6       | Operations      | `+ - * / **`                          |        |
| 7       | Math            | `sqrt`, `square`, `power`, `log`      |        |
| 8       | Statistics      | `mean`, `sum`, `std`, `median`        |        |
| 9       | Reshaping       | `reshape`, `flatten`, `ravel`         |        |
| 10      | Joining         | `concatenate`, `stack`, `vstack`      |        |
| 11      | Splitting       | `split`, `array_split`                |        |
| 12      | Searching       | `where`, `sort`, `argsort`            |        |
| 13      | Copy/View       | `copy`, `view`                        |        |
| 14      | Broadcasting    | Shape compatibility                   |        |
| 15      | Boolean Masking | `&`, `                                | `, `~` |
| 16      | Random          | `rand`, `randint`, `choice`           |        |
| 17      | Linear Algebra  | `dot`, `matmul`, `inv`                |        |
| 18      | Missing Values  | `nan`, `isnan`, `isfinite`            |        |
| 19      | Data Types      | `dtype`, `astype`                     |        |
| 20      | Advanced NumPy  | Vectorization, ufuncs                 |        |
| 21      | Data Science    | preprocessing, ML                     |        |
| 22      | NumPy + Pandas  | conversions                           |        |
| 23      | Projects        | Real-world practice                   |        |

---

# 🧠 MOST IMPORTANT NUMPY FUNCTIONS

### ⭐ Array Creation

```python
np.array()
np.zeros()
np.ones()
np.full()
np.arange()
np.linspace()
np.eye()
```

### ⭐ Information

```python
arr.ndim
arr.shape
arr.size
arr.dtype
arr.itemsize
arr.nbytes
```

### ⭐ Statistics

```python
np.sum()
np.mean()
np.median()
np.std()
np.var()
np.min()
np.max()
np.argmin()
np.argmax()
np.percentile()
```

### ⭐ Array Manipulation

```python
reshape()
flatten()
ravel()
transpose()
```

### ⭐ Searching

```python
np.where()
np.searchsorted()
np.sort()
np.argsort()
```

### ⭐ Random

```python
np.random.rand()
np.random.random()
np.random.randint()
np.random.randn()
np.random.choice()
np.random.seed()
```

### ⭐ Linear Algebra

```python
np.dot()
np.matmul()
np.linalg.inv()
np.linalg.det()
np.linalg.eig()
np.linalg.solve()
```

### ⭐ Missing Data

```python
np.isnan()
np.isfinite()
np.isinf()
np.nanmean()
np.nansum()
```

---

# 💼 JOB-READY NUMPY SKILL MAP

If you're preparing for **Data Science / Python / ML**, make sure you can comfortably do this:

```text
Python
  ↓
NumPy
  ↓
Arrays
  ↓
Indexing + Slicing
  ↓
Vectorized Operations
  ↓
Broadcasting
  ↓
Boolean Masking
  ↓
Statistics
  ↓
Data Cleaning
  ↓
Feature Engineering
  ↓
Pandas
  ↓
Machine Learning
```

🔥 **The most important NumPy concepts for interviews are:**

1. ⭐ `ndarray`
2. ⭐ `shape`
3. ⭐ `ndim`
4. ⭐ `dtype`
5. ⭐ Indexing & slicing
6. ⭐ Broadcasting
7. ⭐ Boolean masking
8. ⭐ Vectorization
9. ⭐ `axis`
10. ⭐ `reshape`
11. ⭐ Copy vs view
12. ⭐ Statistical functions
13. ⭐ `np.where()`
14. ⭐ `np.dot()` / `@`
15. ⭐ NumPy vs Pandas

---

# 🎯 FINAL NUMPY QUIZ

Try answering these **without looking at the answers**.

### Q1. What is NumPy?

### Q2. What is an `ndarray`?

### Q3. What does `shape` tell us?

### Q4. Difference between `size` and `shape`?

### Q5. What does `axis=0` usually mean for a 2D array?

### Q6. What is broadcasting?

### Q7. What is Boolean masking?

### Q8. Difference between `copy()` and `view()`?

### Q9. Difference between `flatten()` and `ravel()`?

### Q10. Difference between `*` and `@`?

### Q11. What does `np.argmax()` return?

### Q12. What does `np.where()` do?

### Q13. Why do we use `astype()`?

### Q14. What does `np.isnan()` check?

### Q15. What is vectorization?

### Q16. Why is NumPy generally faster than Python loops for many numerical array operations?

### Q17. What is the difference between `np.arange()` and `np.linspace()`?

### Q18. What is the difference between NumPy and Pandas?

### Q19. How do you convert a NumPy array to a Pandas DataFrame?

### Q20. What is NumPy used for in Machine Learning?

---

# 🎉 NUMPY COURSE COMPLETE!

You have now covered:

```text
🟢 Beginner
   ↓
Arrays
Indexing
Slicing
Operations
Statistics
   ↓
🟡 Intermediate
   ↓
Reshaping
Joining
Splitting
Searching
Copy/View
Broadcasting
Boolean Masking
Random
   ↓
🔵 Advanced
   ↓
Linear Algebra
Missing Values
Data Types
Vectorization
ufuncs
Advanced Indexing
   ↓
💼 Data Science
   ↓
Pandas
Machine Learning
Image Processing
Projects
```

## 🏆 Your next step

Don't just read these chapters again.

**Build the projects yourself in VS Code without copying the code.**

A good progression is:

```text
Day 1 → Student Marks
Day 2 → Sales Analysis
Day 3 → Employee Salary
Day 4 → Temperature Analysis
Day 5 → Statistical Analysis
Day 6 → Image Processing
Day 7 → Complete Data Science Project
```

When you are ready for the next subject, type **NEXT**.
