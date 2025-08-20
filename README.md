---
# Data-Cleaner-Analyzer-Visualizer (DCAV)

An all‑in‑one tool to **clean**, **analyze**, **visualize**, and optionally **predict** from messy CSV data.
Perfect for quick portfolio demos: drop in a dataset, get a cleaned table, rich charts, and an auto-report.

## ✨ What it does
- Cleans messy data: trims spaces, standardizes column names, fixes types, imputes missing values, removes duplicates, clips outliers.
- Analyzes patterns: summary stats, correlations, skewness, cardinality, date recognition.
- Visualizes: histograms, boxplots, correlation heatmap, pairwise scatter (sampled), time-series if a date column exists.
- Predicts (optional): if you choose a target column, it will train a quick model
  - **Classification**: LogisticRegression + baseline RandomForest
  - **Regression**: LinearRegression + baseline RandomForestRegressor
  - Saves model and metrics.

## 📦 Project Structure
```
Data-Cleaner-Analyzer-Visualizer/
├── data/
│   └── sample_messy.csv
├── src/
│   ├── clean.py
│   ├── analyze.py
│   ├── visualize.py
│   ├── model.py
│   └── app_cli.py
├── outputs/
│   ├── figures/
│   └── report.md
├── notebooks/
│   └── demo.ipynb
├── models/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Quickstart
```bash
pip install -r requirements.txt
python src/app_cli.py
```

## 📝 License
MIT — see [LICENSE](LICENSE).
## Additional Terms

This project is licensed under the MIT License with the following clarification:  
You may use, modify, and share this project for **personal, educational, or research purposes only**.  
**Commercial use of any kind is not permitted** without prior written permission from the author.
