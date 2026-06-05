# 📊✨ Data Analyzer & Transformer ✨📊

### *An Interactive Python Console Toolkit for Data Exploration, Transformation & Statistical Insights*

> *"Data is just numbers until you transform it into knowledge."*

---

## 📌 Overview

The **Data Analyzer & Transformer** is a menu-driven Python application that allows users to perform multiple operations on numerical datasets from a single interactive console interface.

### Features
- 📥 Data Input & Storage
- 📊 Data Summary (Min, Max, Sum, Average)
- 🔢 Recursive Factorial Calculator
- 🎚️ Lambda-Based Data Filtering
- 🔄 Ascending & Descending Sorting
- 📈 Dataset Statistics Generator
- ♾️ Continuous Menu-Driven Execution
- ⚠️ Invalid Input Handling

---

## 🏗️ Project Structure

```text
📦 Data-Analyzer-Transformer
│
├── 📄 PR_4.py
└── 📄 README.md
```

---

## 📥 Data Input Module

Accepts a one-dimensional array of integers and stores it for analysis.

---

## 📊 Data Summary Module

Displays:
- Total Elements
- Minimum Value
- Maximum Value
- Sum of Values
- Average Value

---

## 🔢 Recursive Factorial Calculator

Uses recursion to compute factorial values.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

---

## 🎚️ Data Filtering

Filters values greater than a user-defined threshold using a lambda function.

```python
filtered_data = list(filter(lambda x: x > threshold, data))
```

---

## 🔄 Sorting Operations

- Ascending Order
- Descending Order

---

## 📈 Dataset Statistics

Returns:
- Total Count
- Minimum Value
- Maximum Value
- Average Value

---

## 🛠️ Technologies Used

- Python 3.x
- Lists
- Functions
- Recursion
- Lambda Expressions
- Match-Case Statements
- Built-in Functions

---

## 🚀 Future Improvements

- Data Import from Files
- Graphical Data Visualization
- Advanced Statistics
- GUI Version

---

## 📄 License

MIT License

---

### 💡 Final Thought

*"Numbers tell stories. Analysis reveals their meaning."*
---
<img src="capture.PNG">
<img src="capture2.PNG">
<img src="capture3.PNG">
---