# 🚀 Chapter 14 — NumPy Broadcasting

Welcome to **Chapter 14** 🎯

This is one of the **most important NumPy concepts** for Data Science and Machine Learning.

You already know:

- Arrays
- Shapes
- Dimensions
- Indexing
- Slicing
- Operations
- Reshaping
- Joining
- Splitting
- Searching
- Copy vs View

Now we will learn how NumPy can perform operations on arrays with **different shapes**.

---

# 📚 Chapter 14 Roadmap

We will learn:

1. 🧠 What is Broadcasting?
2. Scalar + Array
3. 1D + 1D
4. 2D + Scalar
5. 2D + 1D
6. 📏 Broadcasting Rules
7. Compatible Shapes
8. ❌ Broadcasting Errors
9. Broadcasting with multiplication
10. 🌍 Real-world examples
11. ⚠️ Common mistakes
12. 💼 Interview Questions
13. 📝 Practice
14. 🎯 Mini Exercise
15. 📋 Summary
16. 🧪 Quiz

---

# 1️⃣ What is Broadcasting?

### 📖 Simple Definition

**Broadcasting** is NumPy's mechanism for performing operations between arrays with **different shapes** when their shapes are compatible.

In simple words:

> NumPy automatically adjusts smaller data to work with larger data during an operation.

For example:

```python
import numpy as np

arr = np.array([10, 20, 30])

result = arr + 5

print(result)
```

Output:

```text
[15 25 35]
```

You gave:

```text
Array → [10 20 30]

Number → 5
```

NumPy effectively applies `5` to every element:

```text
10 + 5 = 15
20 + 5 = 25
30 + 5 = 35
```

This is **broadcasting**.

---

# 2️⃣ Why Do We Need Broadcasting?

Without broadcasting, we might have to manually write:

```python
arr[0] + 5
arr[1] + 5
arr[2] + 5
```

But NumPy lets us simply write:

```python
arr + 5
```

So broadcasting gives us:

### ⚡ Less code

### ⚡ Faster numerical operations

### ⚡ Convenient array calculations

### ⚡ Vectorized computation

---

# 3️⃣ Scalar + Array

A **scalar** is a single value.

Example:

```text
5
10
100
```

An array contains multiple values:

```text
[10 20 30]
```

Now:

```python
import numpy as np

arr = np.array([10, 20, 30])

result = arr + 5

print(result)
```

Output:

```text
[15 25 35]
```

### 🧠 Dry Run

Conceptually:

```text
       [10  20  30]
          +
       [ 5   5   5]
       -------------
       [15  25  35]
```

You did not explicitly create `[5, 5, 5]`.

NumPy **broadcasts** the scalar `5`.

---

# ⭐ Scalar Broadcasting

The same idea works with:

### Addition

```python
arr + 5
```

### Subtraction

```python
arr - 5
```

### Multiplication

```python
arr * 5
```

### Division

```python
arr / 5
```

### Power

```python
arr ** 2
```

Example:

```python
arr = np.array([2, 4, 6])

print(arr * 3)
```

Output:

```text
[ 6 12 18]
```

---

# 4️⃣ Broadcasting with 1D Arrays

Suppose:

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
```

Both have shape:

```text
(3,)
```

So:

```python
a + b
```

Output:

```text
[11 22 33]
```

Dry run:

```text
10 + 1 = 11
20 + 2 = 22
30 + 3 = 33
```

This is straightforward **element-wise operation**.

---

# 5️⃣ Broadcasting with a 2D Array and Scalar

Consider:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Shape:

```text
(2, 3)
```

Now:

```python
result = arr + 10

print(result)
```

Output:

```text
[[20 30 40]
 [50 60 70]]
```

Conceptually:

```text
Original:

10 20 30
40 50 60

       + 10

20 30 40
50 60 70
```

The scalar is broadcast to every element.

---

# 6️⃣ 2D Array + 1D Array

Now we reach the **important part**.

Consider:

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([1, 2, 3])
```

