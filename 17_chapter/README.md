# 🚀 Chapter 17 — NumPy Linear Algebra

Welcome to **Chapter 17**! 🎯

Don't worry if you don't know advanced mathematics. We will learn only the mathematics needed for NumPy, step by step.

---

# 📚 What We Will Learn

In this chapter:

1. 🔹 What is a Matrix?
2. 🔹 Matrix shape
3. 🔹 Matrix addition
4. 🔹 Matrix multiplication
5. 🔹 `np.dot()`
6. 🔹 `np.matmul()`
7. 🔹 `@` operator
8. 🔹 Matrix inverse — `np.linalg.inv()`
9. 🔹 Determinant — `np.linalg.det()`
10. 🔹 Eigenvalues & Eigenvectors — `np.linalg.eig()`
11. 🔹 Solving equations — `np.linalg.solve()`
12. 🔹 Real-world examples
13. 🔹 Common mistakes
14. 🔹 Interview questions
15. 🔹 Practice
16. 🔹 Quiz

---

# 1️⃣ What is a Matrix?

### 📌 Definition

A **matrix** is a rectangular collection of numbers arranged in:

* Rows
* Columns

Example:

```text
        Columns
         ↓
       10  20  30
       40  50  60
Rows → 70  80  90
```

In NumPy:

```python
import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix)
```

### Output

```text
[[10 20 30]
 [40 50 60]
 [70 80 90]]
```

---

# 2️⃣ Matrix Shape

Let's check the shape:

```python
print(matrix.shape)
```

Output:

```text
(3, 3)
```

This means:

```text
3 rows
3 columns
```

### 🧠 Remember

```text
shape = (rows, columns)
```

For:

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Shape:

```text
(2, 3)
```

Visual:

```text
       C1   C2   C3
       ↓    ↓    ↓
R1 →  10   20   30
R2 →  40   50   60
```

So:

```text
2 rows × 3 columns
```

---

# 3️⃣ Matrix Addition

Matrix addition is simple.

Suppose:

```text
A =  10  20
     30  40

B =  1   2
     3   4
```

Add corresponding positions:

```text
10 + 1 = 11
20 + 2 = 22
30 + 3 = 33
40 + 4 = 44
```

Result:

```text
11  22
33  44
```

### Python

```python
import numpy as np

A = np.array([
    [10, 20],
    [30, 40]
])

B = np.array([
    [1, 2],
    [3, 4]
])

result = A + B

print(result)
```

### Output

```text
[[11 22]
 [33 44]]
```

### ⚠️ Important

For normal matrix addition, the arrays need compatible shapes.

---

# 4️⃣ Matrix Multiplication ⭐

This is one of the **most important concepts** in Linear Algebra.

Matrix multiplication is **different from element-wise multiplication**.

Consider:

```text
A =  1  2
     3  4

B =  5  6
     7  8
```

Matrix multiplication:

```text
A × B
```

We calculate each result element using **row × column**.

### First element

```text
(1 × 5) + (2 × 7)

= 5 + 14

= 19
```

### Second element

```text
(1 × 6) + (2 × 8)

= 6 + 16

= 22
```

### Third element

```text
(3 × 5) + (4 × 7)

= 15 + 28

= 43
```

### Fourth element

```text
(3 × 6) + (4 × 8)

= 18 + 32

= 50
```

Therefore:

```text
     19  22
     43  50
```

---

# 🧮 Visual Dry Run

```text
A                     B

1  2                   5  6
3  4                   7  8

Row 1 × Column 1

[1  2] × [5]
         [7]

= 1×5 + 2×7
= 19
```

Then:

```text
[1  2] × [6]
         [8]

= 1×6 + 2×8
= 22
```

So first row becomes:

```text
19  22
```

---

# 5️⃣ `np.dot()`

NumPy provides:

```python
np.dot()
```

for dot products and matrix multiplication in common 2D cases.

Example:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = np.dot(A, B)

print(result)
```

Output:

```text
[[19 22]
 [43 50]]
```

---

# 6️⃣ `np.matmul()`

NumPy also provides:

```python
np.matmul()
```

Example:

```python
result = np.matmul(A, B)

print(result)
```

Output:

```text
[[19 22]
 [43 50]]
