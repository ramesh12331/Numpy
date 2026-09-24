# 🚀 Chapter 22 — NumPy + Pandas

Welcome to **Chapter 22**! 🎯

This chapter is especially important for your **Data Science journey**, because NumPy and Pandas are often used together.

You already learned:

```text
NumPy
 ↓
Numerical calculations
 ↓
Arrays
```

Now we connect it with:

```text
Pandas
 ↓
Series
 ↓
DataFrame
 ↓
Tabular Data
```

---

# 📚 What We Will Learn

1. 🔹 NumPy Array → Pandas Series
2. 🔹 NumPy Array → Pandas DataFrame
3. 🔹 Pandas Series → NumPy Array
4. 🔹 Pandas DataFrame → NumPy Array
5. 🔹 Working with columns
6. 🔹 NumPy operations inside Pandas
7. 🔹 Pandas vs NumPy
8. 🔹 When to use NumPy
9. 🔹 When to use Pandas
10. 🔹 Real-world Data Science workflow
11. 🔹 Complete VS Code practice
12. 🔹 Common mistakes
13. 🔹 Interview questions
14. 🔹 Mini project
15. 🔹 Summary
16. 🔹 Quiz

---

# 1️⃣ NumPy Array → Pandas Series

First, remember:

### NumPy array

```python
import numpy as np

arr = np.array([
    10,
    20,
    30,
    40,
    50
])

print(arr)
```

Output:

```text
[10 20 30 40 50]
```

Now convert it to a Pandas Series.

```python
import pandas as pd

series = pd.Series(arr)

print(series)
```

Output:

```text
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

---

# 🧠 What Happened?

```text
NumPy Array
    ↓
[10 20 30 40 50]
    ↓
pd.Series()
    ↓
Pandas Series
```

The Pandas Series adds an **index**:

```text
Index   Value
  0       10
  1       20
  2       30
  3       40
  4       50
```

---

# 2️⃣ NumPy Array + Custom Index

We can also provide our own index.

```python
arr = np.array([
    10,
    20,
    30,
    40,
    50
])

series = pd.Series(
    arr,
    index=["A", "B", "C", "D", "E"]
)

print(series)
```

Output:

```text
A    10
B    20
C    30
D    40
E    50
dtype: int64
```

Now:

```python
print(series["C"])
```

Output:

```text
30
```

---

# 3️⃣ NumPy 2D Array → Pandas DataFrame ⭐

This is one of the most important conversions.

Create a NumPy 2D array:

```python
import numpy as np

arr = np.array([
    [101, 25, 40000],
    [102, 30, 55000],
    [103, 28, 48000]
])

print(arr)
```

Output:

```text
[[  101     25  40000]
 [  102     30  55000]
 [  103     28  48000]]
```

Convert it to a DataFrame:

```python
import pandas as pd

df = pd.DataFrame(arr)

print(df)
```

Output:

```text
     0   1      2
0  101  25  40000
1  102  30  55000
2  103  28  48000
```

---

# 4️⃣ Adding Column Names

Instead of:

```text
0
1
2
```

we can provide names.

```python
df = pd.DataFrame(
    arr,
    columns=["employee_id", "age", "salary"]
)

print(df)
```

Output:

```text
   employee_id  age  salary
0          101   25   40000
1          102   30   55000
2          103   28   48000
```

### ⭐ Much easier to understand!

---

# 5️⃣ NumPy → DataFrame Visual

Think:

```text
NumPy Array
──────────────────────
101   25   40000
102   30   55000
103   28   48000
──────────────────────
        ↓
    pd.DataFrame()
        ↓
Pandas DataFrame

employee_id   age   salary
     101       25    40000
     102       30    55000
     103       28    48000
```

---

# 6️⃣ Pandas Series → NumPy Array

Now reverse the process.

Create a Series:

```python
import pandas as pd

series = pd.Series([
    10,
    20,
    30,
    40
])

print(series)
```

Convert to NumPy:

```python
arr = series.to_numpy()

