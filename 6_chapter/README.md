# 🚀 NumPy — Chapter 6: Array Operations

Welcome to **Chapter 6 — NumPy Array Operations**! 🎯

In the previous chapters, we learned:

```text
Chapter 2 → Creating Arrays
Chapter 3 → Array Attributes
Chapter 4 → Indexing
Chapter 5 → Slicing
```

Now we will learn how to perform **mathematical operations directly on NumPy arrays**.

---

# 📘 1. What are Array Operations?

**Array operations** are mathematical operations performed on the values stored inside NumPy arrays.

For example:

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
```

We can perform:

```text
Addition
Subtraction
Multiplication
Division
Modulus
Power
Comparison
Logical operations
```

One of NumPy's biggest advantages is that we can perform operations on **entire arrays without writing a loop**.

---

# 🧠 2. Basic Array Operations

Suppose:

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
```

Visual:

```text
a = [10, 20, 30]
b = [ 1,  2,  3]
```

NumPy performs the operation **element by element**.

For example:

```text
10 + 1 = 11
20 + 2 = 22
30 + 3 = 33
```

Therefore:

```text
[11, 22, 33]
```

This is called **element-wise operation**.

---

# 1️⃣ Addition `+`

### Definition

The `+` operator adds corresponding elements of two arrays.

### Syntax

```python
array1 + array2
```

### Example

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

result = a + b

print(result)
```

### Output

```text
[11 22 33]
```

### 🧮 Dry Run

```text
a = [10, 20, 30]
b = [ 1,  2,  3]

10 + 1 = 11
20 + 2 = 22
30 + 3 = 33

Result = [11, 22, 33]
```

---

# 2️⃣ Subtraction `-`

### Definition

Subtracts corresponding elements.

```python
result = a - b
```

Output:

```text
[ 9 18 27]
```

### Dry Run

```text
10 - 1 = 9
20 - 2 = 18
30 - 3 = 27
```

Therefore:

```text
[9, 18, 27]
```

---

# 3️⃣ Multiplication `*`

### Definition

`*` performs **element-wise multiplication**.

```python
result = a * b
```

Output:

```text
[10 40 90]
```

### Dry Run

```text
10 × 1 = 10
20 × 2 = 40
30 × 3 = 90
```

Therefore:

```text
[10, 40, 90]
```

### ⚠️ Important

In NumPy:

```python
a * b
```

means **element-wise multiplication**.

It does **not** mean matrix multiplication.

Matrix multiplication will be covered later in **Chapter 17 — Linear Algebra**.

---

# 4️⃣ Division `/`

```python
result = a / b

print(result)
```

Output:

```text
[10. 10. 10.]
```

### Dry Run

```text
10 ÷ 1 = 10
20 ÷ 2 = 10
30 ÷ 3 = 10
```

So:

```text
[10., 10., 10.]
```

### ⭐ Important

Division generally produces floating-point values.

---

# 5️⃣ Modulus `%`

### Definition

The modulus operator `%` returns the **remainder** after division.

Example:

```python
result = a % b
```

For our arrays:

```text
10 % 1 = 0
20 % 2 = 0
30 % 3 = 0
```

Output:

```text
[0 0 0]
```

---

## Another Example

```python
a = np.array([10, 11, 12])
b = np.array([3, 3, 5])

print(a % b)
```

Output:

```text
[1 2 2]
```

Because:

```text
10 ÷ 3 → remainder 1
11 ÷ 3 → remainder 2
12 ÷ 5 → remainder 2
```

---

# 6️⃣ Power `**`

### Definition

`**` is used for exponent/power operations.

Example:

```python
a = np.array([2, 3, 4])

print(a ** 2)
```

Output:

```text
[ 4  9 16]
```

### Dry Run

```text
2² = 4
3² = 9
4² = 16
```

---

## Array + Array Power

```python
a = np.array([2, 3, 4])
b = np.array([2, 3, 2])

print(a ** b)
```

Output:

```text
[ 4 27 16]
```

Because:

```text
2² = 4
3³ = 27
4² = 16
```

---

# 📊 7. All Basic Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Element-wise multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Remainder | `a % b` |
| `**` | Power | `a ** b` |

---

# 🔥 8. Scalar Operations

We don't always need two arrays.

We can also perform an operation between an array and a **single number**.

This is called a **scalar**.

Example:

```python
arr = np.array([10, 20, 30])
```

---

## Add 5

```python
print(arr + 5)
```

Output:

```text
[15 25 35]
```

Dry run:

```text
10 + 5 = 15
20 + 5 = 25
30 + 5 = 35
```

---

## Subtract 5

```python
print(arr - 5)
```

Output:

```text
[ 5 15 25]
```

---

## Multiply by 2

```python
print(arr * 2)
```

Output:

```text
[20 40 60]
```

---

## Divide by 10

```python
print(arr / 10)
```

Output:

```text
[1. 2. 3.]
```

---

## Power 2

```python
print(arr ** 2)
```

Output:

```text
[100 400 900]
```

---

# 🧠 Why Scalar Operations Are Powerful

Without NumPy, with a Python list:

```python
numbers = [10, 20, 30]
```

This doesn't work as expected:

```python
numbers + 5
```

But NumPy:

```python
arr = np.array([10, 20, 30])