```

---

# 7️⃣ `@` Operator ⭐

Python provides a special operator for matrix multiplication:

```python
@
```

Example:

```python
result = A @ B

print(result)
```

Output:

```text
[[19 22]
 [43 50]]
```

### 🧠 Important Comparison

| Operation         | Meaning                     |
| ----------------- | --------------------------- |
| `A * B`           | Element-wise multiplication |
| `np.dot(A, B)`    | Dot/matrix multiplication   |
| `np.matmul(A, B)` | Matrix multiplication       |
| `A @ B`           | Matrix multiplication       |

---

# 8️⃣ `*` vs `@` ⭐⭐⭐

This is a **very important interview question**.

Consider:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
```

### `A * B`

Each position is multiplied:

```text
1×5   2×6
3×7   4×8
```

Result:

```text
[[ 5 12]
 [21 32]]
```

### `A @ B`

Matrix multiplication:

```text
[[19 22]
 [43 50]]
```

### 🧠 Memory Trick

> `*` → **same position**

> `@` → **row × column**

---

# 9️⃣ Matrix Multiplication Rule ⭐⭐⭐

This is very important.

Suppose:

```text
A = 2 × 3
B = 3 × 4
```

Matrix multiplication is possible because:

```text
2 × 3
    ↓
    3 × 4
    ↑
same
```

The **inside numbers must match**.

Result shape:

```text
2 × 4
```

### General Rule

```text
(m × n) @ (n × p)
          ↓
       (m × p)
```

### Example

```text
(2 × 3) @ (3 × 4)

        ↓

(2 × 4)
```

---

# 🔟 Example with 2 × 3 and 3 × 2

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

result = A @ B

print(result)
```

### Shape

```text
A → (2, 3)

B → (3, 2)
```

Therefore:

```text
Result → (2, 2)
```

### Dry Run

First value:

```text
1×10 + 2×30 + 3×50

= 10 + 60 + 150

= 220
```

Second:

```text
1×20 + 2×40 + 3×60

= 20 + 80 + 180

= 280
```

Third:

```text
4×10 + 5×30 + 6×50

= 40 + 150 + 300

= 490
```

Fourth:

```text
4×20 + 5×40 + 6×60

= 80 + 200 + 360

= 640
```

Output:

```text
[[220 280]
 [490 640]]
```

---

# 1️⃣1️⃣ Matrix Inverse

Now we move to another important concept.

### 📌 What is an inverse?

For a matrix `A`, its inverse is written as:

```text
A⁻¹
```

The important relationship is:

```text
A × A⁻¹ = I
```

where `I` is the **identity matrix**.

For example:

```text
I = 1  0
    0  1
```

Think of the identity matrix as the matrix equivalent of the number `1` in this context.

---

# 1️⃣2️⃣ `np.linalg.inv()`

NumPy provides:

```python
np.linalg.inv()
```

Example:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

inverse = np.linalg.inv(A)

print(inverse)
```

Output approximately:

```text
[[-2.   1. ]
 [ 1.5 -0.5]]
```

Now verify:

```python
result = A @ inverse

print(result)
```

Output approximately:

```text
[[1. 0.]
 [0. 1.]]
```

So:

```text
A × A⁻¹ ≈ I
```

---

# ⚠️ Important: Not Every Matrix Has an Inverse

A matrix must satisfy certain mathematical conditions to have an inverse.

For a square matrix, the determinant must be **non-zero**.

We will learn determinant next.

---

# 1️⃣3️⃣ Determinant

The determinant is a special number calculated from a square matrix.

For a 2 × 2 matrix:

```text
A = a  b
    c  d
```

The determinant is:

```text
det(A) = (a × d) - (b × c)
```

---

# 🧮 Dry Run

Consider:

```text
A = 1  2
    3  4
```

Therefore:

```text
a = 1
b = 2
c = 3
d = 4
```

Formula:

```text
det(A) = (a × d) - (b × c)
```

Substitute:

```text
= (1 × 4) - (2 × 3)

= 4 - 6

= -2
```

So:

```text
det(A) = -2
```

---

# 1️⃣4️⃣ `np.linalg.det()`

NumPy provides:

```python
np.linalg.det()
```

