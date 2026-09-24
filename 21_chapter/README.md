# 🚀 Chapter 21 — NumPy for Data Science

Welcome to **Chapter 21**! 🎯

You have now learned NumPy fundamentals, including:

```text
Arrays
 ↓
Indexing
 ↓
Slicing
 ↓
Operations
 ↓
Statistics
 ↓
Reshaping
 ↓
Joining / Splitting
 ↓
Broadcasting
 ↓
Boolean Masking
 ↓
Random
 ↓
Linear Algebra
 ↓
Missing Values
 ↓
Data Types
 ↓
Advanced NumPy
```

Now we connect NumPy to **real Data Science work**. 📊🤖

---

# 📚 What We Will Learn

1. 🔹 NumPy in Data Science
2. 🔹 Data preprocessing
3. 🔹 Numerical calculations
4. 🔹 Statistics
5. 🔹 Feature engineering
6. 🔹 Normalization
7. 🔹 Machine Learning connection
8. 🔹 Image processing
9. 🔹 Scientific computing
10. 🔹 Real-world dataset example
11. 🔹 Complete VS Code practice
12. 🔹 Common mistakes
13. 🔹 Interview questions
14. 🔹 Mini project
15. 🔹 Summary
16. 🔹 Quiz

---

# 1️⃣ Why Is NumPy Important in Data Science?

Data Science involves a lot of numerical data.

For example:

```text
Age       Salary      Experience
25        40000       2
30        55000       5
28        48000       3
35        75000       10
```

A Data Scientist may need to:

* calculate averages
* clean data
* normalize values
* calculate statistics
* transform features
* perform mathematical operations
* prepare data for Machine Learning

NumPy provides efficient numerical operations for these tasks.

---

# 2️⃣ NumPy's Role in the Data Science Ecosystem

A simplified Data Science workflow:

```text
             DATA
               ↓
        ┌──────────────┐
        │ NumPy        │
        │ Numerical    │
        │ Processing   │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Pandas       │
        │ Tabular Data │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Visualization│
        │ Matplotlib   │
        │ Seaborn      │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Machine      │
        │ Learning     │
        └──────────────┘
```

NumPy is one of the foundational numerical libraries in the Python Data Science ecosystem.

---

# 3️⃣ Data Preprocessing

### 📌 Definition

**Data preprocessing** means preparing raw data before analysis or Machine Learning.

Raw data may contain:

```text
Missing values
Different scales
Invalid values
Wrong data types
Outliers
```

NumPy can help with many numerical preprocessing operations.

---

# 4️⃣ Example Dataset

Let's create a simple employee dataset.

```python
import numpy as np

employees = np.array([
    [101, 25, 40000],
    [102, 30, 55000],
    [103, 28, 48000],
    [104, 35, 75000],
    [105, 40, 90000]
])

print(employees)
```

Output:

```text
[[  101    25 40000]
 [  102    30 55000]
 [  103    28 48000]
 [  104    35 75000]
 [  105    40 90000]]
```

Columns:

```text
Column 0 → Employee ID
Column 1 → Age
Column 2 → Salary
```

---

# 5️⃣ Extracting Features

In Machine Learning, input variables are often called **features**.

Let's extract age:

```python
age = employees[:, 1]

print(age)
```

Output:

```text
[25 30 28 35 40]
```

Salary:

```python
salary = employees[:, 2]

print(salary)
```

Output:

```text
[40000 55000 48000 75000 90000]
```

---

# ⭐ Important Concept

Think:

```text
Dataset
   │
   ├── ID       → identifier
   │
   ├── Age      → feature
   │
   └── Salary   → feature / target depending on the task
```

Whether a column is called a **feature** or **target** depends on the Machine Learning problem.

---

# 6️⃣ Numerical Calculations

NumPy makes numerical calculations simple.

### Average salary

```python
average_salary = np.mean(salary)

print(average_salary)
```

Output:

```text
61600.0
```

### Minimum salary

```python
print(np.min(salary))
```

Output:

```text
40000
```

### Maximum salary

```python
print(np.max(salary))
```

Output:

```text
90000
```

### Standard deviation

