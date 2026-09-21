# 🚀 NumPy — Chapter 7: Mathematical Functions

Welcome to **Chapter 7 — NumPy Mathematical Functions**! 🎯

In Chapter 6, we used operators:

```text
+   -   *   /   %   **
```

Now we will learn NumPy's **built-in mathematical functions**.

---

# 📘 1. What are NumPy Mathematical Functions?

NumPy provides ready-made functions for performing mathematical calculations on arrays.

For example:

```python
np.sqrt()
```

calculates the **square root**.

```python
np.square()
```

calculates the **square**.

```python
np.abs()
```

calculates the **absolute value**.

### 🧠 Basic idea

```text
Python value
     ↓
NumPy function
     ↓
Mathematical result
```

For arrays:

```text
Array
  ↓
NumPy function
  ↓
Function applied to every element
```

---

# 📚 Functions We Learn in Chapter 7

| Function | Purpose |
|---|---|
| `np.add()` | Addition |
| `np.subtract()` | Subtraction |
| `np.multiply()` | Multiplication |
| `np.divide()` | Division |
| `np.sqrt()` | Square root |
| `np.square()` | Square |
| `np.power()` | Power |
| `np.abs()` | Absolute value |
| `np.exp()` | Exponential |
| `np.log()` | Natural logarithm |

---

# 1️⃣ `np.add()`

## 📌 Definition

`np.add()` performs **element-wise addition**.

### Syntax

```python
np.add(array1, array2)
```

### Example

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

result = np.add(a, b)

print(result)
```

### Output

```text
[11 22 33]
```

### 🧮 Dry Run

```text
10 + 1 = 11
20 + 2 = 22
30 + 3 = 33
```

Therefore:

```text
[11 22 33]
```

### 🔄 Equivalent operator

```python
a + b
```

and

```python
np.add(a, b)
```

produce the same element-wise result.

---

# 2️⃣ `np.subtract()`

## 📌 Definition

`np.subtract()` performs **element-wise subtraction**.

### Syntax

```python
np.subtract(array1, array2)
```

### Example

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

result = np.subtract(a, b)

print(result)
```

### Output

```text
[ 9 18 27]
```

### Dry Run

```text
10 - 1 = 9
20 - 2 = 18
30 - 3 = 27
```

Equivalent operator:

```python
a - b
```

---

# 3️⃣ `np.multiply()`

## 📌 Definition

`np.multiply()` performs **element-wise multiplication**.

### Syntax

```python
np.multiply(array1, array2)
```

### Example

```python
a = np.array([2, 3, 4])
b = np.array([5, 6, 7])

result = np.multiply(a, b)

print(result)
```

### Output

```text
[10 18 28]
```

### Dry Run

```text
2 × 5 = 10
3 × 6 = 18
4 × 7 = 28
```

---

# 4️⃣ `np.divide()`

## 📌 Definition

`np.divide()` performs **element-wise division**.

### Syntax

```python
np.divide(array1, array2)
```

### Example

```python
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

result = np.divide(a, b)

print(result)
```

### Output

```text
[5. 5. 6.]
```

### Dry Run

```text
10 ÷ 2 = 5
20 ÷ 4 = 5
30 ÷ 5 = 6
```

---

# 🧠 Operator vs Function

These two approaches are closely related:

```python
a + b
```

and:

```python
np.add(a, b)
```

Similarly:

```python
a - b
np.subtract(a, b)

a * b
np.multiply(a, b)

a / b
np.divide(a, b)
```

### 📊 Comparison

| Operator | NumPy Function |
|---|---|
| `a + b` | `np.add(a, b)` |
| `a - b` | `np.subtract(a, b)` |
| `a * b` | `np.multiply(a, b)` |
| `a / b` | `np.divide(a, b)` |

---

# 5️⃣ `np.sqrt()`

## 📌 Definition

`sqrt` means **square root**.

### Mathematical concept

If:

```text
x² = n
```

then:

```text
√n = x
```

Examples:

```text
√4  = 2
√9  = 3
√16 = 4
√25 = 5
```

### Syntax

```python
np.sqrt(array)
```

### Example

```python
arr = np.array([4, 9, 16, 25])

result = np.sqrt(arr)

print(result)
```

