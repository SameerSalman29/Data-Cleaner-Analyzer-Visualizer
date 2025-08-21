# modeling functions here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
import joblib

def train_model(df: pd.DataFrame, target: str):
    X = df.drop(columns=[target])
    y = df[target]

    # Encode categorical columns
    X = pd.get_dummies(X, drop_first=True)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if y.dtype == 'object' or len(y.unique()) <= 20:
        # Classification
        models = {
            'LogisticRegression': LogisticRegression(max_iter=500),
            'RandomForest': RandomForestClassifier()
        }
        metrics = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            metrics[name] = accuracy_score(y_test, pred)
            joblib.dump(model, f'models/{name}.pkl')
    else:
        # Regression
        models = {
            'LinearRegression': LinearRegression(),
            'RandomForestRegressor': RandomForestRegressor()
        }
        metrics = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            metrics[name] = mean_squared_error(y_test, pred, squared=False)
            joblib.dump(model, f'models/{name}.pkl')

    return metrics