print(arr + 5)
```

gives:

```text
[15 25 35]
```

NumPy automatically applies the operation to every element.

---

# 9️⃣ Comparison Operators

NumPy can also compare array values.

Operators:

```text
>
<
>=
<=
==
!=
```

The result is a **Boolean array**:

```text
True
False
```

---

# 🔹 Greater Than `>`

```python
arr = np.array([10, 20, 30, 40])

print(arr > 25)
```

Output:

```text
[False False  True  True]
```

### Dry Run

```text
10 > 25 → False
20 > 25 → False
30 > 25 → True
40 > 25 → True
```

---

# 🔹 Less Than `<`

```python
print(arr < 25)
```

Output:

```text
[ True  True False False]
```

---

# 🔹 Greater Than or Equal `>=`

```python
print(arr >= 30)
```

Output:

```text
[False False  True  True]
```

---

# 🔹 Less Than or Equal `<=`

```python
print(arr <= 30)
```

Output:

```text
[ True  True  True False]
```

---

# 🔹 Equal `==`

```python
print(arr == 30)
```

Output:

```text
[False False  True False]
```

---

# 🔹 Not Equal `!=`

```python
print(arr != 30)
```

Output:

```text
[ True  True False  True]
```

---

# 📊 Comparison Operators Summary

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `==` | Equal |
| `!=` | Not equal |

---

# 🔥 10. Comparing Two Arrays

We can compare two arrays element by element.

```python
a = np.array([10, 20, 30])
b = np.array([10, 25, 20])

print(a > b)
```

Output:

```text
[False False  True]
```

Dry run:

```text
10 > 10 → False
20 > 25 → False
30 > 20 → True
```

---

# 1️⃣1️⃣ Logical Operations

Sometimes we need **multiple conditions**.

For example:

```text
value > 10 AND value < 40
```

NumPy provides:

```text
&
|
~
```

### ⭐ Important

For NumPy arrays, use:

```text
& → AND
| → OR
~ → NOT
```

Do **not** use Python's:

```text
and
or
```

for element-wise array conditions.

---

# 1️⃣2️⃣ AND `&`

Suppose:

```python
arr = np.array([10, 20, 30, 40, 50])
```

We want values:

```text
greater than 15
AND
less than 45
```

Use:

```python
result = (arr > 15) & (arr < 45)

print(result)
```

Output:

```text
[False  True  True  True False]
```

### Dry Run

```text
10 > 15 AND 10 < 45 → False
20 > 15 AND 20 < 45 → True
30 > 15 AND 30 < 45 → True
40 > 15 AND 40 < 45 → True
50 > 15 AND 50 < 45 → False
```

---

# ⚠️ Why Parentheses?

Use:

```python
(arr > 15) & (arr < 45)
```

not:

```python
arr > 15 & arr < 45
```

### ⭐ Best Practice

Always put each condition inside parentheses:

```python
(condition1) & (condition2)
```

---

# 1️⃣3️⃣ OR `|`

`|` means **OR**.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

result = (arr < 15) | (arr > 45)

print(result)
```

Output:

```text
[ True False False False  True]
```

Meaning:

```text
10 < 15 → True
20 < 15 → False
30 < 15 → False
40 < 15 → False
50 > 45 → True
```

---

# 1️⃣4️⃣ NOT `~`

`~` reverses Boolean values.

Example:

```python
arr = np.array([10, 20, 30, 40])

condition = arr > 25

print(condition)
print(~condition)
```

Output:

```text
[False False  True  True]

[ True  True False False]
```

So:

```text
True  → False
False → True
```

---

# 🧠 Logical Operators Cheat Sheet

```text
&  → AND
|  → OR
~  → NOT
```

Example:

```python
(arr > 10) & (arr < 50)
```

means:

```text
greater than 10
AND
less than 50
```

---

# 🌍 Real-World Example — Student Marks

Suppose:

```python
marks = np.array([35, 42, 67, 80, 25, 90])
```

### Students who scored more than 50:

```python
print(marks > 50)
```

Output:

```text
[False False  True  True False  True]
```

### Students who scored between 40 and 80:

```python
print((marks >= 40) & (marks <= 80))
```

Output:

```text
[False  True  True  True False False]
```

This is the foundation for **Boolean filtering**, which we will study in more depth in Chapter 15.

---

# 🔥 15. Complete Example

```python
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** 2)

print("Greater than 25:", a > 25)
print("Less than 25:", a < 25)

print("Between 15 and 35:", (a > 15) & (a < 35))
```

Output:

```text
Addition: [12 24 35 48]
Subtraction: [ 8 16 25 32]
Multiplication: [ 20  80 150 320]
Division: [5. 5. 6. 5.]
Modulus: [0 0 0 0]
Power: [ 100  400  900 1600]

Greater than 25: [False False  True  True]
Less than 25: [ True  True False False]

Between 15 and 35: [False  True  True False]
```

---

# ⚠️ 16. Common Mistakes

