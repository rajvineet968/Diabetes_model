import pandas as pd
import joblib
import os

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

REFERENCE_PATH = "artifacts/reference_data.pkl"
CURRENT_DATA_PATH = "data/indian_insurance_data.csv"
REPORT_PATH = "reports/data_drift_report.html"

os.makedirs("reports", exist_ok=True)

# Load data
reference_df = joblib.load(REFERENCE_PATH)
current_df = pd.read_csv(CURRENT_DATA_PATH)

# Generate report
report = Report(metrics=[DataDriftPreset()])
report.run(
    reference_data=reference_df,
    current_data=current_df
)

# Save HTML
report.save_html(REPORT_PATH)

print(f"✅ HTML drift report generated at: {REPORT_PATH}")