Shapes:

```text
arr.shape
    ↓
(2, 3)

values.shape
    ↓
(3,)
```

Now:

```python
result = arr + values

print(result)
```

Output:

```text
[[11 22 33]
 [41 52 63]]
```

---

# 🧠 How Did This Work?

Original:

```text
arr

10 20 30
40 50 60
```

Second array:

```text
1 2 3
```

NumPy conceptually applies it to each row:

```text
10 20 30
+  1  2  3
------------
11 22 33
```

and:

```text
40 50 60
+  1  2  3
------------
41 52 63
```

Result:

```text
11 22 33
41 52 63
```

---

# ⭐ Shape Understanding

We have:

```text
A → (2, 3)

B → (3,)
```

NumPy compares shapes from the **right side**.

Write them aligned:

```text
A → (2, 3)
B →    (3)
```

The last dimensions:

```text
3
3
```

match.

Therefore broadcasting works.

---

# 7️⃣ Broadcasting Rules

🔥 **These rules are extremely important.**

When NumPy compares two shapes, it starts from the **rightmost dimension**.

Two dimensions are compatible if:

### Rule 1️⃣

They are equal.

```text
3 and 3
```

✅ Compatible.

---

### Rule 2️⃣

One of them is `1`.

```text
3 and 1
```

✅ Compatible.

---

### Rule 3️⃣

One shape can be missing a leading dimension.

Example:

```text
(2, 3)
(3,)
```

Align them:

```text
(2, 3)
(   3)
```

The missing dimension is effectively treated as `1` for broadcasting comparison.

So:

```text
3 == 3
```

✅ Compatible.

---

# 🧠 Golden Rule

> **Starting from the rightmost dimension, every pair must either be equal or one of them must be 1.**

---

# 8️⃣ Example — Shape `(3,)` and `(2,3)`

Let's understand:

```text
A → (2, 3)
B → (3,)
```

Align:

```text
A → (2, 3)
B → (   3)
```

Compare:

```text
3 vs 3 → ✅
```

The remaining dimension:

```text
2
```

has nothing to compare against because `B` has no more dimensions.

Therefore:

```text
✅ Broadcasting works
```

---

# 9️⃣ Example — Shape `(2,3)` and `(2,1)`

Consider:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([
    [1],
    [2]
])
```

Shapes:

```text
a → (2,3)

b → (2,1)
```

Compare from right:

```text
3 vs 1
```

Since one is `1`:

```text
✅ Compatible
```

Then:

```text
2 vs 2
```

Equal:

```text
✅ Compatible
```

Therefore broadcasting works.

---

# 🧠 Dry Run

`b`:

```text
1
2
```

is conceptually broadcast across columns:

```text
1 1 1
2 2 2
```

Then:

```text
10 20 30      1 1 1
40 50 60  +   2 2 2
```

Result:

```text
11 21 31
42 52 62
```

Code:

```python
result = a + b

print(result)
```

Output:

```text
[[11 21 31]
 [42 52 62]]
```

---

# 🔟 Example — Shape `(3,1)` and `(1,4)`

This is a very important example.

Suppose:

```python
a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([
    [10, 20, 30, 40]
])
```

Shapes:

```text
a → (3,1)

b → (1,4)
```

Compare:

```text
3  1
1  4
```

Rightmost:

```text
1 vs 4
```

One is `1`.

✅

Next:

```text
3 vs 1
```

One is `1`.

✅

Therefore broadcasting works.

---

# 🧠 What Happens?

`a`:

```text
1
2
3
```

is conceptually expanded:

```text
1 1 1 1
2 2 2 2
3 3 3 3
```

`b`:

```text
10 20 30 40
```

is conceptually repeated:

```text
10 20 30 40
10 20 30 40
10 20 30 40
```

Add:

```text
 1  1  1  1
 2  2  2  2
 3  3  3  3

+

