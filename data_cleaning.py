import pandas as pd
import numpy as np

# 1. Load dataset
df = pd.read_csv("students_raw.csv")
print("Raw data:")
print(df)

# 2. Strip spaces and normalize Name
df["Name"] = df["Name"].astype(str).str.strip().str.title()

# 3. Standardize Gender
df["Gender"] = df["Gender"].astype(str).str.strip().str.lower()
gender_map = {"m": "Male", "male": "Male", "f": "Female", "female": "Female"}
df["Gender"] = df["Gender"].replace({"nan": np.nan})
df["Gender"] = df["Gender"].map(gender_map)

# 4. Clean Marks column: convert to numeric and coerce errors to NaN
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# 5. Remove impossible values: marks < 0 or > 100 -> NaN
df.loc[(df["Marks"] < 0) | (df["Marks"] > 100), "Marks"] = np.nan

# 6. Impute missing Marks with class median
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# 7. Convert Class to int (if possible)
try:
    df["Class"] = df["Class"].astype(int)
except:
    pass

# 8. Show cleaned data and export
print("\nCleaned data:")
print(df)

df.to_csv("students_cleaned.csv", index=False)
print("\nSaved students_cleaned.csv")


