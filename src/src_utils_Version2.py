"""
Utility functions for data cleaning, analysis, and visualization.

Author: Sameer Salman
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def load_dataset(path: str) -> pd.DataFrame:
    """Load a dataset from CSV and return a DataFrame."""
    try:
        df = pd.read_csv(path)
        print(f"Loaded dataset with shape {df.shape} from {path}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        raise

def handle_missing(df: pd.DataFrame, strategy: str = 'median') -> pd.DataFrame:
    """Impute missing values using specified strategy."""
    if strategy == 'median':
        return df.fillna(df.median(numeric_only=True))
    elif strategy == 'mean':
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError("Unsupported imputation strategy.")

def plot_correlation_heatmap(df: pd.DataFrame, output_path: Path = None):
    """Plot and optionally save correlation heatmap."""
    plt.figure(figsize=(10,8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    if output_path:
        plt.savefig(output_path)
        print(f"Correlation heatmap saved to {output_path}")
    else:
        plt.show()

def remove_outliers(df: pd.DataFrame, z_thresh: float = 3.0) -> pd.DataFrame:
    """Remove rows with outliers based on Z-score threshold."""
    z_scores = np.abs((df - df.mean()) / df.std())
    filtered_df = df[(z_scores < z_thresh).all(axis=1)]
    print(f"Removed outliers; new shape: {filtered_df.shape}")
    return filtered_df

def save_cleaned_data(df: pd.DataFrame, path: Path):
    """Save cleaned data to CSV."""
    df.to_csv(path, index=False)
    print(f"Cleaned data saved to {path}")
