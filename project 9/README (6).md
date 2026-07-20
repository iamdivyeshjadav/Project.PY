<div align="center">

# -- ! Sales Data Analyzer ! --
### *An Interactive, Menu-Driven CLI for Exploring, Cleaning & Visualizing Sales Data*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![OOP](https://img.shields.io/badge/Design-Object%20Oriented-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"A good CLI doesn't just run — it has a conversation with your data."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Program Workflow](#-program-workflow)
- [🧩 Part A — Class Design](#-part-a--class-design)
- [🔍 Part B — Data Loading & Exploration](#-part-b--data-loading--exploration)
- [🧹 Part C — Handling Missing Data](#-part-c--handling-missing-data)
- [🧮 Part D — DataFrame Operations](#-part-d--dataframe-operations)
- [📊 Part E — Statistics & Visualization](#-part-e--statistics--visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Sales Data Analyzer** is an interactive, menu-driven Python console application built around a `SalesDataAnalyzer` class. It turns a raw sales CSV file into a fully explorable dataset — letting the user load, inspect, clean, transform, summarize, and visualize the data entirely through nested text menus, without writing a single line of code.

This project is designed to:
- Demonstrate object-oriented program design with an encapsulated analyzer class
- Practice building nested, menu-driven CLI programs using Python's `match`/`case` syntax
- Apply core Pandas operations (cleaning, filtering, sorting, grouping, pivoting) interactively
- Generate and save Matplotlib/Seaborn visualizations driven entirely by user input

---

## 🎯 Problem Statement

> **Objective:** Build an interactive console tool that lets a non-programmer explore and visualize a sales dataset through menus alone.

You are building a general-purpose CLI analyst for a `Q1_Sales_Data.csv`-style dataset (or any similarly structured CSV). The program must let the user load a file, explore its structure, handle missing values, run common DataFrame operations, generate descriptive statistics, produce a range of charts, and save the resulting plot — all through a persistent main menu with nested sub-menus per feature area.

| 📂 Feature Area | 📄 Type | 🔍 Description |
|------------------|---------|----------------|
| Data Loading | I/O | Loads any CSV file path provided by the user |
| Data Exploration | Menu | Head/tail rows, columns, dtypes, `.info()` summary |
| Missing Data Handling | Menu | Count, mean-fill, drop, or custom-value replace |
| DataFrame Operations | Menu | NumPy conversion, scaling, concat, split-by-group, filter/sort, aggregates, pivot tables |
| Statistical Analysis | Report | `.describe()` plus std, variance, and quantiles |
| Data Visualization | Menu | Bar, line, scatter, pie, histogram, stack plot, and Seaborn heatmap/boxplot |
| Save Visualization | I/O | Saves the most recently generated chart to a file |

The goal is to demonstrate **clean object-oriented CLI design** built on top of Pandas, NumPy, Matplotlib, and Seaborn.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧩 **Encapsulated Analyzer Class** | All state (`data`, `current_figure`) and behavior live inside `SalesDataAnalyzer` |
| 🔁 **Persistent Nested Menus** | A main menu dispatches to feature-specific sub-menus, each looping until the user exits |
| 🐍 **Modern `match`/`case` Dispatch** | Menu routing uses Python 3.10+ structural pattern matching instead of long `if-elif` chains |
| 🔍 **Full Data Exploration Suite** | Head, tail, column list, dtypes, and a full `.info()` summary on demand |
| 🧹 **Four Missing-Data Strategies** | Inspect, mean-fill numeric columns, drop rows, or replace with a custom value |
| 🔢 **NumPy Interop** | Converts any column to a NumPy array and demonstrates slicing |
| ➗ **Interactive Math Scaling** | Multiplies a chosen numeric column by a user-supplied factor |
| 🔗 **Concat, Split, Filter, Sort, Aggregate, Pivot** | A full suite of DataFrame operations, all driven by typed column names |
| 📊 **Seven Chart Types** | Bar, line, scatter, pie, histogram, stack plot, and Seaborn boxplot/heatmap |
| 💾 **Save-to-File** | The most recently rendered figure can be saved under any filename |
| ⚠️ **Defensive Input Handling** | Guards against missing datasets, invalid columns, and non-numeric menu input throughout |

---

## 🏗️ Project Structure

```
📦 sales-data-analyzer/
│
├── 📄 PR_9.ipynb / sales_data_analyzer.py   ← Main program (entry point)
├── 📄 Q1_Sales_Data.csv                     ← Default source dataset (not included)
│
└── 📄 README.md                             ← Project documentation
```

---

## 🔄 Program Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────────┐
│      Display Main Menu (1-8)    │
└────────────────┬─────────────────┘
                  │
   ┌──────────────┼───────────────────────────────┐
   ▼              ▼                                ▼
┌─────────┐  ┌───────────────┐             ┌─────────────────┐
│ 1. Load │  │ 2. Explore /  │             │ 6. Visualize /   │
│ Dataset │  │ 4. Clean Data │             │ 7. Save Plot     │
└────┬────┘  └───────┬───────┘             └────────┬─────────┘
     │               │                               │
     ▼               ▼                               ▼
┌─────────────────────────────────────────────────────────────┐
│  3. DataFrame Ops   │   5. Descriptive Statistics            │
└─────────────────────────────────────────────────────────────┘
                  │
                  ▼
          Loop Back to Main Menu
                  │
           (Choice: 8) Exit ✅
```

---

## 🧩 Part A — Class Design

### 📝 1. The `SalesDataAnalyzer` Class

> All program state and behavior are encapsulated in a single class, keeping the loaded DataFrame and the last-rendered figure as instance attributes rather than globals.

**Logic:**
```python
class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        self.current_figure = None
        self.FILE_NAME = "Q1_Sales_Data.csv"

    def __del__(self):
        plt.close('all')
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| Instance state | `self.data` holds the DataFrame; `self.current_figure` holds the last plot |
| `__del__` cleanup | Closes any open Matplotlib figures when the analyzer is destroyed |
| Guard clauses | Every method checks `if self.data is None` before operating |

---

## 🔍 Part B — Data Loading & Exploration

### 📂 2. Loading a Dataset

> The user supplies a file path (or the default `Q1_Sales_Data.csv` is used), wrapped in a try/except so a bad path doesn't crash the program.

**Logic:**
```python
def load_data(self, file_path=None):
    target_file = file_path if file_path else self.FILE_NAME
    try:
        self.data = pd.read_csv(target_file)
        print(f"Dataset '{target_file}' Loaded Successfully!")
    except Exception as e:
        print(f"Error Loading File: {e}")
```

---

### 🔎 3. Exploring the Data

> A sub-menu offers five read-only views into the dataset's structure.

**Logic:**
```python
match sub_choice:
    case 1: print(self.data.head())
    case 2: print(self.data.tail())
    case 3: print(self.data.columns.tolist())
    case 4: print(self.data.dtypes)
    case 5: self.data.info()
```

---

## 🧹 Part C — Handling Missing Data

### 🩹 4. Four Ways to Handle Missing Values

> The cleaning sub-menu lets the user inspect missing counts, mean-fill numeric columns, drop incomplete rows, or replace gaps with any custom value.

**Logic:**
```python
case 1:
    missing = self.data.isna().sum()
case 2:
    num_cols = self.data.select_dtypes(include=[np.number]).columns
    self.data[num_cols] = self.data[num_cols].fillna(self.data[num_cols].mean())
case 3:
    self.data.dropna(inplace=True)
case 4:
    val = input("Enter the value to replace missing data: ")
    self.data.fillna(val, inplace=True)
```

---

## 🧮 Part D — DataFrame Operations

### 🔢 5. NumPy Conversion & Slicing

> Converts any chosen column to a NumPy array and prints a slicing example, bridging Pandas and NumPy interactively.

**Logic:**
```python
arr = self.data[col].to_numpy()
print(f"Converted Array (First 5 elements): {arr[:5]}")
print(f"Slicing Example (Elements 2 to 5): {arr[1:5]}")
```

---

### ➗ 6. Mathematical Scaling

> Multiplies an entire numeric column by a user-supplied factor (e.g. simulate a 10% sales increase).

**Logic:**
```python
factor = float(input("Enter scaling factor (e.g., 1.1 for 10% increase): "))
self.data[col] = self.data[col] * factor
```

---

### 🔗 7. Combine, Split, Filter/Sort, Aggregate & Pivot

> The remaining sub-options round out a full DataFrame toolkit: concatenating a dummy row, splitting the dataset by unique values in a column, filtering and sorting, computing aggregate statistics, and building a pivot table.

**Logic:**
```python
# Combine
self.data = pd.concat([self.data, dummy_data], ignore_index=True)

# Split by group
for val in self.data[col].unique():
    subset = self.data[self.data[col] == val]

# Pivot table
pivot = self.data.pivot_table(values=val_col, index=index_col, aggfunc=['sum', 'mean'])
```

---

## 📊 Part E — Statistics & Visualization

### 📈 8. Descriptive & Advanced Statistics

> Beyond `.describe()`, the analyzer reports standard deviation, variance, and quartiles for every numeric column.

**Logic:**
```python
print(self.data.describe())
num_cols = self.data.select_dtypes(include=[np.number]).columns
print(self.data[num_cols].std())
print(self.data[num_cols].var())
print(self.data[num_cols].quantile([0.25, 0.5, 0.75]))
```

---

### 🎨 9. Seven Chart Types on Demand

> A visualization sub-menu builds a bar plot, line plot, scatter plot, pie chart, histogram, stack plot, or a Seaborn boxplot/heatmap — with column names typed in at runtime.

**Logic:**
```python
match sub_choice:
    case 1: sns.barplot(data=self.data, x=x, y=y, ax=ax, palette='Blues_r')
    case 2: sns.lineplot(data=self.data, x=x, y=y, marker='o', color='g', ax=ax)
    case 3: sns.scatterplot(data=self.data, x=x, y=y, ax=ax, color='purple')
    case 4: ax.pie(summary, labels=summary.index, autopct='%1.1f%%')
    case 5: sns.histplot(data=self.data, x=num_col, kde=True, ax=ax, color='orange')
    case 6: ax.stackplot(sorted_df[x_col], sorted_df[y_col], labels=[y_col])
    case 7: sns.heatmap(num_data.corr(), annot=True, cmap='coolwarm', ax=ax)  # or boxplot
```

---

### 💾 10. Saving a Visualization

> The most recently generated figure (`self.current_figure`) is saved to a user-specified filename.

**Logic:**
```python
self.current_figure.savefig(filename, bbox_inches='tight')
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core language — required for `match`/`case` syntax |
| 🐼 **Pandas** | Latest | Data loading, cleaning, filtering, grouping, and pivoting |
| 🔢 **NumPy** | Latest | Array conversion, numeric column selection |
| 📊 **Matplotlib** | Latest | Figure/axes creation, pie charts, stack plots, saving figures |
| 🎨 **Seaborn** | Latest | Bar, line, scatter, histogram, boxplot, and heatmap styling |
| 🧠 **`match`/`case`** | Python 3.10+ | Structural pattern matching for menu dispatch |

---

## 📈 Results & Insights

Running the program produces the following capabilities:

- ✅ **Fully Interactive Analysis** — every operation (clean, transform, aggregate, visualize) is reachable via menus, no code editing required
- 🔁 **Persistent Nested Menus** — each feature area loops until the user explicitly exits back to the main menu
- 🧹 **Flexible Missing-Data Handling** — four distinct strategies for dealing with gaps in the data
- 📊 **Seven Chart Types** — covering categorical comparisons, trends, relationships, distributions, and correlations
- 💾 **Persistent Output** — any generated chart can be saved to disk under a custom filename
- ⚠️ **Graceful Error Handling** — invalid file paths, columns, and menu choices are caught and reported without crashing

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates OOP design, Pandas/NumPy interop, and Matplotlib/Seaborn plotting in one project |
| 🧩 **Encapsulated Design** | State and behavior are cleanly contained in a single reusable class |
| 🔄 **Dataset-Agnostic** | Works with any CSV that has comparable columns, not just the default sales file |
| 🖥️ **No Coding Required by End User** | Every capability is exposed through typed menu choices |
| 🛡️ **Robust Input Handling** | Try/except blocks and column-existence checks throughout prevent crashes |
| ⚡ **Lightweight** | Single-class script with no external config, instantly runnable |
| 🧪 **Extensible** | New chart types, cleaning strategies, or DataFrame operations can be added as new `case` branches |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Your Name Here

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourhandle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yourhandle/)

> *"A good CLI doesn't just run — it has a conversation with your data."*

**🎓 Role:** Python Developer | Data Enthusiast \
**📍 Location:** Your Location \
**🛠️ Skills:** Python · OOP · Pandas · Data Visualization · CLI Design

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Documentation](https://pandas.pydata.org/docs/) — Official Pandas reference
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Array operations reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Base plotting reference
- 🐍 [Python `match` Statement Docs](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) — Structural pattern matching reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data analysis courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