### Output

```text
[2. 3. 4. 5.]
```

### 🧮 Dry Run

```text
√4  = 2
√9  = 3
√16 = 4
√25 = 5
```

---

# 🌍 Real-World Example — Distance

The distance formula often contains a square root:

```text
distance = √(x² + y²)
```

NumPy can calculate this efficiently:

```python
import numpy as np

x = 3
y = 4

distance = np.sqrt(x**2 + y**2)

print(distance)
```

Output:

```text
5.0
```

Because:

```text
√(3² + 4²)
= √(9 + 16)
= √25
= 5
```

---

# 6️⃣ `np.square()`

## 📌 Definition

`np.square()` calculates the **square of each element**.

Mathematically:

```text
square(x) = x²
```

### Syntax

```python
np.square(array)
```

### Example

```python
arr = np.array([2, 3, 4, 5])

print(np.square(arr))
```

### Output

```text
[ 4  9 16 25]
```

### Dry Run

```text
2² = 4
3² = 9
4² = 16
5² = 25
```

---

# 🔄 `np.square()` vs `** 2`

These are equivalent for this purpose:

```python
np.square(arr)
```

and:

```python
arr ** 2
```

Example:

```python
arr = np.array([2, 3, 4])

print(np.square(arr))
print(arr ** 2)
```

Output:

```text
[ 4  9 16]
[ 4  9 16]
```

---

# 7️⃣ `np.power()`

## 📌 Definition

`np.power()` calculates values raised to a specified power.

### Mathematical concept

```text
x^n
```

means multiply `x` by itself `n` times.

Example:

```text
2³ = 2 × 2 × 2 = 8
```

### Syntax

```python
np.power(array, exponent)
```

### Example

```python
arr = np.array([2, 3, 4])

result = np.power(arr, 3)

print(result)
```

### Output

```text
[ 8 27 64]
```

### Dry Run

```text
2³ = 8
3³ = 27
4³ = 64
```

---

# 🔥 Different Powers

```python
arr = np.array([2, 3, 4])

print(np.power(arr, 2))
print(np.power(arr, 3))
print(np.power(arr, 4))
```

Output:

```text
[ 4  9 16]
[ 8 27 64]
[16 81 256]
```

---

# 8️⃣ `np.abs()`

## 📌 Definition

`np.abs()` returns the **absolute value** of each element.

Absolute value means:

> Distance from zero, ignoring the sign.

Examples:

```text
|-10| = 10
|-5|  = 5
|0|   = 0
|5|   = 5
|10|  = 10
```

### Syntax

```python
np.abs(array)
```

### Example

```python
arr = np.array([-10, -5, 0, 5, 10])

print(np.abs(arr))
```

Output:

```text
[10  5  0  5 10]
```

### Visual

```text
-10 → 10
 -5 →  5
  0 →  0
  5 →  5
 10 → 10
```

---

# 🌍 Real-World Example — Temperature Difference

Suppose the expected temperature is:

```text
30°C
```

Actual temperatures:

```python
actual = np.array([28, 32, 25, 35])
```

Calculate the absolute difference:

```python
difference = np.abs(actual - 30)

print(difference)
```

Output:

```text
[2 2 5 5]
```

Meaning:

```text
28 → difference = 2
32 → difference = 2
25 → difference = 5
35 → difference = 5
```

This is useful when we care about **how far a value is from a target**, regardless of whether it is above or below.

---

# 9️⃣ `np.exp()`

## 📌 Definition

`np.exp(x)` calculates:

```text
eˣ
```

where:

```text
e ≈ 2.71828
```

This is called the **exponential function**.

### Syntax

```python
np.exp(array)
```

### Example

```python
arr = np.array([0, 1, 2])

print(np.exp(arr))
```

Output approximately:

```text
[1.         2.71828183 7.3890561 ]
```

### 🧮 Dry Run

```text
e⁰ = 1
e¹ ≈ 2.718
e² ≈ 7.389
```

---

# 🌍 Where is `exp()` Used?

`np.exp()` is important in:

- 📊 Statistics
- 🤖 Machine Learning
- 🧠 Neural Networks
- 📈 Probability
- 📉 Exponential growth/decay

