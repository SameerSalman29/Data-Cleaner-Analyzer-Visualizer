# CLI entrypoint here
import pandas as pd
from clean import clean_data
from analyze import analyze_data
from visualize import visualize_data
from model import train_model
import os

def main():
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('models', exist_ok=True)

    file_path = input("Enter CSV file path (e.g., data/sample_messy.csv): ")
    target = input("Enter target column for prediction (leave blank if none): ")

    df = pd.read_csv(file_path)
    print("\nCleaning data...")
    df = clean_data(df)

    print("Analyzing data...")
    report = analyze_data(df)
    with open('outputs/report.md', 'w') as f:
        f.write(report)
    print("Report saved to outputs/report.md")

    print("Visualizing data...")
    visualize_data(df)
    print("Figures saved to outputs/figures/")

    if target.strip() != '':
        print(f"Training models to predict {target}...")
        metrics = train_model(df, target)
        print("Metrics:", metrics)

if __name__ == "__main__":
    main()
