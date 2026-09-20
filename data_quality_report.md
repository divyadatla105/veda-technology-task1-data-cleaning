# Data Quality Report — Veda Technology Task 1

## Project
**Data Cleaning and Preprocessing — Titanic Practice Dataset**

### Objective
Prepare a raw passenger dataset for reliable analysis by identifying and fixing missing values, duplicates, inconsistent text formats, and incorrect data types.

## Dataset note
This submission uses a **20-row practice subset based on publicly documented Titanic passenger records**. Data-quality problems were deliberately introduced into a working copy so that the internship task requirements can be demonstrated reproducibly. The original public Titanic training data contains 891 records and the standard fields used here.

## Source
Public Titanic dataset reference:  
https://github.com/datasciencedojo/datasets/blob/master/titanic.csv

## Tools
- Python
- Pandas
- Excel

## Before cleaning
- Rows: **22**
- Columns: **12**
- Exact duplicate rows: **1**
- Duplicate PassengerId values: **2**
- Null values detected directly: **1**
- Additional unusable/missing values identified during type conversion: **3 Age values**
- Data types were inconsistent in several columns because of intentionally introduced text values.

## Cleaning decisions
1. **Age:** Converted text to numeric. Missing/unusable values were imputed using the median age (**26.0**).
2. **Embarked:** Standardized to `S`, `C`, or `Q`. Missing value was filled with the mode (**S**).
3. **Cabin:** Blank cabin values were converted to `Unknown` rather than deleting rows.
4. **Sex:** Standardized casing and whitespace.
5. **Fare:** Removed currency symbol and converted to numeric.
6. **Pclass:** Extracted the numeric class from inconsistent text.
7. **Survived:** Converted text-form numeric values to integer.
8. **Name/Ticket/Cabin:** Trimmed whitespace and normalized repeated spaces.
9. **Duplicates:** Removed one exact duplicate and one duplicate PassengerId record.

## After cleaning
- Rows: **20**
- Columns: **12**
- Exact duplicate rows: **0**
- Duplicate PassengerId values: **0**
- Null values: **0**
- Valid Sex categories: **female, male**
- Valid Embarked categories: **C, Q, S**

## Validation checks
The cleaned dataset passes the following checks:
- No exact duplicate rows.
- No duplicate PassengerId values.
- No missing values in the final dataset.
- Age and Fare are numeric.
- Pclass, SibSp, Parch, PassengerId and Survived are integer-type columns.
- Sex contains only `male` or `female`.
- Embarked contains only `S`, `C`, or `Q`.

## Conclusion
The dataset is now in a consistent, analysis-ready structure. The cleaning process is reproducible through `clean_titanic.py`, and the decisions are documented in `change_log.csv`.