```python
print(np.std(salary))
```

This tells us how spread out the salaries are around the mean.

---

# 7️⃣ Statistical Analysis

Suppose:

```python
marks = np.array([
    65,
    70,
    80,
    85,
    90,
    95
])
```

We can calculate:

```python
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))
```

This is basic **descriptive statistics**.

---

# 8️⃣ Data Preprocessing — Handling Missing Values

Suppose:

```python
salary = np.array([
    40000,
    55000,
    np.nan,
    75000,
    90000
])
```

We can detect missing values:

```python
print(np.isnan(salary))
```

Output:

```text
[False False  True False False]
```

Count them:

```python
print(np.sum(np.isnan(salary)))
```

Output:

```text
1
```

Calculate mean ignoring missing values:

```python
mean_salary = np.nanmean(salary)

print(mean_salary)
```

Output:

```text
65000.0
```

---

# 9️⃣ Replacing Missing Values

We can replace the missing salary with the mean.

```python
salary[np.isnan(salary)] = np.nanmean(salary)

print(salary)
```

Output:

```text
[40000. 55000. 65000. 75000. 90000.]
```

### Flow

```text
Missing data
     ↓
np.isnan()
     ↓
Find NaN
     ↓
np.nanmean()
     ↓
Calculate mean
     ↓
Replace NaN
```

---

# 🔟 Feature Scaling

This is a very important Machine Learning concept.

Suppose we have:

```text
Age:
25
30
35
40
```

and:

```text
Salary:
40000
55000
75000
90000
```

These features have very different numerical scales.

Some Machine Learning algorithms can benefit from putting features on comparable scales.

NumPy can help perform these transformations.

---

# 1️⃣1️⃣ Min-Max Normalization ⭐

A common formula is:

$$
x_{normalized} = \frac{x - x_{min}}{x_{max} - x_{min}}
$$

This transforms values approximately into:

```text
0 → minimum
1 → maximum
```

---

# 🧮 Dry Run

Suppose:

```text
Age = [20, 30, 40]
```

Minimum:

```text
20
```

Maximum:

```text
40
```

For `30`:

```text
(30 - 20)
-----------
(40 - 20)

= 10 / 20

= 0.5
```

Therefore:

```text
20
```
------
------
# 🚀 Chapter 21 — NumPy for Data Science — Part 2

We stopped at **Min-Max Normalization**. Let's continue from there and complete Chapter 21.

---

# 1️⃣2️⃣ Min-Max Normalization with NumPy

Suppose:

```python
import numpy as np

age = np.array([20, 30, 40, 50])
```

Formula:

```text
normalized = (x - minimum) / (maximum - minimum)
```

NumPy:

```python
minimum = np.min(age)
maximum = np.max(age)

normalized_age = (age - minimum) / (maximum - minimum)

print(normalized_age)
```

Output:

```text
[0.         0.33333333 0.66666667 1.        ]
```

### 🧠 Dry Run

```text
20 → (20-20)/(50-20) = 0
30 → (30-20)/(50-20) = 0.333
40 → (40-20)/(50-20) = 0.667
50 → (50-20)/(50-20) = 1
```

So:

```text
Original       Normalized

20       →       0.00
30       →       0.33
40       →       0.67
50       →       1.00
```

### ⭐ Why NumPy is useful here

Notice:

```python
(age - minimum)
```

works on the **entire array**.

No `for` loop is required.

This is **vectorization** from Chapter 20.

---

# 1️⃣3️⃣ Standardization

Another common transformation is **standardization**.

Formula:

$$
z = \frac{x-\mu}{\sigma}
$$

Where:

```text
x  → individual value
μ  → mean
σ  → standard deviation
```

Example:

```python
import numpy as np

marks = np.array([
    60,
    70,
    80,
    90,
    100
])

mean = np.mean(marks)
std = np.std(marks)

standardized = (marks - mean) / std

print(standardized)
```

Output will be approximately:

```text
[-1.41421356 -0.70710678  0.          0.70710678  1.41421356]
```

### 🧠 Interpretation

Values:

```text
below average → negative
average        → around 0
above average  → positive
```

---