10 20 30 40
10 20 30 40
10 20 30 40
```

Result:

```text
11 21 31 41
12 22 32 42
13 23 33 43
```

---

# ⭐ Important Concept

Broadcasting does **not necessarily mean NumPy physically creates repeated copies** of the data.

It is better to think of broadcasting as:

> NumPy **conceptually stretches** the smaller shape so the operation can be performed.

This is one reason broadcasting is powerful and efficient.

---

# 1️⃣1️⃣ Broadcasting Error

Now let's see an example that **does not work**.

Consider:

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20])
```

Shapes:

```text
a → (2,3)

b → (2,)
```

Align from right:

```text
(2, 3)
(   2)
```

Compare:

```text
3 vs 2
```

They are:

```text
3 ≠ 2
```

and neither is `1`.

Therefore:

```text
❌ Not compatible
```

---

# ❌ Example

```python
result = a + b
```

This produces a broadcasting-related error, typically similar to:

```text
ValueError:
operands could not be broadcast together with shapes (2,3) (2,)
```

---

# 🧠 Why Did It Fail?

Because:

```text
(2,3)
(2)
```

becomes:

```text
  2 3
    2
```

Compare:

```text
3 vs 2
```

❌ No match.

---

# 1️⃣2️⃣ How to Fix It

Sometimes we can reshape the smaller array.

Instead of:

```python
b = np.array([10, 20])
```

we can use:

```python
b = np.array([
    [10],
    [20]
])
```

Now:

```text
b.shape → (2,1)
```

Compare:

```text
a → (2,3)
b → (2,1)
```

Right side:

```text
3 vs 1 → ✅
```

Left side:

```text
2 vs 2 → ✅
```

So broadcasting works.

```python
result = a + b

print(result)
```

Output:

```text
[[11 12 13]
 [24 25 26]]
```

---

# 🔥 Broadcasting Shape Checklist

Whenever you see:

```python
A + B
```

Ask:

### Step 1️⃣

What are their shapes?

```python
print(A.shape)
print(B.shape)
```

### Step 2️⃣

Align dimensions from the **right**.

### Step 3️⃣

Check every dimension:

```text
Equal?       → ✅

One is 1?    → ✅

Anything else? → ❌
```

---

# 📊 Broadcasting Examples

| Shape A | Shape B | Compatible? |
|---|---|---|
| `(3,)` | `(3,)` | ✅ |
| `(2,3)` | `(3,)` | ✅ |
| `(2,3)` | `(1,3)` | ✅ |
| `(2,3)` | `(2,1)` | ✅ |
| `(3,1)` | `(1,4)` | ✅ |
| `(2,3)` | `(2,)` | ❌ |
| `(3,4)` | `(2,4)` | ❌ |
| `(2,3)` | `(4,1)` | ❌ |

---

# 1️⃣3️⃣ Broadcasting with Multiplication

Broadcasting isn't limited to addition.

Example:

```python
prices = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

discount = np.array([0.9, 0.8, 0.7])
```

Shapes:

```text
prices   → (2,3)
discount → (3,)
```

Now:

```python
result = prices * discount

print(result)
```

Output:

```text
[[ 90. 160. 210.]
 [360. 400. 420.]]
```

### Dry Run

```text
100 × 0.9 = 90
200 × 0.8 = 160
300 × 0.7 = 210
```

Second row:

```text
400 × 0.9 = 360
500 × 0.8 = 400
600 × 0.7 = 420
```

---

# 🌍 Real-World Example — Student Marks

Suppose students have marks in:

```text
Math
English
Science
```

```python
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])
```

Suppose each subject has a weight:

```python
weights = np.array([0.3, 0.3, 0.4])
```

Shapes:

```text
marks   → (3,3)
weights → (3,)
```

Broadcasting allows:

```python
weighted_marks = marks * weights

print(weighted_marks)
```

Output:

```text
[[24.  21.  36. ]
 [18.  25.5 30. ]
 [28.5 27.  35.2]]
```

This is a simple example of how broadcasting can help with **feature weighting**.

