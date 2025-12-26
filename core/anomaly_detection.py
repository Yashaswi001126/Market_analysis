import joblib
from sklearn.ensemble import IsolationForest


MODEL_PATH = "models/anomaly_model.pkl"


def train_anomaly_model(df):
    """
    Train Isolation Forest to detect market anomalies
    """

    features = ["returns", "volatility"]
    X = df[features]

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    # Save model
    joblib.dump(model, MODEL_PATH)

    return model


def detect_anomalies(model, df):
    """
    Detect anomalies in market data
    """

    features = ["returns", "volatility"]
    X = df[features]

    anomalies = model.predict(X)
    # -1 → anomaly, 1 → normal
    return anomalies
