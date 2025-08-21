# visualization functions here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_data(df: pd.DataFrame, output_dir='outputs/figures'):
    os.makedirs(output_dir, exist_ok=True)

    # Histograms
    df.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.savefig(f'{output_dir}/histograms.png')
    plt.close()

    # Boxplots
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.savefig(f'{output_dir}/boxplot_{col}.png')
        plt.close()

    # Correlation heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.savefig(f'{output_dir}/correlation_heatmap.png')
    plt.close()

    # Pairplot (sampled for speed)
    sns.pairplot(df.sample(min(100, len(df))))
    plt.savefig(f'{output_dir}/pairplot.png')
    plt.close()
