<div align="center">

# -- ! Air Quality Analysis ! --
### *Time-Series Analysis of Hourly Air Quality Sensor Data with Pandas, Seaborn & Matplotlib*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"The air we breathe leaves a trail of numbers — this project follows it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [📈 Part B — Trends Over Time](#-part-b--trends-over-time)
- [🕒 Part C — Daily & Weekly Patterns](#-part-c--daily--weekly-patterns)
- [🌡️ Part D — Weather Relationships & Distributions](#️-part-d--weather-relationships--distributions)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Key Insights](#-key-insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Air Quality Analysis** project analyzes hourly air quality sensor data to understand pollution trends over time, daily and seasonal patterns, and how pollution relates to weather conditions such as temperature and humidity.

Using **Pandas** for time-series wrangling and **Seaborn/Matplotlib** for visualization, the notebook walks through cleaning a sensor dataset with placeholder missing values, building a proper datetime index, and analyzing pollutant behavior across time, day-of-week, and weather dimensions.

This project is designed to:
- Practice cleaning real-world sensor data (placeholder missing values, sparse columns, malformed trailing rows)
- Build and use a proper datetime index for time-series resampling
- Identify daily, weekly, and monthly pollution patterns
- Quantify how pollutants relate to weather conditions like temperature and humidity

---

## 🎯 Problem Statement

> **Objective:** Analyze hourly air quality sensor readings to uncover pollution trends over time and their relationship with weather conditions.

You are given an hourly sensor dataset (`Air_Quality.csv`) containing pollutant readings (CO, NOx, NO2, Benzene) alongside temperature, relative humidity, and absolute humidity. The raw file has known quirks — fully empty trailing rows/columns and missing readings encoded as `-200` instead of `NaN`. The task is to clean the data, construct a proper datetime index, and analyze how pollution varies by time of day, day of week, month, and weather condition.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Cleaning | Preprocessing | Drops empty rows/columns and converts `-200` placeholders to `NaN` |
| Missing Value Handling | Preprocessing | Drops a near-empty column and median-fills the rest |
| Datetime Construction | Preprocessing | Builds a `Datetime` index with derived Year/Month/Hour/DayOfWeek columns |
| Trend Analysis | Analysis + Viz | Daily average pollutant levels over the full monitoring period |
| Seasonal/Time Patterns | Analysis + Viz | Monthly, hourly, and day-of-week pollution patterns |
| Weather Correlation | Analysis + Viz | Heatmap and regression plots of pollutants vs. temperature/humidity |
| Distribution Analysis | Analysis + Viz | Histograms of key pollutant concentrations |

The goal is to demonstrate a **time-series exploratory data analysis (EDA) workflow**, from messy sensor data to environmental insight.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Placeholder Cleaning** | Converts sentinel `-200` values to `NaN` and drops fully empty rows/columns |
| 🩹 **Missing Value Handling** | Drops the ~90%-missing `NMHC(GT)` column; median-fills remaining sensor gaps |
| 🕓 **Datetime Index** | Combines `Date` + `Time` into a proper `Datetime` column with Year/Month/Hour/DayOfWeek features |
| 📈 **Time-Series Trends** | Daily-resampled line charts of CO, NO2, NOx, and Benzene over the full period |
| 📅 **Monthly Averages** | Grouped bar chart of average pollutant levels by month |
| 🕒 **Hourly Pattern** | Line chart revealing rush-hour peaks in pollutant concentration |
| 📆 **Day-of-Week Pattern** | Bar chart comparing average CO level across weekdays vs. weekends |
| 🔥 **Weather Correlation Heatmap** | Correlation matrix between pollutants and temperature/humidity |
| 🌡️ **Regression Plots** | CO vs. temperature and NO2 vs. relative humidity with trend lines |
| 📊 **Distribution Grid** | 2×2 histogram grid of CO, NOx, NO2, and Benzene distributions |

---

## 🏗️ Project Structure

```
📦 air-quality-analysis/
│
├── 📄 PR_4.ipynb            ← Main Jupyter notebook (entry point)
├── 📄 Air_Quality.csv       ← Source dataset (not included — see Acknowledgements)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (Air_Quality.csv)
      │
      ▼
┌─────────────────────────────┐
│ Drop Empty Rows/Columns &   │
│ Replace -200 with NaN       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Drop Sparse Column &        │
│ Median-Fill Remaining Gaps  │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Build Datetime Index &     │
│  Derive Year/Month/Hour/DOW │
└────────────┬────────────────┘
             │
     ┌───────┴────────────────┐
     ▼                        ▼
┌─────────────┐      ┌──────────────────────┐
│  Trends     │      │  Daily/Weekly/Monthly │
│  Over Time  │      │       Patterns        │
└──────┬──────┘      └──────────┬────────────┘
       │                        │
       └───────────┬────────────┘
                    ▼
┌─────────────────────────────┐
│ Weather Correlation,        │
│ Regression Plots &          │
│ Distribution Analysis       │
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
df = pd.read_csv("Air_Quality.csv")

print("Dataset Loaded Successfully!")
df.head()
```

Shape, column names, and structure are checked with `df.shape`, `df.columns`, and `df.info()`.

---

### 🩹 2. Cleaning Known Data Issues

The raw file has a few known issues: fully empty trailing rows/columns, and missing sensor readings encoded as `-200` instead of `NaN`.

**Logic:**
```python
# Drop completely empty rows and the two unnamed trailing columns
df = df.dropna(how="all")
df = df.drop(columns=[c for c in df.columns if "Unnamed" in c], errors="ignore")

# -200 is used as a placeholder for missing sensor readings — replace with NaN
numeric_cols = df.columns.drop(["Date", "Time"])
df[numeric_cols] = df[numeric_cols].replace(-200, np.nan)
```

---

### 🩺 3. Handling Missing Sensor Values

`NMHC(GT)` is missing for roughly 90% of rows and isn't usable, so it's dropped entirely. The remaining sensor columns have their gaps filled with the column median.

**Logic:**
```python
# NMHC(GT) is missing for ~90% of rows — not usable, drop it
df = df.drop(columns=["NMHC(GT)"], errors="ignore")

# Fill remaining missing sensor values with the column median
for col in df.columns.drop(["Date", "Time"]):
    df[col] = df[col].fillna(df[col].median())
```

Duplicate rows are also checked with `df.duplicated().sum()`.

---

### 🕓 4. Building a Proper Datetime Index

`Date` and `Time` are combined into a single `Datetime` column, from which `Year`, `Month`, `Hour`, and `DayOfWeek` are derived for time-based grouping and resampling.

**Logic:**
```python
df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], format="%d/%m/%Y %H:%M:%S")
df["Year"] = df["Datetime"].dt.year
df["Month"] = df["Datetime"].dt.month
df["Hour"] = df["Datetime"].dt.hour
df["DayOfWeek"] = df["Datetime"].dt.day_name()
```

---

## 📈 Part B — Trends Over Time

### 📉 5. Pollution Trend Over Time

> The dataset is resampled to daily averages and plotted as line charts for CO, NO2, NOx, and Benzene, showing the overall trend across the full monitoring period.

**Logic:**
```python
daily = df.set_index("Datetime")[["CO(GT)", "NOx(GT)", "NO2(GT)", "C6H6(GT)"]].resample("D").mean()

daily["CO(GT)"].plot(label="CO (mg/m3)")
daily["NO2(GT)"].plot(label="NO2 (µg/m3)")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `set_index("Datetime")` | Enables time-based operations on the DataFrame |
| `resample("D").mean()` | Aggregates hourly readings into daily averages |

---

### 📅 6. Monthly Average Pollution Levels

> A grouped bar chart compares average CO, NOx, NO2, and Benzene levels across the twelve months of the monitoring period.

**Logic:**
```python
monthly_avg = df.groupby("Month")[["CO(GT)", "NOx(GT)", "NO2(GT)", "C6H6(GT)"]].mean()

monthly_avg.plot(kind="bar", colormap="tab10")
```

---

## 🕒 Part C — Daily & Weekly Patterns

### 🕒 7. Hourly Pollution Pattern (Rush Hour Effect)

> A line chart of average pollutant levels by hour of day (0–23) reveals the classic morning and evening rush-hour spikes.

**Logic:**
```python
hourly_avg = df.groupby("Hour")[["CO(GT)", "NOx(GT)", "NO2(GT)"]].mean()

hourly_avg.plot(marker="o")
```

---

### 📆 8. Pollution by Day of the Week

> A bar chart, ordered Monday through Sunday, compares average CO level across each day of the week.

**Logic:**
```python
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dow_avg = df.groupby("DayOfWeek")["CO(GT)"].mean().reindex(day_order)
```

---

## 🌡️ Part D — Weather Relationships & Distributions

### 🔥 9. Relationship Between Pollution and Weather

> A correlation heatmap shows how CO, NOx, NO2, and Benzene relate to temperature (`T`), relative humidity (`RH`), and absolute humidity (`AH`).

**Logic:**
```python
weather_pollution_cols = ["CO(GT)", "NOx(GT)", "NO2(GT)", "C6H6(GT)", "T", "RH", "AH"]
corr = df[weather_pollution_cols].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
```

---

### 🌡️ 10. Pollution vs. Temperature & Humidity

> Two regression plots examine CO against temperature and NO2 against relative humidity, each with a fitted trend line over a semi-transparent scatter.

**Logic:**
```python
sns.regplot(data=df, x="T", y="CO(GT)")
sns.regplot(data=df, x="RH", y="NO2(GT)")
```

---

### 📊 11. Distribution of Key Pollutants

> A 2×2 grid of histograms with KDE overlays shows the distribution shape of CO, NOx, NO2, and Benzene concentrations.

**Logic:**
```python
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
sns.histplot(df["CO(GT)"], bins=40, kde=True, ax=axes[0, 0])
sns.histplot(df["NOx(GT)"], bins=40, kde=True, ax=axes[0, 1])
sns.histplot(df["NO2(GT)"], bins=40, kde=True, ax=axes[1, 0])
sns.histplot(df["C6H6(GT)"], bins=40, kde=True, ax=axes[1, 1])
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, datetime handling, and resampling |
| 🔢 **NumPy** | Latest | Numeric operations and NaN handling |
| 📊 **Matplotlib** | Latest | Time-series line charts and subplot grids |
| 🎨 **Seaborn** | Latest | Bar charts, regression plots, and histograms |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Key Insights

- **CO, NOx, and NO2 levels show a clear rush-hour pattern**, peaking in the morning (~8–9 AM) and evening (~6–8 PM) — consistent with traffic emissions.
- **Pollution is generally higher on weekdays** than weekends, again pointing to traffic and industrial activity as major sources.
- **Temperature is negatively correlated with CO and NOx** — pollutant concentrations tend to be higher during colder months, likely due to increased heating emissions and reduced atmospheric dispersion in winter.
- **Benzene (C6H6) and CO are strongly correlated** with each other, suggesting a shared source (most likely vehicle exhaust).
- **Relative humidity shows a weaker, mixed relationship** with pollutant levels compared to temperature.
- Monthly trends suggest **higher pollution levels in winter months** compared to summer, consistent with seasonal heating and weather-driven dispersion patterns.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates a full time-series EDA workflow, from raw sensor logs to environmental insight |
| 🧹 **Realistic Cleaning** | Handles sentinel missing-value codes, empty rows/columns, and a near-unusable column |
| 🕓 **Proper Time Handling** | Builds a true datetime index enabling resampling and time-based grouping |
| 📊 **Multi-Timescale Analysis** | Covers daily trends, monthly seasonality, hourly rush-hour effects, and weekly patterns |
| 🌡️ **Weather Context** | Ties pollution levels back to temperature and humidity for environmental interpretation |
| 🔄 **Reusable Structure** | Cleaning and datetime logic can be reused for other hourly/sensor time-series datasets |
| 🖥️ **Self-Contained** | Runs entirely within a single Jupyter notebook |

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

> *"The air we breathe leaves a trail of numbers — this project follows it."*

**🎓 Role:** Data Analyst | Python Enthusiast \
**📍 Location:** Your Location \
**🛠️ Skills:** Python · Pandas · Time-Series Analysis · Data Visualization

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Documentation](https://pandas.pydata.org/docs/) — Official Pandas reference, including time-series functionality
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Base plotting reference
- 📓 [Jupyter Project](https://jupyter.org/) — Interactive notebook environment
- 🌫️ [UCI Air Quality Dataset](https://archive.ics.uci.edu/dataset/360/air+quality) — Source and description of the underlying sensor dataset
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses and datasets

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
