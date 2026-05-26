import pandas as pd
import numpy as np

print("Program Started")

# Load Dataset
df = pd.read_csv("IMDb Movies India.csv", encoding='latin1')

# First 5 Rows
print("\n===== First 5 Rows =====")
print(df.head())

# Shape
print("\n===== Shape =====")
print(df.shape)

# Info
print("\n===== Dataset Info =====")
print(df.info())

# Statistical Summary
print("\n===== Statistical Summary =====")
print(df.describe())

# Missing Values
print("\n===== Missing Values =====")
print(df.isnull().sum())

# Numerical Columns
print("\n===== Numerical Columns =====")
print(df.select_dtypes(include=np.number).columns)

# Categorical Columns
print("\n===== Categorical Columns =====")
print(df.select_dtypes(include='object').columns)

# Unique Values
print("\n===== Unique Values in Categorical Columns =====")

for col in df.select_dtypes(include='object').columns:
    print(f"\nColumn Name: {col}")
    print(df[col].unique())

# Data Types
print("\n===== Data Types =====")
print(df.dtypes)

print("\nTask Completed Successfully")