# 1️⃣4️⃣ Feature Engineering

### 📌 Definition

**Feature engineering** means creating useful input variables from existing data.

Suppose we have:

```python
hours = np.array([
    2,
    4,
    6,
    8
])
```

Maybe we want:

```text
study hours²
```

We can create:

```python
hours_squared = hours ** 2

print(hours_squared)
```

Output:

```text
[ 4 16 36 64]
```

This is a simple example of creating a new feature.

---

# 1️⃣5️⃣ Another Feature Engineering Example

Suppose:

```python
height = np.array([
    1.60,
    1.70,
    1.80,
    1.75
])

weight = np.array([
    55,
    65,
    80,
    72
])
```

We can calculate BMI:

$$
BMI = \frac{weight}{height^2}
$$

NumPy:

```python
bmi = weight / (height ** 2)

print(bmi)
```

Output will be approximately:

```text
[21.48 22.49 24.69 23.51]
```

### ⭐ Important

This is a very good example of:

```text
NumPy
 ↓
Vectorization
 ↓
Mathematical formula
 ↓
New feature
```

---

# 1️⃣6️⃣ Conditional Feature Creation

Suppose we have:

```python
marks = np.array([
    35,
    55,
    72,
    90
])
```

We want:

```text
marks >= 50 → Pass
marks < 50  → Fail
```

Use:

```python
result = np.where(
    marks >= 50,
    "Pass",
    "Fail"
)

print(result)
```

Output:

```text
['Fail' 'Pass' 'Pass' 'Pass']
```

This connects:

```text
Chapter 12 → np.where()
Chapter 15 → Boolean Masking
Chapter 20 → Vectorization
```

---

# 1️⃣7️⃣ NumPy in Machine Learning 🤖

Machine Learning models generally work with numerical data.

Suppose:

```text
Age    Experience
25       2
30       5
35       8
40      10
```

We can represent the features as:

```python
X = np.array([
    [25, 2],
    [30, 5],
    [35, 8],
    [40, 10]
])

print(X)
```

Output:

```text
[[25  2]
 [30  5]
 [35  8]
 [40 10]]
```

Here:

```text
X
↓
Input features
```

---

# 1️⃣8️⃣ What is `X`?

In Machine Learning, a common convention is:

```text
X → input features
y → target/output
```

Example:

```python
X = np.array([
    [25, 2],
    [30, 5],
    [35, 8],
    [40, 10]
])

y = np.array([
    40000,
    55000,
    70000,
    85000
])
```

Visual:

```text
             Machine Learning Data

X                              y
Features                       Target
   ↓                             ↓

Age   Experience              Salary
25       2                    40000
30       5                    55000
35       8                    70000
40      10                    85000
```

A Machine Learning algorithm can learn a relationship between `X` and `y`.

---

# 1️⃣9️⃣ Shape of Machine Learning Data

Check:

```python
print(X.shape)
```

Output:

```text
(4, 2)
```

Meaning:

```text
4 → samples/rows
2 → features/columns
```

For:

```python
print(y.shape)
```

Output:

```text
(4,)
```

So:

```text
X → 4 samples × 2 features
y → 4 target values
```

### ⭐ Remember

A common Machine Learning structure is:

```text
X.shape = (number_of_samples, number_of_features)
```

---

# 2️⃣0️⃣ NumPy + Linear Algebra in ML

Suppose:

```python
X = np.array([
    [1, 2],
    [3, 4]
])

weights = np.array([
    0.5,
    2.0
])
```

We can calculate:

```python
prediction = X @ weights

print(prediction)
```

Dry run:

First row:

```text
1 × 0.5 + 2 × 2
= 0.5 + 4
= 4.5
```

Second row:

```text
3 × 0.5 + 4 × 2
= 1.5 + 8
= 9.5
```

Output:

```text
[4.5 9.5]
```

### 🔥 This connects Chapter 17 directly to Machine Learning.

```text
NumPy arrays
     ↓
Matrix multiplication
     ↓
Predictions
```

---

# 2️⃣1️⃣ Image Processing 🖼️

An image can be represented numerically.

For a simple grayscale image:

```text
0 → black
255 → white
```

