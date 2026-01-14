# NumPy Progress Log

## Introduction to NumPy

NumPy (Numerical Python) is a core Python library for numerical computing. It provides fast, efficient operations on large multi-dimensional arrays and matrices. NumPy is widely used in data science, machine learning, scientific computing, and engineering.

### Key Features

* Fast array operations
* Vectorized computation (no loops needed)
* Broadcasting support
* Mathematical & statistical functions
* Random number generation
* Linear algebra tools

---

## Element-wise Operations

NumPy performs operations element by element.

### Examples

* Addition: `v1 + v2`
* Subtraction: `v1 - v2`
* Multiplication: `v1 * v2`
* Power: `v2 ** v1`

---

## Comparison Operators

Comparison operators return boolean arrays.

### Examples

* `ages == 20`
* `ages > 20`
* `ages < 20`

---

## Filtering (Boolean Indexing)

Filtering allows extracting values based on conditions.

### Examples

* Teenagers: `ages[ages <= 18]`
* Adults: `ages[ages >= 30]`

### Conditional Modification

* `ages[ages < 20] = 0`

---

## What I Learned

* NumPy operations are vectorized.
* Math functions work element-wise.
* Comparisons return boolean masks.
* Boolean indexing is powerful for data filtering.
* NumPy is faster and cleaner than Python loops.

---

## Broadcasting

Broadcasting allows NumPy to perform operations on arrays of different shapes.

### Example

```python
a = np.array([1, 2, 3, 4])
b = 2
a * b
```

Output:

```
[2, 4, 6, 8]
```

### Broadcasting Rules (Simplified)

Two arrays are compatible when:

1. They have the same shape
2. One of them has size 1 in a dimension

Otherwise → ❌ Error

---

## 2D Broadcasting Example

```python
v1 = np.array([[1, 2, 3, 4]])
v2 = np.array([[1], [2], [3], [4]])

v1 * v2
```

This produces a (4 × 4) result.

---

## Aggregate Functions

Aggregate functions reduce arrays to a single value.

```python
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
```

### Common Functions

| Function      | Description        |
| ------------- | ------------------ |
| `np.sum()`    | Sum                |
| `np.mean()`   | Mean               |
| `np.std()`    | Standard deviation |
| `np.min()`    | Minimum            |
| `np.max()`    | Maximum            |
| `np.argmin()` | Index of min       |
| `np.argmax()` | Index of max       |

### Axis Operations

* Row-wise: `np.sum(array, axis=1)`
* Column-wise: `np.sum(array, axis=0)`

---

## Advanced Filtering

```python
v = np.array([[21, 17, 22, 2, 89, 36, 74, 17, 66, 3, 0]])
```

### Even Numbers

```python
v[v % 2 == 0]
```

### Odd Numbers

```python
v[v % 2 != 0]
```

---

## Random Numbers

NumPy provides a modern random generator.

```python
rng = np.random.default_rng()
```

### Random Integers

```python
rng.integers(low=1, high=100)
rng.integers(low=1, high=100, size=3)
rng.integers(low=1, high=100, size=(2,5))
```

### Random Floats

```python
np.random.uniform(low=-1, high=1)
np.random.uniform(low=-1, high=1, size=(3,4))
```

---

## Shuffle and Random Choice

### Shuffle

```python
rng.shuffle(a)
```

Shuffles the array in-place.

### Random Choice

```python
rng.choice(fruits)
rng.choice(fruits, size=3)
```

---

## Final Summary

So far, I have learned:

* Vectorized operations
* Boolean masking
* Broadcasting
* Aggregate functions
* Advanced filtering
* Random number generation
* Shuffling and sampling

NumPy allows clean, fast, and expressive numerical computation.
