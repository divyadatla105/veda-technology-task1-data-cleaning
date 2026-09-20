# Veda Technology — Task 1: Data Cleaning and Preprocessing

## Candidate Project
**Data Analytics Track — Level 1, Day 1**

### Objective
Clean and prepare a raw dataset containing null values, duplicates, inconsistent formats, and incorrect data types so that it is ready for reliable analysis.

## Dataset
A 20-row practice subset based on publicly documented Titanic passenger records. Data-quality problems were intentionally introduced into the working copy to demonstrate the required cleaning techniques.

Source reference:
https://github.com/datasciencedojo/datasets/blob/master/titanic.csv

## Tools
- Python
- Pandas
- Excel

## Files
| File | Purpose |
|---|---|
| `raw_titanic_dirty.csv` | Raw working dataset containing deliberate data-quality issues |
| `cleaned_titanic.csv` | Final analysis-ready dataset |
| `change_log.csv` | Documents each cleaning decision |
| `data_quality_report.md` | Before/after quality assessment |
| `clean_titanic.py` | Reproducible Pandas cleaning script |
| `titanic_data_cleaning.xlsx` | Excel workbook with Raw, Cleaned, Change Log and Validation sheets |
| `requirements.txt` | Python dependency |
| `submission_checklist.txt` | Final submission checklist |

## Cleaning workflow
1. Inspect structure and data types using `info()`.
2. Check missing values using `isna().sum()`.
3. Check duplicates using `duplicated().sum()`.
4. Standardize text casing and whitespace.
5. Standardize date/category/unit formats where applicable.
6. Convert incorrect data types.
7. Handle missing values based on column meaning.
8. Remove exact duplicate rows.
9. Remove duplicate PassengerId records.
10. Re-run quality checks after cleaning.

## Key decisions
- **Age:** missing/unusable values → median age (26.0)
- **Embarked:** missing value → mode (S)
- **Cabin:** blank values → `Unknown`
- **Sex:** standardized to `male` / `female`
- **Embarked:** standardized to `S` / `C` / `Q`
- **Fare:** currency symbol removed and converted to numeric
- **Pclass:** numeric class extracted from inconsistent text such as `3rd`
- **Duplicates:** exact duplicate and duplicate PassengerId record removed

## Result
**Before:** 22 rows, 1 exact duplicate, 2 duplicate PassengerId records, and multiple formatting/type/missing-value issues.

**After:** 20 rows, 0 exact duplicates, 0 duplicate PassengerId values, and 0 missing values.

## How to run
```bash
pip install -r requirements.txt
python clean_titanic.py
```

## Suggested GitHub repository name
`veda-technology-task1-data-cleaning`

## Suggested GitHub description
`Data cleaning and preprocessing project using Python, Pandas and Excel — Veda Technology Internship Task 1.`

## Interview questions — short answers

### 1. How do you decide whether to drop or impute a missing value?
I first assess the percentage of missing data, the importance of the field, and whether a reliable replacement can be derived. I use imputation when the record remains useful and a defensible value such as a median or mode is available. I drop records only when missingness makes the row unusable or the missing proportion is too high.

### 2. What is the difference between a duplicate row and a duplicate key?
A duplicate row is a repeated record across all relevant columns. A duplicate key means the field that should uniquely identify a record, such as PassengerId, appears more than once. A duplicate key can exist even when the other columns are not identical.

### 3. How would you handle outliers differently from missing values?
Missing values represent unavailable information, so I consider deletion, imputation or a missing flag. Outliers are actual observations that may be valid or erroneous. I investigate their business/data context first rather than automatically deleting them.

### 4. How do you validate that a dataset is clean?
I rerun structural checks after cleaning: row/column counts, null counts, duplicate counts, data types, valid category values, numeric ranges and key uniqueness. I also compare before-and-after results to confirm that the intended issues were actually resolved.
