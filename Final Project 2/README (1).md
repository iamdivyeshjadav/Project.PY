<div align="center">

# -- ! Global Happiness Report Analysis ! --
### *Exploring the 2015 World Happiness Report with Pandas, Seaborn & Matplotlib*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Happiness is not a number, but numbers can tell us where to look for it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [😊 Part B — Happiness Distribution & Rankings](#-part-b--happiness-distribution--rankings)
- [🌍 Part C — Regional Comparison](#-part-c--regional-comparison)
- [📐 Part D — Correlation & Relationship Analysis](#-part-d--correlation--relationship-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Key Insights](#-key-insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Global Happiness Report Analysis** project explores the **2015 World Happiness Report**, investigating which factors — GDP per capita, social support, life expectancy, freedom, trust in government, and generosity — actually go together with a country's happiness score, and how regions compare to one another.

Using **Pandas** for data wrangling and **Seaborn/Matplotlib** for statistical visualization, the notebook walks through cleaning the dataset, ranking countries, comparing regions, and analyzing correlations to surface the strongest drivers of national happiness.

This project is designed to:
- Practice exploratory data analysis (EDA) on a real-world survey dataset
- Rank and compare countries and regions on a composite happiness metric
- Quantify correlations between happiness and its contributing sub-factors
- Visualize multi-variable relationships using scatter, regression, and pair plots

---

## 🎯 Problem Statement

> **Objective:** Analyze the 2015 World Happiness Report to identify which factors are most strongly associated with national happiness, and how happiness varies by region.

You are given a dataset (`2015.csv`) containing each country's happiness rank and score, along with the sub-factors that compose it — economic output, social support, health, freedom, trust in government, generosity, and a "dystopia residual." The task is to clean the data, rank countries, compare regions, and determine which factors correlate most strongly with overall happiness.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Cleaning | Preprocessing | Checks for missing values, duplicates, and renames long column names |
| Distribution Analysis | Analysis + Viz | Histogram of happiness scores across all countries |
| Country Rankings | Analysis + Viz | Top 10 and bottom 10 happiest countries |
| Regional Comparison | Analysis + Viz | Average happiness and score spread by world region |
| Correlation Analysis | Analysis + Viz | Heatmap and ranked correlations between happiness and its sub-factors |
| Relationship Analysis | Analysis + Viz | Regression plots, a multi-dimensional scatter plot, and a pairplot |

The goal is to demonstrate an **end-to-end exploratory data analysis (EDA) workflow**, from raw survey data to actionable insight.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Data Cleaning** | Checks for nulls and duplicates; renames verbose columns for easier plotting |
| 📊 **Score Distribution** | Histogram with KDE overlay showing the spread of happiness scores |
| 🏆 **Top/Bottom Rankings** | Bar charts of the 10 happiest and 10 least happy countries |
| 🌍 **Regional Breakdown** | Mean happiness by region plus a boxplot showing score spread per region |
| 🔥 **Correlation Heatmap** | Correlation matrix between happiness score and all contributing factors |
| 📈 **Ranked Correlations** | Sorted list of which factors correlate most strongly with happiness |
| 📉 **Regression Plots** | Scatter + trend line for GDP, social support, and life expectancy vs. happiness |
| 🎨 **Multi-Variable Scatter** | GDP vs. life expectancy, colored by happiness score |
| 🔗 **Pairplot** | Pairwise relationships between happiness and its key drivers |

---

## 🏗️ Project Structure

```
📦 global-happiness-report-analysis/
│
├── 📄 PR_2.ipynb            ← Main Jupyter notebook (entry point)
├── 📄 2015.csv               ← Source dataset (not included — see Acknowledgements)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (2015.csv)
      │
      ▼
┌─────────────────────────────┐
│   Inspect Shape & Columns   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Check Missing Values &     │
│  Duplicates, Rename Columns │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Score Distribution &       │
│  Top/Bottom 10 Rankings     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Regional Comparison       │
│  (Mean Score + Boxplot)     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Correlation Heatmap,       │
│  Regression Plots, Pairplot │
└────────────┬────────────────┘
             │
             ▼
        Key Insights
```

---

## 🧹 Part A — Data Loading & Cleaning

### 📝 1. Loading the Dataset

The dataset is loaded with Pandas and inspected for shape, columns, and data types.

**Logic:**
```python
df = pd.read_csv("2015.csv")

print("Dataset Loaded Successfully!")
df.head()
```

Shape, column names, and summary statistics are checked with `df.shape`, `df.columns`, `df.info()`, and `df.describe()`.

---

### 🩹 2. Checking Missing Values & Duplicates

Missing values are checked with `df.isnull().sum()` and duplicate rows with `df.duplicated().sum()` before proceeding — the 2015 report is a clean, complete dataset, so this step mainly confirms data integrity.

---

### ✂️ 3. Renaming Columns

Several original column names are long and awkward for repeated use in plots, so they are shortened for readability.

**Logic:**
```python
df = df.rename(columns={
    "Economy (GDP per Capita)": "GDP_per_Capita",
    "Health (Life Expectancy)": "Life_Expectancy",
    "Trust (Government Corruption)": "Trust_Govt",
    "Happiness Score": "Happiness_Score",
    "Happiness Rank": "Happiness_Rank"
})
```

---

## 😊 Part B — Happiness Distribution & Rankings

### 📊 4. Overall Distribution of Happiness Scores

> A histogram with a KDE overlay shows how happiness scores are spread across all 158 countries in the report.

**Logic:**
```python
sns.histplot(df["Happiness_Score"], bins=20, kde=True, color="steelblue")
```

---

### 🏆 5. Top and Bottom 10 Happiest Countries

> Two horizontal bar charts rank the 10 happiest and 10 least happy countries by their happiness score.

**Logic:**
```python
top10 = df.sort_values("Happiness_Score", ascending=False).head(10)
bottom10 = df.sort_values("Happiness_Score", ascending=True).head(10)
```

---

## 🌍 Part C — Regional Comparison

### 🗺️ 6. Happiness by Region

> Countries are grouped by `Region`, and average happiness score per region is computed and ordered, then visualized as a boxplot to show both the average and the spread within each region.

**Logic:**
```python
region_avg = df.groupby("Region")["Happiness_Score"].mean().sort_values(ascending=False)

sns.boxplot(data=df, x="Happiness_Score", y="Region", order=region_avg.index)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `groupby()` | Aggregates happiness score by region |
| `sort_values()` | Orders regions from happiest to least happy |
| `sns.boxplot()` | Shows median, quartiles, and outliers per region |

---

## 📐 Part D — Correlation & Relationship Analysis

### 🔥 7. Correlation Between Happiness and Its Contributing Factors

> A correlation heatmap and a sorted correlation list identify which sub-factors (GDP, family, life expectancy, freedom, trust, generosity, dystopia residual) move most closely with the overall happiness score.

**Logic:**
```python
factor_cols = ["Happiness_Score", "GDP_per_Capita", "Family", "Life_Expectancy",
               "Freedom", "Trust_Govt", "Generosity", "Dystopia Residual"]

corr = df[factor_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

corr["Happiness_Score"].sort_values(ascending=False)
```

---

### 📉 8. Happiness vs. GDP, Social Support & Life Expectancy

> Three separate regression plots (scatter + trend line) examine happiness score against GDP per capita, social support (Family), and life expectancy individually.

**Logic:**
```python
sns.regplot(data=df, x="GDP_per_Capita", y="Happiness_Score")
sns.regplot(data=df, x="Family", y="Happiness_Score")
sns.regplot(data=df, x="Life_Expectancy", y="Happiness_Score")
```

---

### 🎨 9. GDP, Life Expectancy and Happiness Together

> A single scatter plot combines three dimensions at once — GDP per capita on the x-axis, life expectancy on the y-axis, and happiness score encoded as color — to visualize how these variables cluster together.

**Logic:**
```python
scatter = ax.scatter(df["GDP_per_Capita"], df["Life_Expectancy"],
                      c=df["Happiness_Score"], cmap="viridis", s=70, edgecolor="k", alpha=0.8)
```

---

### 🔗 10. Which Factor Matters Most? (Pairplot)

> A Seaborn pairplot shows every pairwise relationship between happiness score, GDP, family, life expectancy, and freedom in a single grid, with KDE curves on the diagonal.

**Logic:**
```python
sns.pairplot(df[["Happiness_Score", "GDP_per_Capita", "Family", "Life_Expectancy", "Freedom"]],
             diag_kind="kde", plot_kws={"alpha": 0.6})
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Latest | Numeric operations |
| 📊 **Matplotlib** | Latest | Base plotting engine and multi-variable scatter |
| 🎨 **Seaborn** | Latest | Histograms, bar charts, boxplots, heatmaps, regression plots, pairplots |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Key Insights

- **GDP per capita, life expectancy, and social support (family)** show the strongest positive correlation with happiness score — countries that score well on these tend to be happier overall.
- **Trust in government and generosity** have a much weaker correlation with happiness compared to economic and health factors.
- **Western Europe, North America, and Australia/New Zealand** have the highest average happiness scores, while **Sub-Saharan Africa** has the lowest.
- The relationship between happiness and GDP is strong but not perfectly linear — some countries achieve high happiness scores despite modest GDP, suggesting factors like social support and freedom help compensate.
- Wealthier countries (high GDP) generally also have higher life expectancy, and both tend to cluster with higher happiness scores, visible in the combined scatter plot.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates a complete, realistic EDA workflow on survey data |
| 🧹 **Clean Preprocessing** | Explicitly checks for nulls/duplicates and renames columns for readability |
| 📊 **Rich Visualization Mix** | Combines histograms, bar charts, boxplots, heatmaps, regression plots, and pairplots |
| 📐 **Multi-Factor Analysis** | Goes beyond a single metric to examine how sub-factors interact |
| 🔄 **Reusable Structure** | Cleaning, ranking, and correlation logic can be reused for other yearly reports |
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

> *"Happiness is not a number, but numbers can tell us where to look for it."*

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
- 🌍 [World Happiness Report](https://worldhappiness.report/) — Source and methodology for the underlying dataset
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses and datasets

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