print(arr)
```

Output:

```text
[10 20 30 40]
```

### ⭐ Syntax

```python
series.to_numpy()
```

---

# 7️⃣ Pandas DataFrame → NumPy Array

Create a DataFrame:

```python
df = pd.DataFrame({
    "age": [25, 30, 28],
    "salary": [40000, 55000, 48000]
})

print(df)
```

Output:

```text
   age  salary
0   25   40000
1   30   55000
2   28   48000
```

Convert:

```python
arr = df.to_numpy()

print(arr)
```

Output:

```text
[[    25  40000]
 [    30  55000]
 [    28  48000]]
```

---

# 8️⃣ `.values` vs `.to_numpy()`

You may see:

```python
df.values
```

This can return the underlying NumPy representation.

However, for explicit conversion, prefer:

```python
df.to_numpy()
```

### 🧠 Remember

```text
Series → to_numpy()
DataFrame → to_numpy()
```

---

# 9️⃣ NumPy Array → DataFrame With Index

We can provide both:

* column names
* row indexes

Example:

```python
arr = np.array([
    [25, 40000],
    [30, 55000],
    [28, 48000]
])

df = pd.DataFrame(
    arr,
    columns=["age", "salary"],
    index=["A", "B", "C"]
)

print(df)
```

Output:

```text
   age  salary
A   25   40000
B   30   55000
C   28   48000
```

---

# 🔟 NumPy Operations on Pandas Data

Now things become interesting. 🔥

Suppose:

```python
df = pd.DataFrame({
    "salary": [40000, 50000, 60000, 70000]
})
```

We can use NumPy:

```python
import numpy as np

df["salary_log"] = np.log(df["salary"])

print(df)
```

Now Pandas manages the table, while NumPy performs the numerical calculation.

---

# 1️⃣1️⃣ NumPy `sqrt()` With Pandas

```python
df = pd.DataFrame({
    "marks": [25, 36, 49, 64, 81]
})

df["sqrt_marks"] = np.sqrt(df["marks"])

print(df)
```

Output:

```text
   marks  sqrt_marks
0     25         5.0
1     36         6.0
2     49         7.0
3     64         8.0
4     81         9.0
```

### Flow

```text
Pandas DataFrame
       ↓
Select column
       ↓
NumPy function
       ↓
Create new column
```

---

# 1️⃣2️⃣ NumPy `where()` With Pandas

Suppose:

```python
df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "marks": [35, 60, 75, 40]
})
```

We want:

```text
marks >= 50 → Pass
marks < 50  → Fail
```

Use:

```python
df["result"] = np.where(
    df["marks"] >= 50,
    "Pass",
    "Fail"
)

print(df)
```

Output:

```text
  name  marks result
0    A     35   Fail
1    B     60   Pass
2    C     75   Pass
3    D     40   Fail
```

This is a very common Data Science pattern.

---

# 1️⃣3️⃣ NumPy Mathematical Calculation in Pandas

Suppose:

```python
df = pd.DataFrame({
    "price": [100, 200, 300, 400]
})
```

Calculate 18% tax:

```python
df["tax"] = df["price"] * 0.18
```

Calculate final price:

```python
df["final_price"] = df["price"] + df["tax"]

print(df)
```

Output:

```text
   price   tax  final_price
