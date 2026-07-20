<div align="center">

# -- ! COVID-19 Data Analysis & Visualization ! --
### *Exploring Global COVID-19 Spread with Pandas, Seaborn & Plotly*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Numbers tell the story, but visualization makes it unforgettable."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [🌍 Part B — Global & Continental Analysis](#-part-b--global--continental-analysis)
- [🏆 Part C — Country-Level Rankings](#-part-c--country-level-rankings)
- [📐 Part D — Rates & Correlations](#-part-d--rates--correlations)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **COVID-19 Data Analysis & Visualization** project is a data-analysis notebook that explores the spread of COVID-19 across countries and continents. Using **Pandas** for data wrangling, **Seaborn/Matplotlib** for statistical plots, and **Plotly** for interactive charts, the notebook walks through cleaning a raw case-tracking dataset and turning it into clear, comparable insights on cases, recoveries, deaths, and testing.

This project is designed to:
- Practice real-world data cleaning (missing values, duplicate rows, mixed granularity data)
- Separate country-level records from continent/global summary rows
- Compute derived metrics such as death rate, recovery rate, and cases per million
- Build a range of static and interactive visualizations to compare countries and continents

---

## 🎯 Problem Statement

> **Objective:** Analyze a global COVID-19 case-tracking dataset to understand how the pandemic affected different countries and continents, and communicate the findings visually.

You are given a snapshot dataset (`covid_19.csv`) containing per-country daily figures for cases, recoveries, deaths, tests, and population, along with pre-computed continent-level and global summary rows. The task is to clean the data, separate the summary rows from country-level rows, and produce a set of analyses and charts that answer questions like *"Which countries were hit hardest?"* and *"How do death and recovery rates compare across regions?"*

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Cleaning | Preprocessing | Handles missing values and duplicate rows |
| Country vs. Continent Split | Preprocessing | Separates individual countries from continent/global summary rows |
| Global Snapshot | Analysis | Total cases, recoveries, deaths, and global rates |
| Continent Comparison | Analysis + Viz | Bar charts and pie chart of cases by continent |
| Country Rankings | Analysis + Viz | Top 10 countries by cases, deaths, death rate, and cases per million |
| Correlation Analysis | Analysis + Viz | Heatmap of relationships between population, cases, recoveries, deaths, and tests |

The goal is to demonstrate an **end-to-end exploratory data analysis (EDA) workflow** using Python's data-science stack.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Missing Value Handling** | Fills missing `Recovered`, `Deaths`, and `Tests` values with 0 |
| 🔀 **Data Segmentation** | Splits continent/global summary rows from country-level rows |
| 🌍 **Global Snapshot** | Prints total cases, recoveries, deaths, and global death/recovery rates |
| 📊 **Continent-Wise Comparison** | Bar chart and grouped bar chart of cases, recovered, and deaths per continent |
| 🥧 **Interactive Pie Chart** | Plotly donut chart showing each continent's share of global cases |
| 🏆 **Top 10 Rankings** | Bar charts for top countries by total cases, total deaths, and death rate |
| 📐 **Per-Capita Analysis** | Cases per million population, avoiding bias toward large countries |
| 🔬 **Tests vs. Cases Scatter** | Interactive log-scale bubble chart (bubble size = population) |
| 🔥 **Correlation Heatmap** | Correlation matrix between population, cases, recovered, deaths, and tests |

---

## 🏗️ Project Structure

```
📦 covid-19-data-analysis/
│
├── 📄 PR_1.ipynb            ← Main Jupyter notebook (entry point)
├── 📄 covid_19.csv          ← Source dataset (not included — see Acknowledgements)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (covid_19.csv)
      │
      ▼
┌─────────────────────────────┐
│   Inspect Shape & Columns   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Handle Missing Values &    │
│  Check Duplicate Rows       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Split Country-Level Data    │
│ vs. Continent/Global Rows   │
└────────────┬────────────────┘
             │
     ┌───────┴────────┐
     ▼                ▼
┌─────────────┐   ┌──────────────────┐
│   Global    │   │   Continent &     │
│  Snapshot   │   │ Country Analysis  │
└──────┬──────┘   └────────┬─────────┘
       │                   │
       ▼                   ▼
┌─────────────────────────────┐
│  Rates, Per-Capita Metrics, │
│   Correlations & Charts     │
└─────────────────────────────┘
```

---

## 🧹 Part A — Data Loading & Cleaning

### 📝 1. Loading the Dataset

The dataset is loaded with Pandas and inspected for shape, columns, and data types.

**Logic:**
```python
df = pd.read_csv("covid_19.csv")

print("Dataset Loaded Successfully!")
df.head()
```

**Columns:** `country`, `continent`, `population`, `day`, `time`, `Cases`, `Recovered`, `Deaths`, `Tests`

---

### 🩹 2. Handling Missing Values

`Recovered`, `Deaths`, and `Tests` contain missing values for some countries where reporting was incomplete. These are filled with `0` rather than dropped, so no rows are lost.

**Logic:**
```python
df["Recovered"] = df["Recovered"].fillna(0)
df["Deaths"] = df["Deaths"].fillna(0)
df["Tests"] = df["Tests"].fillna(0)
```

Duplicate rows are also checked with `df.duplicated().sum()` before proceeding.

---

### 🔀 3. Separating Countries from Continent Summaries

The raw dataset mixes individual countries with continent-wise (and a global "All") summary rows, where the `country` column holds a continent name instead of an actual country. These are split into two frames so that country-level and continent-level analysis don't mix.

**Logic:**
```python
continent_labels = ["Africa", "South-America", "North-America", "Europe", "Asia", "Oceania", "All"]

continent_df = df[df["country"].isin(continent_labels)].copy()
country_df = df[~df["country"].isin(continent_labels)].copy()
```

---

## 🌍 Part B — Global & Continental Analysis

### 🔢 4. Global Snapshot

> Uses the "All" row from the continent summary to report worldwide totals and rates.

**Logic:**
```python
global_row = continent_df[continent_df["country"] == "All"].iloc[0]

print("Total Cases:     {:,.0f}".format(global_row["Cases"]))
print("Total Recovered: {:,.0f}".format(global_row["Recovered"]))
print("Total Deaths:    {:,.0f}".format(global_row["Deaths"]))
print("Global Death Rate: {:.2f}%".format(global_row["Deaths"] / global_row["Cases"] * 100))
print("Global Recovery Rate: {:.2f}%".format(global_row["Recovered"] / global_row["Cases"] * 100))
```

**Sample Output:**
```
GLOBAL COVID-19 SNAPSHOT
Total Cases:     704,753,890
Total Recovered: 675,619,811
Total Deaths:    7,010,681
Global Death Rate: 0.99%
Global Recovery Rate: 95.87%
```

---

### 📊 5. Continent-Wise Comparison

> A horizontal bar chart ranks continents by total cases, and a grouped bar chart (log scale) compares Cases, Recovered, and Deaths side by side per continent.

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `sort_values()` | Orders continents by total cases before plotting |
| `pd.melt()` | Reshapes wide Cases/Recovered/Deaths columns into a long format for grouped bars |
| `sns.barplot()` | Horizontal and grouped bar charts with the `viridis` palette |
| Log scale y-axis | Keeps small and large continents readable on the same chart |

---

### 🥧 6. Interactive Share-of-Cases Pie Chart

> A Plotly donut chart shows each continent's share of global cases interactively.

**Logic:**
```python
fig = px.pie(continent_only, names="country", values="Cases",
             title="Share of Global COVID-19 Cases by Continent", hole=0.4)
fig.show()
```

---

## 🏆 Part C — Country-Level Rankings

### 🔟 7. Top 10 Countries by Total Cases & Deaths

> Two horizontal bar charts identify the ten most-affected countries by absolute case count and by absolute death count.

**Logic:**
```python
top_cases = country_df.sort_values("Cases", ascending=False).head(10)
top_deaths = country_df.sort_values("Deaths", ascending=False).head(10)
```

---

### ☠️ 8. Death Rate & Recovery Rate

> For countries with more than 10,000 cases (to avoid small-outbreak distortion), death rate (`Deaths / Cases`) and recovery rate (`Recovered / Cases`) are computed and the top 10 by death rate are visualized.

**Logic:**
```python
analysis_df = country_df[country_df["Cases"] > 10000].copy()

analysis_df["Death_Rate_%"] = (analysis_df["Deaths"] / analysis_df["Cases"] * 100).round(2)
analysis_df["Recovery_Rate_%"] = (analysis_df["Recovered"] / analysis_df["Cases"] * 100).round(2)
```

---

### 📐 9. Cases per Million Population

> Raw case counts favor large countries, so cases are normalized by population (`Cases / population * 1,000,000`) to give a fairer, per-capita ranking of the hardest-hit countries.

**Logic:**
```python
pop_df["Cases_per_Million"] = (pop_df["Cases"] / pop_df["population"] * 1_000_000).round(0)
```

---

## 📐 Part D — Rates & Correlations

### 🧪 10. Testing vs. Reported Cases

> An interactive log-log scatter plot (Plotly) compares tests conducted against reported cases, with bubble size representing population and color representing continent — useful for spotting whether more testing correlates with more reported cases.

---

### 🔥 11. Correlation Heatmap

> A Seaborn heatmap shows the correlation coefficients between `population`, `Cases`, `Recovered`, `Deaths`, and `Tests`, helping identify which metrics move together.

**Logic:**
```python
numeric_cols = ["population", "Cases", "Recovered", "Deaths", "Tests"]
corr = country_df[numeric_cols].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Latest | Numeric operations |
| 📊 **Matplotlib** | Latest | Base plotting engine |
| 🎨 **Seaborn** | Latest | Statistical bar charts and heatmaps |
| ⚡ **Plotly Express** | Latest | Interactive pie chart and scatter plot |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Global Snapshot** — worldwide totals for cases, recoveries, and deaths with computed rates
- 🌍 **Continent Comparison** — ranked bar charts and an interactive pie chart of case share
- 🏆 **Top 10 Rankings** — countries with the highest cases, deaths, death rate, and cases per million
- 📐 **Death & Recovery Rates** — normalized rates for countries with more than 10,000 cases
- 🔬 **Testing Relationship** — interactive scatter plot exploring tests vs. reported cases
- 🔥 **Correlation Heatmap** — relationships between population, cases, recoveries, deaths, and tests

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates a complete, realistic EDA workflow from raw CSV to insight |
| 🧹 **Robust Cleaning** | Explicitly handles missing values, duplicates, and mixed-granularity rows |
| 📊 **Multiple Viz Libraries** | Combines static (Matplotlib/Seaborn) and interactive (Plotly) visualizations |
| 📐 **Fair Comparisons** | Uses rates and per-capita metrics instead of raw counts alone |
| 🔄 **Reusable Structure** | Cleaning and splitting logic can be reused for similar time-series case datasets |
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

> *"Data doesn't lie — but it needs a good chart to be heard."*

**🎓 Role:** Data Analyst | Python Enthusiast \
**📍 Location:** Your Location \
**🛠️ Skills:** Python · Pandas · Data Visualization · Exploratory Data Analysis

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Documentation](https://pandas.pydata.org/docs/) — Official Pandas reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- ⚡ [Plotly Express Documentation](https://plotly.com/python/plotly-express/) — Interactive chart reference
- 📓 [Jupyter Project](https://jupyter.org/) — Interactive notebook environment
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses and datasets

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