Example:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

det = np.linalg.det(A)

print(det)
```

Output:

```text
-2.0000000000000004
```

You may see a tiny floating-point difference instead of exactly `-2`.

For practical display:

```python
print(round(det))
```

Output:

```text
-2
```

---

# 🔑 Determinant and Inverse Relationship

Remember:

```text
det(A) != 0
        ↓
inverse can exist
```

If:

```text
det(A) = 0
```

the matrix is **singular**, so it does not have an ordinary inverse.

---

# 1️⃣5️⃣ Eigenvalues and Eigenvectors

Don't worry — we will keep this beginner-friendly.

NumPy provides:

```python
np.linalg.eig()
```

An eigenvalue/eigenvector pair satisfies:

```text
A × v = λ × v
```

Where:

```text
A = matrix
v = eigenvector
λ = eigenvalue
```

The important idea is:

> When matrix `A` acts on an eigenvector `v`, the direction of `v` remains the same; it is scaled by `λ`.

---

# 🧮 Simple Example

```python
import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)
```

Typical output:

```text
Eigenvalues:
[2. 3.]
```

The exact signs/orientation of eigenvectors can vary, because an eigenvector can be multiplied by `-1` and still represent the same eigenvector direction.

For this diagonal matrix, the eigenvector directions correspond to the coordinate axes.

---

# 1️⃣6️⃣ Why Are Eigenvalues Important?

Eigenvalues and eigenvectors appear in:

* 🤖 Machine Learning
* 📊 PCA
* 🖼️ Image processing
* 🔬 Scientific computing
* 📈 Data analysis
* 🧮 Mathematical modeling

You do **not** need to master the full mathematical theory before using the NumPy function.

At this stage, remember:

```text
np.linalg.eig()
       ↓
Eigenvalues + Eigenvectors
```

---

# 1️⃣7️⃣ Solving Linear Equations ⭐

This is one of the most useful practical applications.

Suppose:

```text
2x + y = 5

x + 3y = 6
```

We can represent this as:

```text
A × X = B
```

Where:

```text
A = [2  1]
    [1  3]

X = [x]
    [y]

B = [5]
    [6]
```

---

# 1️⃣8️⃣ `np.linalg.solve()`

NumPy provides:

```python
np.linalg.solve(A, B)
```

Example:

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([
    5,
    6
])

solution = np.linalg.solve(A, B)

print(solution)
```

Output:

```text
[1.8 1.4]
```

Therefore:

```text
x = 1.8
y = 1.4
```

---

# 🧮 Verify the Answer

Let's verify:

```text
2x + y

= 2(1.8) + 1.4

= 3.6 + 1.4

= 5
```

Correct ✅

Second equation:

```text
x + 3y

= 1.8 + 3(1.4)

= 1.8 + 4.2

= 6
```

Correct ✅

---

# 🌍 Real-World Example

Imagine a business has two products:

```text
Product A
Product B
```

You know the total number of products sold and total revenue.

You can create equations such as:

```text
price_A × quantity_A
+
price_B × quantity_B
=
total revenue
```

Linear algebra can solve such systems efficiently.

Other applications include:

* 🤖 Machine Learning
* 📊 Regression
* 💰 Financial modeling
* 🏗️ Engineering
* 🔬 Scientific computing
* 🖼️ Computer vision

---

# 1️⃣9️⃣ Complete Linear Algebra Example

Here is a good VS Code practice program:

