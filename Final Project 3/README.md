<div align="center">

# -- ! Titanic Survival Analysis ! --
### *Exploratory Data Analysis of the Titanic Dataset with Pandas, Seaborn & Matplotlib*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Behind every statistic on that ship was a story of class, chance, and circumstance."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [🚢 Part B — Overall Survival & Demographics](#-part-b--overall-survival--demographics)
- [👨‍👩‍👧 Part C — Family, Fare & Embarkation](#-part-c--family-fare--embarkation)
- [🔥 Part D — Correlation Analysis](#-part-d--correlation-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Key Insights](#-key-insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Titanic Survival Analysis** project is an exploratory data analysis (EDA) of the classic Titanic passenger dataset. It investigates which factors — passenger class, gender, age, family size, fare paid, and port of embarkation — actually influenced whether a passenger survived the disaster.

Using **Pandas** for data cleaning and aggregation and **Seaborn/Matplotlib** for visualization, the notebook walks through handling missing data, computing survival rates across multiple demographic and ticketing dimensions, and identifying which factors correlate most strongly with survival.

This project is designed to:
- Practice real-world data cleaning (missing ages, missing ports, a mostly-empty column)
- Compute and compare survival rates across categorical and numeric groupings
- Engineer new features (age groups, family size) to deepen the analysis
- Visualize single-factor and combined-factor effects on survival

---

## 🎯 Problem Statement

> **Objective:** Explore the Titanic passenger dataset to determine which factors were most strongly associated with survival.

You are given a dataset (`Titanic-Dataset.csv`) containing per-passenger records — class, name, sex, age, siblings/spouses aboard, parents/children aboard, ticket fare, cabin, and port of embarkation — along with whether each passenger survived. The task is to clean the data, then analyze survival rate across class, gender, age, family size, fare, and embarkation port, both individually and in combination.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Cleaning | Preprocessing | Fills missing age/embarked values and drops the sparse `Cabin` column |
| Overall Survival | Analysis + Viz | Total survival count and rate across all passengers |
| Class & Gender Analysis | Analysis + Viz | Survival rate by passenger class, gender, and both combined |
| Age Analysis | Analysis + Viz | Age distribution by survival and survival rate by age group |
| Family & Fare Analysis | Analysis + Viz | Survival rate by family size and fare distribution by survival |
| Embarkation Analysis | Analysis + Viz | Survival rate by port of embarkation |
| Correlation Analysis | Analysis + Viz | Heatmap of numeric features against survival |

The goal is to demonstrate a **complete exploratory data analysis (EDA) workflow** on a well-known, feature-rich dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Missing Value Handling** | Fills `Age` with the median, `Embarked` with the mode, and drops the sparse `Cabin` column |
| 📊 **Overall Survival Rate** | Count plot and printed summary of survivors vs. non-survivors |
| 🎟️ **Class-Based Analysis** | Cross-tab and bar chart of survival rate by passenger class |
| 🚻 **Gender-Based Analysis** | Cross-tab and bar chart of survival rate by gender |
| 🔗 **Combined Class + Gender** | Grouped bar chart showing how class and gender interact |
| 🎂 **Age Distribution** | Stacked histogram of age by survival outcome |
| 👶 **Age Group Bucketing** | Custom age bins (Child, Teen, Young Adult, Adult, Senior) with survival rate per group |
| 👨‍👩‍👧 **Family Size Feature** | Engineered `Family_Size` from `SibSp` + `Parch` + self, plotted against survival |
| 💵 **Fare vs. Survival** | Boxplot comparing fare distribution between survivors and non-survivors |
| ⚓ **Port of Embarkation** | Bar chart of survival rate by boarding port |
| 🔥 **Correlation Heatmap** | Correlation matrix between survival and numeric features |

---

## 🏗️ Project Structure

```
📦 titanic-survival-analysis/
│
├── 📄 PR_3.ipynb                ← Main Jupyter notebook (entry point)
├── 📄 Titanic-Dataset.csv       ← Source dataset (not included — see Acknowledgements)
│
└── 📄 README.md                 ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (Titanic-Dataset.csv)
      │
      ▼
┌─────────────────────────────┐
│   Inspect Shape & Columns   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Handle Missing Values &    │
│  Drop Sparse Cabin Column   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Overall Survival Rate      │
└────────────┬────────────────┘
             │
     ┌───────┴────────────────┐
     ▼                        ▼
┌─────────────┐      ┌──────────────────────┐
│ Class &     │      │ Age, Family Size,     │
│ Gender      │      │ Fare & Embarkation    │
└──────┬──────┘      └──────────┬────────────┘
       │                        │
       └───────────┬────────────┘
                    ▼
┌─────────────────────────────┐
│  Correlation Heatmap &      │
│      Key Insights           │
└─────────────────────────────┘
```

---

## 🧹 Part A — Data Loading & Cleaning

### 📝 1. Loading the Dataset

The dataset is loaded with Pandas and inspected for shape, columns, and data types.

**Logic:**
```python
df = pd.read_csv("Titanic-Dataset.csv")

print("Dataset Loaded Successfully!")
df.head()
```

Shape, column names, and summary statistics are checked with `df.shape`, `df.columns`, `df.info()`, and `df.describe()`.

---

### 🩹 2. Checking and Handling Missing Values

`Age` and `Embarked` have missing values that are meaningful to fill in, while `Cabin` is missing for the vast majority of passengers and is dropped instead of imputed.

**Logic:**
```python
# Age: fill missing with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Embarked: fill missing with the most common port
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin: too many missing values to fill meaningfully, drop the column
df.drop("Cabin", axis=1, inplace=True, errors="ignore")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `fillna(median())` | Robust to outliers for numeric `Age` |
| `fillna(mode()[0])` | Fills categorical `Embarked` with the most frequent port |
| `drop(..., errors="ignore")` | Safely removes a column that is too sparse to impute |

Duplicate rows are also checked with `df.duplicated().sum()`.

---

## 🚢 Part B — Overall Survival & Demographics

### 📊 3. Overall Survival Rate

> A count plot and printed summary show how many passengers survived versus did not, and the overall survival rate.

**Logic:**
```python
survival_counts = df["Survived"].value_counts()
survival_rate = df["Survived"].mean() * 100

print("Overall Survival Rate: {:.2f}%".format(survival_rate))
```

---

### 🎟️ 4. Survival by Passenger Class

> A cross-tabulation and bar chart show that survival rate dropped sharply from 1st to 3rd class.

**Logic:**
```python
pd.crosstab(df["Pclass"], df["Survived"])

class_survival = df.groupby("Pclass")["Survived"].mean() * 100
```

---

### 🚻 5. Survival by Gender

> A cross-tabulation and bar chart compare survival rate between male and female passengers.

**Logic:**
```python
gender_survival = df.groupby("Sex")["Survived"].mean() * 100
```

---

### 🔗 6. Survival by Gender AND Class Combined

> A grouped bar chart (class on the x-axis, gender as hue) reveals how these two factors compound — the effect isn't simply additive.

**Logic:**
```python
sns.barplot(data=df, x="Pclass", y="Survived", hue="Sex", palette="coolwarm")
```

---

### 🎂 7. Age Distribution & Age Groups

> A stacked histogram shows the age distribution split by survival outcome. Ages are then bucketed into five groups (Child, Teen, Young Adult, Adult, Senior) to compare survival rate across life stages.

**Logic:**
```python
bins = [0, 12, 18, 35, 60, 100]
labels = ["Child (0-12)", "Teen (13-18)", "Young Adult (19-35)", "Adult (36-60)", "Senior (60+)"]
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

age_group_survival = df.groupby("Age_Group", observed=True)["Survived"].mean() * 100
```

---

## 👨‍👩‍👧 Part C — Family, Fare & Embarkation

### 👨‍👩‍👧 8. Family Size and Survival

> `SibSp` (siblings/spouses aboard) and `Parch` (parents/children aboard) are combined into a single `Family_Size` feature (including the passenger themselves), then plotted against survival rate.

**Logic:**
```python
df["Family_Size"] = df["SibSp"] + df["Parch"] + 1

family_survival = df.groupby("Family_Size")["Survived"].mean() * 100
```

---

### 💵 9. Fare and Survival

> A boxplot compares the fare distribution between passengers who survived and those who did not, showing that survivors tended to have paid higher fares.

**Logic:**
```python
sns.boxplot(data=df, x="Survived", y="Fare", hue="Survived", palette="Set3", legend=False)
```

---

### ⚓ 10. Survival by Port of Embarkation

> A bar chart shows survival rate for passengers who boarded at Cherbourg (C), Queenstown (Q), and Southampton (S).

**Logic:**
```python
embarked_survival = df.groupby("Embarked")["Survived"].mean() * 100
```

---

## 🔥 Part D — Correlation Analysis

### 🔥 11. Correlation Heatmap of Numeric Features

> A Seaborn heatmap shows the correlation between `Survived` and the numeric features `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`, and the engineered `Family_Size`.

**Logic:**
```python
numeric_df = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare", "Family_Size"]]
corr = numeric_df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, grouping, and feature engineering |
| 🔢 **NumPy** | Latest | Numeric operations |
| 📊 **Matplotlib** | Latest | Base plotting engine |
| 🎨 **Seaborn** | Latest | Count plots, bar charts, histograms, boxplots, and heatmaps |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Key Insights

- **Gender was the single biggest factor** — women survived at a much higher rate than men ("women and children first").
- **Passenger class mattered a lot** — 1st class passengers had the highest survival rate, 3rd class the lowest, reflecting cabin location and lifeboat access.
- **Combining class and gender** shows the effect compounds: 1st class women had the highest survival rate of any group, while 3rd class men had the lowest.
- **Children had a survival advantage** over adults, consistent with priority boarding for children.
- **Passengers who paid higher fares** (usually correlated with class) were more likely to survive.
- **Very large families (5+ members) and solo travelers** had lower survival rates than small families (2-4 members), possibly because large groups struggled to stay together and solo travelers had less help getting to lifeboats.
- **Port of embarkation** shows some difference in survival rate, but this is likely confounded with passenger class distribution at each port rather than being a direct cause.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates a complete, realistic EDA workflow on a widely-used benchmark dataset |
| 🧹 **Thoughtful Cleaning** | Different missing-value strategies applied per column based on how much data is missing |
| 🛠️ **Feature Engineering** | Derives `Age_Group` and `Family_Size` to enable richer analysis |
| 📊 **Multi-Angle Analysis** | Examines single factors and combined factors (e.g., class + gender) |
| 🔄 **Reusable Structure** | Cleaning and grouping logic can be reused for other categorical outcome datasets |
| 🖥️ **Self-Contained** | Runs entirely within a single Jupyter notebook |
| 📖 **Readable Code** | Clear section-by-section markdown headers matching each analysis step |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Divyesh jadav

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourhandle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yourhandle/)

> *"Behind every statistic on that ship was a story of class, chance, and circumstance."*

**🎓 Role:** Data Analyst | Python Enthusiast \
**📍 Location:** Your Location \
**🛠️ Skills:** Python · Pandas · Data Visualization · Exploratory Data Analysis

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Documentation](https://pandas.pydata.org/docs/) — Official Pandas reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Base plotting reference
- 📓 [Jupyter Project](https://jupyter.org/) — Interactive notebook environment
- 🚢 [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic) — Source of the Titanic dataset
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses and datasets

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
