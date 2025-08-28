"""
Main CLI for Data Cleaning, Analysis, and Visualization.

Author: Sameer Salman
"""

import argparse
from pathlib import Path
from utils import load_dataset, handle_missing, plot_correlation_heatmap, remove_outliers, save_cleaned_data

def main():
    parser = argparse.ArgumentParser(description="Data Cleaner, Analyzer, Visualizer")
    parser.add_argument("input", type=str, help="Path to input CSV file")
    parser.add_argument("--output", type=str, default="cleaned_data.csv", help="Path to save cleaned data")
    parser.add_argument("--impute", type=str, choices=['median', 'mean', 'mode'], default='median', help="Imputation strategy")
    parser.add_argument("--remove_outliers", action="store_true", help="Remove outliers")
    parser.add_argument("--correlation", action="store_true", help="Plot correlation heatmap")
    args = parser.parse_args()

    df = load_dataset(args.input)
    df = handle_missing(df, strategy=args.impute)

    if args.remove_outliers:
        df = remove_outliers(df)

    if args.correlation:
        plot_correlation_heatmap(df, output_path=Path("correlation_heatmap.png"))

    save_cleaned_data(df, Path(args.output))

if __name__ == "__main__":
    main()