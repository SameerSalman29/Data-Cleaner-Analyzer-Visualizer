# Data Cleaner, Analyzer, Visualizer

All-in-one Python tool to clean, analyze, visualize, and optionally predict from datasets.

## Features

- Handles missing values (median, mean, mode imputation)
- Removes outliers by Z-score
- Analyzes feature correlations (correlation heatmap)
- Outputs cleaned data, reports, figures
- Easy CLI & notebook support

## Quickstart

```bash
python src/main.py data/mydata.csv --impute median --remove_outliers --correlation --output cleaned_mydata.csv
```

## File Structure

```
Data-Cleaner-Analyzer-Visualizer/
├── src/
│   ├── main.py
│   └── utils.py
├── data/
│   └── mydata.csv
├── README.md
```

## License

MIT License — see [LICENSE](LICENSE).
This project is licensed under the MIT License with the following clarification:  
You may use, modify, and share this project for **personal, educational, or research purposes only**.  
**Commercial use of any kind is not permitted** without prior written permission from the author.
