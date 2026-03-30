import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    data = pd.read_csv("dataset.csv")

    # Fill missing values
    data = data.fillna(data.mean(numeric_only=True))

    # Features & Target
    X = data[['temperature', 'humidity', 'wind', 'rain']]
    y = data['fire']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    return model
