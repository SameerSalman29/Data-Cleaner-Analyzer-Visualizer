# analysis functions here
import pandas as pd

def analyze_data(df: pd.DataFrame) -> str:
    report = []

    report.append("### Summary Statistics\n")
    report.append(df.describe(include='all').to_markdown())

    report.append("\n### Correlation Matrix\n")
    report.append(df.corr().to_markdown())

    report.append("\n### Skewness\n")
    report.append(df.skew().to_markdown())

    report.append("\n### Cardinality\n")
    for col in df.columns:
        report.append(f"{col}: {df[col].nunique()} unique values")

    # Detect date columns
    date_cols = df.select_dtypes(include='datetime').columns
    if len(date_cols) > 0:
        report.append("\n### Date Columns Detected\n")
        for col in date_cols:
            report.append(f"{col}: {df[col].min()} to {df[col].max()}")

    return "\n".join(report)
