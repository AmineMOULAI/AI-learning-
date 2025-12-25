## Day 1 – NumPy Basics: Arrays, Dimensions, Slicing

### What is NumPy (brief)
NumPy is a Python library for numerical computing that introduces the `ndarray` object, a fast, memory-efficient multidimensional array used heavily in data science and machine learning. It offers convenient operations for vectors and matrices, together with metadata such as the number of dimensions (`ndim`) and the shape of the array (`shape`), which makes reasoning about data much easier than with raw Python lists.

### What I did today
- Created a virtual environment and initialized the project structure:
  - `README.md`
  - `week1/np_day1.py`
  - `week1/progres-log.md`
- Wrote my first NumPy script `np_day1.py` to:
  - Create and inspect 1D arrays.
  - Create and inspect 2D arrays (matrices).
  - Practice basic indexing and slicing on rows and columns.

### Code concepts practiced (np_day1.py)
- **1D array creation and inspection**
  - Created a 1D array: `a = np.array([1, 2, 3])`
  - Checked:
    - `a.ndim` → number of dimensions (1)
    - `a.shape` → shape `(3,)`
  - Practiced slicing:
    - `a[1:]` → elements from index 1 to the end

- **2D array creation and inspection**
  - Created a 2D array (matrix):

    ```
    v1 = np.array([
       ,[1][4][5]
       ,[6][7][8]
[9][10][11]
    ])
    ```

  - Checked:
    - `v1.ndim` → 2 (matrix)
    - `v1.shape` → `(3, 3)` (3 rows, 3 columns)
  - Accessed a single element:
    - `v1[1, 2]` → element at row 2, column 3 (0-based indexing)

- **Row slicing**
  - `v1[1:]` → all rows from index 1 (second row) to the end
  - `v1[:-1]` → all rows except the last
  - `v1[::-1]` → rows in reverse order

- **Column slicing**
  - `v1[:, 1:]` → all rows, columns from index 1 to the end
  - `v1[:, :-1]` → all rows, all columns except the last
  - `v1[:, :-2]` → all rows, only the first column
  - `v1[:, ::-1]` → all rows, columns in reverse order

### What I learned / understood
- Difference between 1D and 2D arrays and how `ndim` and `shape` reflect that.
- How to access:
  - A single element with `[row, col]` for 2D arrays.
  - Subparts of an array with slicing syntax (`start:stop:step`).
- How negative indices and step `-1` allow reversing rows or columns.
- That NumPy arrays give a clear structure (dimensions + shape) which is essential before doing any ML or data analysis.
