import joblib
from sklearn.cluster import KMeans


MODEL_PATH = "models/regime_model.pkl"


def train_regime_model(df, n_clusters=3):
    """
    Train KMeans model to detect market regimes
    """

    features = ["returns", "volatility"]
    X = df[features]

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    model.fit(X)

    # Save model
    joblib.dump(model, MODEL_PATH)

    return model


def detect_regimes(model, df):
    """
    Assign market regime to each observation
    """

    features = ["returns", "volatility"]
    X = df[features]

    regimes = model.predict(X)
    return regimes