## ❌ Mistake 1 — Using `and`

Don't write:

```python
(arr > 10) and (arr < 30)
```

For NumPy arrays, use:

```python
(arr > 10) & (arr < 30)
```

---

## ❌ Mistake 2 — Forgetting parentheses

Avoid:

```python
arr > 10 & arr < 30
```

Use:

```python
(arr > 10) & (arr < 30)
```

---

## ❌ Mistake 3 — Confusing `*` and matrix multiplication

```python
a * b
```

means:

> **Element-wise multiplication**

Matrix multiplication uses:

```python
a @ b
```

or:

```python
np.matmul(a, b)
```

We will study this properly in **Chapter 17**.

---

## ❌ Mistake 4 — Different array shapes

For example:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5])

print(a + b)
```

These shapes are incompatible for this operation, so NumPy will raise a broadcasting-related error.

We will understand **why** in detail in **Chapter 14 — Broadcasting**.

---

# 💼 Interview Questions

### Q1. What does `a + b` do in NumPy?

It performs **element-wise addition**.

---

### Q2. What does `a * b` mean?

It performs **element-wise multiplication**.

---

### Q3. How do you multiply every element by 10?

```python
arr * 10
```

---

### Q4. What does `%` do?

It returns the **remainder** after division.

---

### Q5. What does `**` do?

It performs **power/exponentiation**.

---

### Q6. What does `>` return?

It returns a **Boolean array** containing `True` or `False` for each element.

---

### Q7. Which operators are used for element-wise logical operations?

```text
& → AND
| → OR
~ → NOT
```

---

### Q8. Why are parentheses important?

Because NumPy conditions should be grouped clearly before applying `&` or `|`.

Correct:

```python
(arr > 10) & (arr < 50)
```

---

### Q9. What is the difference between `*` and `@`?

```text
* → element-wise multiplication
@ → matrix multiplication
```

---

# 🧪 Practice

Try this:

```python
import numpy as np

prices = np.array([100, 200, 300, 400])
discount = np.array([10, 20, 30, 40])

print("After subtraction:", prices - discount)
print("Double price:", prices * 2)
print("Price + 50:", prices + 50)
print("Price / 2:", prices / 2)
print("Price > 250:", prices > 250)
```

Predict the output before running it. 🧠

---

# 🎯 Mini Coding Exercise

Create:

```python
marks = np.array([35, 45, 55, 65, 75, 85, 95])
```

Write NumPy expressions to find:

### 1. Add 5 to every mark

```python
?
```

### 2. Multiply every mark by 2

```python
?
```

### 3. Find marks greater than 60

```python
?
```

### 4. Find marks less than 50

```python
?
```

### 5. Find marks between 50 and 80

```python
?
```

### 6. Find marks greater than 80 OR less than 40

```python
?
```

---

# 📌 Chapter 6 Summary

| Operation | Operator | Example |
|---|---|---|
| Addition | `+` | `a + b` |
| Subtraction | `-` | `a - b` |
| Multiplication | `*` | `a * b` |
| Division | `/` | `a / b` |
| Modulus | `%` | `a % b` |
| Power | `**` | `a ** 2` |
| Greater | `>` | `a > 10` |
| Less | `<` | `a < 10` |
| Greater/equal | `>=` | `a >= 10` |
| Less/equal | `<=` | `a <= 10` |
| Equal | `==` | `a == 10` |
| Not equal | `!=` | `a != 10` |
| AND | `&` | `(a > 10) & (a < 50)` |
| OR | `\|` | `(a < 10) \| (a > 50)` |
| NOT | `~` | `~(a > 10)` |

---

# 🧠 Final Revision Map

```text
                 NumPy Array Operations
                         │
       ┌─────────────────┼─────────────────┐
       ↓                 ↓                 ↓
   Arithmetic        Comparison          Logical
       │                 │                 │
   +  -  *  /        > < >= <=         &  |  ~
   %  **             == !=
       │                 │
       ↓                 ↓
 Element-wise       True / False
 calculations          arrays
```

### ⭐ Remember These 5 Rules

```text
1. NumPy operations are usually element-wise.

2. arr + 10
   → adds 10 to every element.

3. arr * arr
   → element-wise multiplication.

4. (condition1) & (condition2)
   → AND

5. (condition1) | (condition2)
   → OR
```

## 📝 Chapter 6 Quiz

1. What is an element-wise operation?
2. What is the output of:
   ```python
   np.array([10, 20, 30]) + 5
   ```
3. What does `%` do?
4. What does `**` do?
5. What is the difference between `*` and `@`?
6. What does `arr > 20` return?
7. What does `&` mean?
8. What does `|` mean?
9. What does `~` mean?
10. Why should we use parentheses around NumPy conditions?

---

# ✅ Chapter 6 COMPLETE

### Next → **Chapter 7: NumPy Mathematical Functions**

We will learn:

```text
np.add()
np.subtract()
np.multiply()
np.divide()
np.sqrt()
np.square()
np.power()
np.abs()
np.exp()
np.log()
```

with **mathematical concepts + formulas + dry runs + real-world examples + interview questions**.

Type **`NEXT`** when ready.