# cleaning functions here
import pandas as pd
from sklearn.impute import SimpleImputer

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Strip spaces from column names and string values
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # Fix data types
    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    if 'Salary' in df.columns:
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    if 'Join Date' in df.columns:
        df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')

    # Fill missing numeric values with mean
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = SimpleImputer(strategy='mean').fit_transform(df[num_cols])

    # Fill missing categorical values with mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df
