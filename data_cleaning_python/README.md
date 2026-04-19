# Data Cleaning Project – Customer Call List

## Project Overview
This project focuses on cleaning and preparing a raw customer dataset using Python (Pandas).
The dataset contains inconsistent formats, missing values, and unnecessary columns.

The goal is to transform the data into a clean and usable format for analysis.

---

## Tools Used
- Python
- Pandas
- Jupyter Notebook

---

## 📂 Dataset
- File: Customer Call List.xlsx
- Contains customer information such as:
  - Name
  - Phone Number
  - Address
  - Paying Customer
  - Do Not Contact

---

## 🔧 Data Cleaning Steps

### 1. Remove duplicates
- Deleted duplicate rows

### 2. Drop unnecessary columns
- Removed Not_Useful_Column

### 3. Clean text data
- Trimmed spaces from names

### 4. Format phone numbers
- Removed special characters
- Converted to standard format: XXX-XXX-XXXX

### 5. Handle missing values
- Replaced NaN, N/a, etc.
- Cleaned empty phone numbers

### 6. Standardize categorical data
- Converted:
  - Y → Yes
  - N → No

### 7. Filter data
- Removed customers who should not be contacted

---

## Result
The dataset is now:
- Clean
- Consistent
- Ready for analysis

---

## Future Improvements
- Add data visualization
- Perform exploratory data analysis (EDA)
- Automate cleaning pipeline

---

## Author
Vanessa CHAPTCHET