0    100  18.0        118.0
1    200  36.0        236.0
2    300  54.0        354.0
3    400  72.0        472.0
```

This uses NumPy/Pandas-style vectorized operations.

---

# 1️⃣4️⃣ NumPy Statistics + Pandas

Suppose:

```python
df = pd.DataFrame({
    "salary": [
        40000,
        50000,
        60000,
        70000,
        80000
    ]
})
```

You can use NumPy:

```python
print(np.mean(df["salary"]))
```

Output:

```text
60000.0
```

You can also use Pandas:

```python
print(df["salary"].mean())
```

Output:

```text
60000.0
```

### 🧠 Both can work.

But Pandas has many operations designed specifically for Series/DataFrames.

---

# 1️⃣5️⃣ NumPy vs Pandas ⭐⭐⭐

This is one of the most important concepts.

| Feature                     | NumPy                                | Pandas                   |
| --------------------------- | ------------------------------------ | ------------------------ |
| Main structure              | `ndarray`                            | Series / DataFrame       |
| Best for                    | Numerical arrays                     | Tabular data             |
| Labels                      | Generally no named row/column labels | Yes                      |
| Missing-data tools          | Available                            | Extensive                |
| DataFrame                   | ❌                                    | ✅                        |
| Matrix/numerical operations | ⭐⭐⭐                                  | Good                     |
| Data cleaning               | Basic numerical tools                | ⭐⭐⭐                      |
| CSV/Excel workflows         | Usually through other tools          | ⭐⭐⭐                      |
| GroupBy                     | ❌                                    | ✅                        |
| Merge/Join                  | ❌                                    | ✅                        |
| Time-series tools           | Limited                              | Strong                   |
| ML numerical input          | Very common                          | Often converted to NumPy |

---

# 1️⃣6️⃣ When Should You Use NumPy?

Use NumPy when your main task is:

```text
Numerical computation
Matrix operations
Linear algebra
Mathematical calculations
Large homogeneous numerical arrays
Scientific computing
```

Example:

```python
arr = np.array([
    [1, 2],
    [3, 4]
])

result = arr @ arr
```

NumPy is ideal here.

---

# 1️⃣7️⃣ When Should You Use Pandas?

Use Pandas when working with:

```text
Rows + columns
CSV files
Excel files
Data cleaning
Missing values
Grouping
Filtering
Sorting
Merging datasets
Data analysis
```

Example:

```python
df = pd.read_csv("employees.csv")

print(df.groupby("department")["salary"].mean())
```

Pandas is usually much more convenient for this kind of tabular analysis.

---

# 1️⃣8️⃣ Simple Comparison

Think about this:

### NumPy

```text
[10, 20, 30, 40]
```

Focus:

```text
Numbers
 ↓
Mathematics
 ↓
Arrays
```

### Pandas

```text
Name     Age    Salary
Ramesh   25     40000
Suresh   30     55000
Kiran    28     48000
```

Focus:

```text
Rows
 +
Columns
 +
Labels
 +
Data analysis
```

---

# 1️⃣9️⃣ Data Science Workflow ⭐⭐⭐

Now combine everything you've learned.

```text
             RAW DATA
                 ↓
        CSV / Excel / Database
                 ↓
              Pandas
                 ↓
       Data Cleaning / Analysis
                 ↓
          NumPy Calculations
                 ↓
       Feature Engineering
                 ↓
          NumPy Arrays
                 ↓
       Machine Learning Model
                 ↓
             Prediction
```

In practice, NumPy and Pandas often work **together**, rather than being competing choices.

---

# 2️⃣0️⃣ Real-World Example

Suppose we have employee data:

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "age": [25, 30, 28, 35, 40],
    "salary": [40000, 55000, 48000, 75000, 90000]
})

print(df)
```

Output:

```text
   employee_id  age  salary
0          101   25   40000
1          102   30   55000
2          103   28   48000
3          104   35   75000
4          105   40   90000
```

---

# 2️⃣1️⃣ Analyze With NumPy

Extract salary:

```python
salary = df["salary"].to_numpy()

print(salary)
```

Output:

```text
[40000 55000 48000 75000 90000]
```

Now:

```python
print("Mean:", np.mean(salary))
print("Minimum:", np.min(salary))
print("Maximum:", np.max(salary))
print("Standard Deviation:", np.std(salary))
```

---

# 2️⃣2️⃣ Create a NumPy-Based Feature

Let's convert salary into lakhs:

```python
df["salary_lakhs"] = df["salary"].to_numpy() / 100000

print(df)
```

Output:

```text
   employee_id  age  salary  salary_lakhs
0          101   25   40000          0.40
1          102   30   55000          0.55
2          103   28   48000          0.48
3          104   35   75000          0.75
4          105   40   90000          0.90
```

