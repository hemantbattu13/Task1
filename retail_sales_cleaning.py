# Week 1: Retail Sales Data Cleaning and Preprocessing
# Install: pip install pandas
import pandas as pd

# Replace this filename with the dataset downloaded from Kaggle.
df = pd.read_csv("Retail_Sales.csv")

print("Shape:", df.shape)
print(df.head())
print(df.info())
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Remove exact duplicate rows
df = df.drop_duplicates()

# Example: convert a date column (change "Date" to your actual column name)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Fill numeric missing values with median
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values with mode
for col in df.select_dtypes(include=["object", "category"]).columns:
    mode = df[col].mode()
    if not mode.empty:
        df[col] = df[col].fillna(mode.iloc[0])

# Save the cleaned data
df.to_csv("Cleaned_Retail_Sales.csv", index=False)
print("Cleaned dataset saved.")
