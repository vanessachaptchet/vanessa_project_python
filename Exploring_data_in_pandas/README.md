# World Population Analysis

## Project Overview

This project explores global population data using Python (Pandas) and data visualization.

The goal is to clean, analyze, and extract meaningful insights from population datasets by focusing on trends across continents and countries.

---

## Data Preparation

The dataset was prepared by:

- Removing duplicates  
- Handling missing values  
- Formatting columns  
- Standardizing data types  

---

##  Key Analyses

### 1. Population by Continent

- Grouped data using `groupby`
- Calculated population statistics
- Compared continents

---

### 2. Most Populated Country per Continent (2022)

- Used `groupby` and `idxmax()`
- Selected the country with the highest population in each continent

 Insight:  
A few countries dominate the population in each continent.

---

### 3. Least Populated Country per Continent (2022)

- Used `groupby` and `idxmin()`
- Selected the country with the lowest population in each continent

 Insight:  
Population distribution is very uneven across regions.

---

### 4. Focus Analysis: Africa (2022)

To make the analysis clearer, we focused on Africa.

####  Top 10 Most Populated Countries

- Selected using `nlargest()`
- Displayed using bar charts

#### Top 10 Least Populated Countries

- Selected using `nsmallest()`
- Compared side by side with the top 10

Insight:  
There is a strong population imbalance within Africa, with a few countries having very large populations and others having very small populations.

---

## Visualization

- Bar charts for comparisons  
- Subplots to display multiple charts  
- Values displayed on bars for readability  

---

## Tools Used

- Python  
- Pandas  
- Matplotlib  

---

## Key Learnings

- Data filtering and grouping  
- Using `groupby`, `idxmax`, `idxmin`  
- Extracting top and bottom values  
- Creating clear visualizations  
- Formatting numbers for better readability  

---

## Conclusion

This project shows how data analysis can help understand population distribution across the world.

By combining grouping, filtering, and visualization, we can clearly identify patterns and differences between countries and continents.

---

## Author

Vanessa Chaptchet