---

# 🌍 Real-World Example — Temperature Conversion

Suppose:

```python
celsius = np.array([0, 10, 20, 30, 40])
```

Formula:

```text
Fahrenheit = Celsius × 9/5 + 32
```

NumPy:

```python
fahrenheit = celsius * 9/5 + 32

print(fahrenheit)
```

Output:

```text
[32. 50. 68. 86. 104.]
```

Broadcasting allows scalar values like:

```text
9
5
32
```

to participate in operations with the entire array.

---

# 🌍 Real-World Example — Feature Normalization

Suppose:

```python
data = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
])
```

Suppose we want to subtract column means:

```python
mean = np.mean(data, axis=0)

print(mean)
```

Output:

```text
[ 20. 200.]
```

Now:

```python
centered = data - mean

print(centered)
```

Output:

```text
[[-10. -100.]
 [  0.    0.]
 [ 10.  100.]]
```

Why does this work?

Shapes:

```text
data → (3,2)

mean → (2,)
```

Align:

```text
(3,2)
(  2)
```

The final dimension matches:

```text
2 = 2
```

So broadcasting works.

This pattern appears frequently in **data preprocessing**.

---

# 1️⃣4️⃣ Broadcasting vs Normal Array Operation

### Without broadcasting

Two arrays generally need compatible shapes.

Example:

```text
(3,)
+
(3,)
```

✅

### With broadcasting

Different shapes can work:

```text
(2,3)
+
(3,)
```

✅

because:

```text
(2,3)
(  3)
```

---

# 1️⃣5️⃣ Broadcasting vs Reshaping

These are different concepts.

### Broadcasting

Changes how arrays **participate in an operation**.

```python
arr + [1, 2, 3]
```

### Reshaping

Actually changes the array's **shape**.

```python
arr.reshape(3, 1)
```

So:

```text
Broadcasting
→ operation compatibility

Reshape
→ change array shape
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Checking shapes incorrectly

Don't just look at the first dimension.

Always compare shapes from the **rightmost side**.

Example:

```text
(3,4)
(4,)
```

Align:

```text
(3,4)
(  4)
```

✅

---

## ❌ Mistake 2 — Thinking all different shapes work

This is false:

```text
(2,3)
(2,)
```

❌

because:

```text
3 ≠ 2
```

---

## ❌ Mistake 3 — Confusing broadcasting with copying

Broadcasting does not mean:

```text
"make a physical copy of everything"
```

It is a mechanism for making compatible shapes work together.

---

## ❌ Mistake 4 — Forgetting `shape`

When debugging a broadcasting error, immediately check:

```python
print(arr1.shape)
print(arr2.shape)
```

This is one of the best debugging techniques.

---

# 💼 Interview Questions

### Q1. What is broadcasting?

**Answer:**

Broadcasting is NumPy's mechanism for performing operations on arrays with different but compatible shapes.

---

### Q2. What are the main broadcasting rules?

**Answer:**

Starting from the rightmost dimensions, dimensions must either:

1. Be equal, or
2. One of them must be `1`.

---

### Q3. Does `(2,3)` and `(3,)` broadcast?

**Answer:**

Yes.

```text
(2,3)
(  3)
```

The final dimensions match.

---

### Q4. Does `(2,3)` and `(2,)` broadcast?

**Answer:**

No.

```text
(2,3)
(  2)
```

The rightmost dimensions are:

```text
3 vs 2
```

They are incompatible.

---

### Q5. Does `(2,3)` and `(2,1)` broadcast?

**Answer:**

Yes.

```text
3 vs 1 → compatible
2 vs 2 → compatible
```

---

### Q6. Why is broadcasting useful?

**Answer:**

It allows concise and efficient element-wise calculations without manually repeating data.

---

### Q7. What should you check when broadcasting produces an error?

**Answer:**

Check the shapes:

```python
print(arr1.shape)
print(arr2.shape)
```

Then compare dimensions from right to left.

---

# 📝 Practice

## Practice 1

Predict:

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr + 5)
```

