<div align="center">

# -- ! Stock Market Analysis ! --
### *Cross-Sectional Analysis of a Single-Day Stock Market Snapshot with Pandas, Seaborn & Matplotlib*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"One trading day, ~1,500 stories — this is what the market looked like on a single snapshot in time."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [⚠️ A Note on the Data](#️-a-note-on-the-data)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [🏭 Part B — Sector & Category Breakdown](#-part-b--sector--category-breakdown)
- [📊 Part C — Gainers, Losers & Price Distribution](#-part-c--gainers-losers--price-distribution)
- [📉 Part D — Volatility & Correlation](#-part-d--volatility--correlation)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Key Insights](#-key-insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Stock Market Analysis** project explores a single-day snapshot of the stock market covering roughly 1,568 listed shares — including sector, trading category/signal, last traded price, and the day's high/low. Rather than a time-series analysis, this notebook performs a thorough **cross-sectional analysis**: comparing sectors, identifying top gainers and losers, and examining price and intraday volatility patterns across the market on this one trading day.

Using **Pandas** for cleaning and aggregation and **Seaborn/Matplotlib** for visualization, the notebook walks through fixing spreadsheet-export data issues, comparing sector performance, ranking individual shares, and quantifying volatility and its relationship to price movement.

This project is designed to:
- Practice cleaning messy, spreadsheet-exported financial data (Excel error strings, mixed-type columns, unusable columns)
- Compare performance and composition across market sectors
- Rank individual shares by gains, losses, and volatility
- Examine correlations between price, percentage change, and volatility measures

---

## ⚠️ A Note on the Data

This dataset is a **single-day snapshot** across ~1,568 listed shares (with sector, category/signal, last traded price, and day's high/low), **not a multi-day historical price series**. That means classic time-series techniques like moving averages and price-over-time trend lines aren't possible with this file.

Instead, this notebook does a thorough **cross-sectional analysis**: comparing sectors, finding top gainers/losers, and looking at price and volatility patterns across the market on this trading day.

> To get the full "trend over time" and moving-average analysis, a proper historical **OHLCV** dataset (e.g. from Yahoo Finance / `yfinance` for a specific stock or index, with a date column and daily Open/High/Low/Close/Volume) would be needed instead of this snapshot file.

---

## 🎯 Problem Statement

> **Objective:** Analyze a single-day cross-section of the stock market to compare sector performance, identify top movers, and understand price and volatility patterns.

You are given a dataset (`Stock_Market_Data.csv`) containing one row per listed share, with fields for sector, trading category/signal, last traded price, day's high/low, and percentage change — but no date/time dimension. The task is to clean spreadsheet-export artifacts out of the data, then analyze how sectors and individual shares compare to one another on price, movement, and volatility for this trading day.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Cleaning | Preprocessing | Drops unusable columns, replaces Excel error strings, coerces mixed-type columns |
| Sector Overview | Analysis + Viz | Number of listed shares and average % change by sector |
| Category Breakdown | Analysis + Viz | Distribution and performance by trading category/signal |
| Gainers & Losers | Analysis + Viz | Top 10 shares by percentage gain and by percentage loss |
| Price Distribution | Analysis + Viz | Log-scale histogram of last traded price across all shares |
| Volatility Analysis | Analysis + Viz | Day's high-low range as a volatility proxy, by share and by sector |
| Correlation Analysis | Analysis + Viz | Heatmap of price, % change, and volatility measures |

The goal is to demonstrate a **cross-sectional exploratory data analysis (EDA) workflow** appropriate for a single-point-in-time financial dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Spreadsheet Cleanup** | Drops corrupted `RM`/`Up` columns and replaces `#N/A`/`#REF!`/`#VALUE!` errors with `NaN` |
| 🔢 **Type Coercion** | Forces `% High Movt` to numeric, coercing stray text to `NaN` |
| 🏭 **Sector Composition** | Bar chart of the number of listed shares per sector (top 15) |
| 📊 **Sector Performance** | Diverging bar chart of best and worst performing sectors by average % change |
| 🏷️ **Category/Signal Breakdown** | Distribution and average performance by trading category (e.g. Buy, Exit, HWV, BWLV) |
| 📈 **Top Gainers & Losers** | Bar charts of the 10 biggest gaining and losing shares by % change |
| 💰 **Log-Scale Price Distribution** | Histogram of last traded price on a log10 scale to handle a huge price range |
| 📉 **Volatility Proxy** | Day's High–Low range (%) used to rank the most volatile shares and sectors |
| 🔥 **Correlation Heatmap** | Correlation matrix between price, % change, and volatility measures |

---

## 🏗️ Project Structure

```
📦 stock-market-analysis/
│
├── 📄 PR_5.ipynb                  ← Main Jupyter notebook (entry point)
├── 📄 Stock_Market_Data.csv       ← Source dataset (not included — see Acknowledgements)
│
└── 📄 README.md                   ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (Stock_Market_Data.csv)
      │
      ▼
┌─────────────────────────────┐
│   Inspect Shape & Columns   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Drop Unusable Columns,      │
│ Fix Excel Errors & Types    │
└────────────┬────────────────┘
             │
     ┌───────┴────────────────┐
     ▼                        ▼
┌─────────────┐      ┌──────────────────────┐
│  Sector &   │      │  Gainers, Losers &    │
│  Category   │      │  Price Distribution   │
└──────┬──────┘      └──────────┬────────────┘
       │                        │
       └───────────┬────────────┘
                    ▼
┌─────────────────────────────┐
│ Volatility Analysis &       │
│ Correlation Heatmap         │
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
df = pd.read_csv("Stock_Market_Data.csv")

print("Dataset Loaded Successfully!")
df.head()
```

Shape, column names, and summary statistics are checked with `df.shape`, `df.columns`, `df.info()`, and `df.describe()`.

---

### 🩹 2. Cleaning Spreadsheet-Export Artifacts

The raw file carries typical spreadsheet-export issues: unusable columns, Excel error strings, and a numeric column that was partly read as text.

**Logic:**
```python
# "RM" and "Up" are mostly missing/corrupted (Excel #REF! errors, stray text) — not usable, drop them
df = df.drop(columns=["RM", "Up"], errors="ignore")

# Replace any remaining Excel error strings with NaN
df = df.replace(["#N/A", "#REF!", "#VALUE!"], np.nan)

# % High Movt was read as text in places — force numeric
df["% High Movt"] = pd.to_numeric(df["% High Movt"], errors="coerce")

# Rows with no price data at all aren't useful for this analysis
df = df.dropna(subset=["Last Traded Price"])
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `drop(columns=..., errors="ignore")` | Safely removes columns that are mostly corrupted/unusable |
| `replace([...], np.nan)` | Normalizes known Excel error strings to proper missing values |
| `pd.to_numeric(..., errors="coerce")` | Converts a mixed text/numeric column, turning invalid entries into `NaN` |
| `dropna(subset=[...])` | Removes rows with no usable price, since price is central to every analysis |

Duplicate rows are also checked with `df.duplicated().sum()` before cleaning.

---

## 🏭 Part B — Sector & Category Breakdown

### 📊 3. Sector-Wise Overview

> A horizontal bar chart shows the number of listed shares per sector (top 15), and a diverging bar chart highlights the best and worst performing sectors by average percentage change.

**Logic:**
```python
sector_counts = df["Sector"].value_counts().head(15)

sector_avg_change = df.groupby("Sector")["Percentage Change"].mean().dropna().sort_values(ascending=False)
top_bottom = pd.concat([sector_avg_change.head(8), sector_avg_change.tail(8)])
```

---

### 🏷️ 4. Trading Category / Signal Breakdown

> Each share is tagged with a category (e.g. Buy, Exit, HWV, BWLV) — likely a technical screener signal. A bar chart shows the distribution of shares by category, and average percentage change is compared across categories.

**Logic:**
```python
category_counts = df["Category"].value_counts()

df.groupby("Category")["Percentage Change"].mean().dropna().sort_values(ascending=False)
```

---

## 📊 Part C — Gainers, Losers & Price Distribution

### 📈 5. Top 10 Gainers and Losers

> Two bar charts rank the ten shares with the largest positive and largest negative percentage change on the day.

**Logic:**
```python
top_gainers = df.dropna(subset=["Percentage Change"]).sort_values("Percentage Change", ascending=False).head(10)
top_losers = df.dropna(subset=["Percentage Change"]).sort_values("Percentage Change", ascending=True).head(10)
```

---

### 💰 6. Price Distribution

> Share prices span a huge range (₹0.15 to ₹65,000+), so the distribution is visualized on a log10 scale to make it interpretable.

**Logic:**
```python
sns.histplot(np.log10(df["Last Traded Price"].dropna()), bins=40, kde=True, color="steelblue")
```

---

## 📉 Part D — Volatility & Correlation

### 📉 7. Intraday Volatility (High − Low Range)

> The day's high and low price are used as a simple proxy for volatility, ranking both the most volatile individual shares and the most volatile sectors on average.

**Logic:**
```python
df["Day_Range_%"] = ((df["High Price"] - df["Low Price"]) / df["Low Price"]) * 100

most_volatile = df.dropna(subset=["Day_Range_%"]).sort_values("Day_Range_%", ascending=False).head(10)
sector_volatility = df.groupby("Sector")["Day_Range_%"].mean().dropna().sort_values(ascending=False).head(10)
```

---

### 🔥 8. Correlation Between Numeric Indicators

> A correlation heatmap shows how last traded price, percentage change, high/low price, `% High Movt`, and the derived day-range volatility relate to one another.

**Logic:**
```python
numeric_cols = ["Last Traded Price", "Percentage Change", "High Price", "Low Price", "% High Movt", "Day_Range_%"]
corr = df[numeric_cols].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Latest | Numeric operations and log-scale transforms |
| 📊 **Matplotlib** | Latest | Base plotting engine |
| 🎨 **Seaborn** | Latest | Bar charts, histograms, and heatmaps |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Key Insights

- This dataset is a **single-day cross-section**, not a historical series — so the analysis focuses on how stocks compare to each other on this day, not trends over time.
- **Sector performance varied widely** on this day — some sectors averaged solid gains while others averaged losses, visible in the best/worst sector chart.
- The **"RM" and "Up" columns were unusable** — largely missing or corrupted with spreadsheet errors (`#REF!`) and stray text — and were dropped during cleaning.
- Share prices are **extremely right-skewed** (from under ₹1 to over ₹65,000), which is why a log scale was needed to see the distribution clearly.
- **Day-range volatility (High-Low %) varies a lot by sector**, with some sectors showing far wider intraday swings than others.
- **Percentage change and day-range volatility show a positive relationship** — stocks with bigger price swings tend to also show larger percentage moves, which makes intuitive sense.

> **To extend this into a "trend over time" / moving-average analysis**, a proper historical OHLCV dataset (e.g. from Yahoo Finance / `yfinance` for a specific stock or index, with a date column and daily Open/High/Low/Close/Volume) would be needed instead of this snapshot file.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates cross-sectional EDA — a different skillset from typical time-series stock analysis |
| 🧹 **Realistic Cleaning** | Handles genuine spreadsheet-export issues: error strings, mixed types, unusable columns |
| 🏭 **Sector-Level Insight** | Goes beyond individual stocks to compare performance and volatility at the sector level |
| 📉 **Practical Volatility Proxy** | Derives a day-range volatility measure from data that lacks intraday tick data |
| 🔄 **Reusable Structure** | Cleaning and ranking logic can be reused for other single-snapshot market data exports |
| 🖥️ **Self-Contained** | Runs entirely within a single Jupyter notebook |
| 📖 **Transparent Limitations** | Explicitly documents what the dataset can and cannot support, avoiding misleading trend claims |

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

> *"One trading day, ~1,500 stories — this is what the market looked like on a single snapshot in time."*

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
- 💹 [yfinance](https://pypi.org/project/yfinance/) — Recommended source for historical OHLCV data if extending this project to a time-series analysis
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses and datasets

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
