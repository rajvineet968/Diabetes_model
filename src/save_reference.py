import pandas as pd
import joblib
import os

DATA_PATH = "data/indian_insurance_data.csv"  # 🔴 CHANGE IF NEEDED
TARGET_COL = "diabetes"  # 🔴 CONFIRMED FROM YOUR DATA

os.makedirs("artifacts", exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)

print("Columns found:", list(df.columns))

# Drop target column
X = df.drop(columns=[TARGET_COL])

# Save reference data
joblib.dump(X, "artifacts/reference_data.pkl")

print("✅ Reference data saved successfully")