---

# 2️⃣3️⃣ NumPy + Pandas Filtering

Find salaries above `50000`:

```python
high_salary = df[df["salary"] > 50000]

print(high_salary)
```

Output:

```text
   employee_id  age  salary  salary_lakhs
1          102   30   55000          0.55
3          104   35   75000          0.75
4          105   40   90000          0.90
```

---

# 2️⃣4️⃣ Normalize a Pandas Column Using NumPy

```python
salary = df["salary"].to_numpy()

salary_min = np.min(salary)
salary_max = np.max(salary)

df["salary_normalized"] = (
    (salary - salary_min)
    / (salary_max - salary_min)
)

print(df)
```

Now we have:

```text
salary
salary_lakhs
salary_normalized
```

This is a good example of **Pandas + NumPy working together**.

---

# 2️⃣5️⃣ Complete VS Code Practice

```python
# ============================================================
# NUMPY + PANDAS
# ============================================================

import numpy as np
import pandas as pd


# ============================================================
# 1. CREATE NUMPY ARRAY
# ============================================================

arr = np.array([
    10,
    20,
    30,
    40,
    50
])

print("NumPy Array:")
print(arr)


# ============================================================
# 2. NUMPY ARRAY → PANDAS SERIES
# ============================================================

series = pd.Series(arr)

print("\nPandas Series:")
print(series)


# ============================================================
# 3. NUMPY 2D ARRAY → DATAFRAME
# ============================================================

employee_data = np.array([
    [101, 25, 40000],
    [102, 30, 55000],
    [103, 28, 48000],
    [104, 35, 75000],
    [105, 40, 90000]
])

df = pd.DataFrame(
    employee_data,
    columns=[
        "employee_id",
        "age",
        "salary"
    ]
)

print("\nDataFrame:")
print(df)


# ============================================================
# 4. DATAFRAME → NUMPY ARRAY
# ============================================================

numpy_data = df.to_numpy()

print("\nDataFrame Converted to NumPy:")
print(numpy_data)


# ============================================================
# 5. EXTRACT SALARY
# ============================================================

salary = df["salary"].to_numpy()

print("\nSalary NumPy Array:")
print(salary)


# ============================================================
# 6. NUMPY STATISTICS
# ============================================================

print("\nAverage Salary:")
print(np.mean(salary))

print("\nMinimum Salary:")
print(np.min(salary))

print("\nMaximum Salary:")
print(np.max(salary))

print("\nSalary Standard Deviation:")
print(np.std(salary))


# ============================================================
# 7. SALARY IN LAKHS
# ============================================================

df["salary_lakhs"] = salary / 100000

print("\nSalary in Lakhs:")
print(df)


# ============================================================
# 8. NORMALIZE SALARY
# ============================================================

salary_min = np.min(salary)
salary_max = np.max(salary)

df["salary_normalized"] = (
    (salary - salary_min)
    / (salary_max - salary_min)
)

print("\nNormalized Salary:")
print(df)


# ============================================================
# 9. HIGH SALARY EMPLOYEES
# ============================================================

high_salary = df[df["salary"] > 50000]

print("\nEmployees With Salary > 50000:")
print(high_salary)


# ============================================================
# 10. NUMPY WHERE
# ============================================================

df["category"] = np.where(
    df["salary"] >= 60000,
    "High",
    "Normal"
)

print("\nSalary Category:")
print(df)
```

---

# 2️⃣6️⃣ Common Mistakes

### ❌ Mistake 1 — Confusing Series and DataFrame

```text
Series
 ↓
One-dimensional labeled data
```

```text
DataFrame
 ↓
Two-dimensional labeled table
```

---

### ❌ Mistake 2 — Forgetting `.to_numpy()`

If you need the NumPy representation:

```python
df.to_numpy()
```

For a Series:

```python
series.to_numpy()
```

---

### ❌ Mistake 3 — Assuming NumPy replaces Pandas

They have different strengths.