Example:

```python
image = np.array([
    [0,   50,  100],
    [150, 200, 255],
    [100, 150, 200]
])

print(image)
```

Output:

```text
[[  0  50 100]
 [150 200 255]
 [100 150 200]]
```

This is essentially a **2D numerical array**.

---

# 2️⃣2️⃣ Image Brightness

Suppose we want to increase brightness by `30`.

```python
brighter = image + 30

print(brighter)
```

Output:

```text
[[ 30  80 130]
 [180 230 285]
 [130 180 230]]
```

But there is a problem:

```text
285
```

is outside the normal 8-bit grayscale range:

```text
0–255
```

So we can use:

```python
brighter = np.clip(image + 30, 0, 255)

print(brighter)
```

Output:

```text
[[ 30  80 130]
 [180 230 255]
 [130 180 230]]
```

### ⭐ `np.clip()`

Syntax:

```python
np.clip(array, minimum, maximum)
```

It keeps values inside the specified range.

---

# 2️⃣3️⃣ Image Thresholding

Suppose:

```python
image = np.array([
    [20, 80, 150],
    [200, 50, 240]
])
```

We want:

```text
value >= 100 → 255
value < 100  → 0
```

Use:

```python
result = np.where(
    image >= 100,
    255,
    0
)

print(result)
```

Output:

```text
[[  0   0 255]
 [255   0 255]]
```

This is a simple example of **image thresholding**.

---

# 2️⃣4️⃣ Scientific Computing 🔬

NumPy is also used for scientific calculations.

Example:

```python
time = np.linspace(0, 10, 6)

print(time)
```

Output:

```text
[ 0.  2.  4.  6.  8. 10.]
```

Suppose:

$$
distance = velocity \times time
$$

```python
velocity = 5

distance = velocity * time

print(distance)
```

Output:

```text
[ 0. 10. 20. 30. 40. 50.]
```

No loop is required.

---

# 2️⃣5️⃣ Working With Mathematical Functions

Suppose we want values of:

$$
y = \sin(x)
$$

NumPy:

```python
x = np.linspace(0, 2 * np.pi, 5)

y = np.sin(x)

print(x)
print(y)
```

Output will be approximately:

```text
[0.         1.57079633 3.14159265 4.71238898 6.28318531]

[ 0.0000000e+00  1.0000000e+00  1.2246468e-16 -1.0000000e+00
 -2.4492936e-16]
```

The tiny values close to zero are due to floating-point numerical representation.

---

# 2️⃣6️⃣ Data Cleaning With NumPy

Suppose:

```python
data = np.array([
    10,
    20,
    np.nan,
    40,
    np.inf,
    60
])
```

Find valid values:

```python
clean = data[np.isfinite(data)]

print(clean)
```

Output:

```text
[10. 20. 40. 60.]
```

Flow:

```text
Raw Data
   ↓
NaN / Infinity
   ↓
np.isfinite()
   ↓
Valid numerical data
```

---

# 2️⃣7️⃣ Outlier Detection

NumPy can also help identify unusually high or low values.

A simple method uses the **Z-score**.

Formula:

$$
z = \frac{x-\mu}{\sigma}
$$

Example:

```python
salary = np.array([
    40000,
    42000,
    45000,
    46000,
    48000,
    200000
])

mean = np.mean(salary)
std = np.std(salary)

z_scores = (salary - mean) / std

print(z_scores)
```

You can then inspect unusually large absolute Z-scores:

```python
outliers = salary[np.abs(z_scores) > 2]

print(outliers)
```

Output may identify:

```text
[200000]
```

### ⚠️ Important

This is only **one possible outlier-detection method**. The appropriate method depends on the dataset and assumptions.

---

# 2️⃣8️⃣ Complete Data Science Workflow

Now combine what you've learned.

```text
                  RAW DATA
                     ↓
              NumPy Array
                     ↓
             Check Data Type
                     ↓
            Missing Values?
                ↙       ↘
              Yes        No
               ↓          ↓
          Clean Data      │
               └────┬─────┘
                    ↓
             Numerical Analysis
                    ↓
             Feature Engineering
                    ↓
               Scaling
              ↙      ↘
        Normalization  Standardization
              ↓          ↓
                 Features
                    ↓
             Machine Learning
```