For example, the **sigmoid function** used in machine learning contains `exp()`:

```text
sigmoid(x) = 1 / (1 + e⁻ˣ)
```

You don't need to memorize the complete formula yet. Just remember:

> **`np.exp()` calculates exponential values and is heavily used in data science and machine learning.**

---

# 🔟 `np.log()`

## 📌 Definition

`np.log()` calculates the **natural logarithm**.

Natural logarithm means logarithm with base:

```text
e
```

### Mathematical relationship

If:

```text
eˣ = y
```

then:

```text
ln(y) = x
```

Therefore:

```text
ln(e) = 1
```

and:

```text
ln(1) = 0
```

### Syntax

```python
np.log(array)
```

### Example

```python
arr = np.array([1, np.e, np.e**2])

print(np.log(arr))
```

Output approximately:

```text
[0. 1. 2.]
```

---

# 🧠 `exp()` and `log()` Relationship

These functions are mathematical opposites.

```text
exp(x) → eˣ
log(x) → ln(x)
```

For example:

```text
exp(2) → e²
log(e²) → 2
```

So:

```text
np.log(np.exp(x)) = x
```

for appropriate finite real values.

---

# 🔥 Complete Mathematical Functions Example

```python
import numpy as np

arr = np.array([-4, -1, 0, 1, 4])

print("Absolute:", np.abs(arr))
print("Square:", np.square(arr))
print("Power 3:", np.power(arr, 3))
```

Output:

```text
Absolute: [4 1 0 1 4]
Square: [16  1  0  1 16]
Power 3: [-64  -1   0   1  64]
```

---

# 📊 All Chapter 7 Functions

| Function | Mathematical operation | Example |
|---|---|---|
| `np.add()` | `a + b` | `np.add(a,b)` |
| `np.subtract()` | `a - b` | `np.subtract(a,b)` |
| `np.multiply()` | `a × b` | `np.multiply(a,b)` |
| `np.divide()` | `a ÷ b` | `np.divide(a,b)` |
| `np.sqrt()` | `√x` | `np.sqrt(x)` |
| `np.square()` | `x²` | `np.square(x)` |
| `np.power()` | `xⁿ` | `np.power(x,n)` |
| `np.abs()` | `\|x\|` | `np.abs(x)` |
| `np.exp()` | `eˣ` | `np.exp(x)` |
| `np.log()` | `ln(x)` | `np.log(x)` |

---

# 🧠 One Important Concept — Universal Functions

These NumPy mathematical functions are generally **vectorized** and operate element by element on arrays.

For example:

```python
arr = np.array([1, 4, 9, 16])

np.sqrt(arr)
```

NumPy effectively performs:

```text
√1
√4
√9
√16
```

giving:

```text
[1. 2. 3. 4.]
```

This is one reason NumPy is so useful for numerical computing.

---

# 🆚 Python `math` vs NumPy

Python's `math` module can calculate:

```python
import math

print(math.sqrt(16))
```

But for an array:

```python
arr = np.array([1, 4, 9, 16])
```

NumPy is designed to operate directly on the entire array:

```python
np.sqrt(arr)
```

Output:

```text
[1. 2. 3. 4.]
```

### ⭐ Remember

```text
math → individual scalar values

NumPy → arrays + numerical computing
```

---

# 🌍 Real-World Example — Student Data

Suppose we have marks:

```python
marks = np.array([25, 36, 49, 64, 81, 100])
```

### Square root

```python
print(np.sqrt(marks))
```

Output:

```text
[ 5.  6.  7.  8.  9. 10.]
```

### Square

```python
print(np.square(marks))
```

### Absolute difference from 50

```python
print(np.abs(marks - 50))
```

This demonstrates how NumPy can perform mathematical calculations on an **entire dataset at once**.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Forgetting the `np.`

Wrong:

```python
sqrt(arr)
```

unless you separately imported `sqrt`.

Preferred beginner style:

```python
np.sqrt(arr)
```

---

## ❌ Mistake 2 — Confusing `square()` and `sqrt()`

```text
square → x²
sqrt   → √x
```

Example:

```text
square(4) → 16
sqrt(4)   → 2
```

---