```text
NumPy → numerical computing
Pandas → tabular data analysis
```

They are frequently used together.

---

### ❌ Mistake 4 — Converting everything to NumPy immediately

If you need:

```text
column names
index labels
groupby
merge
CSV/Excel workflows
```

keeping the data in Pandas is often more convenient.

---

### ❌ Mistake 5 — Forgetting data types

When converting:

```python
df.to_numpy()
```

the resulting NumPy array's dtype depends on the columns being combined.

If a DataFrame contains mixed types, the NumPy result may use a dtype that can represent all those values.

---

# 🎤 Interview Questions

### Q1. What is the difference between NumPy and Pandas?

**Answer:**

NumPy is primarily for numerical arrays and mathematical operations, while Pandas provides labeled Series/DataFrame structures for tabular data analysis and manipulation.

---

### Q2. How do you convert a NumPy array to a Pandas Series?

```python
pd.Series(arr)
```

---

### Q3. How do you convert a NumPy 2D array to a DataFrame?

```python
pd.DataFrame(arr)
```

---

### Q4. How do you convert a Pandas Series to NumPy?

```python
series.to_numpy()
```

---

### Q5. How do you convert a DataFrame to NumPy?

```python
df.to_numpy()
```

---

### Q6. What is a Pandas Series?

**Answer:**
A Series is a one-dimensional labeled data structure.

Example:

```text
A    10
B    20
C    30
```

---

### Q7. What is a DataFrame?

**Answer:**
A DataFrame is a two-dimensional labeled tabular data structure containing rows and columns.

---

### Q8. Can NumPy functions be used with Pandas?

Yes.

For example:

```python
np.sqrt(df["marks"])
```

or:

```python
np.mean(df["salary"])
```

---

### Q9. When would you prefer NumPy?

When the main task involves numerical arrays, mathematical operations, linear algebra, or scientific computing.

---

### Q10. When would you prefer Pandas?

When working with labeled tabular data, CSV/Excel files, cleaning, filtering, grouping, joining, and DataFrame-based analysis.

---

# 💻 Practice

## Practice 1

Create:

```python
arr = np.array([
    [101, 25, 40000],
    [102, 30, 50000],
    [103, 35, 60000]
])
```

Convert it to:

```text
DataFrame
```

with:

```text
employee_id
age
salary
```

---

## Practice 2

Create a Series from:

```python
np.array([10, 20, 30, 40, 50])
```

with custom indexes:

```text
A B C D E
```

---

## Practice 3

Convert:

```python
df
```

to NumPy using:

```python
to_numpy()
```

---

## Practice 4

Using NumPy:

```python
marks = np.array([35, 60, 75, 90])
```

create a Pandas DataFrame containing:

```text
marks
result
```

where:

```text
marks >= 50 → Pass
marks < 50 → Fail
```

---

# 🧩 Mini Project — Employee Data Analysis

Create:

```python
employees = np.array([
    [101, 25, 40000],
    [102, 30, 55000],
    [103, 28, 48000],
    [104, 35, 75000],
    [105, 40, 90000],
    [106, 45, 120000]
])
```

Convert it to:

```text
Pandas DataFrame
```

Columns:

```text
employee_id
age
salary
```

Then create:

### 1️⃣ Salary in lakhs

```text
salary / 100000
```

### 2️⃣ Salary normalization

```text
(x - min) / (max - min)
```

### 3️⃣ Salary category

```text
salary >= 60000 → High
otherwise       → Normal
```

### 4️⃣ Find average salary using NumPy.

### 5️⃣ Find maximum salary using NumPy.

### 6️⃣ Convert the final DataFrame back to NumPy.

---

# 🧠 Chapter 22 Memory Map

```text
                    NUMPY + PANDAS
                          │
             ┌────────────┴────────────┐
             ↓                         ↓
          NumPy                      Pandas
             │                         │
        ndarray                    Series
             │                         │
             │                     DataFrame
             │                         │
             └──────────┬──────────────┘
                        ↓
                 Data Science
                        ↓
               Clean / Analyze
                        ↓
                Transform Data
                        ↓
                Machine Learning
```