---

# 2️⃣9️⃣ Complete Data Science Example

Let's create a small employee dataset.

```python
import numpy as np


# ============================================================
# 1. CREATE DATA
# ============================================================

data = np.array([
    [101, 25, 40000],
    [102, 30, 55000],
    [103, 28, 48000],
    [104, 35, 75000],
    [105, 40, 90000]
], dtype=float)


print("Employee Data:")
print(data)


# ============================================================
# 2. EXTRACT FEATURES
# ============================================================

age = data[:, 1]
salary = data[:, 2]


print("\nAge:")
print(age)

print("\nSalary:")
print(salary)


# ============================================================
# 3. BASIC STATISTICS
# ============================================================

print("\nAverage Age:")
print(np.mean(age))

print("\nAverage Salary:")
print(np.mean(salary))

print("\nMinimum Salary:")
print(np.min(salary))

print("\nMaximum Salary:")
print(np.max(salary))

print("\nSalary Standard Deviation:")
print(np.std(salary))


# ============================================================
# 4. MIN-MAX NORMALIZATION
# ============================================================

salary_min = np.min(salary)
salary_max = np.max(salary)

normalized_salary = (
    (salary - salary_min)
    / (salary_max - salary_min)
)

print("\nNormalized Salary:")
print(normalized_salary)


# ============================================================
# 5. STANDARDIZATION
# ============================================================

salary_mean = np.mean(salary)
salary_std = np.std(salary)

standardized_salary = (
    (salary - salary_mean)
    / salary_std
)

print("\nStandardized Salary:")
print(standardized_salary)


# ============================================================
# 6. FILTER HIGH SALARY
# ============================================================

high_salary = salary[salary > 50000]

print("\nSalary Above 50000:")
print(high_salary)


# ============================================================
# 7. FEATURE ENGINEERING
# ============================================================

salary_in_lakhs = salary / 100000

print("\nSalary in Lakhs:")
print(salary_in_lakhs)


# ============================================================
# 8. SALARY INCREASE
# ============================================================

updated_salary = salary.copy()

updated_salary[updated_salary > 50000] *= 1.10

print("\nUpdated Salary:")
print(updated_salary)
```

---

# 3️⃣0️⃣ What Did We Use?

This one program combines many previous chapters:

```text
Chapter 3  → shape / dtype
Chapter 4  → indexing
Chapter 6  → operations
Chapter 8  → statistics
Chapter 15 → Boolean masking
Chapter 18 → missing-value concepts
Chapter 19 → dtype
Chapter 20 → vectorization
Chapter 21 → Data Science workflow
```

This is exactly why learning NumPy chapter-by-chapter is useful.

---

# 3️⃣1️⃣ NumPy in Machine Learning

A simplified Machine Learning workflow:

```text
Dataset
   ↓
NumPy / Pandas
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Feature Scaling
   ↓
X and y
   ↓
Machine Learning Algorithm
   ↓
Prediction
   ↓
Evaluation
```

For example:

```python
X = np.array([
    [25, 2],
    [30, 5],
    [35, 8],
    [40, 10]
])

y = np.array([
    40000,
    55000,
    70000,
    85000
])
```

NumPy helps represent and transform the numerical data.

Libraries such as **scikit-learn** then provide many Machine Learning algorithms and preprocessing tools.

---

# 3️⃣2️⃣ NumPy in Image Processing

A simplified image workflow:

```text
Image
 ↓
Numerical Array
 ↓
NumPy
 ↓
Resize / Crop / Filter / Transform
 ↓
Processed Image
```

For RGB images, the data is commonly represented conceptually as:

```text
Height × Width × Channels
```

For example:

```text
(720, 1280, 3)
```

means:

```text
720 pixels high
1280 pixels wide
3 color channels
```

---

# 3️⃣3️⃣ NumPy in Scientific Computing

Examples include:

* 🔬 Physics
* 🧪 Chemistry
* 🌡️ Temperature analysis
* 🌊 Engineering simulations
* 📈 Numerical modeling
* 🛰️ Scientific measurements

