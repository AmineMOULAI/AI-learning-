# Learning Progress Log

## Day 1 – NumPy Basics: Arrays, Dimensions, Slicing

### What I did

* Set up my project structure and virtual environment.
* Created my first NumPy script: `np_day1.py`.
* Learned how to create 1D and 2D NumPy arrays.
* Practiced indexing and slicing rows and columns.

### Concepts practiced

* `np.array()`
* `ndim` and `shape`
* Basic indexing: `arr[i]`, `arr[row, col]`
* Slicing: `start:stop:step`
* Reversing rows/columns with `[::-1]`

### What I learned

* The difference between 1D and 2D arrays.
* How NumPy represents dimensions and shapes.
* How slicing works on rows and columns.
* Why understanding array structure is important for ML and data analysis.

---

## Day 2 – Vectorized Operations, Math Functions, and Filtering

### What I did

* Practiced vectorized mathematical operations on NumPy arrays.
* Used built-in NumPy math functions on entire arrays.
* Learned how to compare array values using boolean operators.
* Filtered arrays using boolean conditions.
* Modified array values based on conditions.

### Code concepts practiced

#### Vectorized math functions

* Applied math functions directly to arrays:

  * `np.sqrt()`
  * `np.round()`
  * `np.floor()`
  * `np.ceil()`
* Used constants like `np.pi`.

#### Vectorized arithmetic

* Performed element-wise operations:

  * Addition: `v1 + v2`
  * Subtraction: `v1 - v2`
  * Multiplication: `v1 * v2`
  * Power: `v2 ** v1`

#### Comparison operators

* Compared arrays with scalars:

  * `ages == 20`
  * `ages > 20`
  * `ages < 20`
* Learned that comparisons return boolean arrays.

#### Filtering (Boolean indexing)

* Extracted values based on conditions:

  * `ages[ages <= 18]` → teenagers
  * `ages[ages >= 30]` → adults
* Modified values conditionally:

  * `ages[ages < 20] = 0`

### What I learned

* NumPy operations are vectorized, meaning they work on whole arrays at once.
* Math functions in NumPy apply element-wise automatically.
* Comparison operators return boolean masks.
* Boolean indexing is a powerful way to filter and modify data.
* This style of computation is much faster and cleaner than using Python loops.
