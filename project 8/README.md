<div align="center">

# -- ! NumPy Analyzer ! --
### *Interactive Console-Based NumPy Array Creation & Analysis Tool*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/OOP-Class%20Based-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"An array is just a story waiting to be sliced, diced, and summed up."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Part A — Array Creation](#-part-a--array-creation)
- [🔎 Part B — Indexing & Slicing](#-part-b--indexing--slicing)
- [➗ Part C — Mathematical Operations](#-part-c--mathematical-operations)
- [🔗 Part D — Combine & Split](#-part-d--combine--split)
- [🔍 Part E — Search, Sort & Filter](#-part-e--search-sort--filter)
- [📊 Part F — Aggregate Statistics](#-part-f--aggregate-statistics)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **NumPy Analyzer** is an interactive, menu-driven Python console application built around the `numpy` library. It demonstrates core array-handling concepts such as **array creation (1D/2D/3D)**, **indexing & slicing**, **element-wise & matrix arithmetic**, **combining/splitting**, **searching/sorting/filtering**, and **statistical aggregation** — all wrapped in a clean, object-oriented, menu-driven CLI.

This project is designed to:
- Strengthen understanding of NumPy array creation and reshaping
- Practice indexing, slicing, and shape manipulation
- Apply element-wise arithmetic and matrix multiplication
- Explore searching, sorting, and filtering with NumPy
- Compute statistical aggregates like mean, median, and standard deviation

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to create, manipulate, and analyze NumPy arrays.

You are building a utility program for students learning NumPy. The program must accept user choices from a menu and execute the corresponding task — creating arrays, indexing/slicing them, performing arithmetic, combining/splitting, searching/sorting/filtering, or computing statistics.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Array Creation | Console Input | Builds 1D, 2D, or 3D NumPy arrays from user input |
| Indexing & Slicing | Logic | Retrieves values or sub-arrays by position/range |
| Mathematical Operations | Logic | Element-wise arithmetic and matrix multiplication |
| Combine & Split | Logic | Vertically stacks or splits arrays |
| Search / Sort / Filter | Logic | Locates, orders, or filters array values |
| Aggregate Statistics | Logic | Computes sum, mean, median, std dev, variance |

The goal is to demonstrate **practical NumPy skills** through a clean, class-based, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 🧱 **3 Array Dimensions** | Create 1D, 2D, or 3D arrays with custom shapes |
| 🔎 **Indexing & Slicing** | Access single values or row/column ranges |
| ➗ **5 Math Operations** | Addition, Subtraction, Multiplication, Division, Matrix Dot Product |
| 🔗 **Combine & Split** | Vertical stacking and array splitting |
| 🔍 **Search / Sort / Filter** | Find values, sort ascending/descending, filter by threshold |
| 📊 **6 Statistical Aggregates** | Sum, Mean, Median, Std Dev, Variance |
| 🖥️ **CLI Interface** | Simple, clean text-based menu for user interaction |
| ✅ **OOP Design** | Built as a `DataAnalytics` class with dedicated methods per feature |
| ⚠️ **Input & Error Handling** | Catches invalid input, shape mismatches, and empty-array errors |

---

## 🏗️ Project Structure

```
📦 numpy-analyzer/
│
├── 📄 numpy_analyzer.py     ← Main Python script (entry point)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Create / Index-Slice / Math / Combine-Split / Search-Sort-Filter / Stats / Exit
└────────────┬────────────────┘
             │
   ┌─────────┼───────────────────────────────┐
   ▼         ▼            ▼                  ▼
┌────────┐ ┌───────────┐ ┌───────────────┐ ┌────────────────┐
│Choice:1│ │ Choice:2  │ │  Choice:3     │ │  Choice:4/5/6   │
│(Create)│ │(Index/Slc)│ │  (Math Ops)   │ │ (Other Tools)   │
└───┬────┘ └─────┬─────┘ └──────┬────────┘ └────────┬────────┘
    │            │              │                   │
    ▼            ▼              ▼                   ▼
┌─────────────────────────────────────────────────────────┐
│         Sub-Menu → Perform Operation → Print Result      │
└────────────────────────────┬───────────────────────────-─┘
                              │
                              ▼
                     Loop Back to Menu
                              │
                     (Choice: 7) Exit ✅
```

---

## 🧱 Part A — Array Creation

### 📝 1. What is `create_array`?

The `create_array` method builds a NumPy array from user-entered numbers, supporting **1D**, **2D**, and **3D** shapes. It stores the result in the instance attribute `self._array` for use by every other feature in the tool.

---

### 🗺️ 2. Array Types — Overview

| Type | Shape Input | Logic Used |
|------|-------------|------------|
| 1️⃣ | 1D Array | Splits raw input into a flat float array |
| 2️⃣ | 2D Array | Reads rows/cols, reshapes flat input into a matrix |
| 3️⃣ | 3D Array | Reads depth/rows/cols, reshapes into a 3D tensor |

---

### 🔢 3. 1D Array Creation

> Converts space-separated user input directly into a flat array.

**Logic:**
```python
data = input("Enter Elements Separated By Space: ")
self._array = np.array(data.split(), dtype=float)
```

**Sample Output:**
```
Array Created Successfully:
 [1. 2. 3. 4.]
```

---

### 🧮 4. 2D Array Creation

> Reshapes flat input into a `rows x cols` matrix.

**Logic:**
```python
rows = int(input("Enter The Number Of Rows: "))
cols = int(input("Enter The Number Of Columns: "))
data = input(f"Enter {rows*cols} Elements Separated By Space: ")
self._array = np.array(data.split(), dtype=float).reshape(rows, cols)
```

**Sample Output (2x2):**
```
Array Created Successfully:
 [[1. 2.]
 [3. 4.]]
```

---

### 🧊 5. 3D Array Creation

> Reshapes flat input into a `depth x rows x cols` tensor.

**Logic:**
```python
depth = int(input("Enter Depth: "))
rows = int(input("Enter Rows: "))
cols = int(input("Enter Columns: "))
data = input(f"Enter {depth*rows*cols} Elements Separated By Space: ")
self._array = np.array(data.split(), dtype=float).reshape(depth, rows, cols)
```

---

## 🔎 Part B — Indexing & Slicing

### 🔍 6. Indexing

> Retrieves the value at a specific index tuple.

**Logic:**
```python
indices = tuple(map(int, idx.split()))
print(f"Value At Index {indices}: {self._array[indices]}")
```

### ✂️ 7. Slicing

> Extracts a sub-array using `start:end` row and column ranges (2D arrays only).

**Logic:**
```python
r_start, r_end = map(int, r_range.split(':'))
c_start, c_end = map(int, c_range.split(':'))
sliced = self._array[r_start:r_end, c_start:c_end]
```

---

## ➗ Part C — Mathematical Operations

### 🧮 8. Element-Wise Arithmetic

> Addition, Subtraction, Multiplication, and Division between the stored array and a second, same-shaped array.

**Logic:**
```python
second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
result = self._array + second_array   # or -, *, /
```

### ✖️ 9. Matrix Multiplication / Dot Product

> Computes the dot product between two compatible 2D matrices.

**Logic:**
```python
second_array = np.array(data.split(), dtype=float).reshape(self._array.shape[1], r2)
print(np.dot(self._array, second_array))
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| ➕ Element-wise Ops | `+`, `-`, `*`, `/` on matching-shape arrays |
| ✖️ `np.dot()` | Matrix multiplication for 2D arrays |
| 🔷 `.reshape()` | Aligns second array's shape with the first |

---

## 🔗 Part D — Combine & Split

### 🔗 10. Combine Arrays

> Vertically stacks the stored array with a second, same-shaped array using `np.vstack()`.

**Logic:**
```python
np.vstack((self._array, second_array))
```

### ✂️ 11. Split Array

> Splits the stored array into N roughly equal parts using `np.array_split()`.

**Logic:**
```python
np.array_split(self._array, splits)
```

---

## 🔍 Part E — Search, Sort & Filter

### 🔎 12. Search

> Finds all indices where a given value occurs using `np.where()`.

```python
indices = np.where(self._array == val)
```

### 🔃 13. Sort

> Sorts the array ascending (default) or descending (via `np.flip`).

```python
sorted_arr = np.sort(self._array)
np.flip(sorted_arr, axis=-1)   # for descending
```

### 🧹 14. Filter

> Filters values greater than a user-given threshold using boolean masking.

```python
self._array[self._array > val]
```

---

## 📊 Part F — Aggregate Statistics

### 📈 15. Statistical Aggregates

> Computes core descriptive statistics on the stored array.

**Logic:**
```python
np.sum(self._array)
np.mean(self._array)
np.median(self._array)
np.std(self._array)
np.var(self._array)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| ➕ `np.sum()` | Total of all elements |
| 📊 `np.mean()` / `np.median()` | Central tendency measures |
| 📐 `np.std()` / `np.var()` | Spread/dispersion measures |

**Sample Output:**
```
Original Array:
 [1. 2. 3. 4. 5.]

Sum Of Array: 15.0
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🔢 **NumPy** | Latest | Array creation, reshaping, and numerical operations |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🎛️ **`match-case`** | Python 3.10+ | Structural pattern matching for menu branching |
| 🧮 **Arithmetic Operators** | Built-in | Element-wise math and modulus operations |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |
| 📐 **f-strings** | Python 3.6+ | Formatted string output |
| 🏛️ **OOP (Classes)** | Built-in | `DataAnalytics` class encapsulating all features |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **1D/2D/3D Array Creation** — Arrays built and reshaped from user input
- 🔎 **Indexing & Slicing** — Precise value and sub-array retrieval
- ➗ **5 Arithmetic Operations** — Element-wise math plus matrix dot products
- 🔗 **Combine/Split Support** — Vertical stacking and array splitting
- 🔍 **Search, Sort & Filter** — Value lookup, ordering, and threshold filtering
- 📊 **6 Statistical Aggregates** — Sum, Mean, Median, Std Dev, and Variance
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited
- ⚠️ **Error Feedback** — Shape mismatches and invalid input are caught gracefully

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core NumPy concepts in one guided project |
| 🔄 **Reusability** | Each feature is a standalone class method |
| 📚 **Educational** | Reinforces array shape logic and NumPy functions |
| 🖥️ **Single Dependency** | Only requires `numpy` — no other external libraries |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add new operations (e.g., transpose, reshape menu) |
| 📖 **Readable Code** | Clear class structure with dedicated methods per feature |
| 🛡️ **Input Safety** | Invalid menu choices and shape mismatches are caught and reported |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Ayush Isamaliya

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"Every array starts with a single element — just like every program starts with a single line."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · NumPy · CLI Applications · Logic Building · Array Programming

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔢 [NumPy Official Docs](https://numpy.org/doc/stable/) — Official NumPy reference and user guide
- 📐 [GeeksForGeeks — NumPy](https://www.geeksforgeeks.org/numpy/numpy-tutorial/) — NumPy tutorials and examples
- 🖥️ [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp) — Beginner NumPy reference
- 🧮 [Python f-strings Guide](https://realpython.com/python-f-strings/) — Formatted string literals
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and NumPy courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 12 July, 2026*

</div>