Typical operations:

```text
Arrays
+
Mathematics
+
Statistics
+
Linear Algebra
=
Scientific Computing
```

---

# 3️⃣4️⃣ Common Mistakes

### ❌ Mistake 1 — Using loops for everything

Instead of:

```python
for x in arr:
    ...
```

check whether NumPy already supports the operation directly.

For example:

```python
arr * 2
```

---

### ❌ Mistake 2 — Forgetting shapes

Before Machine Learning calculations:

```python
print(X.shape)
```

is often useful.

---

### ❌ Mistake 3 — Mixing incompatible shapes

Always check:

```python
print(arr.shape)
```

before matrix operations or broadcasting.

---

### ❌ Mistake 4 — Blindly normalizing data

Scaling should be chosen based on the Machine Learning algorithm and the nature of the data.

---

### ❌ Mistake 5 — Replacing missing values without understanding them

For example:

```python
NaN → 0
```

is not automatically correct.

The appropriate treatment depends on what the missing value means.

---

# 🎤 Interview Questions

### Q1. Why is NumPy important in Data Science?

**Answer:**
NumPy provides efficient multidimensional arrays and numerical operations used for data processing, statistics, linear algebra, scientific computing, and as a foundation for many Python data tools.

---

### Q2. What is vectorization?

**Answer:**
Vectorization performs an operation on an entire array without requiring an explicit Python-level loop for each element.

---

### Q3. What is feature engineering?

**Answer:**
Feature engineering is the process of creating or transforming input variables to make them useful for analysis or Machine Learning.

---

### Q4. What is normalization?

**Answer:**
Normalization transforms numerical values to a common range. Min-Max normalization commonly maps values to approximately `0–1`.

---

### Q5. What is standardization?

**Answer:**
Standardization transforms values using:

```text
(x - mean) / standard deviation
```

so the transformed values are centered around zero.

---

### Q6. What is `X` in Machine Learning?

**Answer:**
`X` commonly represents the input feature matrix.

---

### Q7. What is `y`?

**Answer:**
`y` commonly represents the target/output variable.

---

### Q8. How can NumPy represent an image?

**Answer:**
An image can be represented as a numerical array. A grayscale image can use a 2D array, while a color image commonly uses a 3D array with height, width, and color channels.

---

### Q9. How can NumPy detect missing numerical values?

```python
np.isnan(arr)
```

---

### Q10. What is the purpose of `np.clip()`?

**Answer:**
It limits values to a specified minimum and maximum range.

Example:

```python
np.clip(arr, 0, 255)
```

---

# 💻 Practice Questions

## Practice 1 — Statistics

Given:

```python
marks = np.array([
    55, 65, 70, 80, 90, 95
])
```

Find:

```text
Mean
Median
Minimum
Maximum
Standard deviation
```

---

## Practice 2 — Normalization

Given:

```python
salary = np.array([
    30000,
    40000,
    50000,
    60000,
    70000
])
```

Perform Min-Max normalization.

---

## Practice 3 — Feature Engineering

Given:

```python
hours = np.array([
    2,
    4,
    6,
    8,
    10
])
```

Create:

```text
hours²
```

using vectorization.

---

## Practice 4 — Image

Create:

```python
image = np.array([
    [0, 50, 100],
    [150, 200, 255],
    [30, 80, 120]
])
```

Increase brightness by `40` but keep all values between `0` and `255`.

Hint:

```python
np.clip()
```

---

# 🧩 Mini Project — Employee Data Science Analysis

Create:

```python
employees = np.array([
    [101, 25, 40000],
    [102, 30, 55000],
    [103, 28, 48000],
    [104, 35, 75000],
    [105, 40, 90000],
    [106, 45, 120000]
], dtype=float)
```

Columns:

```text
Employee ID
Age
Salary
```

### Task 1

Extract:

```python
age
salary
```

### Task 2

Find:

```text
Average age
Average salary
Minimum salary
Maximum salary
```

### Task 3

Find employees whose salary is greater than `60000`.

### Task 4

Increase salaries above `60000` by 10%.

### Task 5