---

## Practice 2

Will this work?

```python
a = np.ones((2, 3))
b = np.array([1, 2, 3])

result = a + b
```

Check the shapes.

---

## Practice 3

Will this work?

```python
a = np.ones((2, 3))
b = np.array([1, 2])
```

Explain why or why not.

---

## Practice 4

Will this work?

```python
a = np.ones((2, 3))
b = np.array([
    [1],
    [2]
])
```

Check:

```text
(2,3)
(2,1)
```

---

## Practice 5

What is the result?

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

print(a + b)
```

---

# 🎯 Mini Coding Exercise

Try this yourself:

```python
import numpy as np

# Student marks
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

# Subject bonus
bonus = np.array([5, 3, 2])

# Add bonus to every student's subject marks
result = ?

print(result)
```

Expected result:

```text
[[ 85  73  92]
 [ 65  88  77]
 [100  93  90]]
```

### 🧠 Think about the shapes:

```text
marks → (3,3)

bonus → (3,)
```

Align:

```text
(3,3)
(  3)
```

Therefore:

```text
✅ Broadcasting works
```

---

# 📋 Chapter 14 Summary

| Concept | Meaning |
|---|---|
| Broadcasting | Operations between compatible different shapes |
| Scalar | Single value |
| `(3,) + scalar` | ✅ |
| `(2,3) + (3,)` | ✅ |
| `(2,3) + (2,1)` | ✅ |
| `(3,1) + (1,4)` | ✅ |
| `(2,3) + (2,)` | ❌ |
| `(2,3) + (4,1)` | ❌ |
| Rightmost dimension | Compared first |
| `1` dimension | Can broadcast |
| Equal dimensions | Can broadcast |

---

# 🧠 One-Minute Revision

Remember this rule:

```text
             BROADCASTING
                  │
                  ↓
       Compare shapes RIGHT → LEFT
                  │
          ┌───────┴────────┐
          ↓                ↓
       Equal            One is 1
          │                │
          └───────┬────────┘
                  ↓
                 ✅
              Compatible
```

If neither is true:

```text
❌ Broadcasting Error
```

### ⭐ Golden Memory Trick

```text
RIGHT → LEFT
   ↓
Equal OR 1
   ↓
Compatible ✅
```

---

# 🧪 Chapter 14 Quiz

### 1. What is broadcasting?

A. Sorting arrays  
B. Joining arrays  
C. Performing operations on compatible different-shaped arrays  
D. Copying arrays

---

### 2. Does this work?

```text
(2,3) + (3,)
```

A. Yes  
B. No

---

### 3. Does this work?

```text
(2,3) + (2,)
```

A. Yes  
B. No

---

### 4. Which side should we start from when comparing shapes?

A. Left  
B. Middle  
C. Right  
D. Random

---

### 5. Which dimensions are compatible?

A. `3` and `4`  
B. `2` and `3`  
C. `3` and `1`  
D. `5` and `2`

---

### 6. Does this work?

```text
(3,1) + (1,4)
```

A. Yes  
B. No

---

### 7. What should you check first when you get a broadcasting error?

A. `dtype`  
B. `shape`  
C. `size`  
D. `itemsize`

---

### 8. Complete the rule:

> Starting from the rightmost dimension, dimensions must be ______ or one of them must be ______.

---

# ✅ Chapter 14 COMPLETE

You now understand:

**Broadcasting → scalar operations → 1D + 2D → shape rules → compatible shapes → broadcasting errors → real-world Data Science examples.**

👉 Type **`NEXT`** when you're ready for:

# 🎯 Chapter 15 — Boolean Masking

We will learn how to use NumPy arrays like a **powerful filtering system**:

```text
marks > 70
marks[(marks > 50) & (marks < 90)]
marks[(marks >= 80) | (marks == 50)]
~condition
```

This is extremely important for **Data Science and Pandas**.