```python
# ============================================================
# NUMPY LINEAR ALGEBRA
# ============================================================

import numpy as np


# ============================================================
# 1. CREATE MATRICES
# ============================================================

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])


print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


# ============================================================
# 2. MATRIX ADDITION
# ============================================================

addition = A + B

print("\nMatrix Addition:")
print(addition)


# ============================================================
# 3. ELEMENT-WISE MULTIPLICATION
# ============================================================

element_multiplication = A * B

print("\nElement-wise Multiplication:")
print(element_multiplication)


# ============================================================
# 4. MATRIX MULTIPLICATION
# ============================================================

matrix_multiplication = A @ B

print("\nMatrix Multiplication:")
print(matrix_multiplication)


# ============================================================
# 5. DOT PRODUCT
# ============================================================

dot_result = np.dot(A, B)

print("\nDot Product:")
print(dot_result)


# ============================================================
# 6. MATRIX MULTIPLICATION USING MATMUL
# ============================================================

matmul_result = np.matmul(A, B)

print("\nMatmul:")
print(matmul_result)


# ============================================================
# 7. MATRIX INVERSE
# ============================================================

inverse = np.linalg.inv(A)

print("\nInverse of A:")
print(inverse)


# ============================================================
# 8. DETERMINANT
# ============================================================

determinant = np.linalg.det(A)

print("\nDeterminant of A:")
print(determinant)


# ============================================================
# 9. EIGENVALUES AND EIGENVECTORS
# ============================================================

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# ============================================================
# 10. SOLVE LINEAR EQUATIONS
# ============================================================

C = np.array([
    [2, 1],
    [1, 3]
])

D = np.array([
    5,
    6
])

solution = np.linalg.solve(C, D)

print("\nSolution of Linear Equations:")
print(solution)
```

---

# 📊 Important Comparison Table

| Function                | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| `A + B`                 | Matrix/array addition                      |
| `A * B`                 | Element-wise multiplication                |
| `np.dot(A, B)`          | Dot/matrix multiplication in common 2D use |
| `np.matmul(A, B)`       | Matrix multiplication                      |
| `A @ B`                 | Matrix multiplication                      |
| `np.linalg.inv(A)`      | Matrix inverse                             |
| `np.linalg.det(A)`      | Determinant                                |
| `np.linalg.eig(A)`      | Eigenvalues + eigenvectors                 |
| `np.linalg.solve(A, B)` | Solve linear equations                     |

---

# ⚠️ Common Mistakes

### ❌ Mistake 1 — Confusing `*` and `@`

```python
A * B
```

is not the same as:

```python
A @ B
```

Remember:

```text
* → element by element
@ → row × column
```

---

### ❌ Mistake 2 — Incompatible matrix shapes

```text
(2 × 3) @ (2 × 2)
```

❌ Not valid.

Why?

```text
(2 × 3)
      ↓
(2 × 2)
 ↑
3 != 2
```

The inner dimensions must match.

---

### ❌ Mistake 3 — Trying inverse of singular matrix

```python
np.linalg.inv(A)
```

will fail if the matrix has no inverse.

---

### ❌ Mistake 4 — Confusing determinant with inverse

```python
np.linalg.det(A)
```

returns a **number**.

```python
np.linalg.inv(A)
```

returns a **matrix**.

---

# 🎯 Interview Questions

### Q1. What is a matrix?

**Answer:**
A matrix is a rectangular arrangement of numbers organized into rows and columns.

---

### Q2. What is matrix multiplication?

**Answer:**
Matrix multiplication calculates each result element using the dot product of a row from the first matrix and a column from the second matrix.

---

### Q3. What is the difference between `*` and `@`?

**Answer:**

```text
* → element-wise multiplication
@ → matrix multiplication
```

---

### Q4. What does `np.dot()` do?

**Answer:**
`np.dot()` calculates a dot product and, for common 2D matrices, performs matrix multiplication.

---

### Q5. What does `np.matmul()` do?

**Answer:**
`np.matmul()` performs matrix multiplication.

---

### Q6. What is the matrix inverse?

**Answer:**
The inverse of matrix `A`, written as `A⁻¹`, satisfies:

```text
A × A⁻¹ = I
```

when the inverse exists.

---

### Q7. What does `np.linalg.det()` return?

**Answer:**
It calculates the determinant of a square matrix.

---

### Q8. What does `np.linalg.eig()` return?

**Answer:**
It returns eigenvalues and the corresponding eigenvectors.

---

### Q9. What does `np.linalg.solve()` do?

**Answer:**
It solves a system of linear equations represented as:

```text
A × X = B
```

---

### Q10. What condition is required for ordinary matrix inverse?

**Answer:**
For a square matrix, its determinant must be non-zero.

---

# 📝 Practice Questions

### Practice 1

Create:

```text
A = [[1, 2],
     [3, 4]]
```

and:

```text
B = [[5, 6],
     [7, 8]]
```

Find:

1. Addition
2. Element-wise multiplication
3. Matrix multiplication

---

### Practice 2

Create:

```python
A = np.array([
    [4, 7],
    [2, 6]
])
```

Find:

```python
np.linalg.det(A)
```

and:

```python
np.linalg.inv(A)
```

---

### Practice 3

Solve:

```text
x + y = 10

2x + 3y = 24
```

using:

```python
np.linalg.solve()
```

---

# 💻 Mini Project

## 🎓 Student Marks Matrix

Suppose:

```text
Students × Subjects
```

```python
marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 92]
])
```

Try to find:

### 1️⃣ Shape

```python
print(marks.shape)
```

### 2️⃣ Total marks for each student

```python
print(np.sum(marks, axis=1))
```

### 3️⃣ Subject totals

```python
print(np.sum(marks, axis=0))
```

### 4️⃣ Average marks

```python
print(np.mean(marks, axis=1))
```

This combines concepts from:

```text
Chapter 8 → Statistics
Chapter 17 → Linear Algebra
```

---

# 🧠 Chapter 17 Memory Map

```text
                 LINEAR ALGEBRA
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       MATRIX       OPERATIONS    EQUATIONS
          │            │            │
          │       ┌────┼────┐       │
          │       ↓    ↓    ↓       ↓
          │       +    *    @    solve()
          │
          ├── inverse()
          │
          ├── det()
          │
          └── eig()
```

---

# ⭐ Final Summary

| Concept             | Remember                    |
| ------------------- | --------------------------- |
| Matrix              | Rows + columns              |
| `shape`             | `(rows, columns)`           |
| `+`                 | Element-wise addition       |
| `*`                 | Element-wise multiplication |
| `@`                 | Matrix multiplication       |
| `np.dot()`          | Dot/matrix multiplication   |
| `np.matmul()`       | Matrix multiplication       |
| `np.linalg.inv()`   | Inverse                     |
| `np.linalg.det()`   | Determinant                 |
| `np.linalg.eig()`   | Eigenvalues + eigenvectors  |
| `np.linalg.solve()` | Solve equations             |

### 🔥 Most Important Memory Trick

```text
*  → Same position
@  → Row × Column

inv()   → Inverse
det()   → Determinant
eig()   → Eigenvalues + Eigenvectors
solve() → Solve equations
```

---

# 🔄 Revision

Before moving forward, make sure you can explain:

* ✅ What is a matrix?
* ✅ What does `(2,3)` mean?
* ✅ Difference between `*` and `@`
* ✅ Matrix multiplication rule
* ✅ What is an inverse?
* ✅ What is a determinant?
* ✅ What does `np.linalg.inv()` do?
* ✅ What does `np.linalg.det()` do?
* ✅ What does `np.linalg.eig()` return?
* ✅ What does `np.linalg.solve()` do?

---

# 🧪 Chapter 17 Quiz

**Q1.** What does `A * B` perform?

A. Matrix multiplication
B. Element-wise multiplication
C. Matrix inverse
D. Determinant

**Q2.** What does `A @ B` perform?

A. Element-wise multiplication
B. Matrix multiplication
C. Addition
D. Sorting

**Q3.** For `(2×3) @ (3×4)`, what is the result shape?

A. `(3,3)`
B. `(2,4)`
C. `(4,2)`
D. Error

**Q4.** Which function calculates the determinant?

A. `np.linalg.inv()`
B. `np.linalg.det()`
C. `np.linalg.eig()`
D. `np.linalg.solve()`

**Q5.** Which function solves `A × X = B`?

A. `np.linalg.solve()`
B. `np.linalg.det()`
C. `np.linalg.inv()`
D. `np.matmul()`

**Q6.** What does `np.linalg.eig()` return?

A. Sum and mean
B. Inverse and determinant
C. Eigenvalues and eigenvectors
D. Rows and columns

---

## 🏁 Chapter 17 — COMPLETE

You now know the fundamentals of **NumPy Linear Algebra**.

**Next → Chapter 18: Handling Missing Values**

We will learn:

`np.nan` → `np.isnan()` → `np.isfinite()` → `np.isinf()` → detecting missing values → cleaning numerical data → real-world datasets → practice → quiz.

Type **NEXT** when ready.