Normalize salary using Min-Max normalization.

### Task 6

Standardize salary using:

```text
(x - mean) / std
```

### Task 7

Convert salary into lakhs:

```text
salary / 100000
```

### Task 8

Print the final results.

---

# 🧠 Chapter 21 Memory Map

```text
                    NUMPY
                      │
                      ↓
                DATA SCIENCE
                      │
        ┌─────────────┼──────────────┐
        ↓             ↓              ↓
   Preprocessing   Statistics    Mathematics
        │             │              │
        ↓             ↓              ↓
 Missing values    Mean          Linear algebra
 Filtering         Median        Matrix operations
 Scaling            Std           Vectorization
        │
        ↓
 Feature Engineering
        │
        ↓
       X / y
        │
        ↓
 Machine Learning
```

---

# ⭐ Final Summary

| Data Science Task    | NumPy Concept                     |
| -------------------- | --------------------------------- |
| Numerical data       | `np.array()`                      |
| Filtering            | Boolean masking                   |
| Missing values       | `np.isnan()`                      |
| Valid values         | `np.isfinite()`                   |
| Statistics           | `mean`, `median`, `std`, etc.     |
| Normalization        | Vectorized arithmetic             |
| Standardization      | Vectorized arithmetic             |
| Feature engineering  | Array operations                  |
| ML features          | 2D NumPy arrays                   |
| ML target            | 1D NumPy array                    |
| Matrix calculations  | `@`, `np.matmul()`                |
| Image representation | 2D/3D arrays                      |
| Image range control  | `np.clip()`                       |
| Scientific computing | Vectorized mathematical functions |
| Performance          | Vectorization                     |

---

# 🔥 Most Important Concepts

```text
1️⃣ NumPy → numerical foundation

2️⃣ Vectorization → fast array operations

3️⃣ Boolean masking → filtering

4️⃣ Statistics → understand data

5️⃣ Normalization → common scale

6️⃣ Standardization → mean-centered scale

7️⃣ Feature engineering → create useful features

8️⃣ X → input features

9️⃣ y → target

🔟 Image → numerical array
```

---

# 🧪 Chapter 21 Quiz

### Q1. What is NumPy mainly used for?

A. Web development
B. Numerical computing
C. HTML design
D. Database administration

### Q2. What does `X` commonly represent in Machine Learning?

A. Target
B. Input features
C. File name
D. Model name

### Q3. What does `y` commonly represent?

A. Input features
B. Target/output
C. Array shape
D. dtype

### Q4. What is Min-Max normalization commonly used for?

A. Sorting
B. Scaling values to a common range
C. Removing columns
D. Creating strings

### Q5. What is the formula for Min-Max normalization?

A.

```text
x + mean
```

B.

```text
(x - min) / (max - min)
```

C.

```text
x × std
```

D.

```text
x / mean
```

### Q6. What is standardization?

A. `(x - mean) / std`
B. `x + max`
C. `x × min`
D. `x / max`

### Q7. Which function limits values to a range?

A. `np.where()`
B. `np.clip()`
C. `np.reshape()`
D. `np.sort()`

### Q8. A grayscale image can commonly be represented as:

A. 1D array only
B. 2D numerical array
C. String only
D. Boolean only

### Q9. What is feature engineering?

A. Deleting all features
B. Creating or transforming useful features
C. Installing NumPy
D. Sorting an array

### Q10. Which NumPy concept is heavily used in numerical Data Science?

A. Vectorization
B. HTML
C. CSS
D. DOM

---

# 🏁 Chapter 21 — COMPLETE

You have now connected NumPy with real Data Science:

**Data preprocessing → Statistics → Scaling → Feature Engineering → Machine Learning → Image Processing → Scientific Computing**

### 🚀 Next → Chapter 22 — NumPy + Pandas

We will learn:

```text
NumPy Array
     ↓
Pandas Series
     ↓
Pandas DataFrame
     ↓
NumPy ↔ Pandas conversion
     ↓
When to use NumPy
     ↓
When to use Pandas
     ↓
Real-world Data Science workflow
     ↓
Practice + Mini Project + Quiz
```

Type **NEXT** when ready.