## ❌ Mistake 3 — Confusing `power()` with `sqrt()`

```python
np.power(arr, 2)
```

means:

```text
arr²
```

while:

```python
np.sqrt(arr)
```

means:

```text
√arr
```

---

## ❌ Mistake 4 — `np.log()` is not base-10 log

```python
np.log(x)
```

means the **natural logarithm**, base `e`.

For base-10 logarithm, NumPy provides:

```python
np.log10(x)
```

We are focusing on `np.log()` in this chapter.

---

# 💼 Interview Questions

### Q1. What does `np.sqrt()` do?

It calculates the **square root** of each element.

---

### Q2. What is the difference between `np.square()` and `np.sqrt()`?

```text
np.square(x) → x²
np.sqrt(x)   → √x
```

---

### Q3. What does `np.power()` do?

It raises each element to the specified power.

```python
np.power([2, 3], 3)
```

Output:

```text
[ 8 27]
```

---

### Q4. What does `np.abs()` do?

It returns the **absolute value** of each element.

---

### Q5. What does `np.exp(x)` calculate?

It calculates:

```text
eˣ
```

---

### Q6. What does `np.log(x)` calculate?

It calculates the **natural logarithm**, `ln(x)`.

---

### Q7. What is the relationship between `exp()` and `log()`?

They are inverse mathematical operations:

```text
log(exp(x)) = x
```

for appropriate finite real values.

---

### Q8. What is the difference between `a + b` and `np.add(a,b)`?

Both perform element-wise addition for compatible arrays. The first uses the operator; the second explicitly calls NumPy's addition function.

---

# 🧪 Practice Program

Run this in VS Code:

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

print("Original:", arr)

print("Square root:", np.sqrt(arr))
print("Square:", np.square(arr))
print("Power 2:", np.power(arr, 2))
print("Absolute:", np.abs(arr))
```

Expected output:

```text
Original: [ 1  4  9 16 25]

Square root: [1. 2. 3. 4. 5.]
Square: [  1  16  81 256 625]
Power 2: [  1  16  81 256 625]
Absolute: [ 1  4  9 16 25]
```

---

# 🎯 Mini Coding Exercise

Create:

```python
numbers = np.array([-16, -9, -4, 0, 4, 9, 16])
```

Write code to find:

### 1. Absolute values

```python
?
```

### 2. Squares

```python
?
```

### 3. Cubes

```python
?
```

### 4. Square roots

⚠️ Think carefully: this array contains **negative values**.

```python
?
```

### 5. Create a positive array and calculate square roots

```python
?
```

---

# 📌 Chapter 7 Summary

```text
                 NumPy Mathematical Functions
                              │
       ┌──────────────────────┼──────────────────────┐
       ↓                      ↓                      ↓
   Arithmetic              Power/Root             Other
       │                      │                      │
 add                    square                    abs
 subtract               sqrt                      exp
 multiply               power                     log
 divide
```

### ⭐ Must Remember

```text
np.add()       → addition
np.subtract()  → subtraction
np.multiply()  → multiplication
np.divide()    → division

np.sqrt()      → √x
np.square()    → x²
np.power()     → xⁿ
np.abs()       → |x|
np.exp()       → eˣ
np.log()       → ln(x)
```

---

# 📝 Chapter 7 Quiz

Try answering without looking above:

1. What is `np.sqrt(25)`?
2. What is `np.square(5)`?
3. What is `np.power(2, 4)`?
4. What does `np.abs(-20)` return?
5. What does `np.exp(0)` return?
6. What does `np.log(1)` return?
7. What is the difference between `np.square()` and `np.power()`?
8. What is the difference between `np.sqrt()` and `np.square()`?
9. What does `np.add()` do?
10. What does `np.log()` represent mathematically?

---

# ✅ Chapter 7 COMPLETE

### Next → 🚀 **Chapter 8 — NumPy Statistical Functions**

We will learn:

```text
np.sum()
np.mean()
np.median()
np.std()
np.var()
np.min()
np.max()
np.argmin()
np.argmax()
Percentiles
Axis concept
```

The **axis concept** is especially important because it will appear throughout NumPy, Pandas, and Data Science.

Type **`NEXT`** when ready.