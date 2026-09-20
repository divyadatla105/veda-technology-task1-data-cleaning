import pandas as pd

INPUT = "raw_titanic_dirty.csv"
OUTPUT = "cleaned_titanic.csv"

cols = ["PassengerId","Survived","Pclass","Name","Sex","Age",
        "SibSp","Parch","Ticket","Fare","Cabin","Embarked"]

df = pd.read_csv(INPUT)

# Inventory
print("Before cleaning:")
print(df.info())
print("\nMissing values:\n", df.isna().sum())
print("\nExact duplicates:", df.duplicated().sum())
print("Duplicate PassengerId:", df["PassengerId"].duplicated().sum())

# Text cleanup
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

for col in ["Name", "Ticket", "Cabin"]:
    df[col] = df[col].apply(
        lambda x: " ".join(x.split()) if isinstance(x, str) and x.strip()
        else (None if isinstance(x, str) else x)
    )

# Standardize categories
df["Sex"] = df["Sex"].astype("string").str.strip().str.lower()
df["Sex"] = df["Sex"].replace({"m": "male", "f": "female"})

df["Embarked"] = df["Embarked"].astype("string").str.strip().str.upper()
df["Embarked"] = df["Embarked"].replace({
    "SOUTHAMPTON": "S",
    "CHERBOURG": "C",
    "QUEENSTOWN": "Q"
})
df.loc[~df["Embarked"].isin(["S", "C", "Q"]), "Embarked"] = pd.NA

# Correct data types
df["PassengerId"] = pd.to_numeric(df["PassengerId"], errors="coerce").astype("Int64")
df["Survived"] = (
    df["Survived"]
      .replace({"Yes": 1, "No": 0, "yes": 1, "no": 0})
      .pipe(pd.to_numeric, errors="coerce")
      .astype("Int64")
)
df["Pclass"] = df["Pclass"].astype("string").str.extract(r"(\d+)")[0]
df["Pclass"] = pd.to_numeric(df["Pclass"], errors="coerce").astype("Int64")
df["Age"] = pd.to_numeric(
    df["Age"].astype("string").str.extract(r"([-+]?\d*\.?\d+)")[0],
    errors="coerce"
)
df["Fare"] = pd.to_numeric(
    df["Fare"].astype("string").str.replace(r"[$₹€,]", "", regex=True),
    errors="coerce"
)
df["SibSp"] = pd.to_numeric(df["SibSp"], errors="coerce").astype("Int64")
df["Parch"] = pd.to_numeric(df["Parch"], errors="coerce").astype("Int64")

# Missing-value treatment
age_median = df["Age"].median()
embarked_mode = df["Embarked"].mode(dropna=True).iloc[0]

df["Age"] = df["Age"].fillna(age_median)
df["Embarked"] = df["Embarked"].fillna(embarked_mode)
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Duplicate handling
df = df.drop_duplicates(keep="first")
df = df.drop_duplicates(subset=["PassengerId"], keep="first")

df["Fare"] = df["Fare"].round(4)
df = df[cols]

# Validation
assert df.duplicated().sum() == 0
assert df["PassengerId"].duplicated().sum() == 0
assert df.isna().sum().sum() == 0
assert set(df["Sex"].unique()) <= {"male", "female"}
assert set(df["Embarked"].unique()) <= {"S", "C", "Q"}

df.to_csv(OUTPUT, index=False)

print("\nAfter cleaning:")
print(df.info())
print("\nMissing values:\n", df.isna().sum())
print("\nExact duplicates:", df.duplicated().sum())
print("Duplicate PassengerId:", df["PassengerId"].duplicated().sum())
print(f"\nSaved cleaned dataset to {OUTPUT}")