---

# ⭐ Final Summary

| Task                     | Code                    |
| ------------------------ | ----------------------- |
| NumPy → Series           | `pd.Series(arr)`        |
| NumPy → DataFrame        | `pd.DataFrame(arr)`     |
| Series → NumPy           | `series.to_numpy()`     |
| DataFrame → NumPy        | `df.to_numpy()`         |
| NumPy function on Pandas | `np.sqrt(df["column"])` |
| Conditional column       | `np.where()`            |
| NumPy statistics         | `np.mean()`, `np.std()` |
| NumPy filtering          | Boolean masking         |
| NumPy numerical work     | Arrays                  |
| Pandas tabular work      | Series/DataFrame        |

---

# 🔥 Most Important Memory Trick

```text
NumPy
  ↓
Numerical calculations
Arrays
Matrix operations
Scientific computing

Pandas
  ↓
Tables
Rows + Columns
Labels
Data cleaning
Data analysis
```

And:

```text
NumPy Array
     ↓
pd.Series()
     ↓
Series

NumPy 2D Array
     ↓
pd.DataFrame()
     ↓
DataFrame

Series
     ↓
.to_numpy()
     ↓
NumPy Array

DataFrame
     ↓
.to_numpy()
     ↓
NumPy Array
```

---

# 🧪 Chapter 22 Quiz

### Q1. Which function converts a NumPy array to a Pandas Series?

A. `pd.Array()`
B. `pd.Series()`
C. `np.Series()`
D. `Series.to_numpy()`

### Q2. Which function converts a NumPy 2D array to a DataFrame?

A. `pd.DataFrame()`
B. `np.DataFrame()`
C. `pd.Array()`
D. `df.numpy()`

### Q3. How do you convert a Series to NumPy?

A. `series.array()`
B. `series.numpy()`
C. `series.to_numpy()`
D. `np.series()`

### Q4. How do you convert a DataFrame to NumPy?

A. `df.to_numpy()`
B. `df.array()`
C. `np.dataframe()`
D. `df.convert()`

### Q5. Which is primarily designed for tabular data analysis?

A. NumPy
B. Pandas
C. Matplotlib
D. Math

### Q6. Which is primarily designed for numerical array operations?

A. NumPy
B. Pandas
C. HTML
D. Flask

### Q7. What does this do?

```python
np.where(df["marks"] >= 50, "Pass", "Fail")
```

A. Sorts marks
B. Creates conditional values
C. Deletes marks
D. Calculates mean

### Q8. What does this return?

```python
df["salary"].to_numpy()
```

A. DataFrame
B. Series
C. NumPy array
D. Dictionary

### Q9. Which structure is two-dimensional and labeled?

A. NumPy scalar
B. Pandas Series
C. Pandas DataFrame
D. Python integer

### Q10. Do NumPy and Pandas compete with each other?

A. Yes, only one should be used
B. No, they are often used together
C. Pandas replaces all NumPy functionality
D. NumPy cannot work with Pandas

---

# 🏁 Chapter 22 — COMPLETE

You now understand the important relationship:

**NumPy Array ↔ Pandas Series ↔ Pandas DataFrame**

and how NumPy can perform numerical calculations while Pandas manages tabular Data Science workflows.

---

## 🚀 Next → Chapter 23 — NumPy Projects

This is the **final chapter of your NumPy syllabus**.

We will build projects from:

```text
🟢 Beginner
   ↓
Student Marks Analysis

🟡 Intermediate
   ↓
Sales Analysis
Employee Salary Analysis
Temperature Analysis

🔴 Advanced
   ↓
Statistical Data Analysis
Simple Image Processing
Complete Data Science-style NumPy Project
```

Each project will include:

**Problem → Dataset → Requirements → Step-by-step code → Output → Explanation → Concepts used → Practice → Interview questions → Final project summary**

Type **NEXT** when ready